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

## Deal types

`real-estate` · `business-debt` · `credit` · `tech-venture` · `pe-ma` · `growth-equity` · `cpg-consumer` ·
`cannabis-hemp` · `energy-infrastructure` · `data-centers` · `crypto-digital-assets` · `niche-assets` · `fund` ·
`secondaries` · `nav-lending` · `evergreen` · `search-fund` · `healthcare` · `litigation-finance`, plus `universal`,
which applies to every deal (sponsor background, KYC/AML and sanctions, source of funds and wealth, proof of cash,
segregation of duties, valuation, fraud red flags).

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
