# Request library schema

Every deal type is one JSON file in this folder (`<type-id>.json`). `universal.json` applies to every deal and is
always merged in first. Files are plain JSON so the library has no dependencies and is easy to diff and edit.

## File shape

```json
{
  "type": "real-estate",
  "name": "Real Estate",
  "summary": "One paragraph: what deals this covers and what the diligence spine is for this type.",
  "chapters": ["01-real-estate.md"],
  "one_check": "THE ONE CHECK for this deal type, one sentence.",
  "subtypes": [
    {"id": "construction", "name": "Ground-up construction", "description": "..."}
  ],
  "intake_questions": [
    {"id": "RE-Q01", "question": "Is this stabilized, value-add, or ground-up construction?",
     "why": "Drives which subtype items apply.", "sets_subtype": true}
  ],
  "requests": [ ...request items, see below... ],
  "kill_tests": [
    {"id": "RE-K01", "test": "No independent appraisal from a state-certified appraiser engaged by us or the lender.",
     "ref": "1.9", "applies_to": ["all"]}
  ],
  "red_flags": [
    {"id": "RE-RF01", "flag": "Rent roll does not tie to bank deposits.",
     "check": "Reconcile 12 months of deposits to the rent roll unit by unit.", "ref": "1.9", "applies_to": ["all"]}
  ],
  "metrics": [
    {"id": "RE-M01", "metric": "Loan-to-value (construction, supervisory limit)", "acceptable": "<= 80% (commercial construction)",
     "source": "Interagency supervisory LTV limits, 12 CFR 34 App. A", "weak": false, "ref": "1.2", "applies_to": ["construction"]}
  ],
  "third_party_reports": [
    {"id": "RE-T01", "report": "MAI appraisal", "provider": "State-certified appraiser engaged by us or the lender",
     "required_when": "Always", "ref": "1.6"}
  ],
  "hard_questions": [
    {"id": "RE-HQ01", "question": "What happens to DSCR if the exit cap rate is 100 bp wider?",
     "good_answer": "A sensitivity table the sponsor built before being asked, with a refinance plan at that cap rate.",
     "ref": "1.10"}
  ],
  "failure_cases": [
    {"case": "Drive Planning", "year": "2024", "what_happened": "...", "check": "...", "ref": "1.8"}
  ]
}
```

## Request item

```json
{
  "id": "RE-FIN-003",
  "order": 30,
  "stage": "confirmatory",
  "priority": "gating",
  "workstream": "Financial",
  "request": "Trailing 36 months of bank statements for every property-owning and operating entity.",
  "format": "Bank-issued PDFs, plus read-only bank portal access or a direct bank confirmation.",
  "why": "Proof of cash: catches revenue that exists only on the P&L.",
  "pass": "Deposits reconcile to reported revenue within 2% for every month; no unexplained related-party transfers.",
  "fail": "Unreconciled gaps, statements produced by the sponsor rather than the bank, or refusal of direct confirmation.",
  "verify": "Request statements directly from the bank (signed authorization) and compare to sponsor copies.",
  "applies_to": ["all"],
  "ref": "1.4, 0.5",
  "weak": false
}
```

| Field | Rule |
|---|---|
| `id` | `<PREFIX>-<WS>-<NNN>`. Prefix is unique per file (e.g. `U`, `RE`, `TV`, `BD`, `CR`, `PE`, `EN`, `DC`, `CPG`, `CAN`, `GE`, `FD`, `CRY`, `NI`, `SEC`, `NAV`, `EV`, `SF`, `HC`, `LF`). |
| `order` | Integer; sort key inside a stage. Number in tens so items can be inserted later. |
| `stage` | One of `screen`, `term-sheet`, `confirmatory`, `third-party`, `closing`, `monitoring`. This is the order the packet is sent in. |
| `priority` | `gating` (must pass or the deal stops), `core` (must be received and pass, or an exception approved in writing), `supporting` (requested; a gap is noted in the report). |
| `workstream` | One of: `Sponsor & Background`, `KYC/AML & Sanctions`, `Corporate & Legal`, `Financial`, `Tax`, `Commercial & Market`, `Operational`, `Technical`, `Collateral & Title`, `Regulatory & Compliance`, `Environmental & ESG`, `Insurance`, `IT & Cyber`, `HR & Management`, `Structure & Terms`, `Valuation & Model`, `Fund Operations`. |
| `request` | What the counterparty must hand over. Imperative, concrete, one deliverable per item. |
| `format` | What acceptable evidence looks like (originals, third-party issued, period covered). |
| `why` | One line: the failure mode this catches. |
| `pass` | Objective pass criterion. Use the numbers from the bible with their benchmark. |
| `fail` | What a fail or red flag looks like. |
| `verify` | How we independently verify it rather than trusting the sponsor's copy. |
| `applies_to` | `["all"]` or a list of subtype ids. |
| `ref` | Bible section(s) the item comes from, so reviewers can read the reasoning and sources. |
| `weak` | `true` if the pass threshold rests on a WEAK source in the bible. The report flags these. |

Keep text plain (no Markdown links). Cite sources by section `ref`; full citations live in `references/`.
