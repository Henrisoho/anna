"""Build data/uhnw_outreach.csv: the enriched list minus people unlikely to engage.

Removes:
  - known age under 40 or 90+ (age from Forbes, Wikidata or Hurun birth year; unknown ages are kept)
  - people research found to have died
  - records research found are not a real individual (funds, companies, placeholders: identity "no")
  - mainland-China entries without international visibility: kept only if they have an English Wikipedia
    article or research found a personal public channel (own X/LinkedIn/Instagram/Substack/podcast/self-published
    email); company IR inboxes and websites don't count
  - duplicates that share the same Chinese name (e.g. "Pony Ma" / "Ma Huateng"); the best-documented row is kept
Writes the removed rows to data/uhnw_weeded_out.csv with a reason, so nothing is lost.
Usage: python3 scripts/build_outreach.py [min_age=40] [max_age_exclusive=90]
"""
import csv
import sys

MIN_AGE = int(sys.argv[1]) if len(sys.argv) > 1 else 40
MAX_AGE = int(sys.argv[2]) if len(sys.argv) > 2 else 90

rows = list(csv.DictReader(open("data/uhnw_enriched.csv", encoding="utf-8")))
research = {}
for line in open("data/research_results.jsonl", encoding="utf-8"):
    import json
    r = json.loads(line)
    research[r["id"]] = r

PERSONAL = {"personal_email", "x", "linkedin", "instagram", "substack", "podcast"}
keep, removed = [], []
for r in rows:
    rr = research.get(r["person_id"], {})
    reason = ""
    age = r.get("age", "").strip()
    if age.isdigit():
        a = int(age)
        if a < MIN_AGE:
            reason = f"age {a} (under {MIN_AGE})"
        elif a >= MAX_AGE:
            reason = f"age {a} ({MAX_AGE}+)"
    if not reason and rr.get("alive") == "no":
        reason = "deceased (per research)"
    if not reason and rr.get("identity_confirmed") == "no":
        reason = "not an identifiable individual (per research)"
    if not reason and r.get("country_code") == "CN":
        personal = any(x.get("type") in PERSONAL for x in rr.get("public_contacts") or [])
        if not (r.get("wikipedia_url") or personal):
            reason = "China, little international visibility"
    if reason:
        removed.append({**r, "weeded_reason": reason})
    else:
        keep.append(r)

# merge duplicates that share a Chinese name (English alias vs pinyin, e.g. "Jack Ma" / "Ma Yun")
def quality(r):
    try:
        nw = float(r["latest_net_worth_usd_m"])
    except ValueError:
        nw = 0.0
    return (r["research_status"].startswith("researched"), bool(r["forbes_profile_url"]), bool(r["public_contact"]), nw)


import re

CHINESE_WORLD = {"CN", "HK", "TW", "MO", "SG", "MY"}


def native_cn_name(r):
    """Chinese name usable as a merge key: only for Chinese-world rows, 2-4 Han characters, no '·' (which marks
    transliterated foreign names). Hurun fills this field with transliterations/placeholders for other names."""
    cn = r.get("name_chinese", "").strip()
    if r.get("country_code") in CHINESE_WORLD and re.fullmatch(r"[一-鿿]{2,4}", cn):
        return cn
    return ""


by_cn = {}
deduped = []
for r in keep:
    cn = native_cn_name(r)
    if cn and cn in by_cn:
        other = by_cn[cn]
        best, worse = (r, other) if quality(r) > quality(other) else (other, r)
        by_cn[cn] = best
        removed.append({**worse, "weeded_reason": f"duplicate of {best['name']} ({best['person_id']})"})
    elif cn:
        by_cn[cn] = r
    else:
        deduped.append(r)
keep = deduped + list(by_cn.values())

# English-alias rows (Forbes "Jack Ma", no Chinese name) vs pinyin rows (Hurun "Ma Yun", 马云): merge when both are
# in the Chinese world, the alias surname equals the pinyin surname, net worth is within 35%, and the match is unique.
def nw(r):
    try:
        return float(r["latest_net_worth_usd_m"])
    except ValueError:
        return 0.0


STOP = {"and", "the", "of", "co", "inc", "ltd", "group", "holdings", "company", "technology", "technologies",
        "diversified", "investments", "founder", "valued", "company"}


def biz_words(r):
    text = " ".join([r.get("source_of_wealth", ""), r.get("industry", ""), r.get("sec_insider_companies", ""),
                     r.get("title_and_organization", ""), r.get("current_role", "")]).lower()
    return {w for w in re.findall(r"[a-z]{3,}", text) if w not in STOP}


pinyin = [r for r in keep if native_cn_name(r)]
by_surname = {}
for r in pinyin:
    by_surname.setdefault(r["name"].split()[0].lower(), []).append(r)
drop_ids = set()
for r in keep:
    toks = r["name"].split()
    if native_cn_name(r) or r.get("country_code") != "CN" or len(toks) != 2 or nw(r) < 1000:
        continue
    cands = [p for p in by_surname.get(toks[-1].lower(), []) if p["person_id"] != r["person_id"]
             and p.get("country_code") == "CN" and nw(p) >= 1000
             and abs(nw(p) - nw(r)) <= 0.35 * max(nw(p), nw(r)) and (biz_words(p) & biz_words(r))]
    if len(cands) == 1:
        p = cands[0]
        best, worse = (r, p) if quality(r) > quality(p) else (p, r)
        if worse["person_id"] in drop_ids or best["person_id"] in drop_ids:
            continue
        drop_ids.add(worse["person_id"])
        removed.append({**worse, "weeded_reason": f"duplicate of {best['name']} ({best['person_id']})"})
# well-known English names whose rows describe the business too differently for the rule above
KNOWN_ALIASES = {"Pony Ma": "马化腾", "William Ding": "丁磊", "Robin Zeng": "曾毓群", "Eric Li": "李书福",
                 "Frank Wang": "汪滔", "Robin Li": "李彦宏", "Jack Ma": "马云", "Colin Huang": "黄峥",
                 "Richard Liu": "刘强东", "Joseph Tsai": "蔡崇信", "Lin Bin": "林斌", "William Li": "李斌"}
cn_rows = {}
for r in keep:
    cn = native_cn_name(r)
    if cn:
        cn_rows.setdefault(cn, []).append(r)
for r in keep:
    cn = KNOWN_ALIASES.get(r["name"])
    others = [p for p in cn_rows.get(cn, []) if p["person_id"] != r["person_id"]] if cn else []
    if len(others) == 1 and r["person_id"] not in drop_ids and others[0]["person_id"] not in drop_ids:
        p = others[0]
        best, worse = (r, p) if quality(r) > quality(p) else (p, r)
        drop_ids.add(worse["person_id"])
        removed.append({**worse, "weeded_reason": f"duplicate of {best['name']} ({best['person_id']})"})
keep = [r for r in keep if r["person_id"] not in drop_ids]
keep.sort(key=lambda r: r["person_id"])

fields = list(rows[0].keys())
with open("data/uhnw_outreach.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(keep)
with open("data/uhnw_weeded_out.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["weeded_reason"] + fields)
    w.writeheader()
    w.writerows(removed)

from collections import Counter
print(f"kept {len(keep)} / {len(rows)}; removed {len(removed)}")
def bucket(reason):
    if reason.startswith("age"):
        return "under %d" % MIN_AGE if "under" in reason else "%d+" % MAX_AGE
    return reason.split(" (")[0]


print(Counter(bucket(r["weeded_reason"]) for r in removed))
print("kept with unknown age:", sum(1 for r in keep if not r.get("age", "").strip().isdigit()))
