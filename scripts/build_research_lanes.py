"""Split data/uhnw_individuals.csv into research lanes for parallel deep-research agents.

Priority: energy / data-center people first (podcast focus), then everyone else by net worth.
Usage: python3 scripts/build_research_lanes.py <out_dir> <wave> [lanes=100] [per_lane=20]
Writes <out_dir>/wave<wave>/lane_NNN.jsonl and skips people already researched in earlier waves.
"""
import csv
import glob
import json
import os
import re
import sys

out_dir, wave = sys.argv[1], int(sys.argv[2])
LANES = int(sys.argv[3]) if len(sys.argv) > 3 else 100
PER = int(sys.argv[4]) if len(sys.argv) > 4 else 20
RTB = "/home/user/komed3/rtb-api/api/profile"

ENERGY = re.compile(r"oil|gas\b|petro|energy|power|solar|wind|batter|pipeline|utilit|nuclear|coal|refin|lng|fuel|hydrogen|renewable|grid|lithium", re.I)
DC_AI = re.compile(r"nvidia|oracle|dell|amd|coreweave|iren|astera|nebius|super ?micro|semiconductor|chip|broadcom|tsmc|data ?cent|cloud|"
                   r"quanta|foxconn|arista|vertiv|equinix|crusoe|lambda|applied digital|artificial intelligence|\bai\b|openai|anthropic|"
                   r"cerebras|marvell|micron|server|cooling|fiber|optical", re.I)
NOT_ENERGY = re.compile(r"palm oil|edible oil|energy drink|vegas|power strip|gas station", re.I)

rows = list(csv.DictReader(open("data/uhnw_individuals.csv", encoding="utf-8")))
done = set()
for f in glob.glob(os.path.join(out_dir, "wave*", "lane_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        done.add(json.loads(line)["id"])


def focus(r):
    text = " ".join([r["source_of_wealth"], r["industry"], r["sec_insider_companies"]])
    t = NOT_ENERGY.sub("", text)
    tags = []
    if ENERGY.search(t):
        tags.append("energy")
    if DC_AI.search(text):
        tags.append("data_center_ai")
    return tags


def nw(r):
    try:
        return float(r["latest_net_worth_usd_m"])
    except ValueError:
        return 0.0


people = []
for i, r in enumerate(rows):
    pid = f"P{i:05d}"
    if pid in done:
        continue
    tags = focus(r)
    uri = r["forbes_profile_url"].rstrip("/").rsplit("/", 1)[-1] if r["forbes_profile_url"] else ""
    bio = {}
    if uri and os.path.exists(f"{RTB}/{uri}/bio"):
        try:
            bio = json.load(open(f"{RTB}/{uri}/bio", encoding="utf-8"))
        except json.JSONDecodeError:
            bio = {}
    people.append((0 if tags else 1, -nw(r), {
        "id": pid, "name": r["name"], "name_chinese": r["name_chinese"], "country": r["country"],
        "net_worth_usd_m": r["latest_net_worth_usd_m"], "net_worth_source": r["net_worth_source"],
        "source_of_wealth": r["source_of_wealth"], "industry": r["industry"],
        "sec_insider_companies": r["sec_insider_companies"], "shared_with": r["net_worth_shared_with"],
        "appears_on": r["appears_on"], "focus": tags,
        "forbes_profile_url": r["forbes_profile_url"], "wikidata_url": r["wikidata_url"],
        "forbes_bio": bio.get("bio", []), "forbes_facts": bio.get("about", []),
    }))
people.sort(key=lambda t: (t[0], t[1]))
batch = [p for _, _, p in people[: LANES * PER]]
wd = os.path.join(out_dir, f"wave{wave}")
os.makedirs(wd, exist_ok=True)
for lane in range(LANES):
    chunk = batch[lane::LANES]  # interleave so every lane gets a similar mix
    if not chunk:
        continue
    with open(os.path.join(wd, f"lane_{lane:03d}.jsonl"), "w", encoding="utf-8") as f:
        for p in chunk:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
print(f"wave {wave}: {len(batch)} people in {LANES} lanes; remaining after this wave: {len(people) - len(batch)}")
print("focus mix:", sum(1 for p in batch if p["focus"]), "energy/data-center,", sum(1 for p in batch if not p["focus"]), "other")
