# Red-team prompt

From Appendix A.3 of The Bible on Due Diligence v2. Replace [deal type] and attach the deal type's failure_cases, red_flags and hard_questions from `library/<type>.json`. The cited authors and sections are in `references/`.


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

