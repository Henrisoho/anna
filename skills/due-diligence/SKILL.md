---
name: due-diligence
description: Institutional due diligence for private-market deals (real estate, venture, PE/M&A, business debt, credit, energy, data centers, funds, secondaries, NAV loans, evergreen funds, search funds, healthcare, crypto, cannabis, CPG, litigation finance and niche assets). Use when a sponsor, founder or manager wants capital or wants into a syndicate or fund and you need to (1) classify the deal and send a due diligence request list (DRL) packet, (2) review what they sent against pass criteria, kill tests and red flags, (3) produce a diligence report with an approve/decline decision, or (4) red-team a pitch deck. Triggers on "due diligence", "DD request", "DRL", "data room request", "diligence packet", "vet this deal", "review this data room", "red-team this deck", "IC memo".
---

# Due Diligence

Run diligence the way an institutional lender, sponsor or large investment bank does: classify the deal, send an
ordered request list, verify everything independently, and decide only on what was confirmed.

**The spine:** verify the sponsor, verify the cash, verify the collateral or the earnings, verify the legal title,
and verify that you see every claim on the same asset. Then separate what you confirmed from what you could not.

**Everything has to pass.** A deal is approved for the investment committee only when every gating and core request is
verified (core items may be waived with a written exception), every kill test is clear, and no red flag is open.
One triggered kill test or one failed gating item is a decline.

## What is in this skill

| Path | What it is |
|---|---|
| `library/*.json` | The request library: one file per deal type, plus `universal.json` which applies to every deal. Each holds intake questions, subtypes, ordered request items with pass/fail criteria and an independent-verification step, kill tests, red flags, benchmarks, third-party reports, hard questions and failure cases. Schema: `library/SCHEMA.md`. |
| `references/*.md` | The full playbook (The Bible on Due Diligence v2), one file per chapter, with every number cited. Load only the chapters for the deal at hand. `00-master-playbook.md` is large: grep for the section you need (e.g. `## 0.4`). |
| `scripts/dd.py` | CLI that builds packets, tracks review status and makes the decision. Python 3 standard library; Excel output if `openpyxl` is installed. |
| `templates/` | Reply email, data room folder index, and the red-team prompt. |

Run the CLI from anywhere: `python3 <skill-dir>/scripts/dd.py <command>`. `dd.py types` lists every deal type and subtype.

## Mode 1: Someone reached out. Build their packet.

1. **Intake.** Ask the intake questions conversationally, not as a wall. Start with the universal ones
   (`dd.py intake`): what it is, deal type, size, instrument, stage, use of proceeds, timeline, who the sponsor is,
   who else is in, jurisdiction. Once the type is clear, ask that type's questions (`dd.py intake --type <type>`)
   to pick subtypes. If the user already gave the answers, don't ask again.
2. **Classify.** Map to one or more types from `dd.py types` and the subtypes that apply. Combine types when the
   deal spans them (a data center with on-site generation: `data-centers,energy-infrastructure`; a fund raising a
   NAV loan: `fund,nav-lending`). If you pick no subtype, every subtype's items are included, so pick them when known.
3. **Build.** `dd.py packet --type <types> --subtype <subtypes> --deal "<name>" --sponsor "<name>" --out <dir>`.
   This writes:
   - `01_request_list.md`: the sponsor-facing list, ordered by stage (screen, term sheet, confirmatory,
     third party, closing, monitoring), with priority, workstream and the evidence format, plus the management
     questionnaire. Send this.
   - `02_reviewer_checklist.md`: internal. Pass criteria, how to verify each item independently, kill tests, red
     flags, benchmarks, third-party reports to commission, good-answer guides for the hard questions, failure cases.
     Never send this to the sponsor.
   - `03_tracker.xlsx` (if openpyxl) and `tracker.json`: the review state.
4. **Reply.** Draft the reply from `templates/reply_email.md`: thank them, name the deal type, attach Stage 1 only
   (screen items), say later stages follow once Stage 1 clears, and include the authorizations for direct
   verification (bank, background check). Show the user the draft; do not send anything yourself unless asked.
5. Tell the user the counts (requests by priority, kill tests, red flags) and the deal type's THE ONE CHECK.

## Mode 2: They sent materials. Run the diligence.

Ask for the tracker (`tracker.json` from Mode 1; if there is none, build the packet first) and the materials
(data room folder, files, links). Then work stage by stage, gating items first.

1. **Read the playbook for this deal.** Open the chapters listed at the end of `02_reviewer_checklist.md`, plus
   `00-master-playbook.md` sections 0.2 to 0.5. Read the type's failure cases: they tell you what to look for.
2. **Test each request against its `pass` criterion** using the documents provided. Record every result:
   `dd.py update --tracker T --id <ID> --status <status> --evidence "<doc, page, figure, who confirmed>" --note "<why>"`
   or many at once with `dd.py bulk --tracker T --json updates.json`.
   - `received`: the document is in hand but not yet independently verified.
   - `verified`: it meets the pass criterion AND the `verify` step was done (confirmed with the issuer, recomputed
     from raw data, or matched to a public record). A sponsor-produced copy alone is never `verified`.
   - `failed`: it misses the pass criterion. Say by how much.
   - `waived` (core or supporting only) or `n/a`: needs a written reason. Gating items cannot be waived.
3. **Recompute, don't accept.** Rebuild every gamed metric from raw data (NRR, adjusted EBITDA and add-backs, DSCR,
   LTV, borrowing base, IRR/MOIC, cap rate). Compare to the type's `metrics` benchmarks. Where the bible gives
   conflicting benchmarks, show both; never average them. Flag any test that relied on a `weak` benchmark.
4. **Run the kill tests and red flags.** Mark each kill test `clear` or `triggered` and each red flag `clear`,
   `present` or `mitigated`, with the evidence. Look for the patterns in the failure cases, especially: one person
   controls decisions, cash and reporting; no independent administrator, custodian or auditor; returns smoother than
   the strategy allows; the same collateral pledged more than once; refusal of direct third-party confirmation.
5. **Hard questions.** Grade each answer against `good_answer`: `good`, `weak` or `evaded`. Treat evasion as a red flag.
6. **Check progress** at any point with `dd.py status --tracker T`. It lists exactly what blocks approval.
7. **Report.** `dd.py report --tracker T` writes `diligence_report.md` with the decision, what was verified and how,
   what could NOT be verified, red flags, kill tests, waivers and weak benchmarks. Then complete the narrative
   sections it lists (deal summary, the numbers with base and downside cases and return attribution, third-party
   reports, open concerns, recommendation and conditions) using `references/A-templates.md` (A.2) and the IC memo
   skeleton (`## 0.7`). Run the IC bias audit (`## 0.12`, form A.4) before recommending approval.

Be explicit about the limits of a desk review: background checks, bank confirmations, site visits, appraisals and
independent engineer reports are done by people and third parties. When one is required and has not been done, the
item stays open. Do not invent evidence, do not assume a document says what the sponsor claims, and do not mark
anything verified that you did not check.

## Mode 3: Red-team a deck or draft memo

Use `templates/red_team_prompt.md` (from Appendix A.3) with the deal type's failure cases, red flags and hard
questions. Output: every claim presented as fact that is not independently sourced; every gameable metric with the
raw recomputation you need; the single check that kills the deal if it fails; missing third parties; what the sponsor
verified versus asserted; the documents to ask for first.

## Mode 4: Quick screen

If the user just pastes a deck or a description and wants a fast read: classify it, apply the screen-stage items,
kill tests and THE ONE CHECK for its type, and return a one-page screen (pass to term sheet, ask for more, or
reject) plus the Stage 1 request list. Say clearly that it is a screen, not diligence.

## Rules

- Present conflicting sources side by side. Mark WEAK benchmarks as WEAK. Dated figures keep their year.
- Regulatory status in the references is as of November 2026. Check for changes before relying on it.
- Background checks and screening are about professional and public records (litigation, regulatory, sanctions,
  bankruptcy, adverse media). Get the subject's written authorization where the law requires it (e.g. consumer
  reports under the US FCRA). Do not dig into private life beyond what diligence needs.
- This skill supports a diligence process. It is not legal, tax, accounting or investment advice; deals still need
  counsel, accountants and the investment committee.
