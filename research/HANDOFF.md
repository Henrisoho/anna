# Deep-research hand-off

Goal: for every person in `data/uhnw_individuals.csv`, an agent-researched small profile, an interesting fact, a sourced
deep-cut fact and published contact channels. Research agents follow `research/INSTRUCTIONS.md`.

## State
- `data/uhnw_individuals.csv` — master list; `person_id` (P00000…) is stable. **Don't rebuild this file with
  `scripts/build_uhnw_csv.py` without carrying `person_id` over**, or research results will join to the wrong people.
- `research/lanes/wave1/lane_000…099.jsonl` — wave 1: 2,000 energy / data-center people, 20 per lane.
- `data/research_results.jsonl` — consolidated results so far (one best record per `id`).
- Lanes 000–020 of wave 1 were run in the first session; many later records in those lanes are thin because that
  session's 200-search cap ran out (records with `identity_confirmed: "uncertain"` and empty facts are worth redoing).

## Continue in a new session
Requires `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` raised in the environment settings (the session can't set it).

1. Merge what exists: `python3 scripts/merge_research.py research/out data/research_results.jsonl`
2. Find the next lanes: wave-1 lanes with no output yet (`research/out/wave1/lane_NNN.jsonl` missing), plus a redo
   lane of thin records if wanted.
3. Launch background agents (max 20 concurrent) with the prompt:
   `Read /home/user/anna/research/INSTRUCTIONS.md and follow it exactly. Your assignment: wave 1, lane NNN.`
   Refill a slot each time an agent finishes.
4. Next waves: `python3 scripts/build_research_lanes.py research/lanes 2 100 20` (skips anyone already in a lane).
5. Periodically merge, rebuild `data/uhnw_enriched.csv` with `scripts/enrich_uhnw.py`, commit and push.
