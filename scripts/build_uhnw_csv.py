"""Merge public rich lists into one de-duplicated CSV of known ultra-high-net-worth individuals.

Sources (all public / openly licensed; see README section in the output notes):
  - komed3/rtb-api (MIT): Forbes real-time billionaires, current list + profiles of people who dropped off
  - FilesUploader/Forbes-Billionaire-List: Forbes annual billionaire lists 1996-2025
  - FilesUploader/Hurun-GRL: Hurun Global Rich List 2014-2024
  - hurun.net ranking data: Hurun China Rich List 1999-2026, India Rich List, Global Rich List,
    Richest Self-Made Women, Global U40 Self-Made Billionaires, China U40 Rich List
  - harveydevereux/TimesRichList2020: Sunday Times Rich List 2020 (UK top 1,000)
  - Wikidata: living people with a recorded net worth (P2218) >= $30M

Usage: python3 scripts/build_uhnw_csv.py [out.csv]
Paths to the downloaded sources are set in SOURCES below.
"""
import csv
import glob
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import pycountry

RTB = "/home/user/komed3/rtb-api/api"
DS = "/home/user/datasets"
UHNW_MIN_USD_M = 30.0

# Approximate USD conversion for Wikidata values in other currencies (order-of-magnitude use only).
WD_UNIT_USD = {
    "Q4917": 1.0,      # US dollar
    "Q4916": 1.08,     # euro
    "Q25224": 1.27,    # pound sterling
    "Q39099": 0.14,    # renminbi
    "Q80524": 0.012,   # Indian rupee
    "Q8146": 0.0067,   # yen
    "Q1104069": 0.73,  # Canadian dollar
    "Q259502": 0.65,   # Australian dollar
    "Q25344": 1.13,    # Swiss franc
    "Q202040": 0.00073,  # won
    "Q41044": 0.011,   # ruble
    "Q122922": 0.093,  # Swedish krona
    "Q132643": 0.093,  # Norwegian krone
    "Q25417": 0.145,   # Danish krone
    "Q31015": 0.128,   # Hong Kong dollar
    "Q4730": 0.055,    # Mexican peso? (not used if absent)
}
GBP_USD_2020 = 1.28

COUNTRY_FIX = {
    "uk": "GB", "united kingdom": "GB", "england": "GB", "scotland": "GB", "wales": "GB",
    "russia": "RU", "south korea": "KR", "korea": "KR", "taiwan": "TW", "hong kong": "HK",
    "macau": "MO", "macao": "MO", "china": "CN", "mainland china": "CN", "czech republic": "CZ",
    "vietnam": "VN", "turkey": "TR", "iran": "IR", "venezuela": "VE", "tanzania": "TZ",
    "bolivia": "BO", "eswatini (swaziland)": "SZ", "swaziland": "SZ", "st. kitts and nevis": "KN",
    "st. kitts & nevis": "KN", "ivory coast": "CI", "the netherlands": "NL", "uae": "AE",
    "united arab emirates": "AE", "usa": "US", "us": "US", "united states": "US",
    "guernsey": "GG", "monaco": "MC", "liechtenstein": "LI", "kingdom of the netherlands": "NL",
    "people's republic of china": "CN", "republic of ireland": "IE", "russian federation": "RU",
    "laos": "LA", "moldova": "MD", "syria": "SY", "palestine": "PS", "kosovo": "XK",
}
_country_cache = {}


def iso2(value):
    if not value:
        return ""
    v = str(value).strip()
    if not v:
        return ""
    key = v.lower()
    if key in _country_cache:
        return _country_cache[key]
    code = ""
    if key in COUNTRY_FIX:
        code = COUNTRY_FIX[key]
    elif len(v) == 2 and v.isalpha():
        code = v.upper()
    else:
        first = re.split(r"[-,/]", v)[0].strip()  # "China-Fujian-Longyan" -> "China"
        for cand in (v, first):
            if cand.lower() in COUNTRY_FIX:
                code = COUNTRY_FIX[cand.lower()]
                break
            try:
                code = pycountry.countries.lookup(cand).alpha_2
                break
            except LookupError:
                continue
    _country_cache[key] = code
    return code


def country_name(code):
    if not code:
        return ""
    if code == "XK":
        return "Kosovo"
    c = pycountry.countries.get(alpha_2=code)
    return getattr(c, "common_name", None) or (c.name if c else code)


TITLES = r"^(sir|dame|lord|lady|dr|the hon|hon|baron|baroness|sheikh|shaikh|prince|princess|mr|mrs|ms)\.?\s+"


def norm_name(name):
    n = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\(.*?\)", " ", n)
    n = re.sub(r"(&|\band\b)\s*(his |her )?(family|siblings|sons|daughters|children)\b.*$", " ", n)
    n = re.sub(r"\bfamily\b", " ", n)
    n = re.sub(r"[^a-z0-9 ]", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    prev = None
    while prev != n:
        prev = n
        n = re.sub(TITLES, "", n)
    return n


def fnum(x):
    if x is None:
        return None
    s = re.sub(r"[^0-9.\-]", "", str(x))
    try:
        return float(s) if s not in ("", ".", "-") else None
    except ValueError:
        return None


records = []  # dicts: name, nw_usd_m, as_of, country, wealth_source, industry, list, year, uri, wikidata, deceased


def add(**kw):
    if not (kw.get("name") or "").strip():
        return
    kw["name"] = re.sub(r"\s+", " ", kw["name"]).strip()
    kw["country"] = iso2(kw.get("country"))
    records.append(kw)


# 1. Forbes real-time current list
cur_files = sorted(glob.glob(f"{RTB}/list/rtb/20*"))
cur = json.load(open(cur_files[-1], encoding="utf-8"))
current_uris = set()
for r in cur["list"]:
    current_uris.add(r["uri"])
    add(name=r["name"], nw_usd_m=r.get("networth"), as_of=cur["date"], country=r.get("citizenship"),
        wealth_source="; ".join(r.get("source", [])), industry="; ".join(r.get("industry", [])),
        list="Forbes real-time", year=int(cur["date"][:4]), uri=r["uri"])

# 2. Forbes real-time profiles of people no longer on the list
deceased_uris = set(json.load(open(f"{RTB}/filter/deceased", encoding="utf-8"))) if os.path.exists(f"{RTB}/filter/deceased") else set()
for d in glob.glob(f"{RTB}/profile/*/"):
    uri = os.path.basename(d.rstrip("/"))
    if uri in current_uris or not os.path.exists(d + "info"):
        continue
    try:
        info = json.load(open(d + "info", encoding="utf-8"))
        latest = json.load(open(d + "latest", encoding="utf-8")) if os.path.exists(d + "latest") else {}
    except (json.JSONDecodeError, OSError):
        continue  # incomplete download
    dead = bool(info.get("deceased")) or uri in deceased_uris
    add(name=info.get("name", ""), nw_usd_m=latest.get("networth"), as_of=latest.get("date", ""),
        country=info.get("citizenship"), wealth_source="; ".join(info.get("source", []) or []),
        industry="; ".join(info.get("industry", []) or []), list="Forbes real-time (former)",
        year=int(latest["date"][:4]) if latest.get("date") else None, uri=uri, deceased=dead)

# 3. Forbes annual lists 1996-2025
for f in glob.glob(f"{DS}/FilesUploader_Forbes-Billionaire-List/*.csv"):
    year = int(re.search(r"(\d{4})", os.path.basename(f)).group(1))
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Wealth (in $1B USD)"))
        add(name=r.get("Name", ""), nw_usd_m=w * 1000 if w is not None else None, as_of=str(year),
            country=r.get("Country of Citizenship"), wealth_source=r.get("Source of Wealth", ""),
            industry=r.get("Industry", ""), list="Forbes annual", year=year)

# 4. Hurun Global Rich List CSVs 2014-2024
for f in glob.glob(f"{DS}/FilesUploader_Hurun-GRL/*.csv"):
    year = int(re.search(r"(\d{4})", os.path.basename(f)).group(1))
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Wealth (in $1B USD)"))
        add(name=r.get("Name", ""), nw_usd_m=w * 1000 if w is not None else None, as_of=str(year),
            country=r.get("Country Headquartered"), wealth_source=r.get("Company", ""),
            industry=r.get("Industry", ""), list="Hurun Global", year=year)

# 5. hurun.net downloads (China, India, Global, women, U40 lists)
HURUN_LABEL = {"china": "Hurun China", "india": "Hurun India", "global": "Hurun Global",
               "cwomen": "Hurun Self-Made Women", "gu40": "Hurun Global U40", "u40": "Hurun China U40"}
def hv(r, suffix):
    """Value of hs_Rank_<List>_<suffix>; each Hurun list uses its own <List> prefix (Rich, India, Global, ...)."""
    for k, v in r.items():
        if re.fullmatch(r"hs_Rank_[A-Za-z0-9]+_" + suffix, k) and v not in (None, ""):
            return v
    return None


INR_CRORE_USD_M = 0.12  # 1 crore INR ~ $0.12M (approximate)
for sub, label in HURUN_LABEL.items():
    for f in glob.glob(f"{DS}/hurun/{sub}/*.json"):
        d = json.load(open(f, encoding="utf-8"))
        label_year = re.search(r"(\d{4})", d["label"])
        for r in d["rows"]:
            year = fnum(hv(r, "Year"))
            year = int(year) if year else (int(label_year.group(1)) if label_year else None)
            chars = [c for c in (r.get("hs_Character") or []) if (c.get("hs_Character_Fullname_En") or c.get("hs_Character_Fullname_Cn"))]
            usd = fnum(hv(r, "Wealth_USD"))
            if usd is not None and sub in ("global", "gu40", "cwomen") and usd < 1000:
                usd *= 1000  # these billionaire lists give USD in billions, not millions
            if usd is None and fnum(hv(r, "Wealth_INR")) is not None:
                usd = fnum(hv(r, "Wealth_INR")) * INR_CRORE_USD_M
            default_country = hv(r, "Permanent_En") or ("China" if sub in ("china", "u40") else "India" if sub == "india" else "")
            common = dict(nw_usd_m=usd, as_of=str(year or ""), list=label, year=year,
                          wealth_source=hv(r, "ComName_En") or hv(r, "ComName_Cn") or "",
                          industry=hv(r, "Industry_En") or "")
            if not chars:  # no per-person records: fall back to the entry name
                add(name=hv(r, "ChaName_En") or hv(r, "ChaName_Cn") or "",
                    country=default_country, name_cn=hv(r, "ChaName_Cn") or "", **common)
                continue
            # one record per person; joint entries (couples, families) share the listed wealth
            names = [c.get("hs_Character_Fullname_En") or c.get("hs_Character_Fullname_Cn") for c in chars]
            for c, nm in zip(chars, names):
                others = [o for o in names if o != nm]
                add(name=nm, country=c.get("hs_Character_Permanent_En") or default_country,
                    name_cn=c.get("hs_Character_Fullname_Cn") or "",
                    joint_with=", ".join(others), **common)

# 6. Sunday Times Rich List 2020
f = f"{DS}/harveydevereux_TimesRichList2020/resources/TimesRichList2020.csv"
if os.path.exists(f):
    for r in csv.DictReader(open(f, encoding="utf-8-sig", errors="replace")):
        w = fnum(r.get("Worth"))
        add(name=r.get("Name", ""), nw_usd_m=w * GBP_USD_2020 / 1e6 if w else None, as_of="2020",
            country="GB", wealth_source=r.get("Source of wealth", ""), industry="",
            list="Sunday Times Rich List", year=2020)

# 7. Wikidata (living people with a net worth statement)
wd_best = {}
for r in csv.DictReader(open(f"{DS}/wikidata/wd_networth.csv", encoding="utf-8")):
    unit = r["unit"].rsplit("/", 1)[-1]
    rate = WD_UNIT_USD.get(unit)
    amt = fnum(r["nw"])
    if rate is None or amt is None:
        continue
    usd_m = amt * rate / 1e6
    date = (r.get("date") or "")[:10]
    if not re.match(r"\d{4}", date):
        date = ""  # unknown or blank-node date
    key = r["p"]
    if key not in wd_best or date > wd_best[key]["as_of"]:
        wd_best[key] = dict(name=r["pLabel"], nw_usd_m=usd_m, as_of=date, country=r.get("country"),
                            wealth_source="", industry="", list="Wikidata",
                            year=int(date[:4]) if date else None, wikidata=key)
for v in wd_best.values():
    if v["nw_usd_m"] >= UHNW_MIN_USD_M and not re.fullmatch(r"Q\d+", v["name"]):
        add(**v)

wd_dead_names = set()
dead_file = f"{DS}/wikidata/wd_dead.csv"
if os.path.exists(dead_file):
    wd_dead_names = {norm_name(r["pLabel"]) for r in csv.DictReader(open(dead_file, encoding="utf-8"))}
# Exact-name matches against Wikidata businesspeople with a death date (checked for names not listed since 2024)
dead_file2 = f"{DS}/wikidata/wd_dead_by_name.csv"
if os.path.exists(dead_file2):
    wd_dead_names |= {norm_name(r["name"]) for r in csv.DictReader(open(dead_file2, encoding="utf-8"))}
RECENT_YEAR = 2025
dropped = Counter()

# ---- merge: group by normalised name, split by country where they clearly differ ----
by_name = defaultdict(list)
for r in records:
    k = norm_name(r["name"])
    if k:
        by_name[k].append(r)

people = []
for k, rs in by_name.items():
    countries = Counter(r["country"] for r in rs if r["country"])
    # Only treat a shared name as several people when one source lists it more than once in the same
    # year (e.g. two different "Wang Wei"s); otherwise country differences are just citizenship vs residence.
    same_list_dupes = max(Counter((r["list"], r.get("year")) for r in rs).values()) > 1
    if len(countries) <= 1 or not same_list_dupes:
        groups = [rs]
    else:
        main = countries.most_common(1)[0][0]
        groups_d = defaultdict(list)
        for r in rs:
            groups_d[r["country"] or main].append(r)
        groups = list(groups_d.values())
    people.extend(groups)

LIST_PRIORITY = {"Forbes real-time": 0, "Forbes real-time (former)": 1, "Forbes annual": 2, "Hurun Global": 3,
                 "Hurun China": 3, "Hurun India": 3, "Hurun Self-Made Women": 4, "Hurun Global U40": 4,
                 "Hurun China U40": 4, "Sunday Times Rich List": 5, "Wikidata": 6}


def as_of_key(r):
    a = str(r.get("as_of") or "")
    return (a + "-06-30") if len(a) == 4 else a  # year-only lists: mid-year, so a dated real-time figure from later that year wins


out_rows = []
for g in people:
    g_sorted = sorted(g, key=lambda r: (as_of_key(r), -LIST_PRIORITY.get(r["list"], 9)), reverse=True)
    best = next((r for r in g_sorted if r.get("nw_usd_m") is not None), g_sorted[0])
    display = min(g, key=lambda r: LIST_PRIORITY.get(r["list"], 9))["name"]
    lists = defaultdict(set)
    for r in g:
        if r.get("year"):
            lists[r["list"]].add(r["year"])
        else:
            lists[r["list"]]
    appears = []
    for name_, yrs in sorted(lists.items(), key=lambda kv: LIST_PRIORITY.get(kv[0], 9)):
        if yrs:
            appears.append(f"{name_} ({min(yrs)}-{max(yrs)})" if min(yrs) != max(yrs) else f"{name_} ({min(yrs)})")
        else:
            appears.append(name_)
    years = [r["year"] for r in g if r.get("year")]
    deceased = any(r.get("deceased") for r in g)
    uri = next((r["uri"] for r in g if r.get("uri")), "")
    wd = next((r["wikidata"] for r in g if r.get("wikidata")), "")
    country = best["country"] or next((r["country"] for r in g if r["country"]), "")
    ws = best.get("wealth_source") or next((r["wealth_source"] for r in g_sorted if r.get("wealth_source")), "")
    ind = best.get("industry") or next((r["industry"] for r in g_sorted if r.get("industry")), "")
    name_cn = next((r["name_cn"] for r in g if r.get("name_cn")), "")
    joint = best.get("joint_with") or ""
    nw = best.get("nw_usd_m")
    last_year = max(years) if years else 0
    if deceased:
        dropped["deceased (Forbes)"] += 1
        continue
    if norm_name(display) in wd_dead_names and last_year < RECENT_YEAR:
        dropped["deceased (Wikidata, not listed since 2024)"] += 1
        continue
    if nw is not None and nw < UHNW_MIN_USD_M:
        dropped["last known net worth under $30M"] += 1
        continue
    out_rows.append({
        "name": display,
        "name_chinese": name_cn,
        "latest_net_worth_usd_m": round(nw, 1) if nw is not None else "",
        "net_worth_as_of": best.get("as_of", ""),
        "net_worth_source": best["list"],
        "net_worth_shared_with": joint,
        "country": country_name(country),
        "country_code": country,
        "source_of_wealth": ws,
        "industry": ind,
        "appears_on": "; ".join(appears),
        "first_listed_year": min(years) if years else "",
        "last_listed_year": max(years) if years else "",
        "possibly_deceased": "yes" if norm_name(display) in wd_dead_names else "",  # still on a recent list
        "forbes_profile_url": f"https://www.forbes.com/profile/{uri}/" if uri else "",
        "wikidata_url": wd,
    })

out_rows.sort(key=lambda r: -(r["latest_net_worth_usd_m"] or 0))
out = sys.argv[1] if len(sys.argv) > 1 else "data/uhnw_individuals.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
    w.writeheader()
    w.writerows(out_rows)

print(f"input records: {len(records)}")
print("records by list:", dict(Counter(r["list"] for r in records)))
print("dropped:", dict(dropped))
print(f"unique living individuals written: {len(out_rows)} -> {out}")
