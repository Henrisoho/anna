"""Add profile / interesting fact / deep-cut fact / public contact columns to data/uhnw_individuals.csv.

Inputs (downloaded separately, see data/README.md):
  - Forbes profile bios and "about" facts: komed3/rtb-api api/profile/<uri>/{bio,info}
  - Wikidata matches (enrich/wd_match.csv) and properties (enrich/wd_props.json)
  - Wikipedia page summaries (enrich/wp_summaries.json)
Writes data/uhnw_enriched.csv.

Contact columns hold only channels the person or their organisation has published (official website, public
social accounts listed on Wikidata). No guessed emails, no home addresses or personal phone numbers.
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date

RTB = "/home/user/komed3/rtb-api/api/profile"
EN = "/home/user/datasets/enrich"
IN = "data/uhnw_individuals.csv"
OUT = sys.argv[1] if len(sys.argv) > 1 else "data/uhnw_enriched.csv"

rows = list(csv.DictReader(open(IN, encoding="utf-8")))


def load_json(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


# Wikidata: name -> QID (only unambiguous matches: exactly one living business person with that name)
wd_by_name = defaultdict(set)
wd_desc = {}
if os.path.exists(f"{EN}/wd_match.csv"):
    for r in csv.DictReader(open(f"{EN}/wd_match.csv", encoding="utf-8")):
        q = r["item"].rsplit("/", 1)[-1]
        wd_by_name[r["name"]].add(q)
        wd_desc[q] = r.get("description", "")
props = load_json(f"{EN}/wd_props.json", {})
research = {}
if os.path.exists("data/research_results.jsonl"):
    for line in open("data/research_results.jsonl", encoding="utf-8"):
        rr = json.loads(line)
        research[rr["id"]] = rr
wp = load_json(f"{EN}/wp_summaries.json", {})


def sentences(text, n=None):
    s = [x.strip() for x in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“])", text or "") if x.strip()]
    return s if n is None else s[:n]


def handle_url(kind, v):
    return {"x": f"https://x.com/{v}", "insta": f"https://www.instagram.com/{v}/",
            "linkedin": f"https://www.linkedin.com/in/{v}/", "fb": f"https://www.facebook.com/{v}"}.get(kind, v)


def fmt_money(m):
    try:
        m = float(m)
    except (TypeError, ValueError):
        return ""
    return f"${m/1000:,.1f}B" if m >= 1000 else f"${m:,.0f}M"


out = []
stats = defaultdict(int)
for r in rows:
    uri = r["forbes_profile_url"].rstrip("/").rsplit("/", 1)[-1] if r["forbes_profile_url"] else ""
    bio = load_json(f"{RTB}/{uri}/bio", {}) if uri else {}
    info = load_json(f"{RTB}/{uri}/info", {}) if uri else {}
    qid = r["wikidata_url"].rsplit("/", 1)[-1] if r["wikidata_url"] else ""
    if not qid and len(wd_by_name.get(r["name"], ())) == 1:
        qid = next(iter(wd_by_name[r["name"]]))
    pr = props.get(qid, {}) if qid else {}
    article = (pr.get("article") or [""])[0]
    summary = wp.get(article, "") if article else ""

    # ---- small profile ----
    bio_s = bio.get("bio") or []
    if bio_s:
        profile = " ".join(bio_s[:2]); psrc = "Forbes"
    elif summary:
        profile = " ".join(sentences(summary, 2)); psrc = "Wikipedia"
    else:
        bits = [r["name"]]
        desc = wd_desc.get(qid, "")
        if desc:
            bits.append(f"is a {desc}" if not desc.lower().startswith(("a ", "an ", "the ")) else f"is {desc}")
        src = r["source_of_wealth"] or r["sec_insider_companies"]
        if src:
            bits.append(f"— wealth from {src}")
        if r["country"]:
            bits.append(f"({r['country']})")
        nw = fmt_money(r["latest_net_worth_usd_m"])
        if nw:
            bits.append(f"Estimated net worth {nw} ({r['net_worth_source']}, {r['net_worth_as_of']}).")
        profile = " ".join(bits); psrc = "list data"
    stats[f"profile:{psrc}"] += 1

    # ---- interesting + deep-cut facts ----
    about = bio.get("about") or []
    extra_bio = bio_s[2:]
    wiki_more = sentences(summary)[2:] if summary else []
    interesting, deep = "", ""
    if about:
        interesting = about[0]
        deep = about[1] if len(about) > 1 else ""
    candidates = [s for s in extra_bio + wiki_more if s not in (interesting, deep)]
    if not interesting and candidates:
        interesting = candidates.pop(0)
    if not deep and candidates:
        deep = candidates[-1]
    if not deep and pr:
        aw = [a for a in pr.get("award", []) if not re.fullmatch(r"Q\d+", a)]
        edu = [e for e in pr.get("edu", []) if not re.fullmatch(r"Q\d+", e)]
        if aw:
            deep = f"Recipient of the {aw[0]}" + (f" (also: {', '.join(aw[1:3])})" if len(aw) > 1 else "") + "."
        elif edu and pr.get("birthplace"):
            deep = f"Born in {pr['birthplace'][0]}; studied at {', '.join(edu[:2])}."
    stats["interesting" if interesting else "no interesting"] += 1
    stats["deep" if deep else "no deep"] += 1

    # ---- public contact (published channels only) ----
    contacts = []
    for kind in ("website", "x", "linkedin", "insta", "fb"):
        for v in pr.get(kind, [])[:1]:
            contacts.append(handle_url(kind, v))
    stats["has contact" if contacts else "no contact"] += 1

    # agent research (data/research_results.jsonl) overrides automated fields where it found something
    rr = research.get(r.get("person_id", ""), {})
    researched = bool(rr)
    if rr.get("alive") == "no":
        stats["research says deceased"] += 1
    if rr.get("profile"):
        profile, psrc = rr["profile"], "research"
    if rr.get("interesting_fact"):
        interesting = rr["interesting_fact"]
    if rr.get("deep_cut_fact"):
        deep = rr["deep_cut_fact"]
    rc = [f"{c.get('type')}: {c.get('value')}" for c in rr.get("public_contacts") or [] if c.get("value")]
    rc_src = sorted({c.get("source_url", "") for c in rr.get("public_contacts") or [] if c.get("source_url")})
    if rc:
        contacts = rc + [c for c in contacts if not any(c in x for x in rc)]

    age = ""
    born = info.get("birthDate") or ((pr.get("born") or [""])[0][:10])
    if born and re.match(r"\d{4}-\d{2}-\d{2}", born) and not born.startswith("1900"):
        b = date.fromisoformat(born[:10])
        t = date.today()
        age = t.year - b.year - ((t.month, t.day) < (b.month, b.day))
    org = info.get("organization") or {}
    sm = info.get("selfMade") or {}
    res = info.get("residence") or {}
    edu_forbes = "; ".join(e.get("school", "") + (f" ({e['degree']})" if e.get("degree") else "") for e in info.get("education", []) or [])
    out.append({
        **r,
        "age": age,
        "title_and_organization": (f"{org.get('title')}, {org.get('name')}" if org.get("title") else org.get("name", "")) if org else "",
        "self_made": ("yes" if sm.get("_is") else "no") if sm else "",
        "self_made_score_1to10": sm.get("rank", "") if sm else "",
        "home_city": ", ".join(x for x in [res.get("city"), res.get("state")] if x),
        "education": edu_forbes or "; ".join(e for e in pr.get("edu", [])[:3] if not re.fullmatch(r"Q\d+", e)),
        "profile": profile,
        "profile_source": psrc,
        "interesting_fact": interesting,
        "deep_cut_fact": deep,
        "current_role": rr.get("current_role", ""),
        "interesting_fact_source": rr.get("interesting_fact_source", "") or ("Forbes profile" if about else ""),
        "deep_cut_fact_source": rr.get("deep_cut_fact_source", "") or ("Forbes profile" if about and deep in about else ""),
        "public_contact": " | ".join(contacts),
        "public_contact_source": " ".join(rc_src) if rc else (f"https://www.wikidata.org/wiki/{qid}" if contacts else ""),
        "research_status": ("researched" if researched else "automated only") + (" (identity uncertain)" if rr.get("identity_confirmed") == "uncertain" else "") + (" (deceased per research)" if rr.get("alive") == "no" else ""),
        "research_notes": rr.get("notes", ""),
        "wikipedia_url": article,
        "wikidata_url": r["wikidata_url"] or (f"http://www.wikidata.org/entity/{qid}" if qid else ""),
    })

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)
print(dict(stats))
print(f"{len(out)} rows -> {OUT}")
