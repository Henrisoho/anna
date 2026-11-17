#!/usr/bin/env bash
# Pull research results pushed by the per-wave sessions (branches claude/research-waveN) and merge them,
# together with this session's local results, into data/research_results.jsonl and data/uhnw_enriched.csv.
# Usage: scripts/collect_research.sh [local_out_dir]
set -euo pipefail
cd "$(dirname "$0")/.."
LOCAL_OUT="${1:-/home/user/datasets/deep/out}"
STAGE=$(mktemp -d)
for w in $(seq 3 12); do
  b="claude/research-wave$w"
  if git fetch -q --depth=1 origin "$b" 2>/dev/null; then
    mkdir -p "$STAGE/wave$w"
    git archive FETCH_HEAD "research/out/wave$w" 2>/dev/null | tar -x -C "$STAGE/wave$w" 2>/dev/null || true
    n=$(find "$STAGE/wave$w" -name 'lane_*.jsonl' | wc -l)
    echo "wave $w: $n lane files"
  else
    echo "wave $w: branch not pushed yet"
  fi
done
mkdir -p research/out
[ -d "$LOCAL_OUT" ] && cp -r "$LOCAL_OUT"/. "$STAGE/local/" 2>/dev/null || mkdir -p "$STAGE/local" && cp -r "$LOCAL_OUT"/. "$STAGE/local/" 2>/dev/null || true
python3 -I scripts/merge_research.py "$STAGE" data/research_results.jsonl
python3 -I scripts/enrich_uhnw.py data/uhnw_enriched.csv > /dev/null
rm -rf "$STAGE"
