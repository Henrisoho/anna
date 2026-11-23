# Findings: General / Primary & Institutional Lane (non-Ivy)
Agent lane: primary and institutional sources (rating agencies, regulators, DOJ/SEC, LBNL/DOE, industry bodies). Structure: chapter findings (0-11), new chapter drafts, source replacements, sources. Tags: [NEW], [STRENGTHENS x.y], [CONTRADICTS x.y], [CORRECTS/UPDATES x.y], [RESOLVES WEAK or GAP]. [VERIFY] marks drafter-knowledge items not yet confirmed on the primary site.

## 0 The Master Playbook

### 0.3 KYC, AML, and sanctions: status as of Nov. 2026
- [NEW] Corporate Transparency Act: FinCEN's final rule (announced Aug. 2026, effective on Federal Register publication Aug. 14, 2026) permanently exempts all DOMESTIC reporting companies and U.S. persons from BOI reporting, adopting and extending the March 2025 interim final rule. Only foreign companies registered to do business in the U.S. still report (FinCEN estimates about 28,000 filers versus 32.6M under the 2022 rule), and FinCEN will delete previously filed BOI on U.S. persons. Consequence for diligence: there is no federal BOI registry to lean on for U.S. sponsors; beneficial ownership must be collected and verified directly. The CDD Rule's 25%/control-person collection by covered financial institutions (31 CFR 1010.230) is unchanged. (Mayer Brown, Aug. 20, 2026, https://www.mayerbrown.com/de/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons; Federal Register 2026-16576, https://public-inspection.federalregister.gov/2026-16576.pdf; KPMG, https://kpmg.com/us/en/articles/2026/cta-beneficial-ownership-info-boi-reporting-fincen-final-rule.html)
- [NEW] Investment Adviser AML/CFT Rule (31 CFR Part 1032, adopted Aug. 2024): FinCEN's final rule (Federal Register Jan. 2, 2026; effective Dec. 31, 2025) postponed the compliance date from Jan. 1, 2026 to Jan. 1, 2028, and FinCEN has said it will revisit scope; the joint SEC/FinCEN CIP proposal for advisers is not final. Until 2028, a registered adviser or exempt reporting adviser has NO federal obligation to run an AML program or file SARs. CHECK: ask every GP whether it voluntarily runs an AML program, who its administrator relies on for investor KYC, and whether the administrator files SARs. (FinCEN, "FinCEN Issues Final Rule to Postpone Effective Date of Investment Adviser Rule to 2028," https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028; Federal Register, https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf; Proskauer, https://www.proskauer.com/blog/fincen-finalizes-twoyear-delay-of-the-investment-adviser-aml-rule-reaffirms-intent-to-further-review-and-tailor-the-rule-and-to-coordinate-with-other-rulemakings)
- [NEW] Sanctions: apply OFAC's 50 Percent Rule (an entity owned 50% or more in aggregate by blocked persons is itself blocked even if unlisted) to every investor, borrower and counterparty chain, and benchmark the sponsor's program against OFAC's "A Framework for OFAC Compliance Commitments" (May 2019: management commitment, risk assessment, internal controls, testing/auditing, training). (OFAC, https://ofac.treasury.gov/) [VERIFY exact document links before publication]
- [UPDATES 0.3 accredited-investor bullet] SEC staff no-action relief (Mar. 12, 2025) lets a 506(c) issuer treat a high minimum investment (at least $200,000 for natural persons, $1,000,000 for entities), paid in cash and not third-party financed, plus a written representation, as "reasonable steps" to verify accredited status. A high minimum is therefore no longer a red flag by itself, but it shifts the burden: verify the source of the cash. [VERIFY letter citation on sec.gov before publication]

### 0.4 Fraud detection: hard numbers (ACFE primary)
- [NEW] ACFE Occupational Fraud 2026: A Report to the Nations (2,402 cases, 143 countries, investigated Jan. 2024 to Sept. 2025): organizations lose an estimated 5% of revenue to fraud; median loss per case $104,000 (average $1.457M); FINANCIAL STATEMENT FRAUD is only 6% of cases but has the highest median loss, $1,000,000; corruption appears in 45% of cases (median $150,000). Owner/executive frauds have a median loss of $475,000, more than 9x employee frauds ($50,000). Frauds with three or more perpetrators: median $324,000 vs $55,000 for one (collusion defeats segregation of duties). 43% are detected by tips (nearly 3x the next method), more than half of tips from employees and almost one-third from vendors and customers. Typical case runs 12 months before detection; financial statement frauds run a median 24 months. More than half of frauds occurred because of a lack of, or override of, internal controls. 84% of perpetrators displayed at least one behavioral red flag. (ACFE, Occupational Fraud 2026, https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf)
- [NEW] Implication for the spine: a sponsor-level fraud is almost always an owner/executive fraud, the most expensive category. CHECK: in reference calls, ask former employees, vendors and customers directly ("have you ever been asked to do something with invoices, payments or records that felt wrong?"); the ACFE data say these are the people who detect fraud.
- [NEW] Duration math from the ACFE data: frauds caught within 6 months had a median loss of $40,000; delaying detection another 1-6 months more than doubled it ($100,000); the 5% lasting over five years had a median loss of $1.115M. Monitoring frequency is a loss-control variable. (ACFE 2026, duration section)

### 0.5 Verification of funds: QoE is not an audit
- [NEW] A QoE report carries no assurance. Under AICPA standards it is typically performed either as an agreed-upon procedures engagement (SSAE No. 19, AT-C 215 as revised, effective for reports dated on or after July 15, 2021: the practitioner reports procedures and findings, gives "no opinion or conclusion," and the engaging parties accept responsibility for the sufficiency of procedures) or as a consulting engagement under CS 100. CHECK: read the engagement letter and the scope section first; ask what was NOT tested and whether proof of cash covered every bank account in the bank confirmations. (Journal of Accountancy, "SSAE No. 19: flexibility for agreed-upon procedures," Sept. 2020, https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html; PCAOB AT 601 reference to CS 100, https://pcaobus.org/oversight/standards/attestation-standards/details/AT601)

### 0.6 Valuation: primary enforcement case for marks
- [NEW] CASE FILE, Infinity Q (valuation fraud): founder/CIO James Velissaris manipulated inputs to the supposedly independent Bloomberg BVAL pricing models to mismark OTC derivatives, allegedly overvaluing fund assets by more than $1B and collecting nearly $27M in fees on inflated NAV; he also fabricated valuation-committee minutes and gave them to the SEC. Sentenced April 2023 to 15 years. THE CHECK: "third-party pricing service" means nothing if the manager can choose models or alter inputs. Ask who has write access to the pricing inputs, obtain the administrator's independent price for a sample of Level 3 positions, and read valuation-committee minutes for dissent. (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-investment-officer-infinity-q-sentenced-15-years-prison; SEC Lit. Rel. 25331, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25331)
- [NEW] CASE FILE, SQN Capital Management (SEC, Oct. 9, 2026, settled): the principal personally prepared the only valuations for four funds while telling investors an independent expert did, and allegedly materially inflated them from at least 2019 through 2025. THE CHECK: obtain the named valuation firm's engagement letter and call the firm. (SEC Lit. Rel. 26671, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671)

## 1 Real Estate

### 1.5 The numbers: LTC/DSCR anchors from primary agency programs (resolves the 1.5 WEAK line and B.1 gap in part)
- [RESOLVES WEAK or GAP: 1.5 "Loan-to-cost, construction 70% to 80% WEAK" and B.1 "Real estate LTC and DSCR cutoffs"] Use the federal programs as the CEILING, not the norm: HUD Mortgagee Letter 2025-03 (Jan. 8, 2025) raised the Section 221(d)(4) market-rate new-construction maximum from 85% to 87% loan-to-cost and cut the minimum DSCR from 1.176x to 1.15x (7% vacancy factor), with the same loosening applied to 223(f) acquisition/refinance; affordable 221(d)(4)/223(f) went to 90% LTC/LTV at 1.11x. These are government-insured, 40-year, fully amortizing, non-recourse loans: a private construction lender at or above these levels is lending at an insured-program ceiling without the insurance. Private bank construction loans therefore anchor below the 12 CFR 365 80% supervisory LTV ceiling for commercial/multifamily construction; the bible's 70%-80% LTC band is consistent with sitting under both. Verify the current ML before use (HUD has issued further MLs in 2025-26, e.g. Middle Income Housing, ML 2025-02/2026-01). (HUD ML 2025-03, https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf; Nixon Peabody summary, Jan. 14, 2025, https://www.nixonpeabody.com/insights/alerts/2025/01/14/hud-adopts-relaxed-loan-sizing-standards-for-fha-insured-loans; HUD 2010 ML on Criterion 5 DSCR history, https://www.hud.gov/sites/documents/10-11hsgn.pdf)
- [STRENGTHENS 1.5] Agency multifamily DSCR/LTV are set in Fannie Mae Form 4660 (Multifamily Underwriting Standards), tiered Tier 1-4; the Guide itself requires a Key Principal non-recourse guaranty on any fixed-rate loan underwritten below 1.35x DSCR, and underwritten debt service uses the HIGHER of the note rate or Fannie's underwriting rate floor. CHECK: ask the sponsor which agency tier the stabilized asset would size to at the floor rate; that is the takeout test for a construction or bridge loan. (Fannie Mae Multifamily Selling and Servicing Guide, Sec. 203.02 and 311, https://mfguide.fanniemae.com/fnmf-pdf/download/9906)
- [NEW] Takeout-sizing CHECK: size the takeout at the agency underwriting floor rate, not the current coupon. A bridge loan underwritten to exit at 1.25x on today's rate can fail at the agency floor.

### 1.2 Regulatory anchor (additions)
- [NEW] The June 29, 2023 interagency Policy Statement on Prudent Commercial Real Estate Loan Accommodations and Workouts (OCC, Fed, FDIC, NCUA; 88 FR 43115) replaced the 2009 workout statement and added a section on short-term accommodations. Use it as the reference for what a "prudent" extend-and-amend looks like; when a sponsor's track record shows serial extensions, ask whether each was a documented workout under this framework or simply deferred loss recognition. (Federal Reserve SR 23-5, https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm; FDIC FIL-34-2023, https://fdic.gov/news/financial-institution-letters/2023/fil23034.html; Federal Register, https://www.govinfo.gov/content/pkg/FR-2023-07-06/html/2023-14247.htm)

### 1.8 Failure modes: new 2025 case files (SEC primary)
- [NEW] CASE FILE, First Liberty Building & Loan (Georgia), SEC July 10, 2025: at least $140M from about 300 investors via promissory notes and loan participations promising up to 18%, purportedly funding short-term business bridge loans "with few defaults." Most loans defaulted; from at least 2021 new money paid old investors; founder allegedly spent $2.4M+ on credit cards, $335K on rare coins. THE CHECK: loan-tape audit with borrower-level payment history traced to bank deposits; any "few defaults" claim must be proven with a delinquency roll. (SEC Press Release 2025-98, https://www.sec.gov/newsroom/press-releases/2025-98-sec-charges-georgia-based-first-liberty-building-loan-its-owner-operating-140-million-ponzi-scheme)
- [NEW] CASE FILE, LeFever Mattson (California), SEC May 22, 2025: former CEO allegedly sold about 200 investors at least $46M of fake interests in real estate LPs and commingled funds. THE CHECK: confirm every claimed LP interest against the entity's own records and the county recorder for the property. (SEC Press Release 2025-76, https://www.sec.gov/newsroom/press-releases/2025-76-sec-charges-former-real-estate-investment-ceo-operating-multimillion-dollar-ponzi-scheme)
- [STRENGTHENS 1.8 Drive Planning] SEC added charges on Dec. 30, 2025 against Drive Planning's former COO and a former managing partner, alleging they told investors the 10% "Real Estate Acceleration Loan" return was guaranteed and backed by collateral. Lesson: the second-tier executives and sales agents are also defendants; background-check the whole placement chain. (SEC litigation releases index, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26456)

## 2 Tech and Venture

### 2.4 The numbers: replace vendor benchmarks with institutional ones
- [RESOLVES WEAK: networkcraft/cxcash/designrevision; RESOLVES GAP B.1 "How venture investors weight the Rule of 40 against NRR by stage"] ICONIQ (State of Software 2025 and its Growth & Efficiency work): the Rule of 40 (YoY ARR growth + FCF margin) became the metric most correlated with public-market multiples over the past year, outperforming growth alone and NRR; yet a one-point increase in revenue growth has nearly twice the valuation impact of a one-point increase in FCF margin. ICONIQ only begins to place real weight on the Rule of 40 at about $25M ARR or more, because early growth rates inflate the score. Practical weighting: below ~$25M ARR, underwrite growth plus NRR/GRR and burn; above ~$25M ARR, Rule of 40 becomes a primary screen. Net dollar retention for scaled software is "settling into a healthy ~110-120% range." (ICONIQ, State of Software 2025, https://www.iconiq.com/growth/reports/2025-state-of-software and https://www.iconiq.com/growth/insights/growth-and-efficiency)
- [CONTRADICTS 2.4 "NRR median about 117% in 2026"] For PRIVATE SaaS the median is much lower: the 2025 KeyBanc Capital Markets / Sapphire Ventures private SaaS survey reports gross retention near 90% and net retention just above 100% (the 2024 edition put median NDR at 101%), with projected 2025 ARR growth of about 20% (15% in 2024). A 117% NRR is a top-quartile public/late-stage number, not a private-company median. (Sapphire Ventures, 2025 KeyBanc Capital Markets and Sapphire Ventures SaaS Survey, https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey)
- [STRENGTHENS 2.4, with vintage warning] Bessemer "Scaling to $100 Million" (2021, refreshed 2024) benchmarks by ARR band: $1-10M ARR median growth 165% (top 230%+), median NRR 125% (top 145%+); $10-25M median growth 87%, NRR 117%; $100M+ median growth 57%, NRR 115%. Gross retention averages 85%-90% (SMB can work at 70%-80%). CAC payback targets: SMB under 12 months, mid-market under 18, enterprise under 24. Gross margin long-run aim 65%-70%, top performers 80%+. These are 2021-vintage (ZIRP) figures: use as the "top-performer" bar, and use KeyBanc/Sapphire for today's median. (Bessemer Venture Partners, Scaling to $100 Million, https://www.bvp.com/atlas/scaling-to-100-million)
- [NEW] CAC payback median 16 months for B2B SaaS in calendar 2025, interquartile 10-24 months (Benchmarkit). Supports the bible's "under 18 months healthy." (Benchmarkit via Growth Unhinged 2025 SaaS Benchmarks Report, https://kylepoyar.substack.com/p/2025-saas-benchmarks-report) [Practitioner data set; acceptable cross-check]
- [NEW] Financing cadence (Carta, Q2 2025): median time between rounds 696 days across stages; seed-to-Series A median 616 days (about 20 months); median primary seed pre-money a record $15.6M; median Series A pre-money $47.9M; seed deal count down 25% YoY, Series A down 18%. Down rounds were about 17% of new rounds in Q3 2025 (just over 19% in Q1 2025). CHECK: runway must cover at least 24 months to the next round at today's cadence, not the 12-18 months of 2021. (Carta, State of Private Markets Q2 2025, https://carta.com/data/state-of-private-markets-q2-2025/; Carta Series A Q2 2025, https://carta.com/data/series-a-fundraising-q2-2025; Carta Q3 2025, https://carta.com/data/state-of-private-markets-q3-2025-full-report/)

### 2.7 Failure modes: primary case file
- [STRENGTHENS 2.7 "Revenue-quality fiction"] CASE FILE, Frank / JPMorgan (DOJ SDNY): founder Charlie Javice claimed 4.25 million users when Frank had about 300,000, and had a synthetic list of 4M+ fake customers generated to pass diligence; JPMorgan paid $175M. When JPMorgan emailed 400,000 "customers," about 70% bounced. Sentenced Sept. 29, 2025 to 85 months; restitution over $287M. Judge Hellerstein said JPMorgan had "a lot to blame themselves" for weak diligence. THE CHECK: never accept a user/customer list as evidence; test a random sample for live activity (logins, transactions, deliverable email) through the company's production systems with your own engineer present. (DOJ SDNY, "Startup CEO Charlie Javice Sentenced to 85 Months," https://www.justice.gov/usao-sdny/pr/startup-ceo-charlie-javice-sentenced-85-months-prison-175-million-fraud)

## 3 Debt to Businesses

### 3.4 The numbers: primary replacements for botminds/coyotewealth/ctacquisitions
- [RESOLVES WEAK: "Federal Reserve data via botminds.ai"; CORRECTS 3.4 "Median interest cover 2.2x"] The primary source is the Federal Reserve FEDS Note "Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution" (Aug. 11, 2026), on 2025 loan issuance (PitchBook, KBRA Direct Lending Deals, S&P): private-credit borrowers median revenue $223M (IQR $35M-$700M) vs $902M for leveraged-loan borrowers; median debt/EBITDA 5.0x vs 3.2x; interest coverage (EBITDA/cash interest) 2.2x vs 3.7x, which the Fed reports as an AVERAGE, not a median. Private credit is marked quarterly on internal or third-party models; leveraged loans are priced daily. (https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html)
- [NEW] Who holds private credit (Fed, Q3 2025): private debt funds 54.7%, perpetual (non-traded) BDCs 18.7%, public BDCs 12.4%, middle-market CLOs 5.9%, private BDCs 5.4%, interval funds 3.0%. About 70% of small firms' new borrowing is in private credit. Ask which vehicle holds your loan: a perpetual BDC with redemption queues behaves differently in a workout than a closed-end fund. (Same FEDS Note, Figs. 2 and 4)
- [NEW] IMF GFSR April 2024, Ch. 2 "The Rise and Risks of Private Credit": global private credit about $2.1T in assets and dry powder (2023); median private-credit borrower about $0.5B in size vs $4.6B for leveraged-loan issuers; almost exclusively floating rate; PIK interest's share of BDC interest income has doubled since 2019; BDC loan marks lag B-rated leveraged loans, and price and NAV take at least four quarters to converge after a shock. The IMF recommends mandatory independent external valuations and more frequent valuation reviews. (IMF, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md)
- [NEW] Default rates, primary: Proskauer Private Credit Default Index (covenant and payment defaults on its loan sample): 1.76% Q2 2025, 1.84% Q3 2025 (705 loans, $141B original principal), 2.46% Q4 2025, 2.73% Q1 2026, 2.41% Q3 2026. Defaults concentrate in smaller borrowers: in Q3 2025, the $25M-$49.9M EBITDA band ran 2.6% vs 1.2% for $50M+. (Proskauer, https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-184-for-q3-2025; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-246-for-q4-2025; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-273-for-q1-2026; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-241-for-q3-2026)
- [NEW] Realized losses, primary: Cliffwater Direct Lending Index long-run average realized loss about 1.0% per year since 2004 (1.03% through 2023); 0.70% for calendar 2025; trailing-four-quarter income has exceeded realized losses in every quarter since 2005, including the GFC. Use 1%/yr as the base-case loss and 2%-3% as the stress. (Cliffwater, Report on U.S. Direct Lending, https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf; 2025 results release, https://cliffwaterdev-staging.azurewebsites.net/files/docs/CliffwaterPressRelease_CDLI_2025_Results.pdf [staging host: confirm on cliffwater.com])
- [CONTRADICTS 3.7 "Covenant-lite 48% of larger deals per Proskauer via botminds"] The IMF notes "headline default rates are relatively high because they include covenant defaults that often lead to renegotiation." Different indices (Proskauer counts covenant defaults; Cliffwater counts realized losses; rating-agency indices count payment defaults/selective defaults) produce very different numbers. CHECK: when a sponsor quotes a default rate, ask which definition. (IMF GFSR Apr. 2024 Ch. 2)

### 3.4 ABL advance rates
- [STRENGTHENS 3.4] Keep the OCC Comptroller's Handbook, Asset-Based Lending, as the primary for advance rates (receivables 70%-85%, inventory up to ~65% of cost / ~80% of NOLV, concentration caps 10%-20%, over-advances 10%-15%); drop ranfunding/donclarkeenterprises/eqfunding as corroboration. (OCC, https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf)

### 3.7 Failure modes: the 2025 private-credit collapses
- [NEW] CASE FILE, First Brands Group (auto parts; Chapter 11 Sept. 2025): indictment unsealed Jan. 29, 2026 (SDNY) charges founder Patrick James and his brother with bank fraud, wire fraud and a continuing financial crimes enterprise, alleging billions in purported customer receivables sold to factoring partners that did not exist, collateral double- and triple-pledged, and massive off-balance-sheet inventory financing through entities James owned. At filing: $12M cash in corporate accounts against more than $9B of liabilities. A former executive pleaded guilty and is cooperating. Defendants deny the charges. THE CHECK: (1) UCC search across ALL affiliates and the founder's personally owned entities, not just the borrower; (2) direct verification of a sample of receivables with the account debtor, with remittance to a lender-controlled lockbox; (3) reconcile total supply-chain/factoring/inventory financing in the footnotes to what the company tells each lender; (4) cash proof at the parent. (DOJ SDNY, https://justice.gov/usao-sdny/pr/first-brands-executives-charged-multibillion-dollar-fraud; IRS-CI, https://irs.gov/compliance/criminal-investigation/first-brands-executives-charged-with-multibillion-dollar-fraud)
- [NEW] CASE FILE, Tricolor Holdings (subprime auto lender; collapsed 2025): DOJ (Dec. 2025) charged the CEO and COO; the CFO and senior director of finance pleaded guilty and are cooperating. Alleged schemes: double-pledging the same auto loans to multiple warehouse lenders and ABS deals, altering loan descriptions to meet eligibility, and booking charged-off loans in a fictitious dealer-management-system "portfolio company" so they looked current. SEC civil charges followed Aug. 18, 2026 ("$1.9 billion collapse"). One report: about $2.2B of collateral pledged against about $1.4B of real collateral by Aug. 2025. THE CHECK: loan-level collateral de-duplication across ALL facilities (VIN-level for autos) by an independent collateral agent or backup servicer; custodial possession of original titles/notes; static-pool charge-off reconciliation from the servicing system to the trustee reports. (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/ceo-cfo-coo-charged-connection-billion-dollar-collapse-tricolor-auto; SEC Press Release 2026-77, https://www.sec.gov/newsroom/press-releases/2026-77-sec-charges-former-executives-fraud-connection-19-billion-collapse-subprime-auto-lender-tricolor; SEC Lit. Rel. 26612, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26612)
- [NEW] Red flag drawn from both: a borrower with multiple warehouse, factoring, or inventory-finance providers who each see only their own collateral, and no single party that sees all of it.

## 4 Credit of All Kinds

- [RESOLVES WEAK: "Private credit now exceeds $1.7 trillion globally (coyotewealth.com)"] Replace with IMF: about $2.1T in assets and undeployed commitments globally in 2023, US managers $1.6T AUM (June 2023), growing about 20%/yr over five years; the Fed's Financial Accounts now estimate about $1.4T of private-credit debt outstanding to U.S. nonfinancial private corporations by Q1 2026. (IMF GFSR Apr. 2024 Ch. 2; Federal Reserve FEDS Note, Aug. 11, 2026, Fig. 1)
- [RESOLVES GAP: B.1 "Credit and specialty advance-rate and loss-rate norms by sub-strategy", partly] Direct lending: realized loss ~1.0%/yr long run (Cliffwater). Consumer auto ABS: Tricolor shows that advance rate is meaningless without collateral de-duplication. NAV loans: initial LTV 10%-30%, max ~40% (see new chapter). Factoring: advance 70%-90% of eligible AR (keep), and verify every account debtor's acknowledgment of assignment on notification deals. Remaining items (consumer installment, equipment residuals) still need lender interviews.
- [NEW] Litigation finance has no federal regulation and no nationwide disclosure requirement; funding is non-recourse to the plaintiff, and GAO found public data on returns and volume too limited to size the market. (GAO-23-105210, Dec. 2022, https://www.gao.gov/products/gao-23-105210) See new chapter.

## 5 Private Equity and M&A

### 5.4 / 5.6 The numbers: deal points (resolves "Reference the ABA deal points studies")
- [NEW] ABA 2025 Private Target M&A Deal Points Study (139 agreements signed and closed in 2024-Q1 2025): R&W insurance referenced in 63% of deals (55% in 2023 study); 41% of deals had reps that do NOT survive closing (30% prior study); among surviving deals, 24 months was most common (26%), then 12 months (23%) and 18 months (19%); about two-thirds of baskets are true deductibles, typically 0.5%-1% of transaction value; mean indemnity cap rose to about 16.8% of transaction value (just over 6% in 2021), skewed by a minority of high-cap deals, so use the median when published. [Survival and deductible splits via secondary summaries of the ABA study; confirm with the ABA PDF.] (Business Law Today announcement, https://businesslawtoday.org/?p=33407; K&L Gates, Dec. 19, 2025, https://www.klgates.com/2025-ABA-Private-Target-Mergers-Acquisitions-Deal-Points-Study-12-19-2025; Goulston & Storrs, https://www.goulstonstorrs.com/insights/article/2025-aba-private-target-m-and-a-deal-points-study-what-s-market)
- [NEW] SRS Acquiom 2025 Deal Terms Study (2,200+ private-target deals, $505B, closed 2019-2024): median survival period where indemnity survives is 12 months; 33% of 2024 deals were "no survival" (walk-away); RWI identified in 42% of 2024 deals (44% in 2021); 57% of RWI deals had non-survival provisions versus 11% of traditional-indemnity deals; separate purchase-price-adjustment escrow median 0.98% of transaction value (1.00% in 2023). (SRS Acquiom, 2025 M&A Deal Terms Study Quick Reference, https://media.taftlaw.com/wp-content/uploads/2025/04/15175412/2025-SRS-Acquiom-MA-Deal-Terms-Study-2-page-quick-reference.pdf; https://www.srsacquiom.com/our-insights/reps-warranties-findings/)
- [NEW] Implication: in a walk-away RWI deal the buyer's only recourse for a bad rep is the insurer, net of retention, and the insurer excludes anything the buyer knew. Diligence quality therefore sets the insurance coverage: what the QoE found is excluded, what it missed but should have found may be disputed.

### 5.7 Failure modes: what R&W claims say actually goes wrong
- [NEW] Aon 2026 Transaction Solutions Global Claims Study (data through 2025): about 18% of R&W policies bound 2019-2023 had at least one claim notification (historical 16%-20%); 2025 North American R&W payments totaled about $440M across about 40 payments, median about $8.2M, average about $10.4M, 41% of payments in the eight-figure range. FINANCIAL STATEMENTS breaches drove 38%-40% of paid loss, material contracts 21%, compliance with laws 15.1%, IP 11%. 51% of claims were notified more than 12 months after closing and 24% more than 24 months. 20.6% of claims (2021-2025 policies) alleged loss on a MULTIPLE basis (purchase price impact), and these made up 68% of 2025 paid loss. Deals under $100M were 41% of claims but 34% of deals. (Aon, https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study)
- [NEW] AIG's claims data: about one claim per six policies (2012-2021); financial statements the leading breach (21%), then tax (19%) and compliance with laws (16%) in its W&I sample; financial-statement and material-contract breaches grow as claim size grows. (AIG M&A claims intelligence, https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2023-r-and-w.pdf.coredownload.pdf; https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2021-r-and-w.pdf)
- [NEW] Translation into diligence priorities: the QoE (financial statements), top-customer/supplier contract review (material contracts) and regulatory compliance review together explain about three-quarters of insured loss. If budget is limited, those three workstreams come first; and because losses are claimed at the deal multiple, a $1M EBITDA miss at 10x is a $10M problem.

### 5.5 Third parties
- [RESOLVES WEAK: ctacquisitions.com for QoE providers and process timing] Replace with the engagement standard (SSAE 19 AUP or CS 100 consulting, see 0.5) and with the R&W insurer requirement: underwriters review the buy-side QoE, legal and tax reports, and exclude matters not diligenced. The provider's brand matters less than whether the scope covers proof of cash, NWC and revenue cut-off.

## 6 Energy and Infrastructure

### 6.5 The numbers: project-finance DSCR (resolves the Moody's/Fitch/S&P scorecard gap)
- [RESOLVES WEAK or GAP: B.1 "Moody's and Fitch DSCR scorecard thresholds"; CONTRADICTS 6.5 "S&P illustrative minimum senior DSCR 1.70x"] S&P's current General Project Finance Rating Methodology (Dec. 14, 2022) maps the forecast MINIMUM DSCR against the Operations Phase Business Assessment (OPBA, 1 = lowest risk, 12 = highest) in Table 8. 'bbb' (investment grade) requires: OPBA 1-2: 1.10x-1.20x; OPBA 3-4: 1.175x-1.40x; OPBA 5-6: 1.30x-1.75x; OPBA 7-8: 1.60x-2.50x; OPBA 9-10: 2.50x-5.00x; OPBA 11-12: no investment-grade outcome (>=3.00x only gets 'bb'). Below 1.05x even an OPBA 1-2 asset is 'b'. Replace the single "1.70x" line with this table: the threshold is a function of asset risk, not a constant. (S&P Global Ratings, General Project Finance Rating Methodology, Dec. 14, 2022, Table 8, https://maalot.co.il/Publications/MT20221215151143.PDF)
- [NEW] S&P downside resiliency test (Table 9): "Very high" resiliency requires DSCR always above 1.0x in the downside scenario AND downside DSCRs mapping to at least 'bbb' in most periods; "Low" means liquidity reserves are depleted by year three. "Stronger liquidity reserves" are defined as at least one year of debt service or at least 5% of total project debt. CHECK: ask the sponsor for the downside case and the year in which the DSRA is exhausted. (S&P 2022, Table 9)
- [NEW] S&P liquidity notching: liquidity is "less than adequate" (minus at least one notch) if sources do not cover next-12-month debt service 1x, if there is no dedicated DSRA, or if a 10% CFADS decline (OPBA 1-4) or 15% decline (OPBA 5-12) would breach a covenant. Strong liquidity (plus one notch) needs sources/uses above 2.0x (OPBA 1-6) or 2.5x (OPBA 7-12) and reserves covering 12 months (OPBA 1-6) or 18 months (OPBA 7-12) of debt service. Use as the DSRA benchmark: 6 months is the floor, 12-18 months is "strong." (S&P 2022, liquidity section)
- [STRENGTHENS 6.5; RESOLVES WEAK "contracted solar >1.2x for IG"] Fitch's published indicative 'BBB' coverage for fully contracted renewable projects with investment-grade offtakers (average DSCR profile): solar PV >=1.40x base case / >=1.30x rating case; CSP >=1.50x / >=1.40x; wind >=1.60x / >=1.30x; biomass/geothermal >=1.60x / >=1.40x. Fitch's rating case uses ONE-YEAR P90 energy production plus availability and O&M haircuts. Dated (2012) but primary; later Fitch rating actions continue to cite 1.30x rating-case minima. Wind gets the higher base-case bar because Fitch's portfolio data show most wind projects underperform their P50. (Fitch Ratings, "Rating Renewable Energy Projects," CDFA course deck, July 2012, https://www.cdfa.net/cdfa/cdfaweb.nsf/ord/iefc12-joassin.html/$file/Joassin.%20Fitch%20CJ%20-%20CDFA%20Intro%20Course%207-31-12.pdf)
- [STRENGTHENS 6.5 merchant row] Morningstar DBRS (Feb. 2025, discussing its Dec. 2024 PF methodology): a merchant hydro/wind/solar project may need a DSCR of about 1.5x-1.7x to reach minimum investment grade, and a merchant THERMAL project roughly three times that. The bible's "fully merchant 2.00x and above" is a floor for renewables, not gas. (Morningstar DBRS, "Takeaways From the Evolution of Project Finance Event," Feb. 4, 2025, https://dbrs.morningstar.com/research/447217)
- [NEW, GAP note] Moody's Power Generation Projects methodology (Jan. 2022) sits outside its generic PF methodology; its scorecard grid is behind registration. Until pulled, use S&P Table 8 and Fitch indicative tables as primary anchors. (Moody's rating action on Longview Power citing the Jan. 2022 methodology, https://www.yahoo.com/video/longview-power-llc-moodys-upgrades-191706199.html; Moody's generic PF methodology scope, https://ratings.moodys.com/api/rmc-documents/361401)

### 6.5 Availability guarantees (resolves the LTSA gap)
- [RESOLVES WEAK or GAP: 6.5 "Availability guarantee, LTSA 95% to 98%" and B.1 "Energy availability-guarantee benchmarks from a primary OEM LTSA"] Primary contract evidence for gas: Entergy's 2020 CCGT tolling RFP term sheet sets a Monthly Availability Requirement of 98% in summer (Jun-Aug) and winter (Dec-Feb) months and 96% in all other months, with a capacity-payment discount of 2% for each 1% shortfall (1% per 1% if the shortfall is force majeure), capped at 100% of the monthly capacity payment. A 95%-98% LTSA/O&M guarantee band is therefore consistent with what a utility offtaker demands; anything below 95% is off-market. (Entergy Services, 2020 ETI CCGT RFP, Appendix B-2 Term Sheet - Toll, https://rfp.entergy.com/ENTRFP/SEND/2020ETICCGTRFP/Documents/04282020/Appendix%20B-2%20-%20Term%20Sheet%20-%20Toll.pdf)
- [NEW] Wind: DOE's O&M agreement checklist describes a typical guarantee of 95% availability during the time wind is sufficient to generate, and warns that higher guarantees cost more. Distinguish time-based availability (owner keeps resource and most performance risk) from energy-based/production-based guarantees (provider bears more); energy-based availability runs lower than time-based. CHECK: read the definition, exclusions (grid outages, force majeure, scheduled maintenance), and LD cap, not just the headline percentage. (U.S. DOE, O&M Agreement Checklist for On-Site Wind Energy, 2023, https://www.energy.gov/sites/default/files/2023-07/om-agreement-checklist-on-site-wind-energy.docx; Definitions of Availability Terms for the Wind Industry white paper, 2017, https://www.ourenergypolicy.org/wp-content/uploads/2017/08/Definitions-of-availability-terms-for-the-wind-industry-white-paper-09-08-2017.pdf)

### 6.4 Interconnection (primary data replaces Goldman-via-blog)
- [CONTRADICTS 6.4/6.7 "executed LGIA" as sufficient; RESOLVES vendor source gi-advisors/plausity] LBNL Queued Up 2026 (data through end-2025): only about 19% of projects (13% of capacity) that requested interconnection 2000-2020 reached commercial operation; 41% of capacity that SIGNED an interconnection agreement 2000-2022 had still withdrawn by end-2025. The median project built in 2025 took 61 months from interconnection request to COD (36 months in 2015, 22 months in 2008); median IR-to-IA is 45 months; median IA-to-COD is 31 months (21 in 2008). Projects of 200 MW+ take a median ~59 months. CHECK: an executed LGIA is necessary but not sufficient; also verify network-upgrade cost allocation, posted security, and milestone deadlines. (LBNL, Queued Up: 2026 Edition, https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf)

## 8 Cannabis and Hemp

- [CORRECTS / UPDATES 8.2 "April 2026 ... moved to Schedule III"] Status as of Nov. 2026: DEA's partial final rule (signed April 22, 2026; published April 28, 2026; consolidated challenges pending in the D.C. Circuit) moved to Schedule III (1) FDA-approved marijuana drug products and (2) marijuana manufactured, distributed or dispensed under a qualifying STATE MEDICAL license, and created an expedited DEA registration pathway for state medical licensees. Adult-use (recreational) marijuana remains Schedule I. The broader rescheduling of all marijuana went to a new DEA ALJ hearing (June 29 - July 15, 2026); post-hearing briefs are filed and the ALJ recommended decision and final Administrator determination are pending. (Federal Register, Apr. 28, 2026, https://govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08176.htm; DOJ, https://www.justice.gov/opa/pr/justice-department-places-fda-approved-marijuana-products-and-products-containing-marijuana; Morgan Lewis, Sept. 2026, https://www.morganlewis.com/pubs/2026/09/high-time-for-a-change-post-dea-hearing-broader-marijuana-rescheduling-questions-remain; Foley, Apr. 2026, https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/)
- [NEW, GAP] No IRS notice or guidance on 280E after the partial rule was located. Law-firm readings say qualifying medical operators are no longer subject to 280E for that activity, but this is not IRS guidance. CHECK: for any operator claiming 280E relief, require (a) a DEA registration under the new pathway, (b) a tax opinion, (c) a dual-license apportionment method (medical vs adult-use COGS, revenue and overhead) that would survive audit, and (d) a model at full 280E treatment as the downside. Do not underwrite refund claims for prior years.
- [NEW] Red flag: a deck that says "cannabis is now Schedule III." That is wrong for adult-use and incomplete for medical (registration and pending litigation).

## 10 Funds and Co-Investments

### 10.2 ILPA baseline: primary documents
- [RESOLVES WEAK: mattercite.com and angelinvestorsnetwork.com as sources for ILPA DDQ] Cite ILPA directly: ILPA Due Diligence Questionnaire 2.0 (2021) and ILPA Principles 3.0 (2019, https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf). Principles 3.0 says subscription lines should be reasonable in size (as % of fund) and duration and LPs should be offered an opt-out at the outset.
- [NEW] ILPA's updated Reporting Template and new Performance Template (published 2025): the Reporting Template replaces the 2016 template for funds still in their investment period in Q1 2026 or launched on/after Jan. 1, 2026; the Performance Template standardizes gross and net IRR and TVPI, WITH and WITHOUT the fund-level subscription facility, using "granular" or "gross-up" methodologies, and subscription-line interest must be a separate expense line. CHECK: ask every GP raising today for the ILPA Performance Template for each prior fund; refusal is a signal. (ILPA Combined Overview, https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf; ILPA Templates Hub, https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub; Katten, https://katten.com/insights/advisories/ilpa-publishes-updated-reporting-template-and-new-performance-template)
- [STRENGTHENS 10.5] ILPA 2020 subscription-line guidance: disclose facility size and outstanding balance quarterly, IRR with and without the facility, and the uncalled-capital estimate; it identified 15%-25% of commitments and 180 days outstanding as the PE-relevant reference points for facility size and duration. (ILPA, https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf)

### 10.3 Regulatory status: the 2023 Private Fund Adviser rules are gone
- [NEW] On June 5, 2024 the Fifth Circuit (National Association of Private Fund Managers v. SEC, No. 23-60471) vacated ALL of the SEC's August 2023 Private Fund Adviser rules: the quarterly statement rule, the private fund audit rule, restricted activities, adviser-led secondaries (fairness/valuation opinion) rule, and preferential treatment rule. No federal rule now requires a quarterly fee/performance statement, a fund audit beyond the Custody Rule's audit option, or a fairness opinion on a GP-led secondary. LPs must contract for these in the LPA/side letter. (Mofo, https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules; Paul Weiss, https://www.paulweiss.com/insights/client-memos/fifth-circuit-vacates-private-fund-adviser-rule)
- [NEW] SEC Division of Examinations private-fund risk alerts (June 2020; Jan. 2022) list the recurring deficiencies to test: undisclosed conflicts in allocations and cross-trades; preferential liquidity in side letters; portfolio-company monitoring/board/deal fees not offset; valuations not following stated policy (leading to excess fees and carry); failure to step down fee base after write-downs post-commitment period; leverage and strategy outside fund documents; inadequate diligence on investments and service providers. Use these as the ODD test list. (SEC, "Observations from Examinations of Investment Advisers Managing Private Funds," https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf; Holland & Knight on the Jan. 2022 alert, https://www.hklaw.com/en/insights/publications/2022/02/division-of-examinations-publishes-risk-alert-for-private-fund)
- [NEW] Fee case (SEC, Aug. 15, 2025): TZP Management charged with overcharging management fees by failing to offset portfolio-company transaction fees. CHECK: recompute fee offsets from portfolio-company payments. [SEC order; confirm release number on sec.gov]
- [NEW] CASE FILE, Momentum Advisors (SEC, Mar. 7, 2025, settled): the COO diverted about $223,000 from a private fund's portfolio companies via company debit cards and excess salary, concealed from the adviser, the portfolio companies' bookkeeper and SEC staff; the managing partner failed to supervise and caused the fund to pay a $346,904 debt of an entity the two controlled; the fund was never audited. Penalties $515,000 total. THE CHECK: an unaudited fund is an automatic pass; also test portfolio-company card and payroll spend for insiders, since the fund audit alone will not catch portfolio-level leakage. (SEC Press Release 2025-53, https://www.sec.gov/newsroom/press-releases/2025-53)

### 10.6 Failure modes: primary case files
- [NEW] CASE FILE, GPB Capital: raised about $1.6B from individual investors; distributions were represented as funded by portfolio operating cash flow but were paid from new investor capital. Founder David Gentile convicted Aug. 2024, sentenced May 2025 to 7 years; sentence commuted by President Trump in late Nov. 2025 after 12 days served (conviction stands). THE CHECK: reconcile every distribution to the source account and to underlying portfolio-company cash flow; a fixed "distribution rate" on an illiquid PE fund is a red flag. (NBC News, https://www.nbcnews.com/politics/white-house/trump-commutes-7-year-prison-sentence-former-private-equity-ceo-david-rcna246744; Bloomberg, https://www.bloomberg.com/news/articles/2025-12-01/trump-commutes-sentence-of-gpb-capital-founder-david-gentile)
- [NEW] CASE FILE, Archegos (family office): Bill Hwang built concentrated exposures through total-return swaps across multiple prime brokers, none of whom saw the whole book; banks lost more than $10B when it collapsed in March 2021. Sentenced Nov. 2024 to 18 years. THE CHECK for co-investments alongside family offices: ask for aggregate exposure across ALL counterparties, not one prime broker's view. (DOJ SDNY, Hwang sentencing release, Nov. 20, 2024 [confirm URL])
- [NEW] CASE FILE, Heller / Paramount-Prestige ATM network (SEC, Sept. 3, 2025): over $770M from about 2,700 mostly retail investors for fixed monthly distributions supposedly from ATM fees; distributions were funded by new money and high-interest short-term loans; about $400M investor losses and $185M+ allegedly misappropriated. THE CHECK: independent confirmation that the claimed operating assets (ATMs, machines, locations) exist and generate the claimed revenue, from the processor, not the sponsor. (SEC Press Release 2025-111, https://www.sec.gov/newsroom/press-releases/2025-111-sec-charges-pennsylvania-resident-his-companies-770-million-ponzi-scheme)

## 11 Crypto and digital assets
- [NEW] Regulatory reset: the SEC dismissed its civil enforcement action against Coinbase on Feb. 27, 2025, explicitly "not a judgment on the merits," to pursue rulemaking via its Crypto Task Force. Absence of an SEC case is no longer evidence that a token or platform is compliant; diligence must rest on custody, audit and on-chain verification. (SEC Press Release 2025-47, https://www.sec.gov/newsroom/press-releases/2025-47)
- [NEW] CASE FILE, FTX: customer deposits were routed to and used by Alameda Research; Sam Bankman-Fried was sentenced to 25 years (March 2024). THE CHECK: proof of reserves alone is insufficient; require proof of LIABILITIES and segregation of customer assets with an independent custodian, and an auditor with crypto-custody competence. (DOJ SDNY, SBF sentencing release, March 28, 2024 [confirm URL])

## Additional chapter items (2.6, 5.4, 6.5)

- [UPDATES 2.6; RESOLVES WEAK: 1752.vc / vcbeast as NVCA sources] NVCA's own page lists the core financing set (Certificate of Incorporation, SPA, Investors' Rights Agreement, Voting Agreement, ROFR and Co-Sale, Management Rights Letter, Indemnification Agreement) as "Updated November 2026," plus a July 2020 LPA insert on CFIUS and 2025 model PIPE sets. Cite nvca.org directly and always diligence against the version in force at signing. (NVCA Model Legal Documents, https://nvca.org/model-legal-documents/)
- [RESOLVES WEAK: "Fed SR 13-3 via ctacquisitions.com"] Cite the primary: Interagency Guidance on Leveraged Lending (Federal Reserve SR 13-3, March 2013). Its 6x total-leverage marker raises supervisory concern for most industries; the 4.0x total / 3.0x senior figure in 3.4 and 5.4 is a common definition of "leveraged," not a cap. (https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm) [confirm the bible's 4x/3x wording against the SR letter text]
- [STATUS of 6.5 gearing WEAK] No primary source fixes "senior debt 60%-80%" in the rating criteria reviewed. S&P, Fitch and DBRS size debt by minimum DSCR and downside resilience; gearing is an OUTPUT of DSCR sculpting, not an input. Recommend rewriting the line: "Size debt to the DSCR table (S&P Table 8 / Fitch indicative) on a P90 rating case; gearing of 60%-80% is the typical result for contracted assets [practitioner], lower for merchant." Keep WEAK on the percentages.
- [STATUS of 5.4 "Entry multiples 6x-10x (soferadvisors)" and "Direct lender share about 70% (Bain via ctacquisitions)"] No primary replacement retrieved; the search-fund data give a hard lower anchor (median search-fund acquisition 5.7x EBITDA at about $12M EV, IESE 2026). Keep WEAK on the middle-market band until a primary (e.g. GF Data, PitchBook-LCD) is pulled.

---

# NEW CHAPTERS (proposed and drafted)

Proposed additions, in priority order for likely deal flow: (A) Secondaries and GP-led continuation vehicles; (B) NAV lending and fund finance; (C) Search funds and ETA; (D) Data centers and digital infrastructure (split from Chapter 6); (E) Healthcare services and physician-practice roll-ups; (F) Litigation finance. Drafted fully: A, B, C, D, E. Drafted in outline: F. Still to research (not drafted): insurance and specialty finance, sports franchises, franchise businesses, family-office direct deals, farmland, art and collectibles, music royalties. Primary sources for each are suggested at the end of this part.

## NEW CHAPTER: Secondaries and GP-Led Continuation Vehicles

**How it works.** LP-led: an LP sells fund interests, priced as a % of the latest reported NAV. GP-led: the sponsor moves one asset (single-asset CV, SACV) or several (MACV) from an old fund into a new vehicle it also manages; existing LPs choose to sell (cash at the set price) or roll. The GP sits on both sides, which is the whole diligence problem.

**Market numbers (cite and update semi-annually).**
- [NEW] H1 2026 global secondary volume $118B (record first half; 2025 full-year record $240B). GP-led $62B (53%); LP-led $56B (47%). Single-asset CVs are 68% of CVs, multi-asset 32%. Buyout is about 66% of GP-led volume. Structured liquidity solutions about 9% of volume. Dedicated secondary capital $290B (from $327B at end-2025). (Jefferies Global Secondary Market Review, July 2026, https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf)
- [NEW] LP portfolio pricing H1 2026: all strategies about 87% of NAV; buyout 91%; venture 79%; infrastructure 91%; credit 89% (from 91%); real estate 68%. Tail-end funds trade at 25%+ discounts; some geographies at 35%+. Portfolios with limited software exposure priced better. (Jefferies, July 2026)
- [NEW] GP commitment to CVs: about 10% of total commitments in North American deals vs about 5% in Europe (where carry in the selling fund is often not crystallized at closing). (Jefferies, July 2026)

**Data room index.** Transaction rationale memo to LPAC; alternatives considered (sale process, IPO, hold) with any third-party bids received; price-setting evidence (lead-buyer bid, auction book, fairness/valuation opinion); asset-level model and 100-day plan of the CV; old-fund LPA and side letters; proposed CV LPA (fees, carry, hurdle, term, GP commitment); GP's crystallized carry and how it is reinvested; election materials and timetable; conflicts disclosure; secondary adviser engagement letter and fee.

**Diligence checklist.**
- Process: was there a genuine market test? Who set the price, and was the GP's own valuation used as the anchor? How many bidders were contacted and how many bid?
- Alignment: GP commitment to the CV as a % of total, and how much is new money vs rolled carry. Is the selling fund's carry crystallized at a price the GP itself set?
- Terms: CV management fee base (invested vs committed), carry tiers, hurdle reset, term and extensions, and whether the status quo option exists.
- Asset: the CV is a concentrated single-company position; underwrite it as a direct deal (Chapter 5) with full QoE, not on the GP's NAV.
- LP mechanics: election period, default election (sell or roll if no response), information parity between rolling LPs and the new lead buyer.

**The standard to hold GPs to (ILPA, May 2023).** [NEW] Continuation fund transactions should maximize value for existing investors, and rolling LPs should be no worse off than if no transaction had occurred; a TRUE status quo option should always be offered (no change in management fee, no change in carry, full roll of carry, side letters carried over); the GP should present the rationale to the LPAC and show it explored alternatives; the LPAC should vote to waive the conflicts, and GPs should bring ALL conflicts to the LPAC even if pre-cleared in the LPA; LPs need enough time to re-underwrite (ILPA's materials cite at least 30 days as a reasonable review window). (ILPA, "Continuation Funds: Considerations for Limited Partners and General Partners," May 2023, https://ilpa.org/resource/continuation-funds-considerations-for-limited-partners-and-general-partners/; ILPA release, https://ilpa.org/wp-content/uploads/2023/05/ILPA-Releases-Continuation-Fund-Guidance.pdf; Torys summary, https://www.torys.com/our-latest-thinking/publications/2023/05/ilpa-releases-continuation-fund-guidance-for-limited-partners-and-general-partners)

**Legal and structure.** [NEW] The SEC's adviser-led secondaries rule (mandatory fairness or valuation opinion plus disclosure of material business relationships with the opinion provider) was vacated with the rest of the Private Fund Adviser rules on June 5, 2024. A fairness opinion is now contractual only. Require one (from a provider with no other mandate from the GP) as a condition of rolling. (Fifth Circuit vacatur, see 10.3)

**Numbers to underwrite.**
- Price vs NAV and vs the most recent arm's-length mark. A SACV at or near 100% of NAV when the GP's LP portfolios trade at 87%-91% needs a reason.
- GP commitment: under ~5% of the CV with mostly rolled carry is weak alignment; ~10% with new cash is market in North America.
- Return attribution for the CV case: how much requires multiple expansion vs EBITDA growth (Jefferies notes buyers increasingly underwrite to static or contracting exit multiples).

**Failure modes and the check that catches each.**
- Price set by the GP's own mark with a thin market test. CHECK: obtain the bid book and the adviser's buyer list; call a bidder who declined.
- No real status quo: rollers forced onto new fees/carry. CHECK: compare old LPA vs CV LPA side by side.
- Carry crystallized on an inflated mark that the CV buyer funds. CHECK: recompute the GP's carry at the transaction price and at a 15%-20% lower price; see who bears the gap.
- Asset quality: a CV used to hold an asset that could not be sold. CHECK: full direct-deal diligence on the company and its debt; ask why the asset did not clear a sale process.
- Information asymmetry: lead buyer receives diligence LPs never see. CHECK: demand the same data room access as the lead.

**Red flags.** Election period under 20 business days; default election is "roll on new terms"; no fairness opinion; adviser paid only on closing by the GP; GP commitment entirely rolled carry; LPAC asked to approve after pricing is fixed.

**Hard questions.** What were the other bids? Why now, and why not a sale? What is the status quo option, exactly? How much new cash is the GP investing? What carry does the GP crystallize at this price?

## NEW CHAPTER: NAV Lending and Fund Finance

**How it works.** Subscription lines lend against LPs' uncalled commitments; NAV facilities lend against the fund's portfolio (cash flows and equity of portfolio companies, often via a pledge of holding-company equity), typically after the investment period. Hybrids blend both. Uses: defensive capital, follow-ons, and early distributions to LPs.

**Market and use numbers.**
- [NEW] Fund Finance Association estimate cited by ILPA: about $100B NAV-facility market (2024), forecast $600B by 2030. About 80% of NAV facilities to date supported portfolio companies; about 20% funded distributions. (ILPA, NAV-Based Facilities Guidance, July 2024, https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf)
- [NEW] Initial LTVs of about 10%-30%, with maximums around 40% as downside buffers; cash sweeps are critical to refinancing risk; lenders should retain rights to third-party valuations; testing is initial, periodic, and event-driven. (Sidley, "NAV-Based Fund Financings: Credit Rating Criteria and Key Structuring Considerations," Aug. 2025, https://www.sidley.com/en/insights/newsupdates/2025/08/net-asset-value-based-fund-financings-credit-rating-criteria-and-key-structuring-considerations)
- [NEW] Rating-agency stress: KBRA starts by haircutting fund value 40%-60% depending on asset type (PE, listed equity, bonds) to test repayment under severe stress; Fitch reportedly rates to the most conservative terms permitted in the facility, not current metrics. KBRA reported record rated NAV issuance in 2025 (about $23B, 38 deals), and 95% of its 279 surveillance actions on PE and secondary NAV loans 2020-1H 2026 were affirmations. (Reuters via Yahoo Finance, May 2024, https://sg.finance.yahoo.com/news/rating-firms-cautious-ratifying-private-101145008.html; KBRA, https://www.kbra.com/publications/qHMNTvyP)
- [NEW] Subscription lines: ILPA reference points are facility size of 15%-25% of commitments and 180 days maximum outstanding for PE; disclose IRR with and without. (ILPA 2020 guidance)

**Data room index (lender or LP view).** Facility agreement and fee letter; borrowing-base and LTV definitions; eligible-asset and concentration criteria; valuation policy and the last two years of marks vs exits; portfolio-company financials and their own debt (structural subordination); cash-sweep and LTV step-down mechanics; recourse to LP commitments (hybrid?); LPAC consent record; disclosure sent to LPs; use of proceeds.

**Diligence checklist.**
- LTV on what NAV: GP marks, or an independent valuation? Run LTV at a 25%-40% NAV haircut and identify when the sweep and cure triggers hit.
- Structural subordination: each portfolio company's senior debt sits ahead of the NAV lender; compute look-through leverage.
- Concentration: top-3 assets as % of NAV; minimum number of assets.
- Use of proceeds: distributions vs portfolio support. If distributions, are they recallable?
- Cost: all-in spread, PIK toggles, and fees; compare to the IRR uplift.
- Governance: LPAC consent obtained (ILPA says GPs should seek it regardless of use of proceeds), and standardized disclosure to all LPs.

**The ILPA standard.** [NEW] Distributions funded by NAV loans materially inflate IRR and DPI and can create perverse incentives; they are often RECALLABLE if the facility falls out of LTV compliance, which disrupts LP cash planning and creates tax and accounting problems; LPs may need a "synthetic DPI" excluding NAV-funded distributions to compare managers. (ILPA, July 2024)

**Failure modes and the check that catches each.**
- DPI manufactured by borrowing. CHECK: recompute DPI excluding NAV-loan-funded distributions; ask the GP for the ILPA Performance Template.
- Recall of distributions in a downturn. CHECK: read the recall clause and the LTV cure waterfall; model a 30% NAV drawdown.
- Cross-collateralization drags good assets down with bad. CHECK: map which assets are pledged and whether a single asset's default triggers the whole facility.
- Stale marks hide LTV breaches (IMF notes private marks lag public markets by at least four quarters). CHECK: independent valuation right and recent exit-to-mark comparison.

**Red flags.** NAV facility put in place without LPAC consent; use of proceeds is "distributions" in a fund raising its next vintage; PIK interest; LTV tested on GP marks only; no cash sweep.

**Hard questions.** What is DPI without the NAV loan? What happens at a 30% NAV decline: who cures, and can you recall distributions? What does the facility cost all-in vs the IRR gain? Why not sell an asset instead?

## NEW CHAPTER: Search Funds and Entrepreneurship Through Acquisition (ETA)

**How it works.** A searcher raises a small search fund (salary and deal costs) from investors who get a right to invest in the eventual acquisition, buys one small private company, and runs it as CEO for 5-10 years. Investors provide search capital, then acquisition equity (often with a step-up on search capital); the searcher earns equity in tranches (acquisition, time, performance).

**Numbers (primary academic surveys; Stanford GSB is outside the Ivy lanes).**
- [NEW] U.S./Canada: 862 known search funds since 1984, 382 acquisitions; aggregate pre-tax IRR 33.9% and ROI 4.75x (Stanford GSB 2026 Search Fund Study, data through Dec. 31, 2025, as cited by IESE). About 58% of concluded U.S./Canada searches ended in an acquisition. (IESE, International Search Funds 2026: Selected Observations, ST-689-E, https://www.iese.edu/media/research/pdfs/ST-0689-E; Stanford GSB 2026 Search Fund Study, https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations)
- [NEW] International (ex-U.S./Canada): 492 known funds, 216 acquisitions; 73% of concluded searches acquired (79% in 2024 study); aggregate ROI 2.8x, IRR 30% (up from 2.0x/18%). Crucial dispersion: the MEDIAN acquisition was valued at only 1.1x investors' capital, the top fund 23.8x. Of concluded funds, about 21% lost money (of which roughly a third total loss). Median international acquisition: $12M purchase price, $8M revenue, 26% EBITDA margin, 5.7x EBITDA, 1.4x revenue, 11% trailing revenue growth, 50 employees. Median search capital $450K (solo) and $649K (partnered); median searcher salary $100K, i.e. 45%-60% of search capital. (IESE 2026)
- [NEW] Why deals die: across 716 LOIs, searchers cited adverse discoveries in due diligence (59%), valuation disagreements (41%), seller retraction (32%) and lack of investor support (31%). Successful searchers signed an average of 4.6 LOIs (first by month six); unsuccessful ones 8.2. (IESE 2026)

**Data room index.** Searcher's PPM and search-fund LPA; investor list and step-up terms; searcher equity grant and vesting schedule; target CIM, 3-5 years of tax returns (small targets often have only tax-basis books), monthly bank statements, customer list; SBA 7(a) or senior loan terms and seller note; seller transition/employment agreement; QoE (required: these are owner-run businesses with personal expenses in the P&L); board composition post-close.

**Diligence checklist.**
- Searcher: references from prior managers and from investors in the search fund; background check; whether the searcher has run a P&L (most have not).
- Target: QoE with proof of cash against TAX RETURNS and bank statements (owner add-backs are the main source of overstatement); customer concentration and whether relationships are personal to the seller; key employees and retention.
- Structure: total leverage including seller note; seller note subordination and standstill; personal guarantee requirements on SBA loans; equity cushion.
- Governance: an experienced board (typically lead investors) with the right to replace the CEO.

**Failure modes and the check that catches each.**
- Owner add-backs that are real operating costs (seller's unpaid labor, deferred capex). CHECK: replace the seller's labor at market salary in the QoE; capex study.
- Relationship revenue that leaves with the seller. CHECK: customer calls before close; transition agreement with earn-out or seller note tied to retention.
- First-time CEO overwhelmed. CHECK: board with operating experience; 100-day plan; CEO coaching.
- Over-leverage on a small, cyclical business. CHECK: fixed-charge coverage in a 20% revenue-decline case.

**Red flags.** Purchase multiple well above the ~5.7x median without recurring revenue to justify it; seller unwilling to stay for transition; no QoE ("too small"); searcher's equity vests fully at close; search capital spent mostly on salary with fewer than three LOIs by month 12.

**Hard questions.** What would you pay if the seller left on day one? What does EBITDA look like with a market-rate replacement for the seller? Who on the board has run this kind of business? Which three customers would you call first, and have you?

## NEW CHAPTER: Data Centers and Digital Infrastructure (split from Chapter 6)

**How it works.** Three distinct risk products share the label: (1) powered land and development (entitlements, interconnection, power); (2) build-to-suit/leased hyperscale campuses, where the long-term lease to an investment-grade hyperscaler is the collateral (real estate/infra credit); (3) colocation/retail (operating-business risk: churn, pricing, power pass-through). Underwrite the one you are actually being offered.

**Demand numbers (primary).**
- [NEW] U.S. data centers used about 176 TWh in 2023, about 4.4% of U.S. electricity; LBNL projects 325-580 TWh by 2028, or about 6.7%-12% of U.S. electricity. The width of that range is the demand risk: underwrite tenant contracts, not the projection. (U.S. DOE / LBNL, "2024 United States Data Center Energy Usage Report," Dec. 20, 2024, https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers)

**Power and interconnection (the binding constraint).**
- [NEW] Median interconnection request-to-COD was 61 months for projects built in 2025; IR-to-IA median 45 months; 41% of capacity with SIGNED interconnection agreements (2000-2022) later withdrew. Large-load (data center) interconnection is a separate process from generator queues and varies by utility; a "will-serve" letter is not an executed electric service agreement. (LBNL Queued Up 2026)
- CHECK: executed electric service agreement or large-load interconnection agreement with the utility, the utility's facilities study, upgrade cost allocation and the security posted, energization date with LDs; for behind-the-meter generation, the Chapter 6 contract suite (EPC, LTSA availability 95%-98%, fuel supply) plus air permits.

**Data room index.** Site control and zoning (data center use permitted by right?); utility service agreement, load ramp schedule and tariff; fiber route diversity and carrier agreements; water rights/permits and cooling design; lease(s) with tenant, guaranty, and termination/contraction rights; development budget and GMP; long-lead equipment orders (transformers, switchgear, generators, chillers) with delivery dates and deposits; commissioning plan (Level 1-5); SLAs and uptime history (operating assets); power pass-through mechanics; property tax abatements and their clawbacks.

**Diligence checklist.**
- Tenant: identity and credit of the LEASE GUARANTOR (parent vs SPV), lease term vs debt tenor, early termination or contraction rights, rent escalators, delivery-date LDs and tenant walk rights if the building is late.
- Power: MW contracted vs MW deliverable by date; who bears the cost of upgrades; curtailment or interruptible provisions in the tariff.
- Construction: equipment provenance and lead times (Chapter 6.4 checks apply: reservation is not an order); contractor's data-center track record; contingency.
- Technology obsolescence: rack density the shell supports (air vs liquid cooling); cost to retrofit if the tenant leaves.
- Operating assets: PUE trend, uptime/outage incidents, churn and renewal spreads, power cost pass-through percentage.

**Numbers.** Leverage on hyperscale build-to-suit tracks the tenant's credit and lease term (rated-equivalent); colocation trades on EBITDA like an operating company. Use S&P Table 8 logic: an investment-grade long lease with no merchant tail is a low-OPBA asset (low DSCR needed); speculative/colocation is higher OPBA and needs far more coverage. [Industry PUE benchmarks (Uptime Institute annual survey) to be added after primary retrieval.]

**Failure modes and the check that catches each.**
- Powered-land story without power. CHECK: executed utility agreement and energization schedule; treat queue position or will-serve letters as option value only.
- Tenant walk right on late delivery. CHECK: read the delivery-date and termination clauses against the realistic equipment and energization timeline.
- SPV tenant, not the hyperscaler parent. CHECK: obtain and read the guaranty.
- Stranded asset on design obsolescence. CHECK: engineer's report on density and cooling retrofit cost.
- Speculative or canceled equipment orders (see Chapter 6.7). CHECK: firm PO, serial numbers, FAT.

**Red flags.** "Up to X GW" of power with no executed agreement; lease signed by an SPV with no parent guaranty; tenant LOI presented as a lease; behind-the-meter gas plan with no air permit; delivery date earlier than the transformer delivery date.

**Hard questions.** Show the executed utility agreement and the energization schedule by MW. Who guarantees the lease? What happens if delivery is six months late? What density does the building support, and what does a liquid-cooling retrofit cost? Which equipment is on firm order with serial numbers?

## NEW CHAPTER: Healthcare Services and Physician-Practice Roll-Ups

**How it works.** A sponsor buys a "platform" practice (dermatology, anesthesia, GI, dental, behavioral, home health, etc.) and adds on smaller practices at lower multiples (multiple arbitrage), centralizing billing and administration in a management services organization (MSO) because many states bar non-physicians from owning medical practices (corporate practice of medicine, CPOM). Revenue is set by payors (Medicare, Medicaid, commercial), so diligence centers on reimbursement durability and compliance.

**Regulatory anchors (primary).**
- [NEW] Oregon SB 951 (2025 Reg. Sess., enacted as Ch. 295, emergency clause): an MSO, and its shareholders, directors, officers and employees, may not own or control shares in, serve as director/officer of, be employed by, or manage a professional medical entity with which the MSO has a management services contract; voids most noncompetition, nondisclosure and nondisparagement agreements between such entities and medical professionals, and voids agreements violating the control prohibitions. This is the template for the strictest CPOM regime; several other states (e.g. California, Massachusetts) enacted PE-healthcare notice or oversight laws in 2024-25. (Oregon Legislature, SB 951 overview, https://olis.oregonlegislature.gov/liz/2025R1/Measures/Overview/SB951) [Other states: VERIFY current statutes per deal]
- [NEW] Federal fraud-and-abuse: the Anti-Kickback Statute (42 U.S.C. 1320a-7b(b)) and Stark (42 U.S.C. 1395nn) govern referral relationships, MSO fee structures (percentage-of-revenue fees are a known risk area), and add-on purchase prices (paying above fair market value for a referral source). False Claims Act liability can reach the sponsor when the sponsor is involved in the conduct. [VERIFY: cite a DOJ FCA settlement naming a PE sponsor, e.g. the 2021 Diabetic Care Rx / Riordan, Lewis & Haden matter, from justice.gov before publication]
- [NEW] Antitrust: the FTC's 2023 suit against U.S. Anesthesia Partners and Welsh Carson attacked a serial roll-up of Texas anesthesia practices followed by price increases; Welsh Carson later entered an FTC consent order requiring prior notice of certain acquisitions. Serial add-ons below HSR thresholds are not safe from challenge. [VERIFY dates and order terms on ftc.gov]

**Data room index.** Payor mix by revenue and by visit; top payor contracts with rates and renewal dates; CPT-level volume and reimbursement trend; revenue-cycle KPIs (days in A/R, initial denial rate, net collection rate, A/R over 90 days) by month; billing and coding audit results; compliance program, hotline log, prior self-disclosures, OIG exclusion checks for every provider; provider employment agreements and compensation formulas; MSO agreement and fee formula; licenses, DEA registrations, accreditation; malpractice history and tail coverage; add-on purchase agreements with FMV opinions; state CPOM analysis.

**Diligence checklist.**
- Revenue: rebuild net revenue from remittances (835 files) and bank deposits, not gross charges; test contractual allowance estimates against cash.
- Coding: independent coding audit on a statistically valid sample per provider; outlier billing vs peers.
- Compliance: FMV and commercial-reasonableness support for every compensation arrangement with referral sources; OIG/SAM exclusion screening; prior overpayments refunded within 60 days.
- Provider retention: post-close comp vs pre-close, noncompetes (void in some states), the number of providers producing the top 50% of revenue.
- Structure: CPOM-compliant ownership; the "friendly physician" owner's agreements; what happens if he or she leaves.
- Real estate: sale-leasebacks used to fund dividends weaken hospitals and practices. [VERIFY: Steward Health Care's 2016 sale-leaseback and May 2024 Chapter 11 as the case file]

**Numbers.** Underwrite with: payor concentration (largest commercial payor % of revenue); Medicare physician fee schedule changes (annual CMS rule); days in A/R and denial rates against HFMA MAP Keys peer data [practitioner standard; confirm]; provider productivity (wRVUs per FTE vs MGMA benchmarks) [practitioner]. Platform vs add-on multiple spread is the thesis; test whether add-ons have actually been integrated (one billing system, one payor contract).

**Failure modes and the check that catches each.**
- Upcoding or medically unnecessary services inflating EBITDA. CHECK: independent coding audit and peer-benchmark outlier analysis before close; escrow or special indemnity for pre-close billing.
- Kickback-tainted referral relationships (above-FMV medical directorships, MSO percentage fees). CHECK: FMV opinions and a healthcare regulatory counsel review.
- Payor rate cuts or out-of-network revenue collapsing (No Surprises Act arbitration changed out-of-network economics from 2022). CHECK: in-network status by payor and the share of revenue from out-of-network billing.
- Physicians leaving after their earn-outs. CHECK: rollover equity and vesting tied to tenure; production concentration.
- Antitrust or state-law block of add-ons. CHECK: local market share by specialty; state notice requirements.

**Red flags.** EBITDA growth driven by price in concentrated local markets; MSO fee as a % of collections; no billing audit in three years; large out-of-network revenue; providers with prior exclusions; "friendly physician" who also owns the MSO's landlord.

**Hard questions.** What share of revenue comes from the top payor, and when does that contract renew? What did the last external coding audit find? Show FMV support for every arrangement with a referral source. Which add-ons are still on separate billing systems? Which state laws require notice or approval for this deal?

## NEW CHAPTER (outline): Litigation Finance

**How it works.** A funder advances non-recourse capital to a claimant or law firm (single case or portfolio) in exchange for a share of recoveries, typically a multiple of capital or a percentage of proceeds, whichever is greater. Returns depend on win rate, collection, and DURATION.

**Primary anchors.**
- [NEW] No federal statute specifically regulates litigation funding, and there is no nationwide requirement to disclose funding agreements to courts or opposing parties; some courts require it case by case; some states cap fees/rates in consumer funding; GAO found public data on volumes and returns too limited to size the market. Commercial deals run into the millions; consumer advances are usually under $10,000. (GAO-23-105210, Dec. 2022, https://www.gao.gov/products/gao-23-105210)
- [NEW] Court-level disclosure is spreading (e.g. standing orders in the U.S. District Court for the District of Delaware since 2022). [VERIFY current federal rulemaking status before publication]

**Diligence checklist.** Independent merits opinion by counsel not involved in the case; damages model and collectability of the defendant (judgment-proof or sovereign defendants with enforcement risk); duration distribution (appeals add years; model IRR at 1.5x the expected duration); the funder's control rights and ethics compliance (the funder must not control litigation strategy where state ethics rules forbid it); portfolio cross-collateralization; the funder's own capital adequacy and commitments vs uncalled capital (can it fund through trial?); fair-value marks of case assets (Level 3) and the auditor's approach.

**Failure modes.** Win-but-cannot-collect; duration blowouts that crush IRR while MOIC looks fine; marks on unresolved cases that move with headlines; funder liquidity squeeze leaving cases unfunded. CHECK each with the items above.

**Red flags.** Marks above cost on cases without a judgment; returns quoted in MOIC only; single-case concentration; a funder that also controls settlement decisions.

## Suggested primary sources for the chapters not yet drafted
- Insurance and specialty finance: NAIC statutory filings and RBC ratios; AM Best methodology; state insurance department exam reports.
- Franchise businesses: FTC Franchise Rule (16 CFR Part 436) and the Franchise Disclosure Document (Item 19 financial performance, Item 20 outlet turnover, Item 21 audited franchisor financials); SBA Franchise Directory.
- Farmland: USDA NASS Land Values and Cash Rents summary (annual, August); NCREIF Farmland Index.
- Music royalties: U.S. Copyright Royalty Board Phonorecords IV mechanical-rate determination; MLC data; historical catalog multiples from public filings (e.g. listed royalty funds' NAV disclosures and write-downs).
- Sports franchises: league ownership and debt rules (league constitutions; leaguewide credit facilities); local media-rights contracts.
- Art and collectibles: auction house disclosure of guarantees and third-party irrevocable bids; title/provenance databases; UCC Article 9 for art lending.

---

# Source replacements

| Bible location | Weak / vendor source now cited | Primary or institutional replacement | Status |
|---|---|---|---|
| 2.4 Rule of 40, NRR | networkcraft.net; cxcash.com; designrevision.com; cfoadvisors.com | ICONIQ State of Software 2025; KeyBanc Capital Markets / Sapphire Ventures 2025 SaaS Survey; Bessemer Scaling to $100M | Replaced. Note: private-company median NRR ~100%, not 117% |
| 2.4 CAC payback, magic number | re-cap.com | Bessemer (CAC payback by segment: SMB <12, MM <18, Ent <24 mo); Benchmarkit 2025 (median 16 mo) | Replaced (magic number remains practitioner, David Skok) |
| 2.4 LTV:CAC | jumpstartpartners.finance | Bessemer Scaling to $100M (CLTV/CAC framing) | Partly replaced |
| 2.4 Burn multiple | vcbeast.com | No primary retrieved; originator is Craft Ventures (David Sacks) | Keep practitioner |
| 2.6 NVCA documents | 1752.vc; vcbeast.com | nvca.org Model Legal Documents (core set updated Nov. 2026) | Replaced |
| 3.4 Unitranche leverage, pricing, private credit size | coyotewealth.com | Federal Reserve FEDS Note (Aug. 11, 2026); IMF GFSR Apr. 2024 Ch. 2 | Replaced for leverage/ICR/size; unitranche pricing still practitioner |
| 3.4 Median leverage 5.0x, ICR 2.2x | botminds.ai ("Fed data via") | Federal Reserve FEDS Note (Aug. 11, 2026), table on 2025 issuance (ICR is an average) | Replaced and corrected |
| 3.7 Cov-lite 48%, equity cures | botminds.ai | Proskauer Private Credit Default Index (default definitions); IMF GFSR on covenant defaults; Sidley (keep) | Partly replaced; cov-lite share needs Proskauer primary |
| 3.4 Supervisory leveraged threshold | ctacquisitions.com | Federal Reserve SR 13-3 (Interagency Guidance on Leveraged Lending) | Replaced |
| 3.4 Venture debt terms | ctacquisitions.com; founderpath; Wikipedia; beancount.io; kadenwoodgroup | None retrieved (Stifel deck remains the best) | Keep WEAK |
| 3.4/4.3 ABL advance rates, factoring cost | ranfunding.com; donclarkeenterprises.com; eqfunding.com | OCC Comptroller's Handbook, Asset-Based Lending | Replaced for advance rates; factoring cost still WEAK |
| 0.5, 5.3 QoE | stacking.capital; modusalliance; v7labs; notveryprivateequity; duedilio | AICPA SSAE No. 19 (AUP) / CS 100; Aon 2026 and AIG R&W claims studies | Replaced for scope and loss evidence |
| 0.1, 5.4 Process timing, LMM | ctacquisitions.com; windsordrake.com; privateequitybro.com; soferadvisors.com | SRS Acquiom 2025 Deal Terms Study; ABA 2025 Deal Points Study; IESE/Stanford search-fund studies (small-deal multiples) | Partly replaced; multiples still WEAK |
| 0.7 Return attribution | goreuben.com | (Harvard/Wharton lanes) | Not in this lane |
| 0.3 Sanctions screening | getcaruso.com; carta.com | OFAC 50 Percent Rule; OFAC Framework for Compliance Commitments (2019) | Replaced (verify links) |
| 0.3 506(c) verification | augment.market; checkfile.ai | 17 CFR 230.506(c)(2)(ii); SEC staff no-action letter, Mar. 12, 2025 (minimum-investment approach) | Replaced (verify letter cite) |
| 0.4 Segregation of duties | thomasmurray.com | ACFE Occupational Fraud 2026 (lack/override of controls in >50% of cases; collusion stats) | Replaced |
| 6.4 Interconnection queues | gi-advisors.com (Goldman via); plausity.com | LBNL Queued Up 2026 | Replaced |
| 6.5 Agency DSCR digest | publicenterprise.org; maalot 2017 S&P | S&P General PF Methodology (Dec. 2022) Table 8/9; Fitch indicative BBB table; Morningstar DBRS (Feb. 2025) | Replaced |
| 6.5 Practitioner DSCR | gridlines.com | S&P Table 8 by OPBA; Fitch | Replaced |
| 6.5 Gearing | uspeglobal.com; jakenenergy.com | None (agencies size by DSCR) | Keep WEAK; reframe as output |
| 6.5 Availability guarantee | "Practitioner. GAP" | Entergy 2020 CCGT toll term sheet (98%/96% monthly availability, 2% per 1% LDs); DOE wind O&M checklist (95%) | Resolved |
| 8.2 280E and rescheduling | greengrowthcpas; cannabizguide; peasebell; getmeadow; bluecloudcpa | Federal Register 2026-08176 (DEA partial final rule); DOJ release; Harborside: Patients Mutual Assistance Collective Corp. v. Commissioner, 151 T.C. 176 (2018), aff'd 995 F.3d 671 (9th Cir. 2021) | Replaced for status; IRS guidance gap remains |
| 10.2 ILPA DDQ | mattercite.com; angelinvestorsnetwork.com | ilpa.org: DDQ 2.0, Principles 3.0, 2025 Reporting and Performance Templates, 2020 sub-line guidance, 2023 CV guidance, 2024 NAV guidance | Replaced |
| 10.3 ODD service-provider checks | dealroom.net; ryanoconnellfinance.com | SEC Division of Examinations private fund risk alerts (2020, 2022); SEC/DOJ case files (Infinity Q, SQN, Momentum, GPB) | Replaced |
| 1.8 Drive Planning | Bisnow | SEC Lit. Rel. 26456 (Dec. 30, 2025) plus SEC 2024-97 | Replaced |

---

# Sources

Rating agencies and project finance
1. S&P Global Ratings, General Project Finance Rating Methodology, Dec. 14, 2022 (hosted by Maalot). https://maalot.co.il/Publications/MT20221215151143.PDF
2. Fitch Ratings, Rating Renewable Energy Projects (CDFA course deck), July 2012. https://www.cdfa.net/cdfa/cdfaweb.nsf/ord/iefc12-joassin.html/$file/Joassin.%20Fitch%20CJ%20-%20CDFA%20Intro%20Course%207-31-12.pdf
3. Morningstar DBRS, Takeaways From the Evolution of Project Finance Event, Feb. 4, 2025. https://dbrs.morningstar.com/research/447217
4. Moody's, generic project finance methodology (scope). https://ratings.moodys.com/api/rmc-documents/361401
5. Moody's rating action on Longview Power (cites Jan. 2022 Power Generation Projects methodology). https://www.yahoo.com/video/longview-power-llc-moodys-upgrades-191706199.html
6. Entergy Services, 2020 ETI CCGT RFP, Appendix B-2 Term Sheet - Toll. https://rfp.entergy.com/ENTRFP/SEND/2020ETICCGTRFP/Documents/04282020/Appendix%20B-2%20-%20Term%20Sheet%20-%20Toll.pdf
7. U.S. DOE, O&M Agreement Checklist for On-Site Wind Energy, 2023. https://www.energy.gov/sites/default/files/2023-07/om-agreement-checklist-on-site-wind-energy.docx
8. Definitions of Availability Terms for the Wind Industry (white paper), 2017. https://www.ourenergypolicy.org/wp-content/uploads/2017/08/Definitions-of-availability-terms-for-the-wind-industry-white-paper-09-08-2017.pdf
9. LBNL, Queued Up: 2026 Edition. https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf
10. LBNL, Queued Up: 2025 Edition. https://emp.lbl.gov/publications/queued-2025-edition-characteristics
11. U.S. DOE / LBNL, 2024 United States Data Center Energy Usage Report (DOE release, Dec. 20, 2024). https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
12. LBNL, U.S. Utility-Scale Solar 2026 Edition. https://emp.lbl.gov/publications/us-utility-scale-solar-2026-edition

Real estate and banking regulators
13. HUD Mortgagee Letter 2025-03. https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf
14. Nixon Peabody, HUD adopts relaxed loan sizing standards, Jan. 14, 2025. https://www.nixonpeabody.com/insights/alerts/2025/01/14/hud-adopts-relaxed-loan-sizing-standards-for-fha-insured-loans
15. HUD Mortgagee Letter 2010-11 (Criterion 5 DSCR). https://www.hud.gov/sites/documents/10-11hsgn.pdf
16. Fannie Mae Multifamily Selling and Servicing Guide. https://mfguide.fanniemae.com/fnmf-pdf/download/9906
17. Federal Reserve SR 23-5, Policy Statement on Prudent CRE Loan Accommodations and Workouts. https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm
18. FDIC FIL-34-2023. https://fdic.gov/news/financial-institution-letters/2023/fil23034.html
19. Federal Register, 88 FR 43115 (July 6, 2023). https://www.govinfo.gov/content/pkg/FR-2023-07-06/html/2023-14247.htm
20. OCC Comptroller's Handbook, Asset-Based Lending. https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf
21. Federal Reserve SR 13-3, Interagency Guidance on Leveraged Lending. https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm

Private credit
22. Federal Reserve FEDS Note, Private Credit and Leveraged Loan Markets, Aug. 11, 2026. https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html
23. Same, accessible data. https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-accessible-20260811.htm
24. IMF, Global Financial Stability Report, April 2024, Ch. 2. https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md
25. Proskauer Private Credit Default Index, Q3 2025. https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-184-for-q3-2025
26. Proskauer, Q4 2025. https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-246-for-q4-2025
27. Proskauer, Q1 2026. https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-273-for-q1-2026
28. Proskauer, Q3 2026. https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-241-for-q3-2026
29. Cliffwater, Report on U.S. Direct Lending. https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf
30. Cliffwater, CDLI 2025 results (staging host; confirm). https://cliffwaterdev-staging.azurewebsites.net/files/docs/CliffwaterPressRelease_CDLI_2025_Results.pdf
31. DOJ SDNY, First Brands executives charged. https://justice.gov/usao-sdny/pr/first-brands-executives-charged-multibillion-dollar-fraud
32. IRS-CI, First Brands executives charged. https://irs.gov/compliance/criminal-investigation/first-brands-executives-charged-with-multibillion-dollar-fraud
33. DOJ SDNY, Tricolor CEO, CFO, COO charged. https://www.justice.gov/usao-sdny/pr/ceo-cfo-coo-charged-connection-billion-dollar-collapse-tricolor-auto
34. SEC Press Release 2026-77, Tricolor. https://www.sec.gov/newsroom/press-releases/2026-77-sec-charges-former-executives-fraud-connection-19-billion-collapse-subprime-auto-lender-tricolor
35. SEC Litigation Release 26612, Tricolor. https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26612
36. Sidley, NAV-Based Fund Financings, Aug. 2025. https://www.sidley.com/en/insights/newsupdates/2025/08/net-asset-value-based-fund-financings-credit-rating-criteria-and-key-structuring-considerations
37. KBRA, Private Credit: NAVigating the PE Landscape. https://www.kbra.com/publications/qHMNTvyP
38. Reuters (via Yahoo), Rating firms cautious ratifying some private credit loans, May 2024. https://sg.finance.yahoo.com/news/rating-firms-cautious-ratifying-private-101145008.html

Venture
39. ICONIQ, State of Software 2025. https://www.iconiq.com/growth/reports/2025-state-of-software
40. ICONIQ, Growth and Efficiency. https://www.iconiq.com/growth/insights/growth-and-efficiency
41. Sapphire Ventures, 2025 KeyBanc Capital Markets and Sapphire Ventures SaaS Survey. https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey
42. Bessemer Venture Partners, Scaling to $100 Million. https://www.bvp.com/atlas/scaling-to-100-million
43. Growth Unhinged (Benchmarkit data), 2025 SaaS Benchmarks Report. https://kylepoyar.substack.com/p/2025-saas-benchmarks-report
44. Carta, State of Private Markets Q2 2025. https://carta.com/data/state-of-private-markets-q2-2025/
45. Carta, Series A fundraising Q2 2025. https://carta.com/data/series-a-fundraising-q2-2025
46. Carta, State of Private Markets Q3 2025. https://carta.com/data/state-of-private-markets-q3-2025-full-report/
47. NVCA Model Legal Documents. https://nvca.org/model-legal-documents/
48. DOJ SDNY, Charlie Javice sentenced to 85 months. https://www.justice.gov/usao-sdny/pr/startup-ceo-charlie-javice-sentenced-85-months-prison-175-million-fraud

M&A deal terms and R&W
49. Business Law Today, ABA 2025 Private Target M&A Deal Points Study. https://businesslawtoday.org/?p=33407
50. K&L Gates, 2025 ABA Deal Points Study, Dec. 19, 2025. https://www.klgates.com/2025-ABA-Private-Target-Mergers-Acquisitions-Deal-Points-Study-12-19-2025
51. Goulston & Storrs, 2025 ABA Deal Points: What's Market. https://www.goulstonstorrs.com/insights/article/2025-aba-private-target-m-and-a-deal-points-study-what-s-market
52. SRS Acquiom, 2025 M&A Deal Terms Study Quick Reference. https://media.taftlaw.com/wp-content/uploads/2025/04/15175412/2025-SRS-Acquiom-MA-Deal-Terms-Study-2-page-quick-reference.pdf
53. SRS Acquiom, Reps & Warranties findings. https://www.srsacquiom.com/our-insights/reps-warranties-findings/
54. Aon, 2026 Transaction Solutions Global Claims Study. https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study
55. AIG, M&A Claims Intelligence 2023 (R&W). https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2023-r-and-w.pdf.coredownload.pdf
56. AIG, M&A Claims 2021 (R&W). https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2021-r-and-w.pdf
57. Journal of Accountancy, SSAE No. 19, Sept. 2020. https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html
58. PCAOB AT 601 (CS 100 reference). https://pcaobus.org/oversight/standards/attestation-standards/details/AT601

AML, KYC, regulatory status
59. FinCEN, Final rule postponing Investment Adviser Rule to 2028. https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028
60. Federal Register, Jan. 2, 2026 (IA rule delay). https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf
61. Proskauer, FinCEN finalizes two-year delay. https://www.proskauer.com/blog/fincen-finalizes-twoyear-delay-of-the-investment-adviser-aml-rule-reaffirms-intent-to-further-review-and-tailor-the-rule-and-to-coordinate-with-other-rulemakings
62. Federal Register 2026-16576 (CTA final rule). https://public-inspection.federalregister.gov/2026-16576.pdf
63. Mayer Brown, FinCEN permanently eliminates BOI reporting for U.S. companies, Aug. 20, 2026. https://www.mayerbrown.com/de/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons
64. KPMG, CTA final rule. https://kpmg.com/us/en/articles/2026/cta-beneficial-ownership-info-boi-reporting-fincen-final-rule.html
65. OFAC. https://ofac.treasury.gov/
66. ACFE, Occupational Fraud 2026: A Report to the Nations. https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf
67. ACFE, Occupational Fraud 2024 (legacy page). https://legacy.acfe.com/report-to-the-nations/2024/

SEC and DOJ enforcement
68. SEC Press Release 2025-98, First Liberty Building & Loan. https://www.sec.gov/newsroom/press-releases/2025-98-sec-charges-georgia-based-first-liberty-building-loan-its-owner-operating-140-million-ponzi-scheme
69. SEC Press Release 2025-76, LeFever Mattson. https://www.sec.gov/newsroom/press-releases/2025-76-sec-charges-former-real-estate-investment-ceo-operating-multimillion-dollar-ponzi-scheme
70. SEC Litigation Release 26456, Drive Planning executives. https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26456
71. SEC Press Release 2025-111, Heller / ATM network Ponzi. https://www.sec.gov/newsroom/press-releases/2025-111-sec-charges-pennsylvania-resident-his-companies-770-million-ponzi-scheme
72. SEC Press Release 2025-53, Momentum Advisors. https://www.sec.gov/newsroom/press-releases/2025-53
73. SEC Litigation Release 26671, SQN Capital. https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671
74. DOJ SDNY, Infinity Q founder sentenced to 15 years. https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-investment-officer-infinity-q-sentenced-15-years-prison
75. SEC Litigation Release 25331, Velissaris. https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25331
76. NBC News, Trump commutes Gentile sentence. https://www.nbcnews.com/politics/white-house/trump-commutes-7-year-prison-sentence-former-private-equity-ceo-david-rcna246744
77. Bloomberg, Trump commutes sentence of GPB Capital founder, Dec. 1, 2025. https://www.bloomberg.com/news/articles/2025-12-01/trump-commutes-sentence-of-gpb-capital-founder-david-gentile
78. SEC Press Release 2025-47, dismissal of Coinbase action. https://www.sec.gov/newsroom/press-releases/2025-47
79. SEC Division of Examinations, Private Fund Risk Alert (June 2020). https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf
80. Holland & Knight, Division of Examinations risk alert (Jan. 2022). https://www.hklaw.com/en/insights/publications/2022/02/division-of-examinations-publishes-risk-alert-for-private-fund
81. MoFo, Fifth Circuit vacates SEC Private Fund Adviser Rules. https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules
82. Paul Weiss, Fifth Circuit vacates private fund adviser rule. https://www.paulweiss.com/insights/client-memos/fifth-circuit-vacates-private-fund-adviser-rule

Cannabis
83. Federal Register, Apr. 28, 2026 (DEA partial rescheduling). https://govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08176.htm
84. DOJ, FDA-approved and state-licensed medical marijuana placed in Schedule III. https://www.justice.gov/opa/pr/justice-department-places-fda-approved-marijuana-products-and-products-containing-marijuana
85. Morgan Lewis, High Time for a Change, Sept. 2026. https://www.morganlewis.com/pubs/2026/09/high-time-for-a-change-post-dea-hearing-broader-marijuana-rescheduling-questions-remain
86. Foley, DEA final order rescheduling certain marijuana products, Apr. 2026. https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/

ILPA, secondaries, funds
87. ILPA Principles 3.0 (2019). https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf
88. ILPA, Guidance on Disclosures Related to Subscription Lines of Credit (2020). https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf
89. ILPA, Combined Overview of ILPA Templates (2025). https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf
90. ILPA, Updated Templates Hub. https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub
91. Katten, ILPA updated Reporting Template and new Performance Template. https://katten.com/insights/advisories/ilpa-publishes-updated-reporting-template-and-new-performance-template
92. ILPA, NAV-Based Facilities Guidance (July 2024). https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf
93. ILPA, Continuation Funds: Considerations for LPs and GPs (May 2023). https://ilpa.org/resource/continuation-funds-considerations-for-limited-partners-and-general-partners/
94. ILPA release on continuation fund guidance. https://ilpa.org/wp-content/uploads/2023/05/ILPA-Releases-Continuation-Fund-Guidance.pdf
95. Torys, ILPA continuation fund guidance summary. https://www.torys.com/our-latest-thinking/publications/2023/05/ilpa-releases-continuation-fund-guidance-for-limited-partners-and-general-partners
96. Jefferies, Global Secondary Market Review, July 2026. https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf

Search funds, healthcare, litigation finance
97. IESE, International Search Funds 2026: Selected Observations (ST-689-E). https://www.iese.edu/media/research/pdfs/ST-0689-E
98. Stanford GSB, 2026 Search Fund Study: Selected Observations. https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations
99. Oregon Legislature, SB 951 (2025). https://olis.oregonlegislature.gov/liz/2025R1/Measures/Overview/SB951
100. GAO-23-105210, Third-Party Litigation Financing. https://www.gao.gov/products/gao-23-105210

Note on method: web-search budget for this run was exhausted before the healthcare, franchise, farmland and music-royalty primaries could be searched; items marked [VERIFY] rest on the drafter's knowledge and must be confirmed on the named primary site before publication.
