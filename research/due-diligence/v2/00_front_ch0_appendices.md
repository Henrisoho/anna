# The Bible on Due Diligence

**INSTITUTIONAL DEAL PLAYBOOKS**

How to build, check, and attack a private market deal at the depth of an institutional data room.

**VERSION 2.0** (November 2026)

US legal and regulatory context. Figures in US dollars. Regulatory status is stated as of November 2026 (see 0.18).

---

## How to use this book

This is a build-to-institutional-depth playbook set. Each chapter gives a data room index, a diligence request list by workstream, metrics with cited acceptable ranges, real failure cases with the specific check that catches each, red flags, and hard questions. The bar is a lender or sponsor data room, not a blog checklist.

Chapter 0 is universal. Read it before any deal-type chapter. Version 2.0 adds nine universal sections to Chapter 0 (0.10 to 0.18, plus 0.19 and 0.20 for real-asset screens), all of which apply to every deal regardless of asset class:

- 0.10 Credit-cycle and bubble overlay: where in the cycle you are buying, and what that does to every other number.
- 0.11 Counterparty, treasury and liquidity risk: where the cash sits, who can gate it, and who fails when you need them.
- 0.12 Decision hygiene and the IC bias audit: how the committee itself fails.
- 0.13 Track-record and performance forensics: how to stop being fooled by a track record.
- 0.14 Leadership diligence: the CEO and team as a full workstream.
- 0.15 Compliance and misconduct diligence: what public records cannot show.
- 0.16 Preserving legal remedies: diligence that keeps your claims alive.
- 0.17 Behavioral and governance red flags: the consolidated list.
- 0.18 Regulatory status as of November 2026: what changed, and what it means for a data room.
- 0.19 Physical-climate, water and insurability risk; 0.20 Policy and appropriation risk.

How to read a chapter. Start with THE SPINE and the THE ONE CHECK callouts. Then read the failure cases: each names the company, the year, what happened, and the CHECK that would have caught it. Then use the request lists and numbers. Every number carries its source and, where dated, its year. Where sources disagree, both positions are shown. Do not average them.

How to use the base rates. Version 2.0 states base rates wherever the research supplies them (for example: about 75% of venture-backed companies never return cash; 69% of buyouts change CEO during the hold; executives' 80% confidence ranges capture outcomes only 36% of the time). A memo that does not state the base rate cannot explain why this deal beats it (0.7, 0.12).

THE SPINE

> Verify the sponsor, verify the cash, verify the collateral or the earnings, verify the legal title, and separate what you confirmed from what you could not.

The single most repeated failure mode across real estate, funds, and credit is one person controlling money movement with no independent administrator, custodian, or proof of cash. That one structural check would have caught Madoff, Drive Planning, and most of the 2024 real estate Ponzi cases.

Version 2.0 adds the second-most repeated failure mode, from the 2025 private-credit collapses: collateral or exposure that no single party sees in full. First Brands' lenders thought leverage was about 5x; counting off-balance-sheet factoring and supply-chain finance it was closer to 20x (Harker, Knowledge at Wharton, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/). Tricolor allegedly pledged the same auto loans to multiple warehouse lenders (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/ceo-cfo-coo-charged-connection-billion-dollar-collapse-tricolor-auto). Archegos spread total-return swaps across prime brokers, none of whom saw the whole book; banks lost more than $10B in March 2021 (DOJ SDNY, Hwang sentencing, Nov. 20, 2024; URL to be confirmed, WEAK). The spine therefore reads, in full: verify the sponsor, verify the cash, verify the collateral or the earnings, verify the legal title, **verify that you see every claim on the same asset**, and separate what you confirmed from what you could not.

Why the spine holds. Owner and executive frauds have a median loss of $475,000, more than 9x employee frauds ($50,000); financial statement fraud is only 6% of cases but has the highest median loss, $1,000,000; more than half of frauds occurred because of a lack of, or override of, internal controls (ACFE, Occupational Fraud 2026: A Report to the Nations, 2,402 cases, https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf). A sponsor-level fraud is almost always an owner/executive fraud, the most expensive category.

## THREE USES

- **The standard.** Every posted deal is built and checked against the relevant chapter.
- **The first pass.** Chapter 0 plus the deal-type chapter is the brief for an AI first-pass review. In v2, the first pass also runs the cycle overlay (0.10), the counterparty screen (0.11) and the regulatory status table (0.18).
- **The red team.** Appendix A holds the prompt for attacking a draft deck before members see it (A.3), and the written bias audit the IC chair reads before the vote (A.4).

## READING THE MARKS

- **WEAK** marks a figure or claim that rests on vendor, aggregator, or practitioner-only sourcing, or that is unverified. In v2 WEAK also covers: anything a research lane tagged [VERIFY] (drafter knowledge not yet confirmed on the primary site); any figure confirmed only at the abstract level of a paper; any figure sourced only to a podcast or interview; any dated practitioner figure kept for its framework. Confirm it before it anchors a posted deal.
- **CHECK:** marks the specific test that catches a failure mode.
- **RED FLAG** marks a condition that should stop or reprice the deal until explained.
- **THE ONE CHECK** marks the single test that, in the case record, would have caught the most losses in that section.
- **CASE FILE** marks a real failure: company, year, what happened, and THE CHECK that would have caught it.
- **CONTRADICTS / BOTH POSITIONS** marks a point where credible sources disagree. Both are shown, with sources. Do not average them.
- Dated figures carry their year. A figure without a year is a structural rule, not a market level.
- Sources appear in parentheses beside each claim, with a short name and URL, and in full at the back (Appendix C, maintained separately). Primary sources (statutes, regulators, court records, enforcement releases, rating-agency criteria) outrank peer-reviewed research, which outranks institutional practitioner data, which outranks vendor and marketing content.

---

# 0 The Master Playbook

Universal diligence that applies to every deal.

THE SPINE

> Verify the sponsor. Verify the cash. Verify the collateral or the earnings. Verify the legal title. Verify that you see every claim on the same asset. Then separate what you confirmed from what you could not.

## 0.1 How top firms run a diligence process

The sequence is the same at every institutional shop. What changes by deal type is the depth of each workstream.

| Step | Stage | What happens |
|---|---|---|
| 1 | Screen | One-page thesis, kill tests, mandate fit, cycle overlay (0.10). Reject fast. |
| 2 | LOI or term sheet | Indication of interest, LOI, or term sheet with exclusivity. Walk-away price set before bidding. |
| 3 | Confirmatory diligence | Parallel workstreams (below). Where deals are won or lost. |
| 4 | Third-party reports | QoE, appraisal, environmental, independent engineer, background checks. Where deals are won or lost. |
| 5 | IC memo and vote | Memo (0.7), bias audit (0.12, A.4), around-the-table poll. |
| 6 | Docs and funding | Final documentation, conditions precedent, funding. Remedies preserved (0.16). |
| 7 | Monitoring | Post-close monitoring and covenant tracking. |
| 8 | Post-mortem | NEW in v2. Diarized at the vote; run on every loss and every surprise. |

FIGURE 1 The institutional diligence sequence. Steps 3 and 4 are where deals are won or lost.

1. Screen. One-page thesis, kill tests, mandate fit. Reject fast. Add two screen-stage questions in v2: where are we in the cycle for this asset (0.10), and what is the sponsor's or lender's deployment pressure (Harker, KaW, Apr. 22, 2026, URL above).
2. Indication of interest, LOI, or term sheet with exclusivity. Set the walk-away price from conservative cash flows before bidding starts, and keep the deal champions separate from the valuation team (Feldman and Chunduru, "Why Many M&A Deals Fail and How to Beat the Odds," KaW, Dec. 8, 2025, https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/).
3. Confirmatory diligence in parallel workstreams: financial, commercial, legal, tax, operational, technical, management and background (with leadership diligence as its own workstream, 0.14), regulatory and compliance (0.15), insurance, environmental and physical-climate (0.19), ESG, IT and cyber, treasury and counterparty (0.11).
4. Third-party reports commissioned: QoE, appraisal, environmental, independent engineer, background checks.
5. Investment committee memo and vote.
6. Final documentation, conditions precedent, funding.
7. Post-close monitoring and covenant tracking.
8. Post-mortem. After losses, review which variables were misjudged and which outcomes were bad luck. Blackstone, as Schwarzman described it at Yale, polls every deal team member at committee and changed its decision process firm-wide after an early failure; even so he estimated only "90 to 93%" of decisions were right (Schwarzman guest lecture, Yale ECON 252, 2008, lecture 20, https://oyc.yale.edu/economics/econ-252-08/lecture-20).

Timing. Buyout confirmatory diligence typically runs weeks 9 to 16 of a process and covers Quality of Earnings, legal, tax, IT, commercial, environmental, and insurance (ctacquisitions.com, WEAK). Leveraged transactions often run 60 to 90 days between signing and closing to accommodate lender underwriting (windsordrake.com, WEAK). No primary source for process timing was retrieved in v2; the SRS Acquiom and ABA deal-term studies replace the vendor sources for deal terms (0.16), not for timing.

### The funnel: how selective a real process is

- Buyout funnel. For every 100 opportunities considered, the average PE firm deeply investigates fewer than 24, signs an LOI or agreement with fewer than 14, and closes about 6 (Gompers, Kaplan and Mukharlyamov, "What Do Private Equity Firms Say They Do?", JFE 2016, NBER w21133, https://www.nber.org/papers/w21133). A sponsor that claims to close a much larger share of what it looks at is either not screening or not seeing competitive deal flow.
- Venture funnel. Per closed deal a VC firm considers about 100 opportunities (151 in IT, 78 in healthcare); about 1 in 4 get a management meeting, a third of those reach a partners meeting, half of those go to due diligence, and a third of diligenced deals get a term sheet. Firms issue 1.7 term sheets per closed deal, about a 60% close rate (Gompers, Gornall, Kaplan and Strebulaev, "How Do Venture Capitalists Make Decisions?", JFE 2020, NBER w22587, https://www.nber.org/papers/w22587).
- Venture diligence effort. The average VC deal takes 83 days from first contact to close, consumes about 118 hours of diligence, and involves about 10 reference calls (13 for late-stage firms, 8 for early-stage) (Gompers et al. 2020, https://leeds-faculty.colorado.edu/bhagat/vc-decisions.pdf). Use these as a floor: a lead investor that spent a fraction of this is not a diligence anchor you can rely on.
- Sourcing reality. PE firms say about 48% of closed deals are "proprietary" in some sense (36% self-generated, 7.4% from management, 8.6% executive network), but 33% come from investment banks, 8.6% from brokers, 4.3% from other PE firms. VC: more than 30% from professional networks, about 30% self-generated, about 20% from other investors, 10% inbound from management, 8% portfolio referrals (Gompers et al. 2016; Gompers et al. 2020; HLS Forum summary, https://corpgov.law.harvard.edu/2019/08/20/how-do-venture-capitalists-make-decisions/). CHECK: treat a "proprietary deal" claim as an assertion to verify. Ask who else saw it and whether a banker ran a process.

### The diligence floor

- Diligence gets thinner when deals are hot, and that costs money. Fu and Taylor used smartphone geolocation to measure hours VCs spend meeting startup staff in person before a round. Diligence hours fall in hot markets, as distance grows, and as investors get busier or more experienced. Thinner diligence does not lower average returns but widens the spread of outcomes; their model puts the value of doubling diligence at 2% to 6% of capital invested (Fu and Taylor, "Due Diligence and the Allocation of Venture Capital," NBER w33987, Jul. 2025, revised Sep. 2026, https://www.nber.org/papers/w33987; only the abstract was read, so the hours distribution is WEAK).
- Rule: set a minimum diligence floor (site visits, in-person management hours, reference calls) that does not shrink because a round is competitive. Record the hours actually spent in the IC memo ("diligence intensity," 0.7 item 7).
- Treat a seller-imposed deadline as a red flag, not a reason to skip work. Use cooling-off periods against "auction fever." Probability-weight synergies and model dis-synergies (lost customers and talent) (Feldman and Chunduru, KaW, Dec. 8, 2025, URL above).
- Diligence run to confirm an answer already chosen is the most common M&A process failure (same source). See 0.12 for the committee-level controls.

RED FLAG: a lead investor or sponsor that cannot say how many hours it spent with management in person, how many sites it visited, and how many references it called.

## 0.2 Sponsor and management background checks

- Identity verification: government ID, entity formation documents.
- Full background check: criminal, civil litigation, bankruptcy, regulatory (SEC, FINRA BrokerCheck, state securities), judgments and liens, adverse news.
- Prior track record verified independently, not from the sponsor's own deck. Confirm claimed exits, AUM, and prior deal outcomes. See 0.13 for the forensic tests.
- Resume verification. In the Drive Planning and Toltec Capital SEC cases, the principals inflated their resumes to lure investors (therealdeal.com; SEC). Resume inflation is a documented fraud precursor.
- Reference calls: former investors, lenders, partners, employees, customers, vendors. The VC norm is about 10 reference calls per deal (13 late-stage, 8 early-stage) (Gompers et al. 2020, URL in 0.1). Ask former employees, vendors and customers directly: "have you ever been asked to do something with invoices, payments or records that felt wrong?" Tips detect 43% of frauds, nearly 3x the next method; more than half of tips come from employees and almost one-third from vendors and customers (ACFE 2026, URL above).
- Litigation search on the sponsor entity and on each principal.

### Why self-disclosure cannot carry the weight

Brown, Goetzmann, Liang and Schwarz studied 444 operational due-diligence reports from a major hedge fund DD firm ("Trust and Delegation," JFE 2012, NBER w15529, https://www.nber.org/papers/w15529):

| Finding | Share of funds |
|---|---|
| Some past legal or regulatory problem (more than twice the rate in Form ADV filings) | 41% |
| Defendants in legal disputes | 32% |
| Regulatory problems | 15% |
| Misrepresented past legal or regulatory problems | 21% |
| Other statements wrong or unverifiable | 28% |
| At least one misrepresentation or inconsistency | 42% |
| Disclosed some problems, hid others ("strategic misstatement") | 6% |
| Disclosed nothing and had problems | 9% |
| Would have passed as clean on DDQ and voluntary disclosure; caught only by the independent background check | 10% |
| Verbal figures in interviews (assets, performance) contradicted the manager's own written documents | 20% |
| Fund or administrator refused to answer some DD questions | 14% |

Not using a Big 4 auditor and using internal pricing were both significantly associated with misrepresentation (same source).

- CHECK: write down every number given in management meetings and reconcile it to the data room. Treat a gap as a finding, not a slip (same source).
- CHECK: make "refused or deflected question" a tracked field in the diligence report (A.2) (same source).
- CHECK: pull Form ADV Parts 1 and 2 (IAPD) for every adviser sponsor and reconcile the disclosure items to the sponsor's own answers. Past legal and regulatory problems in Form ADV were strongly related to conflicts of interest, ownership concentration and leverage; the authors' "omega score" estimates operational risk from public data (performance, volatility, size, age, fees) when no ADV exists (Brown et al., "Mandatory Disclosure and Operational Risk," JF 2008, https://econpapers.repec.org/RePEc:bla:jfinan:v:63:y:2008:i:6:p:2785-2815; omega-score, FAJ 2009, https://econpapers.repec.org/RePEc:taf:ufajxx:v:65:y:2009:i:1:p:43-53; abstract-level, WEAK on the specific coefficients).

### Check the forecast record, not just the background report

- In Schrand and Zechman's sample of 49 SEC enforcement (AAER) firms, about a quarter of misstatements began as unintentional, optimistically biased errors; executives then slid into intentional misreporting to cover the gap. Overconfident executives were more likely to misreport and were not monitored more closely (Schrand and Zechman, "Executive Overconfidence and the Slippery Slope to Financial Misreporting," J. Accounting and Economics 53(1), 2012, https://repository.upenn.edu/accounting_papers/119).
- CHECK: compare the sponsor's or management's past projections and guidance with actual results across every prior deal or year. A pattern of repeated optimistic misses is a fraud precursor, not a style trait.
- Executives' stated 80% confidence intervals captured realized outcomes only 36% of the time across more than 13,300 CFO forecasts (Ben-David, Graham and Harvey, "Managerial Miscalibration," QJE 2013, NBER w16215, https://www.nber.org/papers/w16215). See 0.6 and 0.12.

### Diligence the team, not only the principal

- Fraud is usually a team activity. Public firms that could move to remote work after 2020 saw misconduct fall about 2 percentage points more, roughly half the baseline rate; the drop was nearly twice as large at firms with strong in-person team cultures, which the authors read as collusion becoming harder to sustain (Barrios, Guo and Zhu, via Yale Insights, https://insights.som.yale.edu/insights/remote-work-is-linked-to-decline-in-financial-misconduct). Frauds with three or more perpetrators have a median loss of $324,000 against $55,000 for one; collusion defeats segregation of duties (ACFE 2026, URL above).
- CHECK: run background checks on the CFO, controller and the person who releases wires, not only the named principal. Look for long-tenured, closed inner circles that control both reporting and cash.
- CHECK: background-check the whole placement chain. In Drive Planning, the SEC added charges on Dec. 30, 2025 against the former COO and a former managing partner, alleging they told investors the 10% "Real Estate Acceleration Loan" return was guaranteed and backed by collateral (SEC Lit. Rel. 26456, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26456). Second-tier executives and sales agents are also defendants.
- A "CFO" who is really a controller is a gap. Check that titles match the job actually done, that there is a CFO able to give an independent view, at least one director able to chair an audit committee, and clear revenue recognition. Sloppy numbers signal broader governance problems even where financials are unaudited (O'Dowd and McLarty, "Even Small Businesses Need Corporate Governance," Yale Insights, https://insights.som.yale.edu/insights/even-small-businesses-need-corporate-governance).

### Governance is part of the background check

- Theranos: a dual-class structure gave the founder 100 votes per share against 1 and full control of board composition; the board was politicians and military figures with no medical or financial expertise (KaW, "What Silicon Valley Can Learn from the Theranos Fraud Case," Mar. 19, 2018, https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/; HLS Forum, "Theranos: The Limits of the 'Fake It Till You Make It' Strategy," 2022, https://corpgov.law.harvard.edu/2022/01/30/theranos-the-limits-of-the-fake-it-till-you-make-it-strategy/). CHECK: map voting control, board seats, and each director's domain expertise. Treat founder super-voting control without a sunset as a risk factor and a pricing item.
- Serial-founder base rates (VC-backed companies, 1986 to 2003, success = IPO or IPO filing): founders with a prior success succeed about 30% of the time, against 20% for founders with a prior failure and 18% for first-time founders (Gompers, Kovner, Lerner and Scharfstein, "Performance Persistence in Entrepreneurship," JFE 2010; HLS Forum summary, https://corpgov.law.harvard.edu/2010/04/16/performance-persistence-in-entrepreneurship-and-venture-capital/). CHECK: verify the founder's prior outcome from filings and cap tables, not the founder's bio. "Prior exit" is a material underwriting variable and is often inflated.
- Sponsor deal pace is a measurable risk. In the largest US buyout database (1980 to 2013), effects differ persistently across PE groups, and rapid growth in a group's deal volume is associated with lower employment growth at its targets (Davis, Haltiwanger, Handley, Lipsius, Lerner and Miranda, "The (Heterogenous) Economic Effects of Private Equity Buyouts," NBER w26371, https://www.nber.org/papers/w26371). CHECK: chart the sponsor's deals per year and AUM growth against team size. A sponsor doubling its pace without doubling its operating bench is a yellow flag for co-investors and lenders.
- A clean record proves less than it seems. Misconduct runs far ahead of enforcement: internal records of large multinationals show more than two internally substantiated instances of financial misconduct per firm per week, about 64 times the most expansive public database (Soltes, "The Frequency of Corporate Misconduct," J. Financial Crime 2019, https://papers.ssrn.com/abstract=3347159). White-collar misconduct commonly runs about six years before exposure, typically surfacing in a downturn, so a clean record through a single bull cycle proves little (Soltes, HBS Working Knowledge, 2025, https://www.library.hbs.edu/working-knowledge/ai-schemes-could-make-bernie-madoffs-fraud-look-trivial-eugene-soltes). See 0.15.

## 0.3 KYC, AML, and sanctions

Applies to every investor and every counterparty. Regulatory status as of November 2026 is in 0.18.

- Customer identification (CIP): government ID or entity formation documents, proof of address.
- Beneficial ownership: identify and verify every natural person owning or controlling 25% or more of an entity investor, plus any control person (FinCEN CDD Rule, 31 CFR 1010.230). The CDD Rule's collection requirement for covered financial institutions is unchanged in 2026.
- **There is no federal BOI registry to lean on for US counterparties.** FinCEN's March 26, 2025 interim final rule exempted all domestic reporting companies and US persons from Corporate Transparency Act BOI reporting; the final rule (announced Aug. 2026, effective on Federal Register publication Aug. 14, 2026) made this permanent. Only foreign companies registered to do business in the US still report: FinCEN estimates about 28,000 filers against 32.6M under the 2022 rule, and FinCEN will delete previously filed BOI on US persons (Mayer Brown, Aug. 20, 2026, https://www.mayerbrown.com/de/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons; Federal Register 2026-16576, https://public-inspection.federalregister.gov/2026-16576.pdf; KPMG, https://kpmg.com/us/en/articles/2026/cta-beneficial-ownership-info-boi-reporting-fincen-final-rule.html; HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/08/27/fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons/). BOTH POSITIONS on the count of remaining foreign filers: about 28,000 (FinCEN via Mayer Brown, 2026 final rule) against about 20,000 (HLS Forum summary of the 2025 interim rule). Use the later figure. CHECK: establish beneficial ownership through your own CDD: operating agreements, cap tables, certified ownership charts, and the 25%/control-person test.
- Sanctions screening: every investor, beneficial owner, borrower and counterparty chain against OFAC SDN and sectoral lists, plus UN, EU, and UK lists for international parties, at onboarding and continuously. Apply OFAC's 50 Percent Rule: an entity owned 50% or more in aggregate by blocked persons is itself blocked even if unlisted. Benchmark the sponsor's sanctions program against OFAC's "A Framework for OFAC Compliance Commitments" (May 2019: management commitment, risk assessment, internal controls, testing and auditing, training) (OFAC, https://ofac.treasury.gov/; exact document links WEAK until confirmed). This replaces v1's vendor sources (getcaruso.com; carta.com).
- Crypto counterparties: OFAC screening must include address-level screening, not only name screening. OFAC's SDN list includes crypto addresses, and North Korean state hackers (Lazarus Group) are a primary source of stolen crypto laundered through mixers and DeFi (June Park, Princeton Fung Global Fellow, "Cyber-hacking as a Means of Self-reliance," NCNK/Wilson Center, https://ncnk.org/resources/briefing-papers/all-briefing-papers/cyber-hacking-means-self-reliance).
- PEP and adverse-media screening.
- Source of funds AND source of wealth. These are different. A single bank statement is not a source-of-wealth narrative.
- **Crypto-sourced wealth needs on-chain tracing, and the tools are heuristic.** Blockchain analytics cluster addresses using heuristics (inputs spent together share an owner; fresh change addresses), then label clusters by transacting with known services. These heuristics produce false positives, and "taint" scores assume the adversary uses the same mechanical method, so a low taint score is not proof of clean funds. Mixers and CoinJoin are designed to defeat these heuristics (Narayanan, Bonneau, Felten, Miller and Goldfeder, Bitcoin and Cryptocurrency Technologies, Princeton University Press, ch. 6, https://bitcoinbook.cs.princeton.edu). CHECK for any investor or counterparty whose wealth derives from crypto: (1) wallet addresses and a signed message proving control; (2) a tracing report from an analytics vendor covering the full history to fiat on-ramps, with mixer, darknet, sanctioned-address and high-risk-exchange exposure; (3) exchange account statements and KYC records for the on-ramp; (4) any mixer or privacy-protocol exposure is an escalation, not an automatic pass or fail, and the judgment is documented.
- Accredited investor or qualified purchaser verification. Under Rule 506(c), actual documentary evidence is required (tax returns, W-2s, bank statements, or a licensed professional's letter), not self-certification (17 CFR 230.506(c)(2)(ii)). Third-party verification letters are generally current for only 90 days (augment.market; checkfile.ai; WEAK).
- **Update (506(c) minimum-investment route).** SEC staff no-action relief (Mar. 12, 2025) lets a 506(c) issuer treat a high minimum investment (at least $200,000 for natural persons, $1,000,000 for entities), paid in cash and not third-party financed, plus a written representation, as "reasonable steps" to verify accredited status (general lane; letter citation WEAK until confirmed on sec.gov). A high minimum is therefore no longer a red flag by itself, but it shifts the burden: verify the source of the cash.
- **Who is running AML on the other LPs?** The Investment Adviser AML/CFT Rule (31 CFR Part 1032, adopted Aug. 2024) has been postponed: FinCEN's final rule (Federal Register Jan. 2, 2026; effective Dec. 31, 2025) moved the compliance date from Jan. 1, 2026 to Jan. 1, 2028, and FinCEN has said it will revisit scope; the joint SEC/FinCEN CIP proposal for advisers is not final. Until 2028 a registered or exempt reporting adviser has no federal obligation to run an AML program or file SARs (FinCEN, https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028; Federal Register, https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf; Proskauer, https://www.proskauer.com/blog/fincen-finalizes-twoyear-delay-of-the-investment-adviser-aml-rule-reaffirms-intent-to-further-review-and-tailor-the-rule-and-to-coordinate-with-other-rulemakings). CHECK: ask every GP whether it voluntarily runs an AML program, for its AML and sanctions policy, who its administrator relies on for investor KYC, and whether the administrator files SARs. Do not assume a GP has run CIP or sanctions screening on its other LPs.

## 0.4 Fraud detection: the universal red flags

RED FLAG: ONE PERSON (decides, moves cash, reports) against CLEAN: SEPARATED (manager decides; bank or custodian moves cash; administrator reports; plus independent auditor).

FIGURE 2 Segregation of duties. When one person decides, moves cash, and reports, nothing else in the file can be trusted.

### The universal red flags

- One person controls investment decisions, cash movement, and reporting. No segregation of duties is the single most consistent precursor to operational failure and fraud (thomasmurray.com, WEAK; now anchored in primary data: more than half of frauds occurred because of a lack of, or override of, internal controls, ACFE 2026, URL above). Collusion defeats segregation (three or more perpetrators: median loss $324,000 against $55,000), so segregation is necessary, not sufficient (ACFE 2026).
- No independent administrator, custodian, or auditor, or an auditor too small for the mandate. Madoff's auditor, Friehling and Horowitz, was a two-partner firm with no peer review (academia.edu; thehedgefundjournal.com). In ODD data, a non-Big 4 auditor combined with internal pricing was significantly associated with misrepresentation (Brown et al., NBER w15529, URL in 0.2).
- **Returns that are smooth relative to the stated strategy, at any level** (widened from v1's "guaranteed or fixed above-market returns"). Madoff took in about $65B; investor losses were about $18B; the pitch worked because it promised modest, stock-like returns with almost no downside (Antle, "Where Did Madoff's Money Go?," Yale Insights, https://insights.som.yale.edu/insights/where-did-madoffs-money-go). Anyone who believes higher expected return requires risk should be suspicious of low volatility combined with steady gains.
- Guaranteed or fixed above-market returns. Drive Planning promised 10% every six months on a "bridge loan." The Adam brothers promised up to 13.5% monthly (SEC 2024-97, 2024-107, https://www.sec.gov/newsroom/press-releases/2024-107). A fixed "distribution rate" on an illiquid fund is a red flag (GPB Capital, case file below).
- Refusal to allow on-site diligence or direct contact with the administrator, auditor, or prime broker.
- Statements produced by the manager rather than an independent third party.
- New-investor money paying old-investor returns. This is the definition of a Ponzi. Verify with proof of cash.
- Commingling of personal and fund accounts.
- No accounting function. At FTX there was no accounting department (the work was outsourced), the company could not produce a complete list of its own employees, and customer crypto deposits were not recorded as assets on the main entities' balance sheets; John Ray called it "a complete failure of corporate controls" (Antle, "Did Crypto Cause the FTX Collapse?," Yale Insights, Dec. 2022, https://insights.som.yale.edu/insights/did-crypto-cause-the-ftx-collapse). CHECK: confirm an in-house controller or CFO exists, an employee census reconciles to payroll, and the balance sheet records customer assets and the matching liabilities. Missing accounting function is an automatic pass.
- Customer assets used for other ventures. Werbach's rule for any custodian or exchange: do not commit fraud, and do not use customer money for other ventures; opaque firms may carry unrecognized holes from earlier failures (KaW podcast, "What the FTX Collapse Means for the Cryptocurrency Market," Nov. 22, 2022, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/what-the-ftx-collapse-means-for-the-cryptocurrency-market/; podcast-sourced, WEAK). CHECK: customer assets segregated, held at an independent custodian, and reconciled to liabilities.
- A single person holding the keys. Hot and cold wallets must use separate keys; cold keys should be split (threshold or t-of-n multisignature) so no single person can move funds. QuadrigaCX (2019): after the CEO died, reportedly the sole key holder, the Ontario Securities Commission found the exchange had run as a Ponzi, with fictitious balances credited to aliases and at least C$169M of client losses (Narayanan et al., ch. 4.2 to 4.3, https://bitcoinbook.cs.princeton.edu; OSC, "QuadrigaCX: A Review," June 2020, https://osc.ca/quadrigacxreport/index.html). This is the crypto version of the segregation-of-duties failure.
- Quarter-end window dressing. Lehman used "Repo 105" transactions to move up to $50B of assets off its balance sheet at quarter-ends and report lower leverage; Ernst & Young knew of the practice and did not force disclosure, and the examiner found colorable malpractice claims against EY (YPFS, "Lehman Brothers Bankruptcy C: Repo 105" and "D: The Role of Ernst & Young," JFC 1(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/4/ and https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/5/). CHECK: request average daily or intra-quarter balances of debt, cash and assets, not just period-end figures. Flag any recurring financing that unwinds just after period-end.
- Off-balance-sheet vehicles and implied support. Enron's partnerships and banks' SIVs held risk off the filed balance sheet, with language implying the sponsor would rescue the vehicle (Shiller, "Human Foibles, Fraud, Manipulation, and Regulation," Yale ECON 252 lecture 8, https://oyc.yale.edu/economics/econ-252-08/lecture-8). CHECK: list every SPV, JV, guarantee, keepwell and "moral obligation" support, plus every factoring, supply-chain-finance, receivables-sale and inventory-finance agreement. Require a consolidated look-through and add all of it to leverage.
- Classic sales-side tells: overselling ("doubles every ten years"), steering good deals to insiders, churning for fees, adjusted earnings with no GAAP reconciliation, and pressure to act fast (Shiller, ECON 252 lecture 8).
- Social proof in place of diligence. Ponzis are "psychological schemes" that recruit through trusted networks; affinity and "other sophisticated investors are in" substitute for diligence (Soltes, HBS WK 2025, URL in 0.2). CHECK: never accept "X and Y institutions are already in" as evidence. Ask what diligence those investors actually did and confirm with them directly.
- Small, explained-away irregularities. Frauds usually start small and escalate. Madoff described a slippery slope from payment-for-order-flow practices to naked shorting, to unrecorded short sales, to a Ponzi; he "kept on waiting for the environment to change" (HBS WK, "Bernie Madoff Explains Himself" (Soltes), https://www.library.hbs.edu/working-knowledge/bernie-madoff-explains-himself). A late audit, a restated quarter, an unbooked rebate are the early-stage signal, not noise. About a quarter of AAER misstatements began as unintentional optimistic errors (Schrand and Zechman 2012, URL in 0.2).
- AI-personalized deception (synthetic voice or video of known people, tailored pitches). CHECK: verify wire instructions and any principal's instruction by call-back to a number obtained independently, never from the message (Soltes, HBS WK 2025, URL in 0.2).

### Detection tests that work on the numbers

- Customer data catches revenue fraud at the supplier. Across about 30,000 supplier-years (1976 to 2018), two signals predicted revenue fraud: the gap between the supplier's sales growth and its major customers' purchase growth; and sharp year-over-year jumps in those customers' inventory and accounts payable (channel stuffing), which alone carried about half the predictive power of the 11-variable Dechow model (Zhang, Li and Li, "Using Economic Links between Firms to Detect Accounting Fraud," via Yale Insights, https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms). CHECK: for the top 10 customers, compare the target's reported sales to each customer with the customer's own purchase, inventory or AP trend, from confirmations, filings, or by asking private customers directly.
- Stated income is systematically overstated in booms. In 2002 to 2005, in the 18 zip codes Interthinx rated most fraud-plagued, mortgage-application income was about 90% above average IRS income, and overstating zip codes later had the highest defaults (Mian and Sufi, "Fraudulent Income Overstatement on Mortgage Applications During the Credit Expansion of 2002 to 2005," RFS 2017, NBER w20947, https://www.nber.org/papers/w20947; Princeton SPIA summary, https://spia.princeton.edu/news/how-income-fraud-made-housing-bubble-worse). CHECK: never underwrite borrower- or tenant-stated income. Verify against IRS transcripts (Form 4506-C), payroll records or bank deposits, and test the pool against an external benchmark (IRS SOI zip-code income, BLS wages). A stated-income pool whose income growth outruns local IRS income growth is a fraud signal, not a credit improvement.
- Text-diff the filings ("Lazy Prices"). Firms that materially change the language of their 10-K/10-Q (risk factors, MD&A, litigation, more negative words) subsequently see lower earnings, profitability and returns and higher bankruptcy risk; a short-changers/long-non-changers portfolio earned up to 188 bp a month, accruing for up to 18 months with no announcement reaction (1995 to 2014) (Cohen, Malloy and Nguyen, "Lazy Prices," JF 2020, NBER w25084, https://www.nber.org/papers/w25084). CHECK: for any public target, take-private, carve-out from a public parent, or public borrower, diff the last 8 quarters of filings (risk factors, MD&A, legal proceedings) and require management to explain each material edit. For private targets, diff the last 8 quarterly management letters or lender reports.
- Duration math. Frauds caught within 6 months had a median loss of $40,000; another 1 to 6 months more than doubled it ($100,000); the 5% lasting over five years had a median loss of $1.115M. A typical case runs 12 months before detection; financial statement frauds run a median 24 months. 84% of perpetrators displayed at least one behavioral red flag (ACFE 2026, URL above). Monitoring frequency is a loss-control variable.

### ACFE base rates (Occupational Fraud 2026: 2,402 cases, 143 countries, investigated Jan. 2024 to Sept. 2025)

| Measure | Value |
|---|---|
| Estimated loss to fraud | 5% of revenue |
| Median loss per case (average) | $104,000 ($1.457M) |
| Financial statement fraud: share of cases, median loss | 6%, $1,000,000 |
| Corruption: share of cases, median loss | 45%, $150,000 |
| Owner/executive vs employee median loss | $475,000 vs $50,000 |
| Three or more perpetrators vs one, median loss | $324,000 vs $55,000 |
| Detected by tips | 43% (nearly 3x the next method) |
| Typical duration before detection (financial statement fraud) | 12 months (24 months) |
| Lack or override of internal controls as cause | more than half |
| Perpetrators with at least one behavioral red flag | 84% |

Source: ACFE, Occupational Fraud 2026: A Report to the Nations, https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf. BOTH POSITIONS on tip share: 43% (ACFE 2026, primary) against "about 40%" (earlier ACFE edition as cited by Soltes, HBS 2018). Use 43%.

### Case files: the universal frauds

| Case, year | What happened | THE CHECK that would have caught it |
|---|---|---|
| Madoff, exposed 2008 | About $65B intake, about $18B investor losses; smooth stock-like returns; two-partner auditor with no peer review (Antle, Yale Insights; academia.edu) | Third-party verification of custody and trades; auditor sized to the mandate. Madoff's own rule: "You must do a third-party check. It's an absolute must... It's accounting 101" (quoted in Brown et al., NBER w15529) |
| Drive Planning, SEC 2024 and 2025 | 10% every six months on a "bridge loan"; inflated resumes; COO and a managing partner later charged for calling the return guaranteed and collateral-backed (SEC 2024-97; SEC Lit. Rel. 26456) | Proof of cash; background check on the whole placement chain |
| Theranos, 2003 to 2018 | Raised close to $1B (about $700M per KaW) at a $9B valuation; 2014 revenue projected to investors $100M, actual just over $100,000; analyzer promised about 200 tests ran about a dozen on its own hardware; false DoD deployment claim; unauthorized pharma logos (KaW, Mar. 19, 2018; HLS Forum 2022) | Independent technical validation by your own expert on your own samples; call every named validator, partner and government user; reconcile projections to invoices and cash |
| FTX, 2022 | No accounting department, no complete employee list, customer deposits off the balance sheet and routed to Alameda; raised nearly $2B from VCs with no internal audit; SBF sentenced to 25 years, March 2024 (Antle, Yale Insights; HLS Forum, "Untamed Unicorns," 2026, https://corpgov.law.harvard.edu/2026/11/04/untamed-unicorns-why-startup-finance-is-broken-and-how-to-fix-it/; DOJ SDNY, URL to be confirmed, WEAK) | Controls and accounting infrastructure first; proof of reserves AND liabilities; independent custodian |
| QuadrigaCX, 2019 | CEO reportedly sole key holder; Ponzi with fictitious balances; at least C$169M client losses (OSC 2020) | Key-ceremony documentation and quorum test |
| First Brands Group, Chapter 11 Sept. 2025 | Alleged nonexistent receivables sold to factors, collateral double- and triple-pledged, off-balance-sheet inventory financing through founder-owned entities; $12M cash against more than $9B of liabilities at filing; founder and brother indicted Jan. 29, 2026; defendants deny (DOJ SDNY, https://justice.gov/usao-sdny/pr/first-brands-executives-charged-multibillion-dollar-fraud; IRS-CI, https://irs.gov/compliance/criminal-investigation/first-brands-executives-charged-with-multibillion-dollar-fraud) | UCC search across all affiliates and founder-owned entities; direct verification of a receivables sample with remittance to a lender-controlled lockbox; reconcile all factoring and SCF in the footnotes to what each lender is told; cash proof at the parent |
| Tricolor Holdings, 2025 | Alleged double-pledging of auto loans across warehouse lenders and ABS; altered loan descriptions; charged-off loans parked in a fictitious "portfolio company"; CFO pleaded guilty; SEC civil charges Aug. 18, 2026 ("$1.9 billion collapse"); about 40% of roughly 70,000 loans shared VINs or attributes with another loan (DOJ SDNY; SEC 2026-77, https://www.sec.gov/newsroom/press-releases/2026-77-sec-charges-former-executives-fraud-connection-19-billion-collapse-subprime-auto-lender-tricolor; ABA Business Law Today, https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-october/seeing-red-flags-in-tricolor-collateral-interests). One report: about $2.2B of collateral pledged against about $1.4B real (WEAK, single report) | Loan-level dedupe across all facilities (VIN-level) by an independent collateral agent; custodial possession of titles; static-pool charge-off reconciliation from servicing system to trustee reports |
| GPB Capital, convicted 2024 | About $1.6B from individuals; distributions represented as portfolio cash flow but paid from new capital; founder sentenced May 2025 to 7 years, commuted late Nov. 2025 after 12 days served, conviction stands (NBC News, https://www.nbcnews.com/politics/white-house/trump-commutes-7-year-prison-sentence-former-private-equity-ceo-david-rcna246744) | Reconcile every distribution to its source account and to portfolio-company cash flow |
| Heller / Paramount-Prestige ATMs, SEC 2025 | Over $770M from about 2,700 mostly retail investors for fixed monthly "ATM fee" distributions funded by new money and short-term loans; about $400M losses, $185M+ allegedly misappropriated (SEC 2025-111, https://www.sec.gov/newsroom/press-releases/2025-111-sec-charges-pennsylvania-resident-his-companies-770-million-ponzi-scheme) | Confirm the operating assets exist and earn the claimed revenue, from the processor, not the sponsor |
| Archegos, March 2021 | Concentrated total-return swaps across prime brokers, none seeing the whole book; banks lost more than $10B; Hwang sentenced Nov. 2024 to 18 years (DOJ SDNY; URL to be confirmed, WEAK) | Aggregate exposure across all counterparties, not one counterparty's view |

THE ONE CHECK

> Segregation of duties plus independent verification would have caught Madoff, Drive Planning, and most of the 2024 real estate Ponzi cases. Add one line for 2025: a single, independent view of every claim on the same collateral would have caught First Brands and Tricolor.

## 0.5 Verification of funds and assets

- Proof of cash. Reconcile reported revenue and earnings back to bank statements. Standard in QoE. It catches what the P&L hides, which is why the data request asks for 36 months of statements, not a trial balance (notveryprivateequity.com; duedilio.com; WEAK as sources, the practice is standard).
- **A QoE carries no assurance.** Under AICPA standards a QoE is typically either an agreed-upon procedures engagement (SSAE No. 19, AT-C 215 as revised, effective for reports dated on or after July 15, 2021: the practitioner reports procedures and findings, gives "no opinion or conclusion," and the engaging parties accept responsibility for the sufficiency of procedures) or a consulting engagement under CS 100 (Journal of Accountancy, "SSAE No. 19: flexibility for agreed-upon procedures," Sept. 2020, https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html; PCAOB AT 601 reference to CS 100, https://pcaobus.org/oversight/standards/attestation-standards/details/AT601). CHECK: read the engagement letter and the scope section first. Ask what was NOT tested and whether proof of cash covered every bank account in the bank confirmations.
- Independent confirmation of bank balances, custody statements, and asset existence directly from the third party, unsolicited.
- Title and lien search for real assets. UCC search for personal property, across all affiliates and the principals' personally owned entities, not just the borrower (First Brands, 0.4).
- For funds: call the administrator, auditor, and prime broker directly (dealroom.net, WEAK as source; now anchored in SEC exam findings and case files, 0.15 and Chapter 10).
- Average, not period-end. Ask for average daily or intra-quarter balances of cash, debt and assets (Repo 105, 0.4).

### Verification fails even in professional ODD

Across 444 DD reports (Brown et al., "Trust and Delegation," NBER w15529, URL in 0.2):

| Verification field | Base rate |
|---|---|
| Asset information unverifiable or conflicting with a third-party source | nearly 19% |
| Reported performance with discrepancies or verification problems | 14% |
| Manager's account of the wire-signature process (who can release cash) did not match the administrator's | 16% |
| Pricing process disagreed with the administrator's | 3.6% |
| Major data vendor switched in last 3 years | 11% |

- CHECK: obtain the signatory list and approval matrix from the bank or administrator directly. Do not take the manager's description.
- Madoff's own rule: to investigate a Ponzi, "You must do a third-party check. It's an absolute must... It's accounting 101" (quoted in Brown et al., NBER w15529).
- Segregation of customer assets needs testing, not a statement. Lehman's US broker-dealer was legally required to segregate customer assets, but omnibus cash accounts and group-wide integration made the liquidation slow and messy (YPFS, "Lehman Brothers Bankruptcy E," JFC 1(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/6/). CHECK: confirm customer or fund assets sit in accounts titled to the fund or customer at a custodian outside the manager's group.
- Distributions. Reconcile every distribution to the source account and to underlying portfolio or asset cash flow (GPB Capital, 0.4).
- Operating assets. Where returns are said to come from physical assets (ATMs, machines, locations, loans), confirm existence and revenue from the processor, servicer or counterparty, not the sponsor (Heller ATM case, 0.4). Loan books: a "few defaults" claim must be proven with a borrower-level payment history traced to bank deposits and a delinquency roll (First Liberty Building & Loan, SEC 2025-98, about $140M from about 300 investors at up to 18%, https://www.sec.gov/newsroom/press-releases/2025-98-sec-charges-georgia-based-first-liberty-building-loan-its-owner-operating-140-million-ponzi-scheme). Claimed LP interests: confirm against the entity's own records and the county recorder (LeFever Mattson, SEC 2025-76, at least $46M from about 200 investors, https://www.sec.gov/newsroom/press-releases/2025-76-sec-charges-former-real-estate-investment-ceo-operating-multimillion-dollar-ponzi-scheme).
- Collateral that others may also hold. Run UCC searches across all secured parties and dedupe collateral at the item level (invoice numbers; VINs for auto paper; serial numbers) against other lenders' borrowing bases (Harker, KaW Apr. 22, 2026; general lane on Tricolor). RED FLAG: a borrower with multiple warehouse, factoring or inventory-finance providers who each see only their own collateral, and no single party that sees all of it.
- Proof of reserves is half a proof. For any custodian, exchange or crypto lender require proof of reserves AND proof of liabilities, dated the same block, with the challenge string supplied by you or an independent party, a sample of real customer accounts verifying inclusion, and an on-chain flow review around the attestation date (Narayanan et al., ch. 4.4, https://bitcoinbook.cs.princeton.edu; detail in Chapter 11).
- Wire instructions: call back on an independently obtained number (0.4).
- "Cash equivalents" are not cash. See 0.11 (Reserve Primary Fund; uninsured deposits).

THE ONE CHECK

> Get it from the third party, not from the manager: bank confirmations, the administrator's wire matrix, the custodian's statement, the processor's revenue file. In the ODD data, 1 fund in 6 described its own cash controls differently from its administrator.

## 0.6 Valuation methods across assets

| Asset | Primary methods | v2 cross-checks |
|---|---|---|
| Operating companies | DCF, trading comparables, precedent transactions | Reverse DCF ("what must be true"); flat-margin base case; fully diluted share count |
| Buyouts | LBO and sponsor return model (IRR, MOIC) | Exit multiple at or below entry; entry minus 1 to 2 turns case; return attribution (0.7 item 6) |
| Venture | Venture capital method, scorecard | Value the specific security, not the headline post-money; base-rate failure prior |
| Subscription and repeat-purchase businesses (SaaS, DTC, marketplaces, consumer subscription) | NEW: customer-based corporate valuation (CBCV) | Cohort retention; share of revenue from customers acquired in the period |
| Real estate | Direct capitalization (NOI / cap rate), DCF, sales comps, replacement cost | CAPM and BBB/BB-yield cross-check; Gordon growth; REIT-implied cap rate; inflation-only real growth |
| Credit | Recovery and liquidation analysis, loss given default | Recovery anchors by priority; spread decomposition; marks against other holders' marks |
| Merchant power | NEW: strip of spark-spread options | Spark-spread distribution; DSCR at 10th-percentile spread |
| Fund interests and secondaries | NAV, PME | PME, not compounded IRR; marks against public-factor benchmarks (0.13) |
| Real options in M&A | NEW: core NPV plus growth-option and abandonment value | Explicit, ranged assumptions only; never to rationalize price |

Where sources disagree, present both positions. Do not average them.

### How practitioners actually value deals (base rates)

- PE firms rely on gross IRR and MOIC; over 70% also use comparable-company multiples; fewer than 20% use DCF or APV; at least 55% do not use WACC at all. About 96% use a 5-year forecast horizon; exit value is set by comparable multiples (fewer than 30% use a growing perpetuity; 16% simply assume exit multiple = entry multiple) (Gompers, Kaplan and Mukharlyamov, NBER w21133, https://www.nber.org/papers/w21133).
- Haircut management forecasts. The median and mean PE discount to management's EBITDA forecast is 20% (same source). Bake an explicit haircut into the base case and show it in the IC memo.
- Target returns, buyout: target gross IRR averages 22% (most 20% to 25%; median 25% in the survey table; smaller firms higher); target MOIC median 2.5x, mean 2.85x; net IRR marketed to LPs mostly 20% to 25% (25% to 30% gross). Over 85% adjust the target IRR for risk (same source).
- Target returns, venture: average required IRR 31%; required MOIC mean 5.5x, median 5.0x, higher for early stage and smaller funds; VCs market about 24% net IRR (median 20%) and 3.5x net MOIC (3.8x early, 2.8x late). 64% adjust targets for risk; 9% use no quantitative metric at all and 20% do not forecast cash flows. MOIC is used by 63%, IRR by 42% (Gompers et al. 2020, https://leeds-faculty.colorado.edu/bhagat/vc-decisions.pdf).
- Outside view on all of these. Princeton cut its long-term endowment return assumption from 10.2% to 8% in early 2026, citing excess capital chasing limited opportunities and the loss of special access; its 20-year rolling return fell from over 14% (2005) to under 10% (2025) (iTiger/Deep News summary, https://www.itiger.com/news/1145037528; AI-CIO, https://www.ai-cio.com/?p=107176; Daily Princetonian, https://www.dailyprincetonian.com/article/2025/10/princeton-news-endowment-returns-market-private-equity-tax-research-funding-alternative-assets; press sources, WEAK). If the best-resourced LPs now assume about 8% total portfolio returns, a sponsor projecting 20%+ net IRR for a generic buyout strategy needs specific evidence.

### Forecast discipline

- Management ranges are too narrow. Over 13,300 CFO probability forecasts, realized outcomes fell inside executives' stated 80% confidence intervals only 36% of the time; miscalibrated executives invested and borrowed more (Ben-David, Graham and Harvey, "Managerial Miscalibration," QJE 2013, NBER w16215, https://www.nber.org/papers/w16215). CHECK: treat a management "downside case" as a midpoint, not a floor. Widen sponsor ranges roughly 2x before stress testing, and build the downside yourself from historical outcomes (base rates), not from the sponsor's scenario tab.
- **Margins do not expand with scale on average.** In 6,103 US IPO firms (53,079 firm-years, 1975 to 2016), median real sales growth was above 8% a year, yet cost-to-sales did not fall and profit-to-sales did not rise; the result held for all US public firms, firms worldwide and private European firms. Thomas: "If you are going to project efficiency, you have to have some concrete story" (Thomas, Ertan and Lewellen, "Do Profit Margins Expand for High Growth Firms?," via Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows). CONTRADICTS the implicit margin-expansion assumption behind Rule of 40 projections (2.4) and growth equity models (9.3). CHECK: any model where EBITDA margin rises because of scale needs a line-by-line cost bridge naming each efficiency. Otherwise hold margins flat in the base case.
- High-growth DCF discipline. Start from the expected long-run state of the market and the company's share of it, then work backward to today; do not extrapolate history. Benchmark the projected path against historical high-growth companies (Wessels, co-author of McKinsey's Valuation, KaW, "Kicking the Tires on Uber's $17 Billion Valuation," https://knowledge.wharton.upenn.edu/article/kicking-tires-ubers-17-billion-valuation-worth-much/).
- Reverse valuation: solve for what must be true. Divide the price by a fully diluted share count, then ask what margin, growth and pricing power the price requires. In one example, adding employee RSUs and options moved an implied valuation from $1.25T to about $1.7T; one estimate of understated equivalents put it above $2T (Thomas, "Is Anthropic Worth $1.25 Trillion?," Yale Insights, https://insights.som.yale.edu/insights/is-anthropic-worth-125-trillion). CHECK: always use a fully diluted count (options, RSUs, warrants, SAFEs, benefit-fund issuance). State the implied steady-state margin and growth, and test them against peers.

### Exit multiples: BOTH POSITIONS on how conservative to be

- Position 1 (base case exits at or below entry). Buying at 4x and selling at 6x because markets rise "is not a version of value creation that we feel is predictable" (Blumenthal, "How Does Private Equity Create Value?," Yale Insights, https://insights.som.yale.edu/insights/how-does-private-equity-create-value). In search-fund acquisitions later sold, aggregate enterprise value rose from about $1B to $4B; about 80% came from EBITDA multiple expansion (6.3x at entry to 15.6x at exit) and only about 20% from EBITDA growth, while margins fell from 25% to 19% over holds of about five years (Wasserstein and Thomas, "Do Search Fund CEOs Improve Performance?," Yale Insights, Apr. 2026, https://insights.som.yale.edu/insights/do-search-fund-ceos-improve-performance). Small-buyout returns are back-end-loaded and depend on exit conditions.
- Position 2 (exit = entry is not itself conservative). "Exit = entry" is the survey's most common simplification (16% of PE firms), not a conservative one if entry was at a cyclical peak. Require a case at entry minus 1 to 2 turns (Gompers et al. 2016, NBER w21133).
- Position 3 (pure DCF can underbid). A pure DCF treats uncertainty only as downside. Value a target as NPV of core (Horizon 1) cash flows, plus option value of growth businesses (H2, H3), plus abandonment value. Example: a bank's $800M DCF cap lost a deal to an $840M bid; adding abandonment value would have justified $849M (MacMillan, van Putten and Baghai, "M&A's Overlooked Pitfall: The False Negative," KaW, Mar. 30, 2011, https://knowledge.wharton.upenn.edu/article/mas-overlooked-pitfall-the-false-negative/). Use this only with explicit, ranged assumptions, never to rationalize price.
- Rule for the memo: show all three. Base case at exit multiple equal to or below entry; downside at entry minus 1 to 2 turns; option value, if claimed, as a separate, ranged line that the deal does not need in order to clear its hurdle.

### Customer-based corporate valuation (CBCV) and cohort diligence

- Method: value the company as existing customers plus future cohorts. Forecast acquisition, retention, purchase frequency and spend separately. Minimum data: customers acquired per period and total active customers; non-subscription businesses also need orders placed (Fader and McCarthy, KaW, Feb. 12, 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/; podcast-sourced, WEAK; underlying work: McCarthy, Fader and Hardie, J. Marketing 2017).
- CASE FILE, Blue Apron (2017): about 70% of acquired customers churned within six months; the IPO range was cut from $15 to $17 to $10 within days of the analysis, and shares later fell about 70% more. THE CHECK: cohort retention curves before the price is set (same source, WEAK).
- CASE FILE, Wayfair: CBCV value under $10 per share while the stock traded around $64; the stock fell about 10% the day the paper posted. A "hockey stick made entirely of acquisition," with repeat purchase weaker than the leading incumbent's, means growth needs ever-rising marketing spend (same source, WEAK). THE CHECK: track the share of revenue from customers acquired in the period against prior cohorts.

### Real estate valuation cross-checks

- Cap rates showed little response to alternative investment returns over roughly 25 years; BBB corporate bonds were the exception. Cross-check direct-cap value with CAPM, a comparison against assets of similar credit risk (BBB/BB yields), and the Gordon growth model (Linneman and Rubenstein, "How Should Commercial Real Estate Be Priced?," Wharton Real Estate Review 12(1), 2008, Zell/Lurie WP 637, https://realestate.wharton.upenn.edu/working-papers/how-should-commercial-real-estate-be-priced/).
- Public-market check on private marks. Equity REIT returns predict later returns on the appraisal-based NCREIF index; the lead-lag first found by Gyourko and Keim (1992) persists (Gyourko, Zell/Lurie WP 470 and WP 441, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/441.pdf). Context: Nareit reported REIT-implied caps at 5.74% against NCREIF ODCE appraisal caps of 4.47% in Q2 2026, a 127 bp gap (Nareit via Wharton lane, non-Wharton context, WEAK until confirmed). CHECK: compare the sponsor's exit cap and current appraisal cap against the REIT-implied cap rate for the same property type. A wide gap means the appraisal has not caught up.
- Long-run real home prices are close to flat. Shiller's index back to 1890 shows little long-run trend in real US home prices outside booms; Norway and the Netherlands show the same; real construction costs were flat or falling (Shiller, ECON 252 lecture 12, https://oyc.yale.edu/economics/econ-252-08/lecture-12). Default to inflation-only growth in exit values unless a specific supply constraint is documented.
- Comps set by levered speculators are not durable value (Mian and Sufi, 0.10).

### Credit valuation anchors

- Recovery by priority, in bankruptcies of firms with both loans and bonds outstanding (Moody's Ultimate Recovery Database, 1995 to 2013): loans 84%, secured bonds 60%, senior unsecured bonds 38%. Commentators expect lower loan recoveries next cycle given covenant-lite and thinner junior cushions (Schwert, "Does Borrowing from Banks Cost More than Borrowing from the Market?," JF 2020, Rodney White WP 03-18, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/04/03-18.schwert.pdf). Use as the LGD base.
- Not all spread is pay for default risk. Banks earn a premium over the market price of credit risk of about 142 to 172 bp of an average all-in drawn spread of 279 bp, about half and up to 61% in one model, on secured term loans to non-investment-grade firms (same source). When comparing a private loan's yield with bonds or a fund's "illiquidity premium," do not treat the whole spread as compensation for default.
- Market-index marks are reasonable fair-value guides even in a panic: subprime index (ABX) prices in 2008 to 2009 had significant fundamental components (JFC, "Revisiting Subprime Pricing Irrationality During the Global Financial Crisis," JFC 3(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss2/1/). Marking to observable indices is defensible; model-only marks that ignore them are not.
- Private credit marks lag: BDC loan marks lag B-rated leveraged loans, and price and NAV take at least four quarters to converge after a shock; the IMF recommends mandatory independent external valuations (IMF GFSR April 2024, Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md). CHECK: compare the manager's mark with the same loan's mark in other BDCs' Schedules of Investments (Elias and de Fontenay, "The Credit Markets Go Dark," Yale Law Journal 134(3), https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark).

### Venture and late-stage marks

- Last-round valuation is not a mark. FTX raised $400M at a $32B valuation, up from $25B six months earlier, before it collapsed; Stripe was reported raising about $4B at about $55B, roughly half its 2021 valuation of $95B (Erickson, "What's Wrong with the Private Equity Market and How to Fix It," KaW, Mar. 13, 2023, https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/). CHECK: reprice 2021-vintage round marks against current comparables and model a down round.
- Headline post-money valuations of later-stage rounds are biased upward (Gornall and Strebulaev, confirmed in Ouyang, Yu and Jagannathan, "Return to Venture Capital in the Aggregate," NBER w27690, https://www.nber.org/papers/w27690). CHECK: never mark or price off the headline post-money of a round with liquidation preferences, ratchets or participation. Value the specific security.

### Merchant power as options

- A gas-fired plant is economically a strip of spark-spread call options (power price minus heat rate times gas price, minus variable O&M and carbon cost), one per dispatch hour (Carmona and Coulon, "Electricity price modeling and asset valuation: a multi-fuel structural approach," https://ar5iv.labs.arxiv.org/html/1205.2299). CHECK: the IE or market advisor delivers spark-spread distributions, not a single forward curve; DSCR is tested at the 10th-percentile spark spread; the model must reproduce the plant's historical capacity factor. Panda Temple (6.7) failed on exactly this variable. Detail in Chapter 6.

### Valuation fraud: case files

| Case, year | What happened | THE CHECK |
|---|---|---|
| Infinity Q, sentenced April 2023 | Founder/CIO James Velissaris manipulated inputs to the supposedly independent Bloomberg BVAL models to mismark OTC derivatives, allegedly overvaluing assets by more than $1B and collecting nearly $27M of fees on inflated NAV; fabricated valuation-committee minutes and gave them to the SEC; 15 years (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-investment-officer-infinity-q-sentenced-15-years-prison; SEC Lit. Rel. 25331, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25331) | "Third-party pricing service" means nothing if the manager can choose models or alter inputs. Ask who has write access to pricing inputs, obtain the administrator's independent price for a sample of Level 3 positions, and read valuation-committee minutes for dissent |
| SQN Capital Management, SEC Oct. 9, 2026 (settled) | The principal personally prepared the only valuations for four funds while telling investors an independent expert did; allegedly materially inflated from at least 2019 through 2025 (SEC Lit. Rel. 26671, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671) | Obtain the named valuation firm's engagement letter and call the firm |

## 0.7 The IC memo skeleton

1. Executive summary and recommendation.
2. The ask: amount, instrument, use of proceeds, structure.
3. Sponsor or management, and track record. Track record per 0.13 (with and without the top one or two outcomes; PME; attribution to the partners who led each deal). Leadership assessment per 0.14 (the four questions; successor bench).
4. Market and thesis. Cycle overlay per 0.10 (where in the cycle; bubble checklist score; who the buyer is at exit once supply arrives).
5. The numbers: historicals, projections, base and downside, sensitivities. v2 additions:
   - **Base rates** stated before the case-specific argument (VC: about 75% of venture-backed companies never return cash, 30% to 40% liquidate with investors losing most or all; buyouts: 69% of deals change CEO during the hold; sponsors haircut management EBITDA forecasts by about 20%; R&W claim rates mid-to-high teens) (Ghosh, HBS WK, https://www.library.hbs.edu/working-knowledge/why-companies-failand-how-their-founders-can-bounce-back; HLS Forum CEO study 2026; Gompers et al. 2016; Griffith 2019 and Aon 2026, 0.16). A memo that does not state the base rate cannot explain why this deal beats it.
   - **Management-forecast haircut** shown explicitly (median 20%, Gompers et al. 2016), and sponsor ranges widened about 2x (Ben-David et al. 2013).
   - **What must be true**: the implied steady-state margin, growth and exit multiple the price requires, on a fully diluted count (Thomas, Yale Insights).
   - **Flat-margin base case** unless a costed, line-by-line efficiency bridge exists (Thomas, Ertan and Lewellen).
   - **Exit multiple against entry multiple**, a case at entry minus 1 to 2 turns, and the return with exit = entry and margins flat (Gompers et al. 2016; Blumenthal; Wasserstein and Thomas).
   - **Leverage at close against maximum permitted leverage** under all baskets, ratio debt and EBITDA add-backs. About half of borrowers close below 5x total debt/EBITDA, yet over 70% of contracts permit later senior secured debt above 5x; the median agreement has 8 baskets and the average debt basket exceeds 2.3x EBITDA (Ivashina and Vallee, "Weak Credit Covenants," NBER w27316 / Management Science 2025, https://www.nber.org/papers/w27316).
   - **Synergy table** for M&A and add-ons: probability weights and timing, cost synergies separate from revenue synergies, a dis-synergy line. Cost synergies typically take 1 to 2 years to realize; revenue synergies 2 to 3+ years; 70% to 90% of deals underperform expectations across multiple studies (Feldman and Chunduru, KaW, Dec. 8, 2025).
   - **Stress cases from outside the deal**: +200 bp on debt and discount rate for long-duration assets (Cheema-Fox, Czasonis, Kontu and Serafeim, "The AI-Energy Nexus," HBS WP 26-096, https://aiinstitute.hbs.edu/forget-the-algorithms-follow-the-electricity/); stressed advance rates and haircuts (0.11); counterparty failure (0.11).
6. Return attribution. For buyouts, split the base-case return into earnings growth, debt paydown, and multiple change. A memo that cannot separate these is asking the committee to approve a hope (goreuben.com, WEAK as source; the rule is now corroborated by primary research below). v2 additions:
   - Split IRR from dividend recaps out from earnings growth (KaW, "Lender Roundtable: Outlook on Debt Markets," https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/).
   - Benchmark against the sponsor's own industry: pre-deal, revenue growth is cited as important in more than 70% of deals, incentives 61%, governance 47%, follow-on acquisitions more than 50%, buying cheap 44% to 47%, facilitating a high-value exit about 50%, cost reduction only 36% (47% post-deal) (Gompers et al. 2016). If the plan relies on cost cuts or multiple arbitrage, the sponsor is relying on its weaker levers by its own industry's account.
   - Score the manager on the operating share of realized returns (PRINCO manager-selection principles, "Four Mantras from the Endowment," BU Insights, https://insights.bu.edu/four-mantras-from-the-endowment-a-personal-journey/).
7. Diligence findings by workstream, including what was NOT verified. v2 additions:
   - **Diligence intensity**: hours of in-person management contact, sites visited, references called, and what was skipped because of timing (Fu and Taylor, NBER w33987).
   - **Refused or deflected questions** and **verbal-versus-written discrepancies** (Brown et al., NBER w15529).
   - For each unverified fact, the specific rep, indemnity or closing condition that covers it, and a dated list of statute-of-limitations and indemnity-survival deadlines (Cloudbreak lesson, 0.16).
   - **Compliance diligence scope and gaps**, and a 100-day compliance integration and audit plan (DOJ Evaluation of Corporate Compliance Programs via HLS Forum, 2020, https://corpgov.law.harvard.edu/2020/06/29/justice-department-updates-its-guidance-on-corporate-compliance-programs/).
   - Every "hint" in the data room converted into a written question, with who asked it and the answer (Paragon Metals, 0.16).
   - **7A Bias audit** (NEW): the deal team answers the Kahneman-Lovallo-Sibony 12 questions in writing; the IC chair reads it before the vote (0.12, A.4).
8. Risks and mitigants.
9. Legal structure, security, covenants.
10. Terms and conditions precedent.
11. **Who disagreed and why** (NEW). Record the dissent from the around-the-table poll, and diarize a post-mortem date (Schwarzman, ECON 252 lecture 20).
12. **Plain-language glossary annex** (NEW). Every term of art defined in one sentence with a number attached (Sonnenfeld jargon test, 0.12).

## 0.8 The universal deck order

What investors read, in the order they read it.

1. One line: what it is and the ask.
2. Problem or opportunity.
3. The asset or business.
4. Sponsor and track record. Mark each claim verified (by whom) or asserted.
5. Market. State where in the cycle (0.10).
6. The numbers. Historical first, then projection. State the base rate the projection must beat.
7. Structure, use of proceeds, security.
8. Returns with sensitivities, including exit multiple = entry and margins flat, and what must be true.
9. Risks and mitigants.
10. Terms.

## 0.9 Master reading list

Grouped by topic. URLs where the research lanes supplied them. Free sources are preferred; paid cases are cited by title.

### Private equity and buyouts

- Harvard Extension School MGMT E-2790 Private Equity (Cendrowski et al., Private Equity: History, Governance, and Operations; HBS "A Note on Private Equity Securities" 9-200-027). CORRECTION: v1 labelled this "HBS MGMT E-2790." The MGMT E- prefix is the Harvard Extension School course-code convention, not an HBS MBA course (HBS lane, course-code convention; confirm on extension.harvard.edu). WEAK until confirmed.
- Wharton and Wall Street Prep PE Certificate. Roberto Ippolito, Private Capital Investing.
- Gompers, Kaplan and Mukharlyamov, "What Do Private Equity Firms Say They Do?" JFE 2016, https://www.nber.org/papers/w21133 (HLS summary: https://corpgov.law.harvard.edu/2016/09/21/what-do-private-equity-firms-say-they-do/).
- Davis, Haltiwanger, Handley, Lipsius, Lerner and Miranda, "The (Heterogenous) Economic Effects of Private Equity Buyouts," https://www.nber.org/papers/w26371.
- Bernstein, Lerner and Mezzanotti, "Private Equity and Financial Fragility during the Crisis," https://www.nber.org/papers/w23626.
- Josh Lerner, Ann Leamon and Felda Hardymon, Venture Capital, Private Equity, and the Financing of Entrepreneurship (Wiley).
- Richard Ruback and Royce Yudkoff, HBR Guide to Buying a Small Business (2017) (HBS Entrepreneurship Through Acquisition course; lower middle market and search funds).
- Moskowitz and Vissing-Jorgensen, "The Returns to Entrepreneurial Investment: A Private Equity Premium Puzzle?," AER 2002, https://www.nber.org/papers/w8876 (read with Kartashova, Bank of Canada WP 2011-6, which disputes robustness after the 1990s).
- Princeton Master in Finance electives as a syllabus map: FIN 517 Venture Capital and Private Equity Investment; FIN 519 Corporate Restructuring, Mergers and Acquisitions; FIN 521 Fixed Income, Options and Derivatives; FIN 570 Alternative Investments, https://bcf.princeton.edu/academic-programs/master-in-finance/requirements-core-courses/tracks-and-electives.

### Venture and entrepreneurial finance

- Yale MGT 635 (Sahlman, JFE 1990). MIT OCW 15.431 Entrepreneurial Finance (Walnut Venture Associates and Metapath cases). Stanford E145.
- Gompers, Gornall, Kaplan and Strebulaev, "How Do Venture Capitalists Make Decisions?" JFE 2020, https://www.nber.org/papers/w22587.
- Andrew Metrick and Ayako Yasuda, Venture Capital and the Finance of Innovation (Wiley); "The Economics of Private Equity Funds," RFS 2010, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf; "Venture Capital and Other Private Equity: A Survey," https://www.nber.org/system/files/working_papers/w16652/w16652.pdf.
- William Sahlman, "How to Write a Great Business Plan" (HBR 1997; HBS WK, https://www.library.hbs.edu/working-knowledge/how-to-write-a-great-business-plan) and HBS note "A Method for Valuing High-Risk, Long-Term Investments: The Venture Capital Method" (HBS 9-288-006; paid case).
- Gompers, Kovner, Lerner and Scharfstein, "Performance Persistence in Entrepreneurship," JFE 2010.
- Nanda and Rhodes-Kropf, "Investment Cycles and Startup Innovation," JFE 2013.
- Lerner and Nanda, "Venture Capital's Role in Financing Innovation," JEP 2020, https://www.nber.org/papers/w27492.
- Ouyang, Yu and Jagannathan, "Return to Venture Capital in the Aggregate," https://www.nber.org/papers/w27690.
- Fu and Taylor, "Due Diligence and the Allocation of Venture Capital," https://www.nber.org/papers/w33987.

### Funds, LPs and manager selection

- David Swensen, Pioneering Portfolio Management (Free Press, 2000 and 2009), and his Yale guest lecture (ECON 252, lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9).
- Ivashina and Lerner, Patient Capital: The Challenges and Promises of Long-Term Investing (Princeton UP, 2019); "Pay Now or Pay Later?," https://www.nber.org/papers/w22660.
- Fang, Ivashina and Lerner, "The Disintermediation of Financial Markets: Direct Investing in Private Equity," https://www.nber.org/papers/w19299.
- Lerner, Mao, Schoar and Zhang, "Investing Outside the Box," https://www.nber.org/papers/w24941.
- Lerner, Schoar and Wongsunwai, "Smart Institutions, Foolish Choices?," https://www.nber.org/papers/w11136.
- Begenau and Siriwardane, "Fee Variation in Private Equity," https://www.nber.org/papers/w29887.
- Stafford, "Replicating Private Equity with Value Investing, Homemade Leverage, and Hold-to-Maturity Accounting," RFS 2022.
- Brown, Goetzmann, Liang and Schwarz, "Trust and Delegation" (JFE 2012, https://www.nber.org/papers/w15529) and "Mandatory Disclosure and Operational Risk" (JF 2008). Empirical base rates for ODD.
- Goetzmann, Ingersoll, Spiegel and Welch, "Portfolio Performance Manipulation and Manipulation-Proof Performance Measures," RFS 2007, https://repec.som.yale.edu/icfpub/publications/2471.pdf.
- Malkiel and Saha, "Hedge Funds: Risk and Return," Princeton CEPS WP 104 / FAJ 2005, https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf. Data biases.
- Jurek and Stafford, "The Cost of Capital for Alternative Investments," JF 2015, https://www.nber.org/papers/w19643.
- Fang, Goldstein and Zeng, "The Fragility of Semi-Liquid Private Credit Funds" (2026; KaW summary, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/).
- John Morley, "The Separation of Funds and Managers," Yale Law Journal 123 (2014), https://www.yalelawjournal.org/article/the-separation-of-funds-and-managers-a-theory-of-investment-fund-structure-and-regulation.
- Ang, Chen, Goetzmann and Phalippou, "Estimating Private Equity Returns from Limited Partner Cash Flows," JF 2018. Goetzmann, Gourier and Phalippou, "How Alternative Are Private Markets?" (abstract-level, WEAK).

### Credit, covenants and structured credit

- OCC Comptroller's Handbook: Commercial Real Estate Lending; Asset-Based Lending, https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf.
- Federal Reserve SR 13-3, Interagency Guidance on Leveraged Lending, https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm.
- Ivashina and Vallee, "Weak Credit Covenants," https://www.nber.org/papers/w27316.
- Chava and Roberts (JF 2008, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/CovenantInvestmentJF2008.pdf); Roberts and Sufi (JFE 2009, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf); Roberts, "Dynamic Renegotiation" (JFE 2015, https://www.nber.org/papers/w20484); Nini, Smith and Sufi (RFS 2012).
- Schwert, "Does Borrowing from Banks Cost More than Borrowing from the Market?" (JF 2020); Cordell, Roberts and Schwert, "CLO Performance," https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf.
- Jared Elias and Elisabeth de Fontenay, "The Credit Markets Go Dark," Yale Law Journal 134 (2024).
- Federal Reserve FEDS Note, "Private Credit and Leveraged Loan Markets," Aug. 11, 2026, https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html. IMF GFSR April 2024, Ch. 2.
- YPFS, "Inside the CDO Machine" and "Anatomy of a Trade: The Making of a Subprime CDO," JFC 4(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol4/iss1/10/.

### Cycles, bubbles, crises and liquidity

- Yale Program on Financial Stability, Journal of Financial Crises (free, EliScholar): the Lehman A to H series, the AIG modules, the Reserve Primary Fund, the 2023 bank failures.
- Andrew Metrick, "The Failure of Silicon Valley Bank and the Panic of 2023," JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf.
- Gary Gorton and Andrew Metrick, "Securitized Banking and the Run on Repo," JFE 2012, https://repec.som.yale.edu/icfpub/publications/2358.pdf. John Geanakoplos, "The Leverage Cycle," Cowles DP 1715, https://cowles.yale.edu/sites/default/files/2022-08/d1715.pdf.
- Xiong, "Bubbles, Crises, and Heterogeneous Beliefs," https://www.nber.org/papers/w18905. The best short survey of bubble features.
- Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity," RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf.
- Mian and Sufi: "Household Debt and Business Cycles Worldwide" (with Verner, https://www.nber.org/papers/w21581); "Credit Supply and Housing Speculation" (https://www.nber.org/papers/w24823); "Fraudulent Income Overstatement on Mortgage Applications" (https://www.nber.org/papers/w20947).
- Robert Shiller, Yale ECON 252 Financial Markets (Open Yale Courses, free): lectures 8 (fraud), 12 (real estate), 18 (money managers), 20 (Schwarzman).

### Real estate

- FDIC and Fed interagency real estate lending standards (12 CFR Part 34 / 365). Interagency Policy Statement on Prudent CRE Loan Accommodations and Workouts (2023), https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm.
- Linneman, Real Estate Finance and Investments: Risks and Opportunities (Linneman Associates); Zell/Lurie WP 519 (cap rates, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf) and WP 637 (pricing CRE).
- Levitin and Wachter, "The Commercial Real Estate Bubble" (Harvard Business Law Review, 2013; Zell/Lurie WP 747, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/747.pdf).
- Gyourko, "Understanding Commercial Real Estate: How Different from Housing Is It?," https://www.nber.org/papers/w14708.
- Pavlov and Wachter on non-recourse put underpricing, https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/.
- Keys and Mulder, NBER w32579 (insurance), https://www.nber.org/papers/w32579.
- Hinzen, Severino and Van Nieuwerburgh, "Too-Many-to-Ignore: Regional Banks and CRE Risks" (2025), https://wffi.wharton.upenn.edu/wp-content/uploads/2025/10/HSVRegional-Banks-and-CRE-Risks.pdf.
- Wharton REAL 7210, Real Estate Investment: Analysis and Financing (course description, https://real-estate.wharton.upenn.edu/programs/mba/course-descriptions/).
- Yale SOM cases (cases.som.yale.edu): "Canary Wharf: Financing and Placemaking."

### Valuation

- Koller, Goedhart and Wessels, Valuation (McKinsey).
- Holthausen and Zmijewski, Corporate Valuation: Theory, Evidence and Practice.
- McCarthy, Fader and Hardie on customer-based corporate valuation (J. Marketing 2017; Marketing Science follow-ups).
- Ben-David, Graham and Harvey, "Managerial Miscalibration," QJE 2013, https://www.nber.org/papers/w16215.

### Fraud, governance and compliance

- Eugene Soltes, Why They Do It: Inside the Mind of the White-Collar Criminal (PublicAffairs, 2016); "The Frequency of Corporate Misconduct" (J. Financial Crime 2019, https://papers.ssrn.com/abstract=3347159); "The Difficulty of Being Good: The Efficacy of Integrity Hotlines" (2018).
- ACFE, Occupational Fraud 2026: A Report to the Nations, https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf.
- Schrand and Zechman, "Executive Overconfidence and the Slippery Slope to Financial Misreporting," JAE 2012.
- Cohen, Malloy and Nguyen, "Lazy Prices," https://www.nber.org/papers/w25084.
- Wharton Forensic Analytics Lab (Daniel Taylor) work on insider trading and 10b5-1 abuse.
- Klausner, Ohlrogge and Ruan, "A Sober Look at SPACs," Yale Journal on Regulation 39 (2022).
- SEC Division of Examinations private-fund risk alerts (June 2020; Jan. 2022), https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf.

### Judgement and decision-making

- Kahneman, Thinking, Fast and Slow.
- Kahneman, Lovallo and Sibony, "Before You Make That Big Decision," HBR June 2011 (summary, https://fs.blog/before-you-make-that-big-decision). The IC bias checklist.
- Kellogg KIEI-926, "Down and Dirty Due Diligence."
- Chen, Moskowitz and Shue, "Decision-Making under the Gambler's Fallacy," QJE 2016, https://www.nber.org/papers/w22026.

### Infrastructure, energy and data centers

- Jose Gomez-Ibanez, Regulating Infrastructure: Monopoly, Contracts, and Discretion (Harvard UP, 2003).
- Net-Zero America Final Report Summary and Annexes (Princeton Andlinger Center, 2021), https://netzeroamerica.princeton.edu.
- REPEAT Project (Princeton ZERO Lab), https://repeatproject.org.
- Brancucci, Cutler and Jenkins, "Flexible Data Centers: A Faster, More Affordable Path to Power" (Camus, encoord, Princeton ZERO Lab, Dec. 2025; funded and reviewed by Google).
- LBNL, Queued Up: 2026 Edition, https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf.
- Kleinman Center Energy Policy Now episodes on interconnection reform (Jul. 2025) and PJM data-center demand (Feb. 2026) (podcast, WEAK as sources).
- S&P General Project Finance Rating Methodology (Dec. 14, 2022), https://maalot.co.il/Publications/MT20221215151143.PDF.

### Digital assets

- Narayanan, Bonneau, Felten, Miller and Goldfeder, Bitcoin and Cryptocurrency Technologies (Princeton University Press, 2016; free draft and companion Coursera course, https://bitcoinbook.cs.princeton.edu). Chapters 4 (custody, exchanges, proof of reserves and liabilities) and 6 (anonymity, tracing, mixing).
- Wharton BDAP Stablecoin Toolkit (2026), https://bdap.wharton.upenn.edu/wp-content/uploads/2026/01/Stablecoin-Toolkit.pdf.
- WFFI, Cong, Mayer and Rabetti, "Tokenizing Real-World Assets" (2026), https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf.
- JFC, "A Framework for Understanding the Vulnerabilities of New Money-Like Products," https://elischolar.library.yale.edu/journal-of-financial-crises/vol8/iss3/1/.

### Insurance-linked balance sheets

- Koijen and Yogo, "Shadow Insurance," Econometrica 2016, https://www.nber.org/papers/w19568 (read with the Harrington/ACLI critique).

### Primary standards

- OCC Comptroller's Handbook (CRE Lending; Asset-Based Lending). ILPA DDQ 2.0 (2021); ILPA Principles 3.0 (2019, https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf); ILPA Reporting and Performance Templates (2025, https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub). NVCA Model Legal Documents (core set updated Nov. 2026, https://nvca.org/model-legal-documents/). FDIC and Fed interagency real estate lending standards (12 CFR Part 34 / 365). FinCEN CDD Rule (31 CFR 1010.230). AICPA SSAE No. 19 (AT-C 215).

### Ongoing free feeds

- Harvard Law School Forum on Corporate Governance, tags "due diligence" and "private equity": https://corpgov.law.harvard.edu/tag/due-diligence/ ; https://corpgov.law.harvard.edu/tag/private-equity/
- HBS Working Knowledge, Finance and Investing; Regulation and Compliance: https://www.library.hbs.edu/working-knowledge
- Knowledge at Wharton; Wharton Financial Institutions Center policy series (WFFI), https://wffi.wharton.upenn.edu/policy-series-topics/
- Yale Insights, https://insights.som.yale.edu; YPFS Journal of Financial Crises.
