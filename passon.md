# Pass-on: a large researched dataset of ultra-high-net-worth individuals

*Context for a new Claude chat. I built (with Claude Code) a large, researched list of ultra-high-net-worth (UHNW,
$30M+) people. I want help figuring out what to do with it: possible uses, how to slice it, and what to clean up next.*

Repo: `henrisoho/anna`, branch `claude/hopeful-thompson-r5l5kk`. Everything below lives in `data/`.

---

## 1. What exists

| File | What it is | Rows |
|---|---|---|
| `data/uhnw_outreach.csv` | **The working list.** Weeded (see §3), enriched, research merged in. Start here. | 14,725 |
| `data/uhnw_enriched.csv` | Everyone before weeding (master), same columns. | 22,368 |
| `data/uhnw_weeded_out.csv` | Everyone removed, with `weeded_reason`. | 7,643 |
| `data/energy_datacenter_segment.csv` | Example segment: energy and data-center/AI-infrastructure people who are fully researched, confirmed alive and correctly identified, have a sourced little-known fact and a direct published contact, and no red flags. | 317 |
| `data/research_results.jsonl` | Raw per-person research from ~600 AI research agents (one JSON per person). | 9,320 |
| `data/uhnw_individuals.csv` | Underlying merged rich-list data (no enrichment). | 22,368 |
| `data/README.md` | Source list, column definitions, caveats. | – |

### Key columns (in `uhnw_outreach.csv`)
- **Who:** `name`, `name_chinese`, `age` (+ `age_source`), `country`, `current_role`, `title_and_organization`,
  `education`, `home_city` (city only), `self_made`
- **Money:** `latest_net_worth_usd_m` (US$ millions), `net_worth_as_of`, `net_worth_source`, `source_of_wealth`,
  `industry`, `appears_on` (every list + years), `first_listed_year`, `last_listed_year`, `sec_insider_companies`
- **Profile:** `profile` (2–3 sentences), `interesting_fact`, `deep_cut_fact` (a little-known, positive, sourced
  detail), each with a source URL
- **Contact:** `public_contact` (+ `public_contact_source`): only channels the person or their organisation published:
  press / IR / family-office emails, PR agencies, contact forms, official sites, verified X/LinkedIn. **No guessed
  emails, no home addresses, no personal phones.**
- **Judgement:** `research_status`, `research_notes`. The notes flag sanctions, legal trouble, deaths, role changes and
  identity doubts.
- **Links:** `forbes_profile_url`, `wikipedia_url`, `wikidata_url`, `sec_filings_url`

---

## 2. Where the data came from
Forbes (real-time 2026 list plus annual lists 1996–2025), Hurun (Global, China, India, Self-Made Women, U40, Unicorn
founders), Sunday Times Rich List 2020, Wikidata, and SEC insider filings (US execs holding ≥$30M of their company's
stock). These were merged and de-duplicated into 22,368 people. Then:
- **Automated enrichment for everyone:** Forbes bios and "about" facts, Wikidata (education, awards, official
  sites, social accounts), Hurun birth years.
- **Deep research by AI agents:** 9,320 people got a web-researched profile, interesting fact, sourced little-known fact
  and published contacts. Energy and data-center people were researched first.

## 3. How the list was weeded (22,368 → 14,725)
- Known age **under 40** (347) or **90+** (275)
- **Died** since the lists were published (242 found by research)
- **Not a real individual**, i.e. funds, companies, placeholders (46)
- **Low-visibility mainland-Chinese entries** (6,723). About 200 well-known ones were kept: those with an English
  Wikipedia page or their own public channel.
- **Duplicate** English/pinyin names merged (Jack Ma = Ma Yun, Pony Ma = Ma Huateng…)

Every removed row is kept in `uhnw_weeded_out.csv`, so any rule can be reversed.

## 4. Numbers for the working list (14,725)
- **Deep-researched:** 5,801 (39%). The other 8,924 have automated enrichment only.
- **Little-known fact:** 7,586. **Any published contact:** 5,295.
- **Contact types found by research:** press email 1,865, investor relations 1,328, family office/foundation 995,
  contact form 1,003, PR agency 266, X 502, LinkedIn 488, self-published personal email 38.
- **Wealth:** 5,559 billionaires, 3,347 at $100M–1B, 2,010 under $100M, and 3,809 with no figure. The no-figure group is
  mostly unicorn founders, included because they founded a $1B+ company.
- **Where they come from:**
  - Hurun unicorn founders 3,809
  - SEC insider filings 3,162
  - Forbes real-time list 2,713
  - Hurun Global 1,532
  - Sunday Times 989
  - Hurun India 831
  - The rest from older lists and Wikidata
- **Age known:** 5,085. **Country unknown:** 7,448 (mostly SEC-only US executives and unicorn founders).
- **Top countries:** US 1,657 · UK 1,192 · India 1,115 · Germany 342 · Russia 247 · China 207 · Brazil 159
- **Research notes mentioning sanctions:** 105

## 5. Caveats
- **Verify before relying on it.** Contacts and roles were checked by AI agents against published pages, but some came
  from search snippets (flagged in notes). Several people changed roles in 2025–26.
- **Most contacts are corporate** (press, investor relations, PR agencies), not personal. Only 38 people self-publish a
  personal email.
- **Flagged people** (sanctioned, detained, in court, company collapsed) are marked in `research_notes`.
- **A few duplicates remain** (e.g. "Bill Gates" and "William H. III Gates"). Spot-check big names.
- **Old-list-only entries** (`last_listed_year` < ~2018) may no longer be rich or active.
- Net worth figures are approximate and mixed-source. SEC figures are lower bounds (public stock only).
- **Legal:** this is personal data about real people (from public sources). Any outreach to EU/UK residents falls
  under GDPR/PECR, and to US residents under CAN-SPAM. Keep any contact individual and relevant, not bulk.

## 6. Open questions (what I'd like help thinking through)
1. **What's this useful for?** e.g. business development, fundraising/investor targeting, partnerships, content,
   market research on where wealth comes from. Which uses fit the data's strengths (profiles, facts, published
   channels) and limits (mostly corporate contacts)?
2. **How to segment it:** by industry, country, wealth band, self-made vs inherited, age, and whether there's a
   reachable contact.
3. **More weeding?** Options:
   - drop the 3,162 SEC-only US execs (mostly $30–100M insiders);
   - drop the ~3,800 unicorn founders with no known net worth;
   - drop old-list-only entries;
   - keep only $100M+.
4. **Finish the research?** 8,924 people in the working list have automated data only. Deep research costs a lot of
   Claude usage: the account hit its weekly limit last time. It could be restricted to the most valuable remaining
   segments.
5. **Packaging:** a spreadsheet or CRM with filters, or a database.

## 7. How the research can resume (if wanted)
All the tooling is in the repo: `research/HANDOFF.md`, `research/INSTRUCTIONS.md`, `research/lanes/wave2..wave11`
(people still to research), `scripts/collect_research.sh` (merges results), `scripts/enrich_uhnw.py` and
`scripts/build_outreach.py` (rebuild the files above). Ten "wave" cloud sessions hold partial progress and can be
told to continue.
