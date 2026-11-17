"""Estimate public-stock holdings of US insiders from the SEC Insider Transactions Data Sets (Forms 3/4/5).

For every individual reporting owner, take their latest reported holdings of each issuer's non-derivative
(common/ordinary) shares, value them at the issuer's most recent open-market trade price reported in the
same data sets, and sum across issuers. Keeps individuals with an estimated >= $30M.

This is a LOWER BOUND on net worth: it ignores options, private assets, cash and holdings in companies where
the person is not an insider. Mailing addresses in the data are deliberately not read or written.

Data: https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets
Usage: python3 scripts/sec_insiders.py <dir-with-unzipped-quarters> [out.csv]
"""
import csv
import glob
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

csv.field_size_limit(10**9)
MIN_USD = 30e6
SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else "data/sec_insiders_30m.csv"

ENTITY = re.compile(
    r"\b(LLC|L\.?L\.?C|L\.?P|LP|LLLP|INC|CORP|CORPORATION|FUND|FUNDS|TRUST|CAPITAL|PARTNERS|PARTNERSHIP|HOLDINGS?|"
    r"MANAGEMENT|ADVISORS?|ADVISERS?|GROUP|LTD|LIMITED|COMPANY|CO|BANK|FOUNDATION|VENTURES?|INVESTMENTS?|"
    r"ASSOCIATES|PLC|S\.?A|N\.?V|B\.?V|GMBH|AG|SPV|MASTER|OFFSHORE|SECURITIES|ENTERPRISES|INTERNATIONAL|"
    r"TECHNOLOGIES|ACQUISITION|SERIES|ESTATE|INVESTORS|EQUITY|OPPORTUNITIES|SA|AB|AS|ASA|KG|SE|PTE|PTY|"
    r"FINANCIAL|INSURANCE|PENSION|RETIREMENT|ENDOWMENT|UNIVERSITY|COLLEGE|BOARD|SYSTEM|GP|LIFE|ASSET|ASSETS|"
    r"STRATEGIES|STRATEGIC|PARTNER|OPPORTUNITY|GLOBAL|FAMILY|MANAGER|INVESTMENT|ADVISORY|HOLDCO|TOPCO|"
    r"BIDCO|AUTHORITY|GOVERNMENT|SOVEREIGN|COMMISSION|DEPARTMENT|CORPS|SOCIETY|PROPERTIES|RESOURCES|"
    r"INDUSTRIES|SYSTEMS|SOLUTIONS|NETWORKS|MEDIA|ENERGY|PHARMA|THERAPEUTICS|BIO|LABS?)\b\.?"
)
OPEN_MARKET = {"P", "S"}
FALLBACK_PRICE_CODES = {"F", "D", "J", "X", "C"}


def rows(q, name):
    path = os.path.join(q, name)
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t")


def d(s):
    try:
        return datetime.strptime(s, "%d-%b-%Y")
    except (ValueError, TypeError):
        return None


def f(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def pretty_name(sec_name):
    """SEC names are 'LAST FIRST MIDDLE [SUFFIX]' -> 'First Middle Last Suffix'."""
    n = re.sub(r"\s+", " ", sec_name.replace(",", " ")).strip()
    parts = n.split(" ")
    suffix = ""
    if parts and parts[-1].rstrip(".").upper() in {"JR", "SR", "II", "III", "IV"}:
        suffix = parts.pop()
    if len(parts) >= 2:
        parts = parts[1:] + parts[:1]
    out = " ".join(p.capitalize() if p.isupper() or p.islower() else p for p in parts)
    out = re.sub(r"\bMc([a-z])", lambda m: "Mc" + m.group(1).upper(), out)
    return (out + (" " + suffix.capitalize() if suffix else "")).strip()


subs, owners = {}, defaultdict(list)
price_obs = defaultdict(list)  # issuer -> [(date, priority, price)]
holdings = []  # (accession, title, shares, date, di, nature, sk)
for q in sorted(glob.glob(os.path.join(SRC, "*"))):
    for r in rows(q, "SUBMISSION.tsv"):
        subs[r["ACCESSION_NUMBER"]] = r
    for r in rows(q, "REPORTINGOWNER.tsv"):
        owners[r["ACCESSION_NUMBER"]].append((r["RPTOWNERCIK"], r["RPTOWNERNAME"], r.get("RPTOWNER_RELATIONSHIP", ""),
                                              r.get("RPTOWNER_TITLE", "")))
    for r in rows(q, "NONDERIV_TRANS.tsv"):
        acc = r["ACCESSION_NUMBER"]
        dt = d(r["TRANS_DATE"])
        sh = f(r["SHRS_OWND_FOLWNG_TRANS"])
        if sh is not None and dt:
            holdings.append((acc, r["SECURITY_TITLE"], sh, dt, r["DIRECT_INDIRECT_OWNERSHIP"], r.get("NATURE_OF_OWNERSHIP", ""),
                             int(r["NONDERIV_TRANS_SK"] or 0)))
        p = f(r["TRANS_PRICEPERSHARE"])
        if p and p > 0 and dt:
            code = r["TRANS_CODE"]
            pri = 2 if code in OPEN_MARKET else 1 if code in FALLBACK_PRICE_CODES else 0
            if pri:
                price_obs[acc].append((dt, pri, p, r["SECURITY_TITLE"]))
    for r in rows(q, "NONDERIV_HOLDING.tsv"):
        acc = r["ACCESSION_NUMBER"]
        sh = f(r["SHRS_OWND_FOLWNG_TRANS"])
        s = subs.get(acc)
        dt = d(s["PERIOD_OF_REPORT"]) if s else None
        if sh is not None and dt:
            holdings.append((acc, r["SECURITY_TITLE"], sh, dt, r["DIRECT_INDIRECT_OWNERSHIP"], r.get("NATURE_OF_OWNERSHIP", ""),
                             int(r["NONDERIV_HOLDING_SK"] or 0)))

# issuer price = median of open-market trade prices (codes P/S) in the 90 days before that issuer's latest
# such trade; needs at least 3 trades. Falls back to tax-withholding/other market-priced codes the same way.
from statistics import median
by_issuer = defaultdict(lambda: {2: [], 1: []})
for acc, obs in price_obs.items():
    s = subs.get(acc)
    if not s:
        continue
    for dt, pri, p, title in obs:
        by_issuer[s["ISSUERCIK"]][pri].append((dt, p))
issuer_price = {}
for ik, tiers in by_issuer.items():
    for pri in (2, 1):
        obs = tiers[pri]
        if len(obs) < 3:
            continue
        last = max(dt for dt, _ in obs)
        recent = [p for dt, p in obs if (last - dt).days <= 90]
        if len(recent) >= 3:
            issuer_price[ik] = (last, pri, median(recent))
            break

# latest holding per (owner, issuer, title, direct/indirect, nature)
latest = {}
for acc, title, sh, dt, di, nature, sk in holdings:
    s = subs.get(acc)
    if not s or "warrant" in title.lower() or "note" in title.lower() or "preferred" in title.lower():
        continue
    for cik, name, rel, otitle in owners.get(acc, []):
        key = (cik, s["ISSUERCIK"], title.strip().lower(), di, nature.strip().lower())
        if key not in latest or (dt, sk) > (latest[key][0], latest[key][1]):
            latest[key] = (dt, sk, sh, name, rel, otitle, s["ISSUERNAME"], s.get("ISSUERTRADINGSYMBOL", ""))

# only keep each owner's most recent filing date per issuer (drop stale lines from older filings)
newest = defaultdict(lambda: datetime.min)
for (cik, ik, *_), v in latest.items():
    newest[(cik, ik)] = max(newest[(cik, ik)], v[0])

people = defaultdict(lambda: {"value": 0.0, "issuers": {}, "name": "", "as_of": datetime.min})
for (cik, ik, title, di, nature), (dt, sk, sh, name, rel, otitle, iname, sym) in latest.items():
    if (newest[(cik, ik)] - dt).days > 400 or ik not in issuer_price:
        continue
    val = sh * issuer_price[ik][2]
    p = people[cik]
    p["value"] += val
    p["name"] = name
    p["as_of"] = max(p["as_of"], dt)
    role = otitle or rel
    prev = p["issuers"].get(iname, (0.0, role, sym))
    p["issuers"][iname] = (prev[0] + val, role or prev[1], sym)
    p.setdefault("issuer_ciks", set()).add(ik)

out = []
for cik, p in people.items():
    if p["value"] < MIN_USD or ENTITY.search(p["name"].upper()):
        continue
    if len(p["name"].split()) < 2:
        continue
    top = sorted(p["issuers"].items(), key=lambda kv: -kv[1][0])
    out.append({
        "name": pretty_name(p["name"]),
        "sec_name": p["name"],
        "owner_cik": cik.lstrip("0"),
        "est_public_holdings_usd_m": round(p["value"] / 1e6, 1),
        "as_of": p["as_of"].strftime("%Y-%m-%d"),
        "issuer_ciks": ";".join(sorted(c.lstrip("0") for c in p.get("issuer_ciks", ()))),
        "companies": "; ".join(f"{n} ({sym})" + (f" - {role}" if role else "") for n, (v, role, sym) in top[:5]),
        "sec_filings_url": f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik.lstrip('0')}&type=4",
    })
out.sort(key=lambda r: -r["est_public_holdings_usd_m"])
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print(f"filings: {len(subs)}, owner-issuer-security lines: {len(latest)}, issuers priced: {len(issuer_price)}")
print(f"individuals >= $30M: {len(out)} -> {OUT}")
