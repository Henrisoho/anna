# Wharton lane findings for The Bible on Due Diligence (v1 -> v2)

Source lane: The Wharton School (Knowledge at Wharton (KaW) articles and podcasts, Wharton faculty research on SSRN, NBER and faculty pages, Zell/Lurie Real Estate Center working papers and Wharton Real Estate Review, Rodney L. White Center working papers, Wharton Financial/Policy initiative (WIFPR, now WFFI), Kleinman Center for Energy Policy, Wharton Blockchain and Digital Asset Project).

How to read this file
- Each bullet is written so it can go straight into the bible. Then comes a tag: [NEW], [STRENGTHENS x.y], [CONTRADICTS x.y] or [RESOLVES WEAK/GAP: ...]. The source is in parentheses.
- "Wharton-hosted" means the paper sits on a Wharton server or came from a Wharton program but the authors are elsewhere. Those bullets say so.
- "Context (non-Wharton)" marks a fact taken from another source to anchor a Wharton finding. Confirm it separately.
- Some figures come from papers 10 to 20 years old (Linneman 2005, Levitin and Wachter 2013, KaW 2002 to 2011). They are kept for the framework and the failure lesson, not as current market levels. Each one is dated.
- Research note: this lane hit the shared web-search budget (200 searches) before every planned query had run. The gaps are listed at the end. Everything here was read in the primary or Wharton-hosted source or its official abstract page.

---

## 0 The Master Playbook

### 0.1 How top firms run a diligence process

- **Diligence gets thinner when deals are hot, and that costs money.** Fu and Taylor used smartphone geolocation to measure how many hours VCs spend meeting startup staff in person before a round. Diligence hours fall in hot markets, as distance grows, and as investors get busier or more experienced. Thinner diligence does not lower average returns, but it widens the spread of outcomes, which is capital misallocation. Their model puts the value of doubling diligence at 2% to 6% of capital invested. Rule: set a minimum diligence floor (site visits, management hours, reference calls) that does not shrink because a round is competitive. Record the hours actually spent in the IC memo. [NEW] (Fu and Taylor, "Due Diligence and the Allocation of Venture Capital," NBER w33987, Jul 2025, revised Sep 2026, https://www.nber.org/papers/w33987)
- **Diligence run to confirm an answer already chosen is the most common M&A process failure.** Wharton's six-stage M&A checklist:
  - Set a walk-away price from conservative cash flows before bidding starts.
  - Keep deal champions separate from the valuation team.
  - Probability-weight synergies and model dis-synergies (lost customers and talent).
  - Use cooling-off periods against "auction fever."
  - Treat a seller-imposed deadline as a red flag, not a reason to skip work.
  [STRENGTHENS 0.1, 5.3] (Feldman and Chunduru, "Why Many M&A Deals Fail and How to Beat the Odds," KaW, Dec 8 2025, https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/)
- **Cycle signal: a complex, illiquid product being marketed to unsophisticated investors usually means the cycle is near its peak.** Late entrants understand least why the strategy worked, and very large deployment targets make selective underwriting hard. Example: the largest perpetual private-credit fund must deploy about $43B a year, more than a quarter of annual US direct lending. Add "deployment pressure" as a screen-stage question for any manager or lender. [NEW] (Patrick Harker, "These investments promise high yield with bond-like safety...," KaW opinion, Apr 22 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/)

### 0.2 Sponsor and management background checks

- **Check the sponsor's forecast record, not just the background report.** In Schrand and Zechman's sample of 49 SEC enforcement (AAER) firms, about a quarter of misstatements began as unintentional, optimistically biased errors. Executives then slid into intentional misreporting to cover the gap. Overconfident executives were more likely to misreport and were not monitored more closely.
  - CHECK: compare the sponsor's or management's past projections and guidance with actual results across every prior deal or year.
  - A pattern of repeated optimistic misses is a fraud precursor, not just a style trait.
  [STRENGTHENS 0.2, 0.4] (Schrand and Zechman, "Executive Overconfidence and the Slippery Slope to Financial Misreporting," J. Accounting and Economics 53(1), 2012, https://repository.upenn.edu/accounting_papers/119; KaW podcast "Are Overconfident Executives More Inclined to Commit Fraud?", https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/are-overconfident-executives-more-inclined-to-commit-fraud/)
- **Governance is part of the background check.** In Wharton's Theranos post-mortem, Wayne Guay pointed to:
  - a dual-class structure giving the founder 100 votes per share against 1, with full control of board composition;
  - a board of politicians and military figures with no medical or financial expertise.
  CHECK: map voting control, board seats, and each director's domain expertise. Treat founder super-voting control without a sunset as a risk factor. [NEW] (KaW, "What Silicon Valley Can Learn from the Theranos Fraud Case," Mar 19 2018, https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/)

### 0.4 Fraud detection: the universal red flags

- **CASE FILE: double-pledged collateral and off-balance-sheet leverage. First Brands Group and Tricolor Holdings, September 2025.**
  - What happened: First Brands (auto parts) and Tricolor (subprime auto lender) collapsed within days of each other, both with allegations of collateral pledged to more than one lender. First Brands' lenders thought leverage was about 5x. Counting off-balance-sheet factoring and supply-chain finance, it was closer to 20x. Per Cambridge Associates, high-quality private-credit managers saw the warning signs and avoided both. Banks, broadly syndicated loan funds, and rating agencies did not.
  - THE CHECK: get every factoring, supply-chain-finance, and receivables-sale agreement and add it to leverage. Run UCC searches across all secured parties. Dedupe collateral at the item level (invoice numbers; VINs for auto paper) against other lenders' borrowing bases.
  [NEW, STRENGTHENS 3.7, 4.5] (Harker, KaW opinion, Apr 22 2026, URL above.) Context (non-Wharton): a forensic review cited by ABA Business Law Today found about 40% of roughly 70,000 Tricolor loans shared VINs or attributes with at least one other loan (https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-october/seeing-red-flags-in-tricolor-collateral-interests).
- **Theranos as a red-flag set.**
  - Revenue projected to investors for 2014: $100M. Actual: just over $100,000.
  - The analyzer, promised to run about 200 tests, ran about a dozen on its own hardware.
  - The company falsely claimed Department of Defense deployment.
  - About $700M was raised.
  - CHECK: independently test the core technical claim, reconcile projections to actual invoices and cash, and confirm every named marquee customer or government deployment directly with that counterparty.
  [STRENGTHENS 0.4, 2.7] (KaW, Mar 19 2018, URL above)
- **Customer-asset misuse at an intermediary.** Werbach's rule for any custodian or exchange: do not commit fraud, and do not use customer money for other ventures. His warning after FTX: opaque firms may have been carrying unrecognized holes from earlier failures (Celsius, Three Arrows, Terra). CHECK: confirm that customer assets are segregated, held at an independent custodian, and reconciled to liabilities. [STRENGTHENS 0.4, 11.1] (KaW podcast, "What the FTX Collapse Means for the Cryptocurrency Market," Nov 22 2022, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/what-the-ftx-collapse-means-for-the-cryptocurrency-market/)

### 0.6 Valuation methods across assets

- **Add a method row: customer-based corporate valuation (CBCV) for subscription and repeat-purchase businesses** (DTC, SaaS, marketplaces, consumer subscription).
  - Method: value the company as existing customers plus future cohorts. Forecast acquisition, retention, purchase frequency, and spend separately.
  - Minimum data: customers acquired per period and total active customers. Non-subscription businesses also need orders placed.
  - Blue Apron (2017): about 70% of acquired customers churned within six months. The IPO range was cut from $15–17 to $10 within days of the analysis, and shares later fell about 70% more.
  - Wayfair: CBCV value under $10 per share while the stock traded around $64. The stock fell about 10% the day the paper posted.
  [NEW] (KaW podcast with Peter Fader and Daniel McCarthy, Feb 12 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/)
- **Value the "false negative" as well as the false positive.** A pure DCF treats uncertainty only as downside, so it can underbid. Value a target as NPV of core (Horizon 1) cash flows, plus option value of growth businesses (H2, H3), plus abandonment value (the option to sell or exit). Example: a bank's $800M DCF cap lost a deal to an $840M bid. Adding abandonment value would have justified $849M. Use this only with explicit, ranged assumptions, never to rationalize price. [NEW] (MacMillan, van Putten and Baghai, "M&A's Overlooked Pitfall: The False Negative," KaW, Mar 30 2011, https://knowledge.wharton.upenn.edu/article/mas-overlooked-pitfall-the-false-negative/)
- **High-growth DCF discipline (Wessels).** Wessels co-authors McKinsey's *Valuation*. For high-growth companies, start from the expected long-run state of the market and the company's share of it, then work backward to today. Do not extrapolate history. Then benchmark the projected path against historical high-growth companies to test plausibility. [STRENGTHENS 0.6, 2.4] (KaW, David Wessels on tech valuation, e.g. "Kicking the Tires on Uber's $17 Billion Valuation," https://knowledge.wharton.upenn.edu/article/kicking-tires-ubers-17-billion-valuation-worth-much/)
- **Real estate cap rates need a cross-check.** Over roughly 25 years, cap rates showed little response to alternative investment returns. BBB corporate bonds were the exception. Cross-check the direct-cap value with CAPM, a comparison against assets of similar credit risk (BBB/BB yields), and the Gordon growth model. [STRENGTHENS 0.6, 1.5] (Linneman and Rubenstein, "How Should Commercial Real Estate Be Priced?," Wharton Real Estate Review 12(1), 2008, Zell/Lurie WP 637, https://realestate.wharton.upenn.edu/working-papers/how-should-commercial-real-estate-be-priced/)
- **Public-market check on private marks.** Equity REIT returns predict later returns on the appraisal-based NCREIF index. The lead-lag first found by Gyourko and Keim (1992) persists in the modern REIT era. Rule: compare the sponsor's exit cap and current appraisal cap against the REIT-implied cap rate for the same property type. A wide gap means the appraisal has not caught up. [NEW] (Gyourko, Zell/Lurie WP 470, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/441.pdf and WP 470 listing at realestate.wharton.upenn.edu.) Context (non-Wharton): Nareit reported REIT-implied caps at 5.74% against NCREIF ODCE appraisal caps of 4.47% in Q2 2026, a 127 bp gap.

### 0.7 The IC memo skeleton

- **Add to item 7 (diligence findings): "Diligence intensity."** Record hours of in-person management contact, sites visited, references called, and what was skipped because of timing. This follows the Fu and Taylor result that thin diligence in hot markets is where misallocation happens. [NEW] (NBER w33987, URL above)
- **Add to item 5 for M&A and add-ons:** a synergy table with probability weights and timing, cost synergies separate from revenue synergies, plus a dis-synergy line.
  - Cost synergies typically take 1 to 2 years to realize; revenue synergies 2 to 3+ years.
  - 70% to 90% of deals underperform expectations across multiple studies.
  [STRENGTHENS 0.7, 5.3] (Feldman and Chunduru, KaW Dec 8 2025)

---

## 1 Real Estate

### 1.4 Diligence checklist by workstream

- **INSURANCE (new workstream line): underwrite the insurance reset, not last year's bill.**
  - Using more than 74M premiums inferred from mortgage escrow data (2014–2024), Keys and Mulder find that average homeowners premiums rose about 33% from 2020 to 2023 ($1,902 to $2,530).
  - Against 2018: Florida premiums up 90% by 2023, Texas up 50%.
  - The pass-through from disaster risk into premiums doubled. Reinsurance costs roughly doubled from 2017 to 2023 and drove most of the rise.
  - Premium increases are capitalized into values: home price growth was more than $40,000 lower in the most exposed ZIP codes (an earlier version reported about 11% lower relative 2024 prices).
  - CHECK: get a three-year premium history, a current bound quote at closing, and the deductible and named-storm or wildfire terms. Stress insurance expense in catastrophe-exposed markets, and stress exit value for capitalization of higher premiums.
  - The data is residential, but the reinsurance channel is the same one that prices commercial property coverage.
  [NEW] (Keys and Mulder, "Property Insurance and Disaster Risk: New Evidence from Mortgage Escrow Data," NBER w32579, rev. Oct 2026, https://www.nber.org/papers/w32579; KaW, "How Higher Property Insurance Premiums Mirror Climate Risk," Sep 24 2024, https://knowledge.wharton.upenn.edu/article/how-higher-property-insurance-premiums-mirror-climate-risk/)
- **FINANCIAL: underwrite on cash flow after recurring capex, not NOI.** NOI-based and cash-flow-based cap rates differ by the recurring capex reserve.
  - Recurring capex as a share of NOI (NCREIF history): about 16% to 18% for institutional apartments (17% used), 31% industrial, 33% office, 36% retail.
  - CHECK: ask whether the sponsor's cap rate is on NOI or cash flow, and current-year or next-year income. Apply the reserve before comparing.
  [STRENGTHENS 1.4, 1.5] (Linneman, "What Should Stabilized Multifamily Cap Rates Be?," Zell/Lurie Real Estate Center Review, c. 2005, WP 519, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf)
- **COMMERCIAL AND MARKET, office: treat work-from-home as a permanent obsolescence shock.**
  - Gyourko expects average attendance of 1 to 2 days a week, which implies a 20% to 40% fall in office demand. Elsewhere he estimates 15% to 20%.
  - Class B vacancy typically runs 15% to 20%, some buildings above 30%.
  - Some offices have traded at 25% to 50% of their pre-pandemic purchase price.
  - Because office leases run 5 to 10 years, failure arrives at each lease expiry, so some buildings are failing now and more will fail over the next five years.
  - CHECK: line up lease expiry against loan maturity, and test the takeout on post-rollover occupancy for Class B. Do not assume historical occupancy.
  [NEW] (KaW Ripple Effect podcast, "Next Crisis: Empty Office Buildings | Joe Gyourko," May 14 2024, https://knowledge.wharton.upenn.edu/podcast/ripple-effect/next-crisis-empty-office-buildings-joe-gyourko/)
- **COMMERCIAL AND MARKET, office-to-residential conversion: verify the conversion math.**
  - Gyourko cites conversion costs of about $300/sf in Philadelphia and about $500 to $600/sf in New York, where top Manhattan rents reach about $8/sf a month.
  - He expects no more than about five conversions in Philadelphia this cycle. Most failing Class B buildings will more likely be demolished and replaced over the next decade.
  - CHECK: a conversion business plan needs a real cost estimate per sf, residential rents that support it, and a basis low enough after the write-down. "Conversion optionality" is not a value floor.
  [NEW] (same podcast; related KaW coverage, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-going-to-happen-to-all-those-empty-office-buildings/)
- **CONSTRUCTION AND TECHNICAL: when value falls below replacement cost, expect deferred maintenance.** Owner-occupied homes worth less than construction cost spend about 50% less on renovation than comparable homes. Land is about 30% of the value of the US housing stock. CHECK: on any asset trading below replacement cost, assume deferred maintenance and get a property condition report with a capex backlog estimate. [NEW] (Gyourko and Saiz, Zell/Lurie WP 407, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/407.pdf; Glaeser and Gyourko, cited in the same listing)
- **LEGAL AND TITLE, entitlement cost:** local land-use rules can raise the cost of a developed single-family lot by about 35% (Charlotte case study). CHECK: budget entitlement time and fees explicitly. [STRENGTHENS 1.4] (Crosland, Zell/Lurie WP 659, via realestate.wharton.upenn.edu working-paper index)

### 1.5 The numbers

- **Cap rate sanity check (Linneman framework).** Forward cash-flow cap rate = r − g. NOI cap rate = cash-flow cap / (1 − d), where d is recurring capex as a share of NOI.
  - Required return r = 10-year Treasury + a risk premium set by bond-equivalent credit quality:
    - Class A multifamily is about BB: roughly 210 bp.
    - Class B is about BB−: roughly 260 bp.
    - Class C is about B: roughly 350 bp.
  - With g of about 2% and d of 17%, the implied stabilized NOI cap rates are:

  | 10-yr UST | Class A | Class B | Class C |
  |---|---|---|---|
  | 4.2% | 5.1% | 5.7% | 6.7% |
  | 5.0% | 6.0% | 6.6% | 7.7% |

  - In normal markets the forward cash-flow spread to the 10-year Treasury is about 0 bp for A, about 60 bp for B, and about 150 bp for C.
  - Linneman found an unlevered beta for high-quality apartments of about 0.5.
  - Use: if the sponsor's going-in or exit cap is below the framework rate for the current Treasury yield, the sponsor must show why growth or risk differs.
  - The paper is c. 2005. Use the method, not the levels.
  [RESOLVES GAP: exit-cap benchmark; STRENGTHENS 1.5] (Linneman, Zell/Lurie WP 519, URL above)
- **Add a fifth standard stress case: VALUE DECLINE.**
  - Run a 30% fall in CRE prices from current marks. That is the size of the Fed's adverse scenario used in regional-bank CRE stress work; the Fed's 2024 severely adverse scenario used 40%.
  - Add foreclosure deadweight of about 5%, plus distressed-sale discounts of 20% to 30%. Transfer taxes are often paid twice in foreclosure.
  - Recompute LTV and lender loss at loan level.
  [STRENGTHENS 1.5 Figure 4] (Hinzen, Severino and Van Nieuwerburgh, "Too-Many-to-Ignore: Regional Banks and CRE Risks," Oct 2025, Wharton-hosted WFFI paper; authors at Tuck and Columbia, https://wffi.wharton.upenn.edu/wp-content/uploads/2025/10/HSVRegional-Banks-and-CRE-Risks.pdf)
- **Reported delinquency understates CRE distress about 4 to 1.**
  - Re-marking each loan's collateral with granular location-by-property-type price indices and flagging current LTV above 95% finds "latent distress" about four times reported delinquencies.
  - A loan that locked in a low rate can stay current while deeply underwater.
  - CHECK: for any loan purchase, note-on-note financing, or bank-portfolio deal, re-mark collateral to current value. Do not rely on payment status.
  [NEW] (same paper)
- **Historical anchors for downside cases.**
  - CMBS 30-day delinquency went from under 2% before 2008 to about 9% in 2011, then about 5% in 2014.
  - The Fed reported CRE loan delinquency doubling to 7% by mid-2009.
  - CMBS loans move to the special servicer after about 60 days delinquent.
  [STRENGTHENS 1.5] (Zell/Lurie Wharton Real Estate Review CMBS papers, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/730.pdf; KaW podcast "On Shaky Ground," Jul 22 2009, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/on-shaky-ground-commercial-real-estate-faces-financial-tremors/)

### 1.7 Legal and structure (syndications and real estate funds)

- **Investor reporting standard to require in the operating agreement or LPA** (Linneman and Ross):
  - Gross and net IRR, with fees, expenses, and carried interest shown.
  - For each asset: debt level, ownership percentage, and loan-covenant compliance, including partnership-level ventures.
  - Assets grouped as sold, stabilized (ahead of, on, or below underwriting), or non-stabilized.
  - Non-stabilized assets carried at cost and tested for impairment quarterly.
  - Asset-level cost, equity, reserves, debt, NOI, current value, IRR, and equity multiple.
  - 8-K-style notices for unusual events.
  - The same methods across all of the sponsor's funds.
  - Fee benchmark at the time: 1% to 2% of committed capital plus a 20% promote. Sponsor co-invest ranged from 2% to 25%.
  [NEW] (Linneman and Ross, KaW, "Towards Greater Transparency in Real Estate Private Equity Funds," Jul 31 2002, https://knowledge.wharton.upenn.edu/article/towards-greater-transparency-in-real-estate-private-equity-funds/)

### 1.8 Failure modes and the check that catches each

- **CASE FILE: CMBS underwriting decay, 2004–2007.**
  - What happened: CRE CDOs outbid the experienced B-piece buyers who had policed conduit credit, and underwriting decayed.
  - Interest-only loans rose from 47% of CMBS loans in 2004 to 86% in 2007. Conduit loans with partial or full IO went from 10% to 90% between 2003 and 2007 (Gyourko).
  - About $40B of "pro forma" loans sized DSCR on anticipated, not in-place, leases: the CRE equivalent of NINJA loans.
  - Stated LTVs stayed flat while prices inflated, which means standards were falling.
  - Rating agencies' own stressed LTVs rose and stressed DSCRs fell, while AAA spreads tightened.
  - THE CHECK: DSCR on in-place leases only. An amortization requirement. Compare underwritten LTV and DSCR with a third party's stressed LTV and DSCR. Treat flat LTVs in a rising market as loosening.
  [NEW] (Levitin and Wachter, "The Commercial Real Estate Bubble," Harvard Business Law Review 3, 2013, Zell/Lurie WP 747, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/747.pdf; Gyourko, NBER w14708, 2009, https://www.nber.org/papers/w14708)
- **CASE FILE: underpriced non-recourse lending.**
  - What happened: the right to walk away from a non-recourse loan is a put option the lender writes. In a competitive lending boom, every lender rationally underprices it, and asset prices inflate.
  - In the 1990s Asian real estate bubble, countries that curbed underpricing saw value declines of 30% to 40%. Countries showing underpricing symptoms fell 80% or more. A 19-country study of more than 500 REITs found deeper crashes where the put was underpriced.
  - THE CHECK: a lender-side red flag is spreads compressing while LTVs rise and recourse falls. Ask what the loan is worth if values fall 30%.
  [NEW] (Pavlov and Wachter, Zell/Lurie WPs on "Robbing the Bank: Non-Recourse Lending and Asset Prices" and "Real Estate Crashes and Bank Lending," https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/; https://realestate.wharton.upenn.edu/working-papers/real-estate-crashes-and-bank-lending/)
- **CASE FILE: Canary Wharf, Olympia & York, 1992 bankruptcy.**
  - What happened: a 14M sf project failed for six reasons: a London property recession, competition from the City, poor transport links, few British tenants, complicated finances, and developer overconfidence. A new consortium took it out of bankruptcy in 1995; it went public in 1999.
  - THE CHECK: for large development, verify every off-site dependency (transit, infrastructure) and who funds it. Require pre-leasing. Map the full financing structure. Discount the sponsor's conviction.
  [NEW] (Gordon, "The Crash and Rebound of Canary Wharf," Zell/Lurie WP 418, https://realestate.wharton.upenn.edu/working-papers/the-crash-and-rebound-of-canary-wharf/)
- **CASE FILE: refinancing wall, General Growth Properties, 2009.**
  - What happened: GGP filed for bankruptcy after lenders refused to refinance $27B of debt. CRE maturities were then estimated at $400B for 2009, growing past $1.8T by 2012. Wachter and Linneman named private equity real estate funds, with thin reserves and short-term debt, as the most vulnerable owners.
  - THE CHECK: a maturity ladder against realistic refinance terms (rate, DSCR, and proceeds at a stressed value). Count reserves at the fund level, not just the asset level.
  [NEW] (KaW podcast, "On Shaky Ground," Jul 22 2009, URL above)
- **Lender behavior 2023–26: banks rolling distressed loans without paydown.**
  - Regional banks hold almost a third of US commercial mortgage dollars (over $1.6T).
  - Borrowers at regional banks were more than 50% less likely to put in additional equity when their loans were underwater. Where undercollateralization was worse, the paydowns were smaller.
  - Within each market, regional banks disproportionately hold loans on the oldest properties and in low-rent neighborhoods.
  - THE CHECK: when buying a property or note from, or partnering with, a bank lender, assume the existing loan has been extended to delay loss recognition. Re-mark it.
  [NEW] (Hinzen, Severino and Van Nieuwerburgh, Oct 2025, Wharton-hosted, URL above)

### 1.9 Red flags and automatic passes (additions)

- DSCR built on anticipated leases or market rent rather than leases in place (the 2005–07 "pro forma" loan). [NEW] (Levitin and Wachter 2013)
- Interest-only for the full term on a transitional or office asset. [NEW] (same)
- LTV held flat while the market's cap rates compressed. [NEW] (same)
- Class B office underwritten at historical occupancy, or a conversion exit with no costed plan. [NEW] (Gyourko, KaW May 2024)
- Insurance expense held flat in a coastal or wildfire market. [NEW] (Keys and Mulder 2024–26)
- Cap rate quoted without saying NOI or cash flow, or current or forward year. [NEW] (Linneman WP 519)

### 1.10 Hard questions (additions)

- What is DSCR on leases in place, after a recurring capex reserve of about 17% (MF) to 36% (retail) of NOI? [NEW]
- Is your exit cap NOI- or cash-flow-based? What spread to the 10-year Treasury does it imply? How does it compare with today's REIT-implied cap for the sector? [NEW]
- What is the bound insurance quote today against your pro forma, and what did premiums do over the last three renewals? [NEW]
- Show lease expiries by year against the loan maturity. What occupancy did you assume after rollover? [NEW]
- At a 30% lower value, what is the LTV, and who funds the paydown at maturity? [NEW]

### NEW 1.11 CRE distress 2023–26: what changed and how to underwrite it

- Office is a structural, not cyclical, problem: demand down 15% to 40% and trades at 25% to 50% of pre-pandemic prices. Distress arrives lease-roll by lease-roll over a five-year window (Gyourko, KaW 2024).
- Bank lenders matter more than CMBS for many mid-size loans. Regional banks make up about 70% of bank lending to real estate (Wachter, KaW 2023, https://knowledge.wharton.upenn.edu/article/fallout-from-the-banking-crisis-whats-ahead). They are the most likely to extend rather than enforce (HSV 2025).
- Regional-bank CRE concentration:
  - The median regional bank's CRE loans run about 312% of total capital.
  - 54.8% of regional banks exceed the 300% supervisory-attention threshold, up from 37.7% in 2015.
  - Outliers (NYCB/Flagstar) were above 500%.
  - Concentration leaves banks exposed to even local shocks, most often in multifamily and retail.
  - Use: when the counterparty is a regional bank (seller of notes, co-lender, A-note holder), check its CRE/capital ratio. A highly concentrated bank may be a forced seller or a slow enforcer. (HSV 2025, Wharton-hosted)
- Discovery method for loan buyers: use county mortgage and deed records with property-type price indices to rebuild a lender's portfolio and LTVs when the lender discloses little (HSV 2025).
- Insurance and climate repricing is now a standing underwriting line (Keys and Mulder).

---

## 2 Tech and Venture

### 2.3 Diligence checklist by workstream

- **FINANCIAL AND METRICS: ask for the cohort inputs behind any retention claim.** Request quarterly customers acquired, total active customers, and orders or transactions per period. Rebuild cohort value (CBCV). Blue Apron's pre-IPO data showed declining cumulative net revenue per recent cohort and about 70% six-month churn. Pricing fell from a $15–17 range to $10 within days of the analysis. [STRENGTHENS 2.3, 2.7] (Fader and McCarthy, KaW Feb 2018, URL above)
- **TECH: independently verify the core technical claim against a stated demo or test protocol.** Separate "a technology that did not work out," which is ordinary venture risk, from "lying about what works today," which is fraud (Hughes). [STRENGTHENS 2.3] (KaW Theranos, Mar 2018)
- **TEAM AND GOVERNANCE: check voting control, board expertise, and sunset terms on founder super-voting shares.** [NEW] (Guay, KaW Theranos)
- **PROCESS: keep the diligence floor in competitive rounds.** Hot rounds and busy partners are where diligence hours fall and misallocation rises (Fu and Taylor). [NEW] (NBER w33987)

### 2.4 The numbers

- **Last-round valuation is not a mark.**
  - FTX raised $400M at a $32B valuation, up from $25B six months earlier, before it collapsed.
  - Stripe was reported to be raising about $4B at about $55B, roughly half its 2021 valuation of $95B.
  - CHECK: reprice any 2021-vintage round marks against current comparables, and model a down round.
  [NEW] (Erickson, "What's Wrong with the Private Equity Market — and How to Fix It," KaW, Mar 13 2023, https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/)
- **Acquisition-driven growth.** A "hockey stick made entirely of acquisition" (Fader on Wayfair), with repeat purchase weaker than the leading incumbent's, means growth needs ever-rising marketing spend. Track the share of revenue from customers acquired in the period against prior cohorts. [NEW] (KaW Feb 2018)

### 2.7 Failure modes (additions)

- **CASE FILE: Theranos, about $700M raised.** False technical, revenue, and customer claims under founder voting control. THE CHECK: independent technical validation, revenue-to-invoice-to-cash reconciliation, direct confirmation of named customers, and a governance map. [NEW] (KaW Mar 2018)
- **CASE FILE: Blue Apron IPO, 2017.** Growth bought with marketing; about 70% of acquired customers churned within six months. THE CHECK: cohort-level CBCV before pricing. [NEW] (KaW Feb 2018)

---

## 3 Debt to Businesses

### 3.2 Data room index (additions)

- **The complete amendment, waiver, and consent history for every credit facility since origination.** Over 90% of long-term private credit agreements are renegotiated before stated maturity, usually early and usually not because of distress. A typical bank loan is renegotiated about five times, roughly every nine months, with pricing, maturity, amount, and covenants all changing. The amendment trail is the real credit history. [NEW] (Roberts and Sufi, "Renegotiation of Financial Contracts: Evidence from Private Credit Agreements," JFE 93, 2009, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf; Roberts, "The Role of Dynamic Renegotiation and Asymmetric Information in Financial Contracting," JFE 116, 2015, https://www.nber.org/papers/w20484)
- **Every factoring, supply-chain finance, receivables-sale, and off-balance-sheet obligation.** First Brands: about 5x stated leverage against about 20x all-in. [NEW] (Harker, KaW Apr 2026)

### 3.3 Diligence checklist (additions)

- **Maintenance covenants have measurable teeth. Price them; do not give them away.**
  - After a financial covenant violation, capital expenditure falls by about 1% of capital per quarter, a 13% drop against pre-violation levels.
  - Violations are followed by cuts to acquisitions, leverage, and shareholder payouts, and by more forced CEO turnover. The Chicago Booth summary of Nini, Smith and Sufi puts it at about 1.5% before a violation and about 8% four quarters after.
  - Operating and stock performance improve after violations on average.
  - Use: in a covenant-lite deal the lender gives up an early-intervention right that, on average, adds value. Ask what the spread pays for that loss.
  [STRENGTHENS 3.6, 3.7] (Chava and Roberts, "How Does Financing Impact Investment? The Role of Debt Covenants," JF 63, 2008, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/CovenantInvestmentJF2008.pdf; Nini (then Wharton), Smith and Sufi, "Creditor Control Rights, Corporate Governance, and Firm Value," RFS 25, 2012, https://ideas.repec.org/a/oup/rfinst/v25y2012i6p1713-1761.html)
- **Covenant-lite delays the signal.** Lenders may not see trouble until full default, and the lack of covenants can make problem deals worse over time (practitioners at the 2009 Wharton PE and VC conference). [STRENGTHENS 3.7] (KaW, "Continuing Defaults by Private Equity Portfolio Companies Transform the Middle Market," Aug 5 2009, https://knowledge.wharton.upenn.edu/article/continuing-defaults-by-private-equity-portfolio-companies-transform-the-middle-market/)
- **PE-backed borrowers and AI-exposed software borrowers need their own stress.** About one-fifth of loans in semi-liquid private credit funds are to software firms. AI disruption of SaaS led to sharp revisions in their default probabilities in 2026 (a "software crisis"). CHECK: for recurring-revenue loans, stress ARR for AI substitution (seat compression, price pressure) and test the debt on downside ARR, not on ARR multiples. [NEW] (KaW, "Why Semi-Liquid Private Credit Funds Are in Fragile Territory," Oct 26 2026, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/)

### 3.4 The numbers (additions)

- **How much of a loan spread is credit risk.**
  - Matching syndicated loans with the same firm's bond spreads on the same day, then adjusting for seniority, banks earn a premium over the market price of credit risk.
  - The premium is about 142 to 172 bp of an average all-in drawn spread of 279 bp: about half, and up to 61% in one model, for secured term loans to non-investment-grade firms.
  - Use: when comparing a private loan's yield with bonds or a fund's "illiquidity premium," do not treat the whole spread as pay for default risk.
  [NEW] (Schwert, "Does Borrowing from Banks Cost More than Borrowing from the Market?," JF 2020, Rodney White WP 03-18, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/04/03-18.schwert.pdf)
- **Recovery anchors by priority.** In bankruptcies of firms with both loans and bonds outstanding (Moody's Ultimate Recovery Database, 1995–2013), average recovery was:
  - Loans: 84%.
  - Secured bonds: 60%.
  - Senior unsecured bonds: 38%.
  Use as the base for LGD in 0.6 credit valuation. Commentators expect lower loan recoveries in the next cycle given covenant-lite and thinner junior debt cushions. [NEW] (Schwert, same paper)
- **Middle-market distress reference (2009).** Senior debt traded at 60 to 80 cents. Predicted middle-market default rates were 10% or more over 12 months. Lack of DIP financing made Chapter 11 a likely route to liquidation, so plan for out-of-court, equity-funded restructuring. [STRENGTHENS 3.7] (KaW Aug 5 2009)

### 3.7 Failure modes (additions)

- **CASE FILE: Toys "R" Us.**
  - What happened: a $7.5B 2005 LBO by Bain Capital, KKR, and Vornado. Debt service and 2018–19 maturities, combined with failure to adapt to e-commerce, ended in a September 2017 Chapter 11 and liquidation.
  - THE CHECK: a maturity wall tested against a secular-decline revenue case, not a cyclical one. Count capex the business needs to stay competitive before debt service.
  [NEW] (KaW podcasts, "The Demise of Toys R Us," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-demise-of-toys-r-us/, and "Can Toys R Us Recapture Its Glory Days?")
- **Do not "be wrong twice."** Be careful about buying more debt in a company where you already hold equity (Harvest Partners, 2009 Wharton PE conference). [NEW] (KaW Aug 5 2009)

### 3.9 Hard questions (additions)

- Show every amendment and waiver since origination, and what each one changed. [NEW]
- List every factoring, supply-chain-finance, and receivables-sale facility. What is leverage including them? [NEW]
- Is any collateral, invoice, or VIN pledged under another facility? Show the dedupe. [NEW]

---

## 4 Credit of All Kinds

### 4.2 Diligence by sub-strategy (additions)

- **Consumer credit and loan pools: look for clustering just above a credit cutoff.**
  - Low-documentation subprime loans just above the 620 FICO threshold, where securitization was easier, defaulted about 10% to 25% more than loans just below it (about 20% in one version), against a mean two-year default rate of about 5%.
  - The authors attribute this to lax screening when loans could be sold. The interpretation is contested (Bubb and Kaufman point to underwriting rules of thumb), but the diligence test holds either way.
  - CHECK: plot the loan tape's FICO and DTI distribution and default rates around every eligibility cutoff. A bunch or a performance jump at the cutoff signals origination gaming.
  [NEW] (Keys (now Wharton), Mukherjee, Seru and Vig, "Did Securitization Lead to Lax Screening? Evidence from Subprime Loans," QJE 2010, https://corpgov.law.harvard.edu/2009/06/08/did-securitization-lead-to-lax-screening/)
- **CLO equity and debt (structured credit row).**
  - CLO collateral pools perform like loan mutual funds with similar risk and fees: a gross PME of about 0.97.
  - Equity tranches have an average PME of about 2.47 before management fees. After fees, outside equity earns about what its systematic risk would predict.
  - Management fees are typically about 50 bp of the collateral balance, and have fallen since 2017. Returns eroded as the market grew.
  - Two-thirds of leveraged loan issuance since 2008 (about $2.1T) was funded by CLOs.
  - CHECK: underwrite CLO managers on after-fee PME by vintage, and on how much of the gross outperformance the manager keeps.
  [NEW] (Cordell, Roberts and Schwert, "CLO Performance," Nov 2020, Rodney White and Jacobs Levy, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf)
- **CLO structural resilience.**
  - With 40% recovery, about 60% of the loans in a CLO pool would have to default before AAA tranches lose money. For comparison, the cumulative 1931–33 default rate for risky debt was 31%.
  - Typical concentration limits: 15% per industry and 2% per obligor.
  - Pre-2008 AAA CLO tranches lost nothing (S&P). Pre-2008 AAA CDO tranches lost $325B (Cordell et al. 2019).
  - CHECK: for any CLO or CLO-like vehicle, confirm the obligor and industry limits and the AAA break-even default rate at a stated recovery.
  [NEW] (Roberts and Schwert, "Why Collateralized Loan Obligations Will Not Cause the Next Financial Crisis," KaW, Aug 10 2020, https://knowledge.wharton.upenn.edu/article/clos-will-not-cause-next-financial-crisis/)
- **Distressed and special situations.** Liability management exercises (LMEs) are now a main out-of-court workout tool. Diligence must map which creditors can be primed or stripped under the existing documents (Hotchkiss roundtable). [NEW, WEAK: roundtable listing only, no white paper reviewed] (WFFI Policy Series, "The Ambiguous Economics of Out-of-Court Workouts," Apr 16 2026, https://wffi.wharton.upenn.edu/policy-series-topics/)

### 4.5 Failure modes (additions)

- **CASE FILE: Tricolor Holdings, 2025.** A subprime auto lender with alleged double-pledging of collateral across warehouse lenders. THE CHECK: collateral-level dedupe across all lenders and independent verification of each pledged receivable. [NEW] (Harker, KaW Apr 2026)
- **Private credit opacity.** Private credit is about $1.8T to $2T. Pricing and risk are visible only to a few parties, marks are model-based, and regulators have limited system-wide data. Labels like "alternative assets," "direct lending," or "multi-strategy income" can hide private-loan exposure. CHECK: look through to holdings and how marks are set. [STRENGTHENS 4.6] (Goldstein, "Five Things to Know About Private Credit," KaW, May 5 2026, https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit)
- **Bank leverage behind private credit.** Bank lending to private-credit vehicles rose from about $8B (2013) to about $95B (end-2024). Bank commitments to PE and private-credit sponsors are about 14% of bank lending to nonbanks, up from about 1% a decade earlier. CHECK: the fund-level leverage stack (subscription line, NAV facility, asset-based facility) and its margin-call triggers. [NEW] (Harker, KaW Apr 2026)

---

## 5 Private Equity and M&A

### 5.3 Diligence by workstream (additions)

- **IT and cyber diligence moves price.** Verizon cut $350M from the Yahoo price after late-stage discovery of undisclosed data breaches. Budget cyber diligence before signing, not after. [STRENGTHENS 5.3] (Feldman and Chunduru, KaW Dec 2025)
- **Litigation diligence can dwarf the price.** Bayer–Monsanto ($63B, 2018) erased more than $50B of shareholder value on underestimated litigation risk. BofA–Countrywide (about $4B, 2008) led to at least $17B of mortgage settlements. CHECK: a model of contingent liabilities, including mass-tort and successor exposure. [NEW] (same)
- **Accounting diligence.** HP–Autonomy ($11B, 2011) was followed by an $8.8B write-down in 2012 over alleged accounting problems. CHECK: forensic revenue testing of the target, not a review of the seller's QoE alone. [NEW] (same)
- **Healthcare carve-out or roll-up (cross-ref 11).**
  - PE ownership of nursing homes raised short-term patient mortality by about 10% to 11% (about 1.7 percentage points, detectable within 15 days of discharge).
  - Frontline nursing-assistant hours per patient-day fell about 3%.
  - Costs shifted toward non-patient items: monitoring fees, interest, and lease payments.
  - Sample: 1,674 acquisitions in 128 deals among 12,400 for-profit homes.
  - CHECK: in government-reimbursed care (about 75% of nursing-home revenue), model regulatory and reputational exposure from staffing and quality metrics, and from fee, lease, and interest leakage to the sponsor or landlord.
  [NEW] (Atul Gupta (Wharton), Howell, Yannelis and Abhinav Gupta, NBER w28474, https://www.nber.org/papers/w28474; KaW, Jul 22 2024, https://knowledge.wharton.upenn.edu/article/how-to-align-private-equity-motives-with-nursing-home-outcomes/)

### 5.4 The numbers (additions)

- **Base rate: 70% to 90% of acquisitions underperform their own expectations.** High premiums are hard to recover through synergies. Examples:
  - Tyson–Hillshire: a 70% premium, about $2B of value destroyed against a fair value near $47/share.
  - GE–Alstom: a $22B impairment.
  - Kraft Heinz: more than $28B of write-downs.
  - Microsoft–Nokia: a $7.6B impairment on a $7.2B deal.
  - Sprint–Nextel: nearly $30B of goodwill impairment.
  - Quaker–Snapple: bought for $1.7B, sold for $300M.
  - Yahoo–Tumblr: bought for $1.1B, sold for about $3M.
  [NEW] (Feldman and Chunduru, KaW Dec 2025)
- **Search funds.**
  - Historical average investor IRR is about 37% (Stanford study, cited 2007).
  - About 25% of searches never close an acquisition.
  - Historical enterprise values were $4M to $11M.
  - Search-stage capital is about $30K to $50K per unit, and about 90% of search investors take up the acquisition round.
  - Failures cluster in capital-intensive targets whose growth fell short.
  - The seller typically stays 6 to 12 months for transition.
  - Figures are dated (2007); update against the current Stanford GSB search fund study.
  [NEW, WEAK: dated practitioner figures] (KaW podcast, "Looking for a Company to Run? Search Funds Could Be the Answer," Aug 22 2007, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/looking-for-a-company-to-run-search-funds-could-be-the-answer/)

### 5.7 Failure modes (additions)

- **CASE FILE: Toys "R" Us, $7.5B LBO in 2005, Chapter 11 in 2017.** See 3.7. THE CHECK: a secular-decline downside case plus a maturity wall. [NEW] (KaW)
- **CASE FILE: Steward Health Care / Cerberus.** A 2016 sale-leaseback of the hospital real estate to MPT ($1.25B for Massachusetts) funded dividends and left escalating rents. Chapter 11 followed in May 2024. THE CHECK: model rent coverage after any sale-leaseback, and trace where the proceeds went. [NEW, context (non-Wharton sources): Brookings, https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/; Wharton evidence on the lease-payment channel is in Gupta et al. above]
- **Dividend recaps.** In 2006–07, Wharton lender roundtables reported recaps priced at little discount to LBO leverage. Some lenders refused to finance them. CHECK: in return attribution (0.7 item 6), split IRR from recaps out from earnings growth. [STRENGTHENS 0.7, 5.9] (KaW, "Lender Roundtable: Outlook on Debt Markets," https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/)

### 5.9 Hard questions (additions)

- What is our walk-away price, who set it, and is that person on the deal team? [NEW] (Feldman)
- Which synergies are cost and which are revenue? What is each one's probability and timing? What are the dis-synergies? [NEW]
- What contingent liabilities (litigation, data breach, product) did diligence price, and how? [NEW]

---

## 6 Energy and Infrastructure

### 6.4 Diligence checklist: power and grid (additions)

- **An interconnection queue position is not power. Base rates:**
  - About 20% of projects that requested interconnection from 2000 to 2018 reached commercial operation by end-2023 (LBNL).
  - In PJM, of projects entering 2014 to 2023, 67% withdrew and 16% are operating.
  - Time to connect went from under 2 years before 2008 to more than 5 years, and 7+ in places.
  - Projects in PJM's 2018–2020 entry cohort got interconnection agreements only in April 2025.
  [STRENGTHENS 6.4, 6.8] (Kleinman Center, "Will Interconnection Reform Unlock the Grid?," Energy Policy Now, Jul 8 2025, https://kleinmanenergy.upenn.edu/commentary/podcast/will-interconnection-reform-unlock-the-grid/)
- **Post-agreement delay is its own line item.** In PJM data, permitting delays averaged more than 14 months, and transmission-owner procurement (largely high-voltage transformers) added nearly 20 months. Public queue data often omits or overwrites signed-agreement dates, so get the executed agreement itself. [NEW] (same)
- **FERC Order 2023 checks.**
  - Studies moved to a "first-ready, first-served" cluster process, with readiness deposits that scale with project size.
  - The required maximum cluster-study duration is 150 days.
  - Regions may get variations. PJM, for example, proposed "reasonable efforts" instead of delay penalties.
  - CHECK: the project's cluster, its readiness status, and the region's compliance posture.
  [NEW] (same)
- **Firm versus non-firm service for data centers (PJM 2026).** PJM's board letter of January 16, 2026 proposed:
  - "Bring your own generation" for firm service.
  - "Connect and manage," meaning curtailable service that may force a switch to diesel backup.
  - A new-supply-only backstop auction with longer-term pricing, subject to FERC approval.
  - CHECK: whether the site's power is firm or curtailable, the backup-generation permit and fuel, and who bears incremental transmission and capacity costs.
  - In PJM, network service does not prevent curtailment because dispatch is cost-based. In ERCOT, connect-and-manage projects can be curtailed under grid stress.
  [NEW] (Kleinman Center, "How PJM Is Grappling With Data Center Power Demand," Feb 3 2026, https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/)
- **Tax credits (federal policy, check per deal).**
  - Kleinman's April 2026 summary of the OBBBA: wind and solar had to begin construction before July 2026, with a four-year completion window, or be placed in service before 2028. Credits phase out starting in 2028 and end by 2032. Transferability was preserved.
  - Foreign-entity-of-concern (FEOC) "material assistance" rules apply to facilities beginning construction after December 31, 2025. They can effectively disqualify projects using Chinese-sourced supply or IP, and developers warn PPA prices will rise.
  - CHECK: the begin-construction evidence (safe harbor), a FEOC supply-chain trace with supplier certifications, and transfer-buyer recapture protection.
  - Verify against current Treasury and IRS guidance.
  [NEW] (Kleinman Center, Draves, Apr 27 2026, https://kleinmanenergy.upenn.edu/commentary/blog/the-landscape-of-renewable-energy-in-the-united-states-in-an-era-of-subsidy-scrutiny/; Ying and Hu, "RE+ 2025," Oct 9 2025, https://kleinmanenergy.upenn.edu/commentary/blog/re-2025-navigating-the-u-s-power-systems-current-challenges/)

### 6.5 The numbers (additions)

- **PJM capacity price shock (merchant revenue and data-center cost input).** These are speaker figures and need confirming against PJM auction reports.
  - Total PJM capacity bills went from about $2.2B for 2023 and 2024 combined to more than $14B in a single year.
  - Capacity costs were about $40B over three years. The market monitor attributes about half to data centers; NRDC cites $47B.
  - The last auction cleared about $16B under a price collar, against about $26B uncapped.
  - About 6.5 GW a year of data-center load is being added through 2030.
  - Use: merchant revenue models that rely on capacity payments need a collar-extension case and a collar-expiry case.
  [NEW, WEAK until confirmed with PJM/IMM primary reports] (Kleinman, Feb 3 2026)
- **Build times by technology (development to operation).**
  - Solar plus storage: 12 to 18 months (other Kleinman pieces say 18 to 24 months for solar).
  - Wind: about 2 years.
  - Combined-cycle gas: 3 to 4 years.
  - Gas turbine lead times: 4 to 6 years (Kleinman podcast). This corroborates bible 6.4's 3 to 7 years.
  - The cost of new gas generation roughly doubled over five years.
  [STRENGTHENS 6.4 Figure 11] (Kleinman Apr 2026; Kleinman Feb 2026; Kleinman Oct 2025)
- **Nuclear and contracted-baseload PPAs as offtake comparables.** Constellation–Microsoft: a 20-year PPA tied to the Three Mile Island Unit 1 (Crane) restart. Talen–AWS: up to 1,920 MW front-of-meter through 2042, which Talen says significantly reduces its market risk. Kleinman flags two risks: data-center demand that never shows up stranding grid build-out, and behind-the-meter deals shifting costs to other ratepayers, which is regulatory risk to the deal. [NEW] (Kleinman podcast "The Future of Electricity Demand in the AI Era," https://kleinmanenergy.upenn.edu/commentary/podcast/the-future-of-electricity-demand-in-the-ai-era/; company 8-Ks via SEC)

### 6.8 Red flags (additions)

- An interconnection agreement with no permitting plan and no transformer procurement schedule. [NEW]
- A data-center site marketed as having "secured power" whose service is non-firm or curtailable. [NEW]
- A renewable project relying on credits with no begin-construction evidence or FEOC trace. [NEW]

### 6.9 Hard questions (additions)

- Is the service firm or curtailable? If curtailed, what runs the load, under what permit, and for how many hours? [NEW]
- What has the queue done to your cluster? What is your withdrawal-penalty exposure? [NEW]
- Who pays for network upgrades and incremental capacity costs, and is that in the lease or PPA? [NEW]

---

## 7 CPG and Consumer Brands

- **Use customer-based valuation as the core commercial test for DTC.**
  - Get cohort data: customers acquired per period, active customers, orders, spend.
  - Fit retention and repeat rates.
  - Check whether revenue growth is acquisition-led. Wayfair's "hockey stick made entirely of acquisition," with repeat rates below Amazon's two decades earlier, priced at under $10 against a $64 stock.
  - Strong retainers (Harry's, Dollar Shave Club) show flattening cohort curves.
  [NEW for 7.2; STRENGTHENS 7.3 LTV:CAC] (Fader and McCarthy, KaW Feb 2018)
- **Treat company-defined unit economics as marketing.** Allbirds' S-1 framed CAC payback against first-purchase contribution on a $124 AOV, and the top-25% cohort's lifetime spend at $446. These are company projections, not audited. Recompute LTV from cohorts. [STRENGTHENS 7.4] (Context (non-Wharton): Allbirds S-1, 2021, SEC EDGAR)
- **Red flag: the company cannot or will not give acquisition counts and active-customer counts by period.** Fader and McCarthy note that most non-subscription firms disclose none of this. [NEW for 7.5]

---

## 8 Cannabis and Hemp

- **Banking access is the operating risk that industry participants underrated** (Wharton Business Daily). A Federal Reserve master-account denial after an eight-month review was called "a death sentence" for a cannabis-serving institution. CHECK: the operator's depository relationship, its tenure, any account-closure history, and the bank's own regulatory standing. Add a contingency plan for a sudden de-banking. [STRENGTHENS 8.3, WEAK: 2018–19 commentary, update for 2026 status] (KaW podcasts, "CannaBusiness: Marijuana Regulations and Banking Concerns," https://knowledge.wharton.upenn.edu/podcast/this-week-in-business/cannabusiness-marijuana-regulations-banking-concerns/; "The Pot Paradox," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/policy-paradox-legalized-marijuana/)
- Lane note: Wharton sources had nothing current on 280E or rescheduling. Defer to the bible's existing sources.

---

## 9 Operating Company Growth Equity

- **Forecast-record test (cross-ref 0.2).** Management with a history of optimistic misses is the population where unintentional errors become intentional misreporting. Compare the last three budgets with actuals. [STRENGTHENS 9.2] (Schrand and Zechman 2012)
- **Customer-cohort data request (cross-ref 2.3, 7).** [STRENGTHENS 9.2]

---

## 10 Funds and Co-Investments

### 10.4 Diligence checklist (additions)

- **Fee economics: most GP revenue is fixed.** In 238 funds raised 1992–2006, about two-thirds of expected GP revenue came from fixed components (management fees and transaction fees), which are not sensitive to performance (about 60% in the working-paper version). Buyout funds earn relatively more from fixed fees than VC funds. CHECK: model GP revenue under base and downside. If fixed fees dominate in the downside, alignment is weaker than headline carry suggests. [NEW] (Metrick and Yasuda (Wharton at the time), "The Economics of Private Equity Funds," RFS 23, 2010, Rodney White WP 07-17, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf; KaW podcast "Secrets of the Private Equity Trade," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/secrets-of-the-private-equity-trade/)
- **Manager selection rule.** Decline managers whose recent funds land consistently in the third or fourth quartile. Expect fund-size discipline (cut or right-sized funds) after a bubble. [NEW] (Erickson, KaW Mar 2023)
- **Semi-liquid and evergreen credit or RE vehicles (BDCs, interval funds, NAV REITs): a liquidity checklist.**
  - Redemption cap: typically 5% of shares per quarter. Check gating history and whether unmet requests carry forward.
  - Liquidity coverage: average cash about 5.5% of total net assets, net investment income about 2.5% a quarter (mostly paid out, since BDCs must distribute 90%), and loan maturities under 0.5% a quarter. Recurring 5% redemptions exhaust this quickly.
  - Secondary liquidity: about 80% of loans are unrated, and fewer than 20% are held by 10 or more fund families, so forced sales mean fire-sale discounts.
  - Leverage response: net debt issuance rises 0.38 percentage points of TNA for each 1-point increase in net outflows. That is a leverage-redemption feedback loop.
  - "Repurchases payable": deferred redemption payments that work like trade credit owed to exiting investors.
  - Stale NAV: if marks lag, redeeming investors exit above economic value at remaining holders' expense, which creates a first-mover run incentive.
  - Sponsor support (e.g. insiders buying in) is discretionary and may not scale.
  [NEW] (Fang, Goldstein and Zeng, via KaW Oct 26 2026, URL above)

### 10.5 The numbers (additions)

- **The 2026 semi-liquid credit stress test.**
  - Semi-liquid private credit net assets grew from $10B (2019) to $300B (end-2025), within a $3.5T global private credit market.
  - Q2 2026: $7.1B of repurchases against $3.8B of inflows, the sector's first aggregate net outflow. $10.7B of requests went unmet (gated).
  - Blue Owl Capital Corp II received redemption requests for about 22% of shares and Blue Owl Credit Income Corp about 40%. Blackstone, BlackRock, and Apollo vehicles also saw requests above the cap.
  - Earlier in 2026, Blue Owl ended quarterly redemptions from the $1.6B OBDC II, and Blackstone met record redemptions of about 8% of its flagship credit fund.
  [NEW] (KaW Oct 26 2026; Harker, KaW Apr 22 2026)
- **IRR is sensitive to holding period and financing events.** Report gross and net IRR with multiples (TVPI, DPI) and a PME. Use PME as Wharton researchers do for CLOs and private funds (Kaplan–Schoar PME; generalized PME, Korteweg–Nagel). [STRENGTHENS 10.5] (Cordell, Roberts and Schwert 2020 methodology; Linneman and Ross 2002)

### 10.6 Failure modes (additions)

- **CASE FILE: semi-liquid fund run dynamics, 2026.** Stale marks plus a 5% gate plus thin cash produced gating, rising fund leverage, and deferred payments. THE CHECK: the liquidity coverage ratio (cash + NII + maturities against the redemption cap), mark-to-market lag tests, and the redemption queue history. [NEW] (KaW Oct 2026)

---

## 11 Further Categories and Niches

- **Healthcare services (row addition).** Under PE ownership, nursing-home short-term mortality rose about 10% to 11%, frontline staffing fell about 3%, and costs shifted to fees, interest, and leases. Government payors are about 75% of revenue. CHECK: staffing ratios, CMS Five-Star trend after acquisition, fees and leases paid to related parties or landlords, and whether a sale-leaseback leaves rent coverage. [STRENGTHENS 11 healthcare row] (Gupta et al., NBER w28474; KaW Jul 2024)

### 11.1 Crypto and digital assets (additions)

- **Tokenized real-world assets (tokenized credit, RE, treasuries) are a new row.**
  - Market size: about $29B on public chains as of April 2026, excluding about $300B of stablecoins, plus $16.9B of private-credit tokens on Figure's Provenance chain, for about $46B in total. That is up from about $2.9B in 2022 and about $12B at end-2024.
  - The token is usually a contractual or beneficial claim on an off-chain asset held by an issuer, custodian, trust, or SPV, not direct title.
  - Core principle: a tokenized claim's trading speed should match the speed at which the underlying asset can honor redemptions.
  - CHECK:
    - what legal right the token conveys, and whether it is enforceable;
    - the custodian and whether the asset is bankruptcy-remote from the sponsor;
    - redemption mechanics, timing, and gates;
    - oracle design, governance, and fallback rules for NAV and collateral prices;
    - independent audit of the reserves or underlying assets.
  [NEW] (Cong, Mayer and Rabetti, "Tokenizing Real-World Assets," WFFI (Wharton) Policy Series white paper, 2026, https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf)
- **Stablecoin exposure.** Diligence covers reserve composition, redemption mechanism, and regulatory status. Algorithmic, crypto-collateralized, and synthetic designs sit largely outside the segregated-reserve frameworks. A reserve report shows backing at a point in time; controls keep it between reports. Context (non-Wharton): AICPA reserve-report criteria were issued March 2025. [NEW] (Wharton BDAP, "Stablecoin Toolkit" Parts I–II, 2026, https://bdap.wharton.upenn.edu/wp-content/uploads/2026/01/Stablecoin-Toolkit.pdf)
- **FTX lesson (cross-ref 0.4).** A $32B valuation at the last round. Customer assets were used for other ventures. CHECK: segregation and independent custody, as in 0.4. [STRENGTHENS 11.1] (KaW Nov 2022; Erickson KaW Mar 2023)

---

## A Templates

- **A.2 Diligence report template: add a "Diligence intensity" line** (hours with management in person, sites visited, references) and a "Collateral dedupe" line for credit (UCC sweep and item-level dedupe). [NEW] (Fu and Taylor 2025; Harker 2026)
- **A.3 Red-team prompt: add these items.**
  - Is any DSCR computed on anticipated rather than in-place leases?
  - Is the cap rate NOI- or cash-flow-based?
  - Is there off-balance-sheet financing (factoring, SCF) excluded from leverage?
  - Is any growth acquisition-driven, with weak cohorts?
  - Does any semi-liquid vehicle have redemptions above its liquidity coverage?
  [NEW]

## B Open Gaps and Interview Guide

- **B.1 "Real estate LTC and DSCR cutoffs":** partly addressed. Wharton gives an exit-cap benchmark (Linneman framework) and the in-place-lease DSCR rule (Levitin and Wachter), but no current LTC norms by deal size. Still a gap. [RESOLVES WEAK partially]
- **B.1 "Credit and specialty advance-rate and loss-rate norms":** adds recovery anchors (loans 84%, secured bonds 60%, unsecured 38%) and the CLO AAA break-even (60% defaults at 40% recovery). Advance rates are still a gap. [RESOLVES GAP partially]
- **B.2 interview additions.**
  - "How many hours did you spend with management in person before you committed?"
  - "Show me the amendment history."
  - "What is your fixed-fee share of GP revenue in the downside?"
  [NEW]

---

## NEW: proposed sections and chapters

1. **NEW 1.11 "CRE Distress 2023–26 and Bank Counterparties"** (drafted above). Covers office obsolescence, latent distress against reported delinquency, regional-bank concentration and extend-and-pretend, value-decline stress, and insurance repricing.
2. **NEW 4.x "Semi-Liquid and Evergreen Vehicles" (or 10.x).** BDCs, interval funds, NAV REITs, and evergreen PE. A liquidity coverage test, gate mechanics, stale-NAV run risk, and the leverage-redemption loop (Fang, Goldstein and Zeng 2026). Many LP and wealth-channel deals now come through these.
3. **NEW 3.x / 4.x "Collateral Integrity and Off-Balance-Sheet Leverage."** A standalone procedure:
   - a UCC sweep across all secured parties;
   - item-level dedupe (invoice, VIN, serial number);
   - an inventory of factoring and supply-chain-finance facilities;
   - direct debtor verification;
   - lockbox control.
   Anchored on First Brands and Tricolor (2025).
4. **NEW 0.x "Customer-Based Valuation and Cohort Diligence"** for any recurring-revenue or repeat-purchase business (SaaS, DTC, marketplaces, consumer subscription), with the CBCV data request list.
5. **NEW 0.x "Behavioral and Governance Red Flags":** forecast-miss history (Schrand and Zechman), founder voting control and board expertise (Theranos), deal-team confirmation bias and auction fever (Feldman), and thinner diligence in hot markets (Fu and Taylor).
6. **NEW 11.x "Tokenized Real-World Assets"** (drafted above).
7. **NEW 6.x "Data Center Power: Firm vs Non-Firm Service and Capacity-Market Exposure"** (PJM 2026 rules, BYOG, curtailment, backstop auction).
8. **NEW 4.x "Liability Management Exercises (LMEs)."** Document-level diligence on priming, uptiers, and drop-downs. Flagged by WFFI 2026 but needs non-Wharton primary sources (law-firm and court materials).

---

## Reading list additions (for 0.9)

- **Real estate.**
  - Linneman, *Real Estate Finance and Investments: Risks and Opportunities* (Linneman Associates). Zell/Lurie WP 519 (cap rates) and WP 637 (pricing CRE).
  - Levitin and Wachter, "The Commercial Real Estate Bubble" (Harvard Business Law Review, 2013).
  - Gyourko, "Understanding Commercial Real Estate: How Different from Housing Is It?" (NBER w14708).
  - Pavlov and Wachter on non-recourse put underpricing.
  - Keys and Mulder, NBER w32579 (insurance).
  - Hinzen, Severino and Van Nieuwerburgh, "Too-Many-to-Ignore" (2025).
  - Wharton REAL 7210, Real Estate Investment: Analysis and Financing (course description: https://real-estate.wharton.upenn.edu/programs/mba/course-descriptions/).
- **Credit and covenants.**
  - Chava and Roberts (JF 2008).
  - Roberts and Sufi (JFE 2009).
  - Roberts (JFE 2015).
  - Nini, Smith and Sufi (RFS 2012).
  - Schwert (JF 2020).
  - Cordell, Roberts and Schwert, "CLO Performance."
- **Private funds.**
  - Metrick and Yasuda, "The Economics of Private Equity Funds" (RFS 2010).
  - Metrick and Yasuda, *Venture Capital and the Finance of Innovation*.
  - Fang, Goldstein and Zeng, "The Fragility of Semi-Liquid Private Credit Funds" (2026).
- **Venture and valuation.**
  - Fu and Taylor, NBER w33987.
  - McCarthy, Fader and Hardie on customer-based corporate valuation (J. Marketing 2017; Marketing Science follow-ups).
  - Koller, Goedhart and Wessels, *Valuation* (McKinsey).
  - Holthausen and Zmijewski, *Corporate Valuation: Theory, Evidence and Practice*.
- **Fraud and governance.**
  - Schrand and Zechman (JAE 2012).
  - Wharton Forensic Analytics Lab (Daniel Taylor) work on insider trading and 10b5-1 abuse.
- **Energy.**
  - Kleinman Center *Energy Policy Now* episodes on interconnection reform (Jul 2025) and PJM data-center demand (Feb 2026).
  - LBNL "Queued Up" (cited there).
- **Digital assets.**
  - Wharton BDAP Stablecoin Toolkit (2026).
  - WFFI "Tokenizing Real-World Assets" (2026).

---

## Gaps this lane could not close (search budget exhausted)

- No current Wharton source on: construction LTC norms, real estate promote structures by deal size, venture debt terms, ABL advance rates, 280E/rescheduling, an EBITDA add-back study, subscription-line IRR inflation, or continuation-vehicle pricing.
- Faculty not mined in depth: Asuka Yamazaki, Raffi Amit, Christian Opp, Jules van Binsbergen, Robert Holthausen (beyond his textbook), Wayne Guay (beyond Theranos), and Daniel Taylor's specific 10b5-1 "three red flags."
- Not retrieved: Gyourko's NBER w14708 full text (CRE price-decline figures), and the Fu and Taylor hours-of-diligence distribution (only the abstract was read).

---

## Sources

1. Fu and Taylor, "Due Diligence and the Allocation of Venture Capital," NBER w33987 — https://www.nber.org/papers/w33987
2. Feldman and Chunduru, "Why Many M&A Deals Fail and How to Beat the Odds," KaW, Dec 8 2025 — https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/
3. Harker, "These investments promise high yield with bond-like safety...," KaW opinion, Apr 22 2026 — https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/
4. Magubane (quoting Goldstein), "Five Things to Know About Private Credit," KaW, May 5 2026 — https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit
5. "Why Semi-Liquid Private Credit Funds Are in Fragile Territory" (Fang, Goldstein, Zeng), KaW, Oct 26 2026 — https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/
6. Schrand and Zechman, JAE 2012 — https://repository.upenn.edu/accounting_papers/119
7. KaW podcast, "Are Overconfident Executives More Inclined to Commit Fraud?" — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/are-overconfident-executives-more-inclined-to-commit-fraud/
8. KaW, "What Silicon Valley Can Learn from the Theranos Fraud Case," Mar 19 2018 — https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/
9. KaW podcast, "What the FTX Collapse Means for the Cryptocurrency Market," Nov 22 2022 — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/what-the-ftx-collapse-means-for-the-cryptocurrency-market/
10. KaW, Fader and McCarthy on CBCV, Feb 12 2018 — https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/
11. MacMillan, van Putten and Baghai, "M&A's Overlooked Pitfall: The False Negative," KaW, Mar 30 2011 — https://knowledge.wharton.upenn.edu/article/mas-overlooked-pitfall-the-false-negative/
12. KaW, Wessels on Uber valuation — https://knowledge.wharton.upenn.edu/article/kicking-tires-ubers-17-billion-valuation-worth-much/
13. Linneman and Rubenstein, "How Should Commercial Real Estate Be Priced?," Zell/Lurie WP 637 — https://realestate.wharton.upenn.edu/working-papers/how-should-commercial-real-estate-be-priced/
14. Linneman, "What Should Stabilized Multifamily Cap Rates Be?," Zell/Lurie WP 519 — https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf
15. Gyourko, REIT/NCREIF lead-lag, Zell/Lurie WP 470 and WP 441 — https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/441.pdf
16. Keys and Mulder, NBER w32579 — https://www.nber.org/papers/w32579
17. KaW, "How Higher Property Insurance Premiums Mirror Climate Risk," Sep 24 2024 — https://knowledge.wharton.upenn.edu/article/how-higher-property-insurance-premiums-mirror-climate-risk/
18. KaW Ripple Effect, "Next Crisis: Empty Office Buildings | Joe Gyourko," May 14 2024 — https://knowledge.wharton.upenn.edu/podcast/ripple-effect/next-crisis-empty-office-buildings-joe-gyourko/
19. KaW podcast, "What's Going to Happen to All Those Empty Office Buildings?" — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-going-to-happen-to-all-those-empty-office-buildings/
20. Gyourko and Saiz, Zell/Lurie WP 407 — https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/407.pdf
21. Hinzen, Severino and Van Nieuwerburgh, "Too-Many-to-Ignore: Regional Banks and CRE Risks," Oct 2025 (Wharton-hosted) — https://wffi.wharton.upenn.edu/wp-content/uploads/2025/10/HSVRegional-Banks-and-CRE-Risks.pdf
22. Wharton Real Estate Review, "The Past, Present, and Future of CMBS," 2012 — https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/730.pdf
23. KaW podcast, "On Shaky Ground: Commercial Real Estate Faces Financial Tremors," Jul 22 2009 — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/on-shaky-ground-commercial-real-estate-faces-financial-tremors/
24. Linneman and Ross, "Towards Greater Transparency in Real Estate Private Equity Funds," KaW, Jul 31 2002 — https://knowledge.wharton.upenn.edu/article/towards-greater-transparency-in-real-estate-private-equity-funds/
25. Levitin and Wachter, "The Commercial Real Estate Bubble," Zell/Lurie WP 747 — https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/747.pdf
26. Gyourko, "Understanding Commercial Real Estate," NBER w14708 — https://www.nber.org/papers/w14708
27. Pavlov and Wachter, "Robbing the Bank: Non-Recourse Lending and Asset Prices" — https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/
28. Pavlov and Wachter, "Real Estate Crashes and Bank Lending" — https://realestate.wharton.upenn.edu/working-papers/real-estate-crashes-and-bank-lending/
29. Gordon, "The Crash and Rebound of Canary Wharf," Zell/Lurie WP 418 — https://realestate.wharton.upenn.edu/working-papers/the-crash-and-rebound-of-canary-wharf/
30. KaW, "Fallout from the Banking Crisis: What's Ahead" (Wachter) — https://knowledge.wharton.upenn.edu/article/fallout-from-the-banking-crisis-whats-ahead
31. Zell/Lurie, "The Premature Pricing of Commercial Real Estate Distress," WP 633 — https://realestate.wharton.upenn.edu/working-papers/the-premature-pricing-of-commercial-real-estate-distress/
32. Erickson, "What's Wrong with the Private Equity Market — and How to Fix It," KaW, Mar 13 2023 — https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/
33. Roberts and Sufi, JFE 2009 — https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf
34. Roberts, "Dynamic Renegotiation," NBER w20484 / JFE 2015 — https://www.nber.org/papers/w20484
35. Chava and Roberts, JF 2008 — https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/CovenantInvestmentJF2008.pdf
36. Nini, Smith and Sufi, RFS 2012 — https://ideas.repec.org/a/oup/rfinst/v25y2012i6p1713-1761.html
37. KaW, "Continuing Defaults by Private Equity Portfolio Companies Transform the Middle Market," Aug 5 2009 — https://knowledge.wharton.upenn.edu/article/continuing-defaults-by-private-equity-portfolio-companies-transform-the-middle-market/
38. Schwert, "Does Borrowing from Banks Cost More than Borrowing from the Market?," Rodney White WP 03-18 — https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/04/03-18.schwert.pdf
39. Cordell, Roberts and Schwert, "CLO Performance," Rodney White WP 10-20 — https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf
40. Roberts and Schwert, "Why Collateralized Loan Obligations Will Not Cause the Next Financial Crisis," KaW, Aug 10 2020 — https://knowledge.wharton.upenn.edu/article/clos-will-not-cause-next-financial-crisis/
41. Keys, Mukherjee, Seru and Vig, "Did Securitization Lead to Lax Screening?" (HLS Forum summary) — https://corpgov.law.harvard.edu/2009/06/08/did-securitization-lead-to-lax-screening/
42. KaW podcast, "The Demise of Toys R Us" — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-demise-of-toys-r-us/
43. KaW, "Lender Roundtable: Outlook on Debt Markets" — https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/
44. Gupta, Howell, Yannelis and Gupta, NBER w28474 — https://www.nber.org/papers/w28474
45. KaW, "How to Align Private Equity Motives with Nursing Home Outcomes," Jul 22 2024 — https://knowledge.wharton.upenn.edu/article/how-to-align-private-equity-motives-with-nursing-home-outcomes/
46. KaW podcast, "Looking for a Company to Run? Search Funds Could Be the Answer," Aug 22 2007 — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/looking-for-a-company-to-run-search-funds-could-be-the-answer/
47. Metrick and Yasuda, "The Economics of Private Equity Funds," Rodney White WP 07-17 — https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf
48. KaW podcast, "Secrets of the Private Equity Trade" — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/secrets-of-the-private-equity-trade/
49. Kleinman Center, "Will Interconnection Reform Unlock the Grid?," Jul 8 2025 — https://kleinmanenergy.upenn.edu/commentary/podcast/will-interconnection-reform-unlock-the-grid/
50. Kleinman Center, "How PJM Is Grappling With Data Center Power Demand," Feb 3 2026 — https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/
51. Kleinman Center, Draves, "The Landscape of Renewable Energy in the United States in an Era of Subsidy Scrutiny," Apr 27 2026 — https://kleinmanenergy.upenn.edu/commentary/blog/the-landscape-of-renewable-energy-in-the-united-states-in-an-era-of-subsidy-scrutiny/
52. Kleinman Center, Ying and Hu, "RE+ 2025: Navigating the U.S. Power System's Current Challenges," Oct 9 2025 — https://kleinmanenergy.upenn.edu/commentary/blog/re-2025-navigating-the-u-s-power-systems-current-challenges/
53. Kleinman Center podcast, "The Future of Electricity Demand in the AI Era" — https://kleinmanenergy.upenn.edu/commentary/podcast/the-future-of-electricity-demand-in-the-ai-era/
54. KaW podcast, "CannaBusiness: Marijuana Regulations and Banking Concerns" — https://knowledge.wharton.upenn.edu/podcast/this-week-in-business/cannabusiness-marijuana-regulations-banking-concerns/
55. KaW podcast, "The Pot Paradox" — https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/policy-paradox-legalized-marijuana/
56. Cong, Mayer and Rabetti, "Tokenizing Real-World Assets," WFFI Policy Series 2026 — https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf
57. WFFI Policy Series topics (LME roundtable, AML white paper) — https://wffi.wharton.upenn.edu/policy-series-topics/
58. Wharton BDAP, Stablecoin Toolkit — https://bdap.wharton.upenn.edu/wp-content/uploads/2026/01/Stablecoin-Toolkit.pdf
59. Wharton Real Estate MBA course descriptions (REAL 7210) — https://real-estate.wharton.upenn.edu/programs/mba/course-descriptions/
60. Context (non-Wharton): ABA Business Law Today on Tricolor — https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-october/seeing-red-flags-in-tricolor-collateral-interests
61. Context (non-Wharton): Brookings, "Lessons from the Collapse of Steward Health Care" — https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/
