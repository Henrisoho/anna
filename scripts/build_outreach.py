"""Build data/uhnw_outreach.csv: the enriched list minus people unlikely to engage.

Removes:
  - known age under 40 or 90+ (age from Forbes, Wikidata or Hurun birth year; unknown ages are kept)
  - people research found to have died
  - records research found are not a real individual (funds, companies, placeholders: identity "no")
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
    if reason:
        removed.append({**r, "weeded_reason": reason})
    else:
        keep.append(r)

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
print(Counter(r["weeded_reason"].split(" (")[0] if r["weeded_reason"].startswith("age") is False else
              ("under %d" % MIN_AGE if "under" in r["weeded_reason"] else "%d+" % MAX_AGE) for r in removed))
print("kept with unknown age:", sum(1 for r in keep if not r.get("age", "").strip().isdigit()))
