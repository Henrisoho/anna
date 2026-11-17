"""Build data/billionaires_all.csv from the komed3/rtb-api archive of the Forbes real-time list.

Usage: python3 scripts/build_billionaires_csv.py <path-to-rtb-api-list-json> [out.csv]
The list JSON lives at api/list/rtb/<YYYY-MM-DD> in https://github.com/komed3/rtb-api (MIT).
"""
import csv
import json
import re
import sys

ENERGY_WORDS = r"oil|gas|petro|energy|power|solar|wind|battery|batteries|pipeline|utilit|nuclear|coal|refin|lng|fuel|hydrogen|renewable|electric|grid|catl|reliance|adani green"
DC_AI_WORDS = (
    r"nvidia|oracle|dell|amd|coreweave|iren|astera|nebius|super ?micro|semiconductor|chip|broadcom|tsmc|"
    r"data ?cent|cloud|quanta|foxconn|hon hai|arista|vertiv|equinix|airtrunk|crusoe|lambda|applied digital|"
    r"artificial intelligence|\bai\b|openai|anthropic|xai|scale ai|cerebras|groq|marvell|micron|sk hynix|"
    r"wiwynn|wistron|inventec|asml|lam research|applied materials|cooling|server"
)
ENERGY_FALSE_POSITIVES = r"palm oil|edible oil|energy drink|vegas|power strip|gas station|electric (bike|scooter)|olive oil"
HYPERSCALER_WORDS = r"microsoft|amazon|google|alphabet|meta|facebook|tesla|spacex|alibaba|tencent|bytedance|baidu"


def tag(record):
    text = " ".join(record.get("source", []) + record.get("industry", [])).lower()
    tags = []
    energy_text = re.sub(ENERGY_FALSE_POSITIVES, "", text)
    if "energy" in record.get("industry", []) or re.search(ENERGY_WORDS, energy_text):
        tags.append("energy")
    if re.search(DC_AI_WORDS, text):
        tags.append("data_center_ai")
    if re.search(HYPERSCALER_WORDS, text):
        tags.append("big_tech_hyperscaler")
    return ";".join(tags)


def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "data/billionaires_all.csv"
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    fields = [
        "rank", "name", "net_worth_usd_bn", "age", "gender", "citizenship",
        "industry", "source_of_wealth", "podcast_relevance", "forbes_profile_url",
        "list_date",
        # filled in later by contact research; only published channels, each with a source URL
        "contact_type", "contact_value", "contact_source_url", "notes",
    ]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in data["list"]:
            w.writerow({
                "rank": r.get("rank"),
                "name": r.get("name"),
                "net_worth_usd_bn": round(r["networth"] / 1000, 2) if r.get("networth") is not None else "",
                "age": r.get("age", ""),
                "gender": r.get("gender", ""),
                "citizenship": (r.get("citizenship") or "").upper(),
                "industry": "; ".join(r.get("industry", [])),
                "source_of_wealth": "; ".join(r.get("source", [])),
                "podcast_relevance": tag(r),
                "forbes_profile_url": f"https://www.forbes.com/profile/{r['uri']}/" if r.get("uri") else "",
                "list_date": data.get("date", ""),
            })
    print(f"wrote {len(data['list'])} rows to {out} (list date {data.get('date')})")


if __name__ == "__main__":
    main()
