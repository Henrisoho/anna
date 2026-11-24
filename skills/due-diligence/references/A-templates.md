# Appendix A Templates

The deck, the diligence report, the red-team prompt, and three v2 forms: the bias audit, the ODD scorecard, and the universal first-request list.

## A.1 One-page deck template

1. What it is, and the ask, in one line.
2. Sponsor and track record (verified). Mark each claim verified (by whom) or asserted. Track record with and without the top one or two outcomes (0.13).
3. Asset or business, and market. Where in the cycle (0.10 scorecard, one line).
4. The numbers: historical, then projection. State the base rate the projection must beat, and the management-forecast haircut applied (0.6, 0.7).
5. Structure, use of proceeds, security.
6. Returns and sensitivities. Include: exit multiple = entry and margins flat; entry minus 1 to 2 turns; what must be true (implied margin, growth, exit multiple).
7. Top 3 risks and mitigants.
8. Terms.
9. What we could NOT verify (one line, pointing to the diligence report).

## A.2 Diligence report template

This is the PDF that ships with each deal.

- Deal summary and structure.
- What was checked, by workstream, and the evidence reviewed.
- What was verified independently, and by whom.
- What could NOT be verified. An explicit list. For each item: the rep, indemnity or closing condition that covers it, and its survival or limitations date (0.16).
- Open concerns and unresolved questions.
- Red flags found and their status (0.17 list).
- Third-party reports obtained. Sponsor background-check summary. QoE engagement type (SSAE 19 AUP or CS 100) and what its scope excluded (0.5).
- Numbers: the model, base and downside, sensitivities.
- Recommendation and conditions.

v2 fields:

| Field | Why | Source |
|---|---|---|
| Diligence intensity: hours of in-person management contact, sites visited, references called, what was skipped for timing | Thin diligence in hot markets is where misallocation happens | Fu and Taylor, NBER w33987 |
| Refused or deflected questions (count and topic) | 14% of ODD investigations met refusals | Brown et al., NBER w15529 |
| Verbal-versus-written discrepancies | 20% of managers gave verbal figures contradicting their documents | same |
| Wire-authority matrix as confirmed by the bank or administrator | 16% mismatch with administrator | same |
| Average versus period-end balances (cash, debt, assets) | Repo 105 | YPFS, JFC 1(1) |
| Collateral dedupe: UCC sweep across all secured parties and affiliates; item-level dedupe (invoice, VIN, serial) | First Brands, Tricolor | Harker, KaW 2026; DOJ SDNY |
| Off-balance-sheet financing added to leverage (factoring, SCF, receivables sales, inventory finance, guarantees, keepwells) | First Brands about 5x reported vs about 20x actual | Harker, KaW 2026 |
| Leverage at close vs maximum permitted under baskets and add-backs | Weak covenants | Ivashina and Vallee |
| Net cash per share (SPAC or structured equity) | De-SPACs delivered a mean $4.10 (median $5.70) of cash per $10 share, Jan. 2019 to June 2020 | Klausner, Ohlrogge and Ruan, Yale J. on Reg. 39, https://openyls.law.yale.edu/entities/publication/44dd0075-0956-44d1-bb2e-ea326755b4b5 |
| Implied expectations ("what must be true") from the reverse valuation | Price-implied margin and growth | Thomas, Yale Insights |
| Hints log: each data-room hint, the written question, who asked it, the answer | Paragon Metals | HLS Forum 2026 |
| Third parties named as validators, partners, customers or co-investors, and whether each was contacted directly | Theranos | HLS Forum 2022 |
| Hotline test result and 3-year hotline statistics; internal investigations log | One-fifth of hotlines non-functional | Soltes 2018 |
| Compliance diligence scope and gaps; 100-day compliance plan | DOJ ECCP | HLS Forum 2020 |
| Treasury and counterparty map: banks, insured share, pooled cash vehicles, prime brokers, hedge counterparties, financing lines with haircuts | SVB, Reserve Primary, Credit Suisse, Lehman | 0.11 |
| Cycle scorecard | Late-cycle signals | 0.10 |
| Bias audit (A.4) attached | IC hygiene | Kahneman, Lovallo and Sibony |
| Regulatory status lines checked at signing | Rules changed 2024 to 2026 | 0.18 |
| ILPA Performance Template obtained (fund deals): yes or no | Refusal is a signal | ILPA 2025 |

## A.3 Red-team prompt

For an AI reviewer, per deal type.

PROMPT

> You are a skeptical institutional investor attacking this deck. Use the failure modes, red flags, and hard questions for [deal type], plus Chapter 0. You are not trying to be balanced. You are trying to find the reason this deal loses money.

Core (v1):

1. List every claim presented as fact that is not independently sourced.
2. Identify every metric that could be gamed (NRR, adjusted EBITDA, ACV, DSCR, IRR) and demand the raw recomputation.
3. Name the single check that, if it fails, kills the deal.
4. Flag any guaranteed return, missing third-party report, missing independent administrator, appraiser, or engineer, or unreconciled cap table or borrowing base.
5. Separate what the sponsor verified from what they assert. Produce the list of documents the sponsor rarely has ready and should be asked for first.
6. State what a good answer to each hard question looks like, and treat evasion as a red flag.

Language and numbers (v2):

7. Restate every term of art in one plain sentence with a number. Flag any you cannot (Sonnenfeld jargon test).
8. Recompute the return with exit multiple equal to entry multiple and margins flat; report how much of the base case survives. Then at entry minus 1 to 2 turns (Thomas et al.; Wasserstein and Thomas; Gompers et al. 2016).
9. Identify every number that is a period-end snapshot and ask for the average (Repo 105).
10. Identify every short-term funding line and stress its haircut to crisis levels (50% non-Treasury structured, 100% esoteric) (Gorton and Metrick).
11. Compute maximum permitted senior secured leverage including all baskets, ratio debt and add-backs; compare with closing leverage (Ivashina and Vallee).
12. Is there off-balance-sheet financing (factoring, supply-chain finance, receivables sales, guarantees) excluded from leverage? (First Brands.)
13. Is any DSCR computed on anticipated rather than in-place leases? Is the cap rate NOI-based or cash-flow-based? (Wharton lane; Levitin and Wachter.)
14. Is any growth acquisition-driven, with weak cohorts? Show revenue from customers acquired in the period against prior cohorts (Fader and McCarthy).
15. Does any semi-liquid vehicle have redemption rights above its liquidity coverage (cash + NII + maturities against the cap)? (Fang, Goldstein and Zeng.)
16. Widen every sponsor range about 2x and rebuild the downside from base rates, not the sponsor's scenario tab (Ben-David, Graham and Harvey).
17. Show any VC or fund track record with and without the top one or two outcomes, as PME, never as a compounded IRR (Ouyang et al.; Yale 2018).
18. When a default rate, loss rate or benchmark is quoted, name its definition and whether it excludes backfill and includes dead funds (IMF 2024; Malkiel and Saha).

Evidence trail (v2):

19. Diff the target's last eight quarterly and annual filings or management letters; list every changed risk factor or legal disclosure and require an explanation (Lazy Prices).
20. For every "hint" in the data room (references to lost customers, cancellation letters, volume declines), name the written question asked, who asked it, and the answer received (Paragon Metals).
21. Identify every third party the sponsor cites as validator, partner, customer or co-investor, and record whether we contacted each directly (Theranos).
22. For the top 10 customers, compare the target's reported sales with each customer's purchase, inventory and payables trend (Zhang, Li and Li).
23. Reconcile every distribution to its source account and to underlying cash flow (GPB Capital).
24. For any named valuation firm, pricing service or administrator, state whether we hold its engagement letter and spoke to it, and who has write access to pricing inputs (Infinity Q; SQN).
25. Read the QoE engagement letter: AUP or consulting, and what was NOT tested (SSAE 19).

Cycle, counterparties and bias (v2):

26. Score the asset class on Xiong's four bubble features and the 0.10 scorecard; if three or more, name the exit buyer and multiple once supply arrives.
27. Where is the cash, what share is uninsured or in gateable vehicles, and which counterparty failure would stop the business or the fund? (0.11.)
28. Run the 12 bias-audit questions (A.4) against the deal team's own memo and answer questions 10 and 11 with an outside-view base rate.
29. Which regulatory line in 0.18 does this deck rely on, and is the deck's description of it current? (Example: "cannabis is now Schedule III" is wrong for adult-use.)
30. What would the post-mortem say if this deal lost half its value in three years? Write it now.

## A.4 IC bias audit form

Completed in writing by the deal team; read by the IC chair before the vote; attached to the diligence report (Kahneman, Lovallo and Sibony, HBR 2011; Ben-David, Graham and Harvey, QJE 2013).

| # | Question | Answer (one paragraph) | Evidence or base rate cited |
|---|---|---|---|
| 1 | Self-interest: does compensation or a pipeline target skew the call? | | |
| 2 | Affect: is the team in love with the deal? | | |
| 3 | Groupthink: were dissenting views recorded and explored? Who disagreed? | | |
| 4 | Saliency: is the thesis an analogy to one memorable past win? | | |
| 5 | Confirmation: were credible alternatives (pass, smaller ticket, different structure) evaluated? | | |
| 6 | Availability: what would we want to know in a year, and can we get it now? | | |
| 7 | Anchoring: where did each key number come from? Is it the sponsor's figure re-labelled? | | |
| 8 | Halo: are we assuming success in one asset class carries to this one? | | |
| 9 | Sunk cost: are we attached because of time spent or a prior deal with this sponsor? | | |
| 10 | Is the base case too optimistic? (Reference class and its outcome distribution.) | | |
| 11 | Is the worst case bad enough? (Sponsor range widened about 2x?) | | |
| 12 | Is the team being too cautious? | | |
| 13 | Process: order of review randomized; materials scored before the pitch; more than one rater (Chen et al.; Ma and Hu) | | |
| 14 | Diligence floor met despite competition? Hours, sites, references (Fu and Taylor) | | |
| 15 | Post-mortem date diarized | | |

## A.5 ODD scorecard with base rates

Compare each fund or sponsor against the base rates from 444 third-party ODD reports (Brown, Goetzmann, Liang and Schwarz, "Trust and Delegation," NBER w15529). A typical third-party ODD report then cost about $12,500 (same source; dated, WEAK as a current price).

| Field | Base rate in the ODD sample | This sponsor |
|---|---|---|
| Past legal or regulatory problem | 41% | |
| Misrepresented past legal or regulatory problems | 21% | |
| At least one misrepresentation or inconsistency | 42% | |
| Verbal figures contradict written documents | 20% | |
| DD questions refused | 14% | |
| Assets unverifiable or disagreeing with a third party | about 19% | |
| Performance unverifiable or disagreeing | 14% | |
| Wire-signature process disagrees with the administrator | 16% | |
| Pricing process disagrees with the administrator | 3.6% | |
| Major data vendor switched in last 3 years | 11% | |
| Non-Big 4 auditor; internal pricing (each associated with misrepresentation) | flag | |
| Form ADV disclosures reconciled to DDQ answers | required | |
| SEC exam deficiency list tested (LPAC consents, fee step-downs, extensions, strategy and leverage limits, key-person, track-record presentation, service-provider diligence, hedge clauses) | required | |
| AML program and investor KYC owner (no federal adviser AML obligation until Jan. 1, 2028) | required | |
| ILPA Performance Template for every prior fund | required | |

## A.6 Universal first-request list

The documents sponsors rarely have ready. Ask for these first; the speed and completeness of the response is itself a finding.

1. 36 months of bank statements for every account, and the bank confirmations used in the QoE (0.5).
2. Bank or administrator-confirmed signatory list and wire approval matrix (0.5).
3. Average daily or intra-quarter balances of cash and debt (0.4).
4. Every factoring, supply-chain-finance, receivables-sale, inventory-finance and guarantee agreement; UCC search results across all affiliates and principals' entities (0.4, 0.5).
5. Bank accounts list with balances by institution and insured share; all pooled cash vehicles (0.11).
6. Every financing line with haircut, advance rate, margin-call mechanics and term (0.11).
7. Past projections and guidance against actuals for every prior deal or year (0.2).
8. Track record as LP cash flows, every fund and vehicle ever managed (including closed and abandoned), ILPA Performance Template with and without sub lines and NAV debt (0.13).
9. Carry and GP-ownership split by person, current and prior fund (0.13; Ivashina and Lerner).
10. Form ADV Parts 1 and 2; any SEC deficiency letters or Wells notices in the last 5 years (0.2; HBS lane fund checklist).
11. Fee and expense allocation policy and a 3-year schedule of all portfolio-company fees (monitoring, transaction, director, operating-partner) with offset calculations; broken-deal expense allocation across funds and co-investors (HLS Forum, SEC enforcement 2015 to 2016, https://corpgov.law.harvard.edu/2016/12/19/the-year-in-review-sec-enforcement-actions-against-investment-advisers/).
12. Co-invest allocation policy and the list of co-invests offered and to whom (Fang, Ivashina and Lerner; Lerner, Mao, Schoar and Zhang).
13. NAV-facility and subscription-line terms; LPA consent provisions for NAV debt and GP-leds (0.13, 0.16).
14. Internal investigations log, hotline log and 3-year hotline statistics (0.15).
15. Valuation policy, valuation-committee minutes, the named valuation firm's engagement letter, and who has write access to pricing inputs (0.6).
16. Customer-level volume forecasts and contracts for the top customers, and permission to call them (0.16).
17. Cohort data: customers acquired per period, total active customers, orders (0.6 CBCV).
18. Cap table on a fully diluted basis (options, RSUs, warrants, SAFEs), and every investor veto over financing and M&A (0.6, 0.16).
19. AML and sanctions policy, and who performs investor KYC (0.3).
20. Insurance: bindable quotes for the full hold; water will-serve letter and source seniority where relevant (0.19).
21. Every government lease and appropriation-dependent revenue line, with termination rights (0.20).
