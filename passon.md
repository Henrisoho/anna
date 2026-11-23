# Pass-on: UHNW guest list for an energy / data-center / entrepreneurship podcast

*Context for a new Claude chat. I'm starting a podcast about the energy and data-center world, focused on
entrepreneurship. I built (with Claude Code) a big researched list of ultra-high-net-worth people and want help
deciding what to do with it: who to pitch first, how to pitch, and what to clean up next.*

Repo: `henrisoho/anna`, branch `claude/hopeful-thompson-r5l5kk`. Everything below lives in `data/`.

---

## 1. What exists

| File | What it is | Rows |
|---|---|---|
| `data/uhnw_outreach.csv` | **The working list.** Weeded (see §3), enriched, research merged in. Start here. | 14,725 |
| `data/podcast_shortlist.csv` | **Best leads now:** energy or data-center/AI-infra people who are researched, confirmed alive and correctly identified, have a sourced deep-cut fact AND a direct published contact, and no red flags in their notes. | 317 |
| `data/uhnw_enriched.csv` | Everyone before weeding (master), same columns. | 22,368 |
| `data/uhnw_weeded_out.csv` | Everyone removed, with `weeded_reason`. | 7,643 |
| `data/research_results.jsonl` | Raw per-person research from ~600 AI research agents (one JSON per person). | 9,320 |
| `data/uhnw_individuals.csv` | Underlying merged rich-list data (no enrichment). | 22,368 |
| `data/README.md` | Source list, column definitions, caveats. | – |

### Key columns (in `uhnw_outreach.csv`)
- **Who:** `name`, `name_chinese`, `age` (+ `age_source`), `country`, `current_role`, `title_and_organization`
- **Money:** `latest_net_worth_usd_m` (US$ millions), `net_worth_as_of`, `net_worth_source`, `source_of_wealth`, `industry`, `appears_on` (every list + years), `last_listed_year`
- **Story:** `profile` (2–3 sentences), `interesting_fact`, `deep_cut_fact` (+ `_source` URLs). The deep-cut facts are little-known, positive, sourced details meant to open a pitch ("you started as a dishwasher at 12…").
- **Reach:** `public_contact` (+ `public_contact_source`): only channels the person or their organisation published: press / IR / family-office emails, PR agencies, contact forms, official sites, verified X/LinkedIn. **No guessed emails, no home addresses, no personal phones.**
- **Judgement:** `research_status`, `research_notes`. **Read the notes before contacting anyone.** They flag sanctions, legal trouble, deaths, role changes and identity doubts.
- **Links:** `forbes_profile_url`, `wikipedia_url`, `wikidata_url`, `sec_filings_url`

---

## 2. Where the data came from
Forbes (real-time 2026 list plus annual lists 1996–2025), Hurun (Global, China, India, Self-Made Women, U40, Unicorn
founders), Sunday Times Rich List 2020, Wikidata, and SEC insider filings (US execs holding ≥$30M of their company's
stock). These were merged and de-duplicated into 22,368 people. Then:
- **Automated enrichment for everyone:** Forbes bios and "about" facts, Wikidata (education, awards, official
  sites, social accounts), Hurun birth years.
- **Deep research by AI agents:** 9,320 people got a web-researched profile, interesting fact, sourced deep-cut fact
  and published contacts. Energy and data-center people went first.

## 3. How the list was weeded (22,368 → 14,725)
- Known age **under 40** (347) or **90+** (275)
- **Died** since the lists were published (242 found by research)
- **Not a real individual**, i.e. funds, companies, placeholders (46)
- **Low-visibility mainland-Chinese entrepreneurs** (6,723). About 200 well-known ones were kept: those with an English
  Wikipedia page or their own public channel (Zhang Yiming, CATL's Robin Zeng, Lei Jun, BYD's Wang Chuanfu, Jack Ma…).
- **Duplicate** English/pinyin names merged (Jack Ma = Ma Yun, Pony Ma = Ma Huateng…)

## 4. Numbers for the working list (14,725)
- **Deep-researched:** 5,801 (39%). The other 8,924 have automated enrichment only.
- **Deep-cut fact:** 7,586. **Any published contact:** 5,295.
- **Contact types found by research:** press email 1,865, investor relations 1,328, family office/foundation 995,
  contact form 1,003, PR agency 266, X 502, LinkedIn 488, podcast appearances 110, self-published personal email 38.
- **Wealth:** 5,559 billionaires, 3,347 at $100M–1B, 2,010 under $100M, and 3,809 with no figure. The no-figure group is
  mostly unicorn founders, included because they founded a $1B+ company.
- **Age known:** 5,085. **Country unknown:** 7,448 (mostly SEC-only US executives and unicorn founders).
- **Top countries:** US 1,657 · UK 1,192 · India 1,115 · Germany 342 · Russia 247 · China 207 · Brazil 159
- **Research notes mentioning sanctions:** 105

## 5. Strong leads for the show (from `podcast_shortlist.csv` and research notes)

**Data centers / AI infrastructure**
- **Michael Intrator, Brian Venturo, Brannin McBee** (CoreWeave). The co-founders came from natural-gas trading. Contact: press@coreweave.com
- **Jim Trout** (founder of Vantage Data Centers, now CEO of CleanArc, building a 900 MW Virginia campus). Contact: CleanArc's PR firm
- **Rick Perry** (co-founder of Fermi America, a 17 GW private power + AI campus in Texas) and **Griffin Perry**. Contact: media@fermiamerica.com
- **Gary Wu, Jamie Cox** (Fluidstack). **Josh Payne** (Nscale). **Daniel & Will Roberts** (IREN). **Jason Zhang** (Applied Digital)
- **Jensen Huang / Colette Kress** (Nvidia). One agent reported a Nov 2026 CEO change; **verify before pitching**
- **Chris Ré** (Stanford, "Intelligence Per Watt" study on AI power limits). He publishes his own email

**Power / energy**
- **Mac McFarland** (Talen: nuclear power sold to AWS data centers). **Joseph Dominguez** (Constellation: Three Mile Island restart for Microsoft)
- **Jacob DeWitte** (Oklo microreactors). **Doug Bernauer, Bob Urberger** (Radiant microreactors; Equinix pre-ordered 20). **Robert Mumgaard** (Commonwealth Fusion; Google power deal)
- **KR Sridhar** (Bloom Energy fuel cells for data centers). **Lawrence Coben** (NRG; also a working archaeologist)
- **Michael Polsky** (Invenergy). **Harold Hamm** (fracking pioneer; his Hamm Institute runs an "American Energy AI Initiative")
- **Brad Keywell** (Gigawatt AI, AI software for utilities; has his own podcast). **Haiyun Cao** (JinkoSolar; pitches solar for AI). **Yet-Ming Chiang** (MIT battery pioneer)
- **Michael Sabel / Robert Pender** (Venture Global LNG). **Kelcy Warren** (Energy Transfer). **Richard Kinder** (Kinder Morgan)

**Easy-to-reach and media-friendly:** Guillermo Rauch (Vercel), Amjad Masad (Replit), Brendan Foody (Mercor),
Lukas Biewald (hosts the Gradient Dissent podcast, now at CoreWeave), Peter Mallouk (runs his own podcasts), Satyen Sangani
(hosts AI Radicals), Bret Taylor and Greg Brockman (both publish their own email; Brockman is 38, so he was weeded out
by the age rule but is still in `uhnw_enriched.csv`).

## 6. Caveats to keep in mind
- **Verify before sending.** Contacts and roles were checked by AI agents against published pages, but some came from
  search snippets (flagged in notes). Several people changed roles in 2025–26.
- **Most contacts are corporate** (press, investor relations, PR agencies), not personal. That's the normal route for
  guest booking. Only 38 people self-publish a personal email.
- **Don't pitch flagged people.** Avoid anyone sanctioned (Russian oligarchs especially), detained, in court, or
  whose company recently collapsed. `research_notes` says which.
- **A few duplicates remain** (e.g. "Bill Gates" and "William H. III Gates"). Spot-check big names.
- **Old-list-only entries** (`last_listed_year` < ~2018) may no longer be rich or active.
- Net worth figures are approximate and mixed-source. SEC figures are lower bounds (public stock only).
- **Legal:** cold outreach to EU/UK people falls under GDPR/PECR, and to US people under CAN-SPAM. Keep pitches
  individual, relevant and easy to decline. Don't mass-blast.

## 7. Open decisions (what I'd like help thinking through)
1. **Who to pitch first.** I'd suggest the 317 in `podcast_shortlist.csv`, tiered by fit and reachability. Big names
   via PR, and mid-tier founders (more likely to say yes) directly.
2. **The pitch.** A short, personal email per guest that uses the `deep_cut_fact` and the show's energy/data-center
   angle. Templates for: press office, PR agency, founder's own channel, LinkedIn/X DM.
3. **More weeding?** Options:
   - drop the 3,162 SEC-only US execs (mostly $30–100M insiders);
   - drop the ~3,800 unicorn founders with no known net worth;
   - drop old-list-only entries;
   - keep only $100M+.
4. **Finish the research?** 8,924 people in the working list still have automated data only. Deep research costs a lot
   of Claude usage: the account hit its weekly limit last time. It could be restricted to the best remaining segments.
5. **Tracking.** Move the shortlist into a CRM/sheet with status columns (pitched, replied, booked).

## 8. How the research can resume (if wanted)
All the tooling is in the repo: `research/HANDOFF.md`, `research/INSTRUCTIONS.md`, `research/lanes/wave2..wave11`
(people still to research), `scripts/collect_research.sh` (merges results), `scripts/enrich_uhnw.py` and
`scripts/build_outreach.py` (rebuild the files above). Ten "wave" cloud sessions hold partial progress and can be
told to continue.
