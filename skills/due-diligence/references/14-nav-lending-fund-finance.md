# 14 NAV Lending and Fund Finance

*Subscription lines, NAV facilities, hybrids, and the fund-level leverage stack, from both the lender's and the LP's side.*

## 14.1 How it works

- **Subscription lines** lend against LPs' uncalled commitments. The GP borrows instead of calling capital, then calls capital to repay. Effect: the LP's money goes in later, so reported IRR rises without any change in multiple (v1 10.5; ILPA 2020 guidance).
- **NAV facilities** lend against the fund's portfolio (cash flows and equity of portfolio companies, often via a pledge of holding-company equity), typically after the investment period. **Hybrids** blend both (general lane draft; ILPA NAV guidance, July 2024, https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf).
- **Three uses** (HLS Forum, "Private Equity and Net Asset Value Debt," 2024, https://corpgov.law.harvard.edu/2024/07/15/private-equity-and-net-asset-value-loans-ticking-time-bomb-or-ticking-all-the-right-boxes/):
  - Offensive: fund bolt-ons and refinancings.
  - Defensive: rescue struggling portfolio companies, often on PIK terms.
  - Liquidity: fund distributions while exits stall.
- **Market size (two estimates; do not average):**
  - About $100B NAV-facility market (2024), forecast $600B by 2030 (Fund Finance Association estimate cited by ILPA, July 2024).
  - Roughly $100B in 2023, lender forecasts of $700B by 2030 (HLS Forum, 2024).
- **About 80% of NAV facilities to date supported portfolio companies; about 20% funded distributions** (ILPA, July 2024).
- **Banks are behind it.** Bank lending to private-credit vehicles rose from about $8B (2013) to about $95B (end-2024); bank commitments to PE and private-credit sponsors are about 14% of bank lending to nonbanks, up from about 1% a decade earlier (Harker, KaW, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).

## 14.2 Data room index (lender or LP view)

1. Facility agreement and fee letter.
2. Borrowing-base and LTV definitions; eligible-asset and concentration criteria.
3. Valuation policy; last two years of marks versus exits; any third-party valuation rights.
4. Portfolio-company financials and their own debt (structural subordination).
5. Cash-sweep and LTV step-down mechanics; cure rights and waterfall.
6. Recourse to LP commitments (hybrid?).
7. LPAC consent record; LPA clause permitting fund-level borrowing.
8. Disclosure sent to LPs (ILPA Reporting and Performance Templates).
9. Use of proceeds; for distributions, recallability terms.
10. For sub lines: facility size as % of commitments, days outstanding history, LP opt-out offered, uncalled-capital estimate (ILPA 2020).
11. Rating-agency report if rated.
12. Complete amendment, waiver and consent history since origination; the amendment trail is the real credit history (Roberts and Sufi, JFE 2009, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf).

## 14.3 Diligence checklist by workstream

*Collateral and LTV*
- LTV on what NAV: GP marks or an independent valuation? Run LTV at a 25% to 40% NAV haircut and identify when the sweep and cure triggers hit (general lane; Sidley, Aug. 2025, https://www.sidley.com/en/insights/newsupdates/2025/08/net-asset-value-based-fund-financings-credit-rating-criteria-and-key-structuring-considerations).
- Stale marks hide LTV breaches: private marks lag public markets by at least four quarters (IMF GFSR Apr. 2024, Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md). Require an independent-valuation right and a recent exit-to-mark comparison.
- Structural subordination: each portfolio company's senior debt sits ahead of the NAV lender; compute look-through leverage.
- Concentration: top-3 assets as % of NAV; minimum number of assets.
- Cross-collateralization: which assets are pledged, and does one asset's default trigger the whole facility? Good assets may be sold to cure an LTV breach (HLS Forum 2024).

*Use of proceeds and LP impact*
- Distributions versus portfolio support. If distributions, are they recallable?
- Carry: is carry paid on NAV-funded distributions? Refuse it (HLS Forum 2024).
- Fee life: does the facility extend the fund's life and fee stream? (HLS Forum 2024.)
- Recompute DPI and IRR excluding NAV-funded distributions ("synthetic DPI," ILPA 2024).
- Timing: was the facility drawn near a fundraise? Interim IRR/DPI inflation near a fundraise is a named concern (HLS Forum 2024).

*Cost*
- All-in spread, PIK toggles and fees; compare with the IRR uplift. Why not sell an asset instead?

*Governance*
- LPAC consent obtained (ILPA says GPs should seek it regardless of use of proceeds); standardized disclosure to all LPs (ILPA, July 2024).
- Does the LPA permit NAV debt and give LPs consent? (HLS Forum 2024.)

*Stress*
- Model a simultaneous 20% to 30% collateral price fall plus a haircut increase; confirm which assets are sold first and whether a forced sale breaches covenants elsewhere (Brunnermeier and Pedersen, RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf).
- Advance rates are a state variable, not a constant: repo haircuts on nine non-Treasury collateral classes went from about zero in early 2007 to nearly 50% at the late-2008 peak, and some classes could not be financed at all (Gorton and Metrick, JFE 2012, https://repec.som.yale.edu/icfpub/publications/2358.pdf); Ellington margins went from about 10% to above 40% in months (Geanakoplos, Yale lane). Underwrite at the stressed advance rate.
- Bank-financed booms are the dangerous ones: bank systemic risk rises in a bubble's build-up and further in the bust (Brunnermeier, Rother and Schnabel, RFS 2020, https://nber.org/papers/w25775). Stress facility non-renewal at the same time as the asset-price fall.
- Map the full fund-level leverage stack (subscription line, NAV facility, asset-based facility) and its margin-call triggers (Harker, KaW 2026).

*Subscription lines*
- Size and duration against ILPA reference points: 15% to 25% of commitments and 180 days outstanding for PE (ILPA 2020, https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf).
- Quarterly disclosure of facility size and balance, IRR with and without, uncalled-capital estimate (ILPA 2020).
- LP opt-out at the outset (ILPA Principles 3.0, 2019, https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf).
- ILPA Performance Template: gross and net IRR and TVPI with and without the facility; sub-line interest as a separate expense line (ILPA 2025, https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf).

## 14.4 The numbers

| Metric | Value | Source |
|---|---|---|
| NAV market size | About $100B (2024) → $600B forecast by 2030 | FFA estimate cited by ILPA, July 2024 |
| NAV market size (alternative) | About $100B (2023) → $700B lender forecast by 2030 | HLS Forum, 2024 |
| Use split to date | About 80% portfolio support; about 20% distributions | ILPA, July 2024 |
| Initial LTV | About 10% to 30%; maximums around 40% as downside buffers | Sidley, Aug. 2025 |
| Rating-agency stress haircut | KBRA starts by haircutting fund value 40% to 60% depending on asset type (PE, listed equity, bonds) | Reuters via Yahoo Finance, May 2024, https://sg.finance.yahoo.com/news/rating-firms-cautious-ratifying-private-101145008.html |
| Fitch approach | Reportedly rates to the most conservative terms permitted in the facility, not current metrics | Same |
| Rated NAV issuance, 2025 | Record, about $23B in 38 deals (KBRA) | KBRA, https://www.kbra.com/publications/qHMNTvyP |
| KBRA surveillance, PE and secondary NAV loans, 2020-1H 2026 | 95% of 279 actions were affirmations | Same |
| Sub-line reference points (PE) | 15% to 25% of commitments; 180 days outstanding | ILPA 2020 |
| Bank lending to private-credit vehicles | About $8B (2013) → about $95B (end-2024) | Harker, KaW 2026 |
| Repo haircut index, stressed | About 0% (early 2007) → nearly 50% (late 2008) | Gorton and Metrick, JFE 2012 |
| Private-mark lag | At least four quarters to converge after a shock | IMF GFSR Apr. 2024 |

Structuring points: cash sweeps are critical to refinancing risk; lenders should retain rights to third-party valuations; testing is initial, periodic and event-driven (Sidley, Aug. 2025).

## 14.5 Third parties

- Independent valuation agent (lender right to third-party valuations).
- Rating agency (KBRA, Fitch) for rated facilities and rated feeder notes.
- Lender's and LP's counsel (LPA borrowing authority, LPAC consent, recall mechanics, tax).
- Fund administrator for borrowing-base certificates and capital-call verification.

## 14.6 Legal and structure

- **The ILPA standard (July 2024).** Distributions funded by NAV loans materially inflate IRR and DPI and can create perverse incentives; they are often RECALLABLE if the facility falls out of LTV compliance, which disrupts LP cash planning and creates tax and accounting problems; LPs may need a "synthetic DPI" excluding NAV-funded distributions to compare managers; GPs should seek LPAC consent regardless of use of proceeds (ILPA, July 2024).
- **What to negotiate in the LPA:** cap on fund-level leverage; LPAC or LP consent for NAV facilities; no carry on borrowed distributions; disclosure of recallability; sub-line size and duration caps with opt-out (Principles 3.0); performance reporting with and without facilities (ILPA 2025).
- **No federal backstop.** The vacated 2023 SEC rules would not have required these disclosures directly, and since June 2024 nothing does; all of it is contractual (Chapter 10.15).
- **Pledge structure:** NAV lenders typically take a pledge of holding-company equity, not the portfolio companies' assets; they sit behind every portfolio company's own lenders (structural subordination).

## 14.7 Failure modes and the check that catches each

| Failure | What happens | CHECK |
|---|---|---|
| DPI manufactured by borrowing | Fund looks liquid; raises next fund on borrowed distributions | Recompute DPI excluding NAV-funded distributions; ILPA Performance Template |
| Recall of distributions in a downturn | LPs must return cash when they least have it | Read the recall clause and LTV cure waterfall; model a 30% NAV drawdown |
| Cross-collateralization contagion | Good assets sold to cure an LTV breach caused by bad ones | Map pledged assets; single-asset default triggers |
| Stale marks hide LTV breaches | Lender and LPs learn late | Independent-valuation right; exit-to-mark comparison |
| Carry on borrowed distributions | GP paid before LPs are whole | LPA: no carry on NAV-funded distributions |
| Defensive PIK loans to rescue weak companies | Leverage compounds on the weakest assets | Use-of-proceeds test; PIK share |
| Fee life extended | Fees run longer on a fund that should be winding down | Term-extension consent; fee step-down |
| Sub-line-inflated IRR | IRR rises with no change in multiple | Recompute without the facility (v1 10.6) |
| Haircut and non-renewal spiral | Lender cuts advance rate as asset prices fall | Stress haircuts to crisis levels; staggered maturities |

No named NAV-facility default case file was sourced by the research lanes; KBRA's surveillance record (95% affirmations, 2020-1H 2026) suggests the stress has not yet been tested at scale. **GAP**: add a case file when one is public.

> **THE ONE CHECK (fund finance).** Ask for DPI and IRR without the subscription line and without NAV-loan-funded distributions. If the GP cannot or will not produce them, you do not know the fund's real liquidity or return.

## 14.8 Red flags

- NAV facility put in place without LPAC consent.
- Use of proceeds is "distributions" in a fund raising its next vintage.
- PIK interest.
- LTV tested on GP marks only; no independent-valuation right.
- No cash sweep.
- Carry paid on NAV-funded distributions.
- Sub line above 25% of commitments or outstanding beyond 180 days without disclosure.
- No LP opt-out on the sub line; no with/without reporting.
- Multiple layers (sub line plus NAV plus asset-level facilities) with no single map.

## 14.9 Hard questions

1. What is DPI without the NAV loan? IRR without the sub line?
2. What happens at a 30% NAV decline: who cures, and can you recall distributions?
3. What does the facility cost all-in against the IRR gain? Why not sell an asset instead?
4. Which assets are pledged, and does one default trigger the whole facility?
5. Who values the collateral for the LTV test?
6. Did the LPAC consent, and what were LPs told?
7. Is any carry being paid on borrowed distributions?
8. Show every amendment and waiver since origination.

---
