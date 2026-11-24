# due-diligence: a Claude skill for institutional deal diligence

An open-source [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) that runs
private-market due diligence the way an institutional lender, sponsor or investment bank does.

When someone asks you for capital or wants into your syndicate or fund, call the skill. It:

1. **Asks intake questions** and classifies the deal into one or more of 19 deal types and their subtypes.
2. **Builds a due diligence request list (DRL) packet**, ordered by stage (screen, term sheet, confirmatory,
   third-party reports, closing, post-close monitoring). Every item has a priority (gating / core / supporting),
   a workstream, and the form of evidence required. It also builds a management questionnaire, an internal reviewer
   checklist with pass criteria and independent-verification steps, and a tracker (JSON, plus Excel if `openpyxl`
   is installed).
3. **Runs the diligence** on what the sponsor sends back. It tests each item against its pass criterion, recomputes
   the metrics people game, runs kill tests and red flags, and grades the answers to the hard questions.
4. **Decides and reports.** Everything has to pass: one triggered kill test or failed gating item is a decline.
   The report separates what was verified, and how, from what could not be verified.
5. **Red-teams** a pitch deck or draft IC memo on request.

The knowledge base is *The Bible on Due Diligence v2*: about 110,000 words across 22 chapters, citing about 400
sources. They include academic work from Harvard, Wharton, Yale and Princeton, regulators (SEC, OCC, Fed, FDIC,
FinCEN, OFAC), rating-agency criteria, ILPA, NVCA, ABA deal-point studies, and court and enforcement records.
Benchmarks resting on weak sourcing are marked WEAK. Where sources disagree, both figures are kept.

## Deal types and coverage

`universal` applies to every deal: sponsor background, KYC/AML and sanctions, source of funds and wealth, proof of
cash, segregation of duties, valuation, and fraud red flags. Its "subtypes" are deal conditions, such as
`operating-company`, `levered-vehicle` and `earnout`, that switch on the items relevant to the deal. Run
`python3 scripts/dd.py types` to list every subtype.

| Type | Name | Requests | Kill tests | Red flags | Benchmarks | Hard questions | Failure cases |
|---|---|---|---|---|---|---|---|
| `business-debt` | Debt to Businesses | 84 (14 gating) | 7 | 18 | 42 | 16 | 19 |
| `cannabis-hemp` | Cannabis and Hemp | 48 (11 gating) | 6 | 12 | 11 | 9 | 4 |
| `cpg-consumer` | CPG and Consumer Brands | 48 (7 gating) | 5 | 16 | 16 | 13 | 8 |
| `credit` | Credit of All Kinds | 89 (18 gating) | 8 | 19 | 44 | 17 | 18 |
| `crypto-digital-assets` | Crypto and Digital Assets | 61 (13 gating) | 7 | 18 | 12 | 10 | 8 |
| `data-centers` | Data Centers and Digital Infrastructure | 67 (11 gating) | 6 | 15 | 25 | 12 | 12 |
| `energy-infrastructure` | Energy and Infrastructure | 126 (29 gating) | 14 | 31 | 62 | 21 | 17 |
| `evergreen` | Evergreen and Semi-Liquid Vehicles | 57 (16 gating) | 5 | 14 | 24 | 9 | 8 |
| `fund` | Funds, Co-Investments and Manager Selection | 162 (45 gating) | 14 | 34 | 69 | 25 | 29 |
| `growth-equity` | Operating Company Growth Equity | 43 (7 gating) | 6 | 16 | 16 | 10 | 8 |
| `healthcare` | Healthcare Services and Physician Practice Roll-Ups | 68 (22 gating) | 6 | 13 | 12 | 8 | 12 |
| `litigation-finance` | Litigation Finance | 35 (12 gating) | 4 | 7 | 4 | 6 | 6 |
| `nav-lending` | NAV Lending and Fund Finance | 55 (10 gating) | 6 | 12 | 15 | 8 | 9 |
| `niche-assets` | Niche Assets and Further Categories | 67 (15 gating) | 6 | 21 | 16 | 13 | 9 |
| `pe-ma` | Private Equity and M&A | 98 (16 gating) | 8 | 28 | 54 | 22 | 28 |
| `real-estate` | Real Estate | 92 (16 gating) | 12 | 25 | 57 | 21 | 19 |
| `search-fund` | Search Funds and Entrepreneurship Through Acquisition | 54 (16 gating) | 6 | 10 | 20 | 7 | 7 |
| `secondaries` | Secondaries and GP-Led Continuation Vehicles | 56 (17 gating) | 7 | 12 | 16 | 10 | 8 |
| `tech-venture` | Tech and Venture | 103 (19 gating) | 9 | 23 | 42 | 20 | 11 |
| `universal` | Universal (applies to every deal) | 206 (49 gating) | 25 | 74 | 113 | 60 | 57 |
| **Total** | | **1619** | **167** | **418** | **670** | **317** | **297** |

Gating items (16 to 30% of each library) are the ones where a failure alone ends the deal: title, existence of the
cash or collateral, legal ability to do the deal, direct-verification access, and each type's single most important
check.

## Install

Claude Code (all projects):

```bash
cp -r due-diligence ~/.claude/skills/
```

Claude Code (one project): copy the folder to `.claude/skills/due-diligence` in the repo.

Claude apps: zip the `due-diligence` folder and upload it under Settings → Capabilities → Skills.

Requirements: Python 3.8+. Optional: `pip install openpyxl` for the Excel tracker.

## Use

Talk to Claude:

> /due-diligence A developer wants $8M of preferred equity for a 220-unit ground-up multifamily project in Phoenix.
> Build the request packet.

> /due-diligence Here's the data room for Project Atlas (folder attached) and the tracker. Run the review.

> /due-diligence Red-team this deck.

Or use the CLI directly:

```bash
python3 scripts/dd.py types
python3 scripts/dd.py intake --type real-estate
python3 scripts/dd.py packet --type real-estate --subtype construction,multifamily --deal "Phoenix 220" --sponsor "Acme Dev" --out dd-phoenix
python3 scripts/dd.py update --tracker dd-phoenix/tracker.json --id U-FIN-030 --status verified --evidence "Bank confirmation from First Bank, 2026-11-20"
python3 scripts/dd.py status --tracker dd-phoenix/tracker.json
python3 scripts/dd.py report --tracker dd-phoenix/tracker.json
python3 scripts/dd.py validate
```

## Layout

```
SKILL.md            instructions Claude follows
library/            request library, one JSON file per deal type (schema in library/SCHEMA.md)
references/         the full playbook, one Markdown file per chapter, with citations
scripts/dd.py       packet builder, tracker and decision engine (standard library only)
templates/          reply emails, data room folder index, red-team prompt
```

## Contributing

The library is plain JSON so it is easy to review in a pull request. To add or change an item, edit the deal
type's file, keep IDs unique, cite the reference section in `ref`, and run `python3 scripts/dd.py validate`.
The most useful contributions are primary sources for items marked `weak: true`, and practitioner input on the
open gaps in `references/B-open-gaps-interview-guide.md`.

## Disclaimer

This is a diligence workflow and reference, not legal, tax, accounting or investment advice. Benchmarks are
approximate, dated and sometimes disputed; regulatory status is as of November 2026. Background checks must follow
applicable law (for example, US FCRA authorization for consumer reports). Use qualified counsel, accountants and
your own investment committee.

## License

MIT. See `LICENSE`.
