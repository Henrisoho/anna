# Deep-research lane instructions

You are one of ~100 parallel research agents building profiles of ultra-high-net-worth people for a journalist
starting an entrepreneurship / energy / data-center podcast. Your lane is a JSONL file of ~20 people. Research each
person and append one JSON line per person to your output file. This is research only: never contact anyone.

## Files
- Input: `/home/user/anna/research/lanes/wave<W>/lane_<NNN>.jsonl` (one person per line; fields include `id`, `name`,
  `country`, `source_of_wealth`, `sec_insider_companies`, `forbes_bio`, `forbes_facts`, `forbes_profile_url`, `wikidata_url`).
- Output: `/home/user/anna/research/out/wave<W>/lane_<NNN>.jsonl` (create the directory if needed).
- Resumable: if the output file exists, skip ids already in it. Append each person's line as soon as you finish them
  (e.g. `python3 -c` or a heredoc `>>`), so progress survives if you are interrupted.

## Isolation (important — ~20 agents run at once)
- Put any helper scripts or temp files ONLY in `/home/user/anna/research/tmp/lane_<NNN>/` (create it). Never use the
  shared scratchpad or another lane's paths, and never write to any output file except your own lane's.
- If web search reports a rate/usage limit, wait ~60s and retry once, then fall back to `curl` on Wikipedia, company
  sites, press releases and filings.

## Tools
- Load web search with ToolSearch (`select:WebSearch`); use `mode: "standard"`. Also load `WebFetch` if available.
  The network is open, so `curl -sL --max-time 20 <url>` also works for reading a page (pipe through
  `python3 -c` / `sed` to strip HTML). Budget roughly 3–6 searches/fetches per person; move on rather than stall.

## Tips for Chinese names (from earlier lanes)
- Hurun's own list data is the best way to decode its English company labels: `https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=<list code>&search=<name>&offset=0&limit=20` (send header `X-Requested-With: XMLHttpRequest`) returns the Chinese name, Chinese company name, city and birth year.
- Exchange filings: eastmoney announcement PDFs (`pdf.dfcfw.com`) and SEC full-text search work when Baidu/cninfo/Sogou are blocked. Toutiao search (`so.toutiao.com`) and 360 search (`m.so.com`) work for Chinese news.

## For each person, produce
1. **identity check** — confirm who they are (the listed company/source of wealth should match). If the name is
   ambiguous and you can't tell which person it is, say so and keep the rest minimal.
2. **alive** — yes / no / unknown. If they have died, record it with the source and skip the rest.
3. **current_role** — current title and organisation (one line).
4. **profile** — 2–3 sentences: who they are, how they made their money, what they are doing now.
   If `forbes_bio` is provided, condense/update it rather than re-researching.
5. **interesting_fact** — something notable and genuinely interesting (can come from `forbes_facts`).
6. **deep_cut_fact** — a specific, little-known, TRUE fact that would impress the person if mentioned in an outreach
   note: e.g. an early job, a first company that failed, a niche hobby or record, a specific philanthropic project,
   a hometown detail, a technical contribution, a quote from an old interview. Must be verifiable: give the source
   URL. Positive or neutral only — no scandals, lawsuits, family conflict, health or wealth losses. If you cannot
   find a sourced one, leave it empty rather than inventing one.
7. **public_contacts** — ways to reach them that have been PUBLISHED by them or their organisation, best first:
   - `personal_email` (only if they published it themselves, e.g. on their own site or a public post)
   - `office_email` (their family office / foundation / personal office, as published)
   - `press_email` / `ir_email` (the company's published press or investor-relations contact)
   - `pr_agency` (published PR firm contact for them or the company)
   - `contact_form` (URL of an official contact or press-inquiry form)
   - `official_website`, `x`, `linkedin`, `instagram`, `substack`, `podcast` (their own verified accounts/sites)
   Every contact needs the `source_url` where it is published.

## Hard rules
- No guessed or pattern-constructed emails (first.last@company.com), no email-finder/enrichment tools, data brokers,
  leaked data or people-search sites.
- No home addresses, personal phone numbers, family members' contacts or anything about their children.
- Don't make anything up. Empty fields are fine; wrong facts are not. Facts must be about THIS person.
- Keep each text field under ~350 characters.

## Output line (JSON, one per person)
{"id": "...", "name": "...", "identity_confirmed": "yes|no|uncertain", "alive": "yes|no|unknown",
 "current_role": "...", "profile": "...", "interesting_fact": "...", "interesting_fact_source": "url",
 "deep_cut_fact": "...", "deep_cut_fact_source": "url",
 "public_contacts": [{"type": "press_email", "value": "...", "source_url": "..."}],
 "notes": "anything the journalist should know (e.g. very private, best route is via X)"}

When the lane is done, reply with one line: `lane <NNN>: <n> done, <n> with deep-cut fact, <n> with a contact`.
