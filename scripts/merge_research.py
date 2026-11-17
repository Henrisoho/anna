"""Consolidate deep-research lane outputs into data/research_results.jsonl (one best record per person_id).

Lane agents occasionally wrote records into another lane's file; records are matched by id, so placement
doesn't matter. When an id appears more than once, the most complete record wins.
Usage: python3 scripts/merge_research.py <out_dir_with_wave_folders> [data/research_results.jsonl]
"""
import glob
import json
import os
import sys

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "data/research_results.jsonl"


def score(r):
    s = sum(1 for k in ("profile", "interesting_fact", "deep_cut_fact", "current_role") if r.get(k))
    s += len(r.get("public_contacts") or [])
    s += 2 if r.get("identity_confirmed") == "yes" else 0
    return s


best = {}
existing = out if os.path.exists(out) else None
files = glob.glob(os.path.join(src, "**", "lane_*.jsonl"), recursive=True) + ([existing] if existing else [])
bad = 0
for f in files:
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            bad += 1
            continue
        pid = r.get("id")
        if pid and (pid not in best or score(r) > score(best[pid])):
            best[pid] = r
with open(out, "w", encoding="utf-8") as fh:
    for pid in sorted(best):
        fh.write(json.dumps(best[pid], ensure_ascii=False) + "\n")
print(f"{len(best)} people researched -> {out} ({bad} unparseable lines skipped)")
