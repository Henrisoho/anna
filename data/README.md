# Data

## `uhnw_individuals.csv` — known ultra-high-net-worth individuals (≥ $30M)

One row per living person, merged and de-duplicated from public rich lists and SEC filings.
Built by `scripts/build_uhnw_csv.py` (SEC part: `scripts/sec_insiders.py`).

### Sources
| List | Coverage | Where it came from |
|---|---|---|
| Forbes real-time billionaires | current (daily) + people who dropped off since ~2021 | [komed3/rtb-api](https://github.com/komed3/rtb-api) (MIT) |
| Forbes World's Billionaires (annual) | 1996–2025 | [FilesUploader/Forbes-Billionaire-List](https://github.com/FilesUploader/Forbes-Billionaire-List) |
| Hurun Global Rich List | 2014–2026 | [FilesUploader/Hurun-GRL](https://github.com/FilesUploader/Hurun-GRL) + hurun.net |
| Hurun China Rich List | 1999–2026 (cutoff ~$300M–$700M recent years) | hurun.net |
| Hurun India Rich List | 2015–2022 (cutoff ₹1,000 crore ≈ $120M; 2020–22 top 100 only) | hurun.net |
| Hurun Self-Made Women, Global U40, China U40 | various years | hurun.net |
| Sunday Times Rich List | 2020 (UK top 1,000) | [harveydevereux/TimesRichList2020](https://github.com/harveydevereux/TimesRichList2020) |
| Wikidata | living people with a net-worth statement ≥ $30M | query.wikidata.org |
| SEC insider filings (Forms 3/4/5) | Q4 2024 – Q3 2026 | [SEC Insider Transactions Data Sets](https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets) |

### Columns
- `latest_net_worth_usd_m`, `net_worth_as_of`, `net_worth_source` — most recent estimate (US$ millions). Rich-list figures are preferred; `SEC insider holdings` means the only figure is the SEC estimate (a lower bound: public stock in companies where they are an insider, valued at the median recent open-market trade price).
- `net_worth_shared_with` — Hurun joint entries (couples/families) share one figure.
- `appears_on` — every list and year range the person appears on; `first_listed_year` / `last_listed_year`.
- `possibly_deceased` — name matches a Wikidata death record but the person is still on a recent list (check manually).
- `forbes_profile_url`, `wikidata_url`, `sec_filings_url`, `sec_insider_companies`.

### Caveats
- People are matched by name. Different people with identical names can occasionally be merged, and one person can appear twice under different spellings.
- Rows seen only on old lists (`last_listed_year` well in the past) may have lost their wealth or died without it being recorded; confirmed deaths (Forbes flag, or a Wikidata death record for people not listed since 2024) are removed.
- Currency conversions for Wikidata, Sunday Times and Hurun India values are approximate.
- No contact details or addresses are included. The SEC data contains mailing addresses; they are deliberately not used.

## `uhnw_enriched.csv` — the same people with profiles, facts and published contacts
Built by `scripts/enrich_uhnw.py` from `uhnw_individuals.csv` plus:
- Forbes profile bios and "about" facts (≈5,000 Forbes-tracked people),
- Wikidata (description, education, awards, official website, public social accounts) and Wikipedia summaries,
- agent deep research (`research_results.jsonl`, see `research/`), which overrides the automated fields.

Extra columns: `age`, `title_and_organization`, `self_made`, `self_made_score_1to10`, `home_city` (city only),
`education`, `current_role`, `profile` (+ `profile_source`), `interesting_fact` (+ source), `deep_cut_fact`
(+ source), `public_contact` (+ `public_contact_source`), `research_status`, `research_notes`, `wikipedia_url`.

`public_contact` only contains channels published by the person or their organisation (company press/IR inboxes,
family-office or foundation inboxes, contact forms, official websites and verified social accounts), each with the
page it was found on. No guessed emails, no home addresses, no personal phone numbers.
Read `research_notes` before outreach: it flags sanctions, legal issues, retirements, deaths and identity doubts.

## `uhnw_outreach.csv` — the outreach list
`uhnw_enriched.csv` minus people unlikely to engage (built by `scripts/build_outreach.py`): known age under 40 or 90+,
people research found to have died, records that are not an identifiable individual, and mainland-China entries
without international visibility (kept only with an English Wikipedia article or a personal public channel).
Duplicates of the same Chinese entrepreneur under English and pinyin names (e.g. Jack Ma / Ma Yun) are merged.
Unknown ages are kept.
Removed rows, with the reason, are in `uhnw_weeded_out.csv`. Ages come from Forbes, Wikidata or Hurun birth years
(`age_source`; Hurun ages are approximate).

## Other files
- `billionaires_all.csv` — Forbes real-time list (2026-11-16) with energy / data-center relevance tags.
- `energy_datacenter_pilot.csv` — 25 energy and data-center billionaires with published press contacts.
- `sec_insiders_30m.csv` — intermediate SEC output (all insiders with ≥ $30M estimated public holdings, before filtering).
