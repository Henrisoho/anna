---
title: "The Bible on Due Diligence"
subtitle: "How to build, check, and attack a private market deal at the depth of an institutional data room. Version 2.0"
---

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

## 0.10 Credit-cycle and bubble overlay

Every deal is underwritten at a point in the credit cycle. Run this screen at step 1 (screen) and again before the IC vote. Record the result in memo item 4.

THE SPINE OF THE OVERLAY

> Cheap credit, not broad optimism, sets marginal prices; diligence thins exactly when prices are highest; and lending terms move against you at the moment you need to refinance. Underwrite the exit, the refinance and the advance rate in the regime you will meet them, not the one you entered in.

### Household and credit-supply screen

- Household-debt booms predict busts. Across 30 countries, 1960 to 2012, a one-standard-deviation rise in household debt to GDP over three years (6.2 percentage points) predicts 2.1 percentage points lower GDP growth over the following three years, plus higher unemployment; IMF and OECD forecasters systematically over-predicted growth at the end of these booms. Household debt predicts downturns better than corporate debt, and the booms are driven by credit supply (falling spreads, rising share of risky issuance), not income growth (Mian, Sufi and Verner, "Household Debt and Business Cycles Worldwide," QJE 2017, NBER w21581, https://www.nber.org/papers/w21581; NBER Digest, https://www.nber.org/digest/jan16/household-debt-and-business-cycles-worldwide). CHECK: for consumer credit, consumer brands, housing, and any deal whose exit depends on consumer demand, record the 3-year change in household debt to GDP (BIS; Fed Z.1) for the relevant market, and run a downside case with revenue growth 2 points lower for 3 years if the change is in the top third of history.
- Cheap credit lets a small optimistic minority set the price. The 2003 surge in private-label securitization expanded mortgage credit through lenders funded by non-core deposits; zip codes more exposed saw transaction volume surge, driven almost entirely by a small group of speculators (repeat buyers, under about 1.5% of the population), followed by an amplified boom and bust (Mian and Sufi, "Credit Supply and Housing Speculation," RFS 2022, NBER w24823, https://www.nber.org/papers/w24823). CHECK: ask what share of recent comparable sales were to investors or repeat buyers and how those buyers were financed. If comps were set by levered investors financed by a lender class that has since pulled back (non-bank, private-label), the comp is not a durable value.
- Securitization and loan sales loosen screening. Low-documentation subprime loans just above the 620 FICO threshold, where securitization was easier, defaulted about 10% to 25% more than loans just below it, against a mean two-year default rate of about 5% (Keys, Mukherjee, Seru and Vig, "Did Securitization Lead to Lax Screening?," QJE 2010, HLS Forum summary, https://corpgov.law.harvard.edu/2009/06/08/did-securitization-lead-to-lax-screening/). BOTH POSITIONS: the authors attribute this to lax screening when loans could be sold; Bubb and Kaufman point to underwriting rules of thumb. The test holds either way. CHECK: plot the tape's FICO and DTI distribution and default rates around every eligibility cutoff. A bunch or a performance jump at the cutoff signals origination gaming.

### Bubble checklist (Xiong's four features)

Historical bubbles (tulips, South Sea, railways, the 1920s, the internet, Chinese warrants) share four features (Xiong, "Bubbles, Crises, and Heterogeneous Beliefs," NBER w18905, https://www.nber.org/papers/w18905):

| # | Feature | What to look for in the deal's asset class |
|---|---|---|
| 1 | A technological or financial innovation story | "AI," "tokenization," "digital infrastructure," "democratized private markets" |
| 2 | Frenzied trading and an influx of new, inexperienced investors | Retail and wealth-channel inflows; turnover far above fundamentals (Chinese warrants with near-zero fundamental value turned over 328% a day in 2005 to 2008) |
| 3 | A coming increase in supply | New issuance, IPOs, lockup expiries (the internet bubble's collapse coincided with mass lockup expirations in early 2000, Ofek and Richardson), token unlocks, new construction, queued generation |
| 4 | Sudden bursts without a visible trigger | No identifiable catalyst needed |

CHECK: if three of the four are present in the asset class at entry, the IC memo must state the exit assumption explicitly in terms of who the buyer will be and at what multiple once supply arrives.

- Thematic launches buy at the top. Specialized (thematic) ETFs lose about 30% in risk-adjusted terms over their first five years, not because of fees but because they launch holding stocks already overvalued after a run of performance, media attention and sentiment (Ben-David, Franzoni, Kim and Moussawi, "Competition for Attention in the ETF Space," RFS 2023, NBER w28369, https://nber.org/papers/w28369). The same logic applies to private "theme" vehicles (AI, crypto, space, climate SPVs) raised after a hype cycle. CHECK: compare entry valuation with the sector's own history and with the date the theme peaked in media and fund-launch counts. A wave of new vehicles in the same theme is a late-cycle signal.
- Rational speculators ride bubbles rather than correct them. Hedge funds were heavily overweight tech stocks in 1998 to 2000 and cut exposure before the peak; the large fund that refused to ride (Tiger) did not survive (Brunnermeier and Nagel, "Hedge Funds and the Technology Bubble," JF 2004, https://www.princeton.edu/~markus/research/papers/hedgefunds_bubble.htm). A sophisticated co-investor being in a hot asset is not evidence of value. Ask what their exit plan and timing assumption are.
- Hot-market vintages. Startups first funded in hot VC markets are more likely to go bankrupt but also more likely to be extreme successes, and are valued higher at IPO, even for experienced VCs (Nanda and Rhodes-Kropf, "Investment Cycles and Startup Innovation," JFE 2013, https://corpgov.law.harvard.edu/2011/11/28/investment-cycles-and-startup-innovation/). In a hot market, widen the downside case rather than relying on the round's price as validation.
- Diligence thins in hot markets (Fu and Taylor, 0.1). The overlay and the diligence floor are the same control seen from two sides.

### Late-cycle product and manager signals

- A complex, illiquid product marketed to unsophisticated investors usually means the cycle is near its peak. Late entrants understand least why the strategy worked, and very large deployment targets make selective underwriting hard. Example: the largest perpetual private-credit fund must deploy about $43B a year, more than a quarter of annual US direct lending (Harker, KaW opinion, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/). CHECK: ask every manager and lender for its annual deployment target against the market it lends into ("deployment pressure").
- Retail and 401(k) channel. A 2025 executive order directed the SEC and DOL to open 401(k) plans (about $10T) to private assets; Harvard Forum authors argue retail access erodes the illiquidity and contracting advantages that made PE work, keeps higher fees, and creates liquidity mismatch (HLS Forum, "Private Equity for All," 2026, https://corpgov.law.harvard.edu/2026/02/28/private-equity-for-all-the-paradoxical-push-to-democratize-private-markets/). Treat a sponsor's pivot to retail capital as a cycle signal and read the vehicle's gates (0.11).
- Semi-liquid private credit in 2026. Net assets grew from $10B (2019) to $300B (end-2025) within a $3.5T global private credit market. In Q2 2026 the sector had $7.1B of repurchases against $3.8B of inflows, its first aggregate net outflow, with $10.7B of requests unmet (gated); Blue Owl Capital Corp II received redemption requests for about 22% of shares and Blue Owl Credit Income Corp about 40%; Blackstone, BlackRock and Apollo vehicles also saw requests above the cap (Fang, Goldstein and Zeng via KaW, Oct. 26, 2026, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/). Net debt issuance rises 0.38 percentage points of TNA for each 1-point increase in net outflows: a leverage-redemption feedback loop (same source). Detail in Chapter 10.
- Bank leverage behind private credit. Bank lending to private-credit vehicles rose from about $8B (2013) to about $95B (end-2024); bank commitments to PE and private-credit sponsors are about 14% of bank lending to nonbanks, up from about 1% a decade earlier (Harker, KaW Apr. 22, 2026). CHECK: map the fund-level leverage stack (subscription line, NAV facility, asset-based facility) and its margin-call triggers.
- Covenants weaken late in the cycle and are repriced only after a public event. LBO loans and loans with more non-bank funding have significantly weaker contracts, priced only modestly higher; the market repriced only after J.Crew (2016 to 2017) (Ivashina and Vallee, NBER w27316). Leverage is set "as much as the market will bear" (cited by about two-thirds of PE firms), not by the target's cash-flow volatility; fewer than 10% cite financial flexibility (Gompers et al. 2016). CHECK: ask the sponsor to justify leverage by the target's cash-flow volatility, not by what lenders will provide.
- Private credit risk map. Growth to roughly $2 trillion since 2008 was driven by banks shedding high-LTV leveraged loans and by PE needing leverage to hit about 20% promised returns; the main concerns are uncertain valuations (marks drive jumpy flows), high leverage and credit risk, and interconnection with banks (Ivashina, HBS WK, "How Private Debt Became a $2 Trillion Industry," https://library.hbs.edu/working-knowledge/how-private-debt-became-2-trillion-industry). BOTH POSITIONS on size, which depends on definition: about $2.1T of assets and dry powder globally in 2023 (IMF GFSR Apr. 2024); about $1.8T to $2T (Goldstein, KaW, May 5, 2026, https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit); about $1.4T of private-credit debt outstanding to US nonfinancial corporations by Q1 2026 (Federal Reserve FEDS Note, Aug. 11, 2026); $3.5T global market (Fang, Goldstein and Zeng, 2026). CHECK: ask how marks are set, who independently values Level 3 loans, and what bank facilities sit beneath the fund.
- Private credit opacity hides the cycle. Private lenders often hold a borrower's entire debt and need not mark or trade it, so they can forbear indefinitely; market prices that once gave early warning largely disappear. Assets in private-credit strategies grew from about $300B (2010) to an estimated $1.6T (2023); loans held by private-credit BDCs rose from 1,395 to 20,182 between 2010 and 2022 (Elias and de Fontenay, YLJ 134(3), https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark). CHECK: track amend-and-extend, PIK toggles and maturity extensions by loan. PIK interest's share of BDC interest income has doubled since 2019 (IMF GFSR Apr. 2024, Ch. 2).
- Default definitions move with the cycle. Proskauer's Private Credit Default Index (covenant and payment defaults) ran 1.76% (Q2 2025), 1.84% (Q3 2025), 2.46% (Q4 2025), 2.73% (Q1 2026), 2.41% (Q3 2026); in Q3 2025 the $25M to $49.9M EBITDA band ran 2.6% against 1.2% for $50M+ (Proskauer, https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-184-for-q3-2025 and successor releases). Cliffwater's realized-loss series averages about 1.0% a year since 2004 and 0.70% for 2025 (Cliffwater, https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf; 2025 release on a staging host, WEAK until confirmed on cliffwater.com). BOTH POSITIONS are true at once: they measure different things (covenant defaults that often lead to renegotiation, against realized losses) (IMF GFSR Apr. 2024). CHECK: when a sponsor quotes a default rate, ask which definition.

### Leverage-cycle and liquidity-spiral stress

- Leverage cycles move lending terms, not just prices. Average margins on mortgage securities (Ellington's book) fell to about 10% from late 2005 to 2007, then jumped above 40% in late 2007; in 2006 a AAA mortgage bond could be financed with a 1.6% haircut (about 60:1); average leverage on the $2.5T of "toxic" mortgage securities was about 16:1, and about 1.2:1 by mid-2009 (Geanakoplos, "The Leverage Cycle," Cowles DP 1715 / NBER Macro Annual 2009, https://cowles.yale.edu/sites/default/files/2022-08/d1715.pdf). Advance rates are a state variable, not a constant. Underwrite the takeout and the facility at the stressed advance rate.
- Short-term secured funding runs through haircuts. Gorton and Metrick's repo-haircut index (nine non-Treasury collateral classes) went from about zero in early 2007 to nearly 50% at the late-2008 peak; several classes could not be repo'd at all (a 100% haircut). With $10T of repo and a 20% average haircut, borrowers face a $2T shortfall (Gorton and Metrick, "Securitized Banking and the Run on Repo," JFE 2012, https://repec.som.yale.edu/icfpub/publications/2358.pdf).
- Liquidity spirals. Market liquidity and funding liquidity reinforce each other: falling prices raise margins and haircuts (margin spiral) and inflict losses on levered holders (loss spiral), so liquidity can vanish suddenly and across assets at once (Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity," RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf). CHECK: for any levered vehicle (NAV facility, margin loan, repo-funded credit fund, crypto lender), obtain the haircut and margin schedule and model a simultaneous 20% to 30% collateral price fall plus a haircut increase; confirm what assets are sold first and whether a forced sale would breach covenants elsewhere.
- Bubbles financed by banks are the dangerous ones. Using about 30 years of bank-level data, bank systemic risk rises during a bubble's build-up and further in the bust, more for larger banks and banks with high loan growth; after a median real estate bust, systemic risk of banks with unfavorable characteristics rises by almost 70% of the median (Brunnermeier, Rother and Schnabel, "Asset Price Bubbles and Systemic Risk," RFS 2020, NBER w25775, https://nber.org/papers/w25775). CHECK: when a borrower or fund relies on bank or warehouse facilities concentrated in a boomed asset class, stress the facility's renewal (advance-rate cuts, non-renewal) at the same time as the asset-price decline. The lender will be under stress when you need it.
- The PE premium itself is cyclical. Using LP cash flows, the estimated PE premium over traded factors was positive in the first half of the sample and negative later, with strong cyclicality by fund type (Ang, Chen, Goetzmann and Phalippou, JF 2018, https://econpapers.repec.org/RePEc:bla:jfinan:v:73:y:2018:i:4:p:1751-1783; abstract-level for the published figures, WEAK). Do not underwrite a constant illiquidity premium.
- Appraisal lag. REIT-implied caps against appraisal caps (127 bp gap in Q2 2026, 0.6, WEAK) and the four-quarter lag of BDC marks behind traded loans (IMF 2024) tell you how far private marks have yet to move.
- Refinancing wall. In late 2023 office values were estimated down about 30%, roughly two-thirds of office CRE debt needed refinancing within about four years, and many legacy coupons were near 1% against market near 7% (Metrick, "Is Commercial Real Estate in for a Downturn... or a Crisis?," Yale Insights, Dec. 2023, https://insights.som.yale.edu/insights/is-commercial-real-estate-in-for-downturnor-crisis). CHECK: re-underwrite any debt maturing within 48 months at the current market rate, size the refinance gap, and name who funds it.

### Cycle scorecard (record in memo item 4)

| Signal | Source | Late-cycle reading |
|---|---|---|
| 3-year change in household debt to GDP | Mian, Sufi and Verner 2017 | Top third of history |
| Share of comps bought by levered investors or repeat buyers | Mian and Sufi 2022 | Rising; financing class pulling back |
| Bubble features present (of 4) | Xiong | 3 or more |
| New thematic vehicles in the asset class | Ben-David et al. 2023 | Wave of launches |
| Complex illiquid product sold to retail; manager deployment target vs market | Harker 2026 | Yes; target is a large share of the market |
| Covenant baskets and permitted leverage | Ivashina and Vallee | Max permitted far above closing leverage |
| Haircuts, advance rates, margin terms | Geanakoplos; Gorton and Metrick | At cycle lows (high advance rates) |
| Private marks against public proxies | Gyourko; IMF 2024 | Appraisal or BDC marks above public-implied |
| Diligence hours per deal | Fu and Taylor | Falling |
| Semi-liquid fund flows and gates | Fang, Goldstein and Zeng 2026 | Net outflows; requests above caps |

RED FLAG: a deck that cites the round's price, a marquee co-investor, or a national demand forecast as validation, in an asset class scoring late-cycle on three or more lines above.

## 0.11 Counterparty, treasury and liquidity risk

Applies to every chapter. Ask it of the target, the sponsor, the fund, and your own side of the trade.

THE ONE CHECK

> Where is the cash, who holds it, what share is uninsured or gateable, and who fails first? Silicon Valley Bank's 94% uninsured deposits and a $17B unrealized loss larger than its $15B book equity were in public filings before the run (Metrick, JEP 2024).

### Bank and deposit concentration

- CASE FILE, Silicon Valley Bank, March 2023. About 94% of deposits were uninsured against an FDIC limit of $250,000. By Dec. 31, 2022, mark-to-market losses on its securities (about $17B) exceeded its $15B book equity, leaving about -$3B, all in public filings. Depositors withdrew $42B (almost a quarter of deposits) on March 9, 2023; Signature lost about $10B and First Republic about $25B the next day (Metrick, "The Failure of Silicon Valley Bank and the Panic of 2023," JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf). Hundreds of startups held large uninsured balances at SVB, which threatened payroll (Song Ma, "What's Next for the Startups That Banked with SVB?," Yale Insights, https://insights.som.yale.edu/insights/whats-next-for-the-startups-that-banked-with-svb). THE CHECK for every operating company and fund: where the cash is held, what share is above insured limits, and whether a loan covenant forces a single bank. Require deposits spread across banks, or held in insured sweeps or Treasury MMFs. Data room item: bank accounts list with balances by institution and insured share. Hard question: "If your bank closed this morning, how many weeks of payroll could you meet?"
- Bank-like counterparties (any bank, credit union, fintech lender or specialty finance company funded with deposits or short-term money): uninsured share of funding; unrealized losses on securities against equity; IRRBB (economic value of equity under rate shocks); an LCR-style 30-day outflow test. One JFC analysis argues the Basel IRRBB standard would have flagged SVB's asset-liability strategy 10 quarters before failure, and the LCR would have forced tens of billions more liquidity at least 4 quarters before (JFC, "How US Bank Regulation Failed SVB and Its Supervisors," JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/12/). Signature Bank was "particularly unprepared": it lacked collateral pre-positioned at the Fed (Metrick, JEP 2024).
- CASE FILE, First Republic Bank, 2023, as a lender. $212.6B of assets; low-coupon jumbo mortgages funded by uninsured deposits; lost $25B of deposits on March 10 and $40B more on March 13; borrowed up to $109B from the Fed; a $30B deposit from 11 banks bought only five weeks; the failure cost the FDIC about $15.6B (YPFS, JFC 7(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/24/). THE CHECK for anyone whose construction, bridge or revolving commitment sits with a regional lender: confirm the lender's funding mix, and that the draw commitment survives a lender failure (replacement lender, assignment rights).

### "Cash equivalents" and pooled cash vehicles

- CASE FILE, Reserve Primary Fund, 2008. The $62.5B fund held $785M of Lehman paper, got more than $40B of redemption requests in two days, broke the buck on Sept. 16, 2008, and suspended redemptions. Investors got about 50 cents within six weeks and 99 cents only after two years; the final distribution (99.1 cents) came in 2014 (YPFS, JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/9/). THE CHECK: look through MMF and "cash management" holdings, and model a 6-to-24-month gate on any pooled cash vehicle.
- Gates and suspensions recur and carry stigma. Suspensions of fund withdrawals work like bank holidays: they only pause the run, and stigma makes managers reluctant to use them until late (YPFS, "Survey of Bank Holidays and Fund Suspensions," JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/1/). For interval funds, non-traded BDCs, NAV REITs and evergreen vehicles, read the gate, suspension and in-kind provisions and assume they will be used. Typical BDC redemption caps are 5% of shares per quarter; average cash is about 5.5% of total net assets, NII about 2.5% a quarter (mostly paid out), and loan maturities under 0.5% a quarter, so recurring 5% redemptions exhaust liquidity quickly (Fang, Goldstein and Zeng via KaW, Oct. 26, 2026). CHECK: liquidity coverage ratio (cash + NII + maturities against the redemption cap), mark-lag tests, and redemption-queue history. Stale NAV lets redeeming investors exit above economic value at remaining holders' expense, which creates a first-mover run incentive (same source).
- Stablecoins and tokenized cash held as treasury or collateral. Score each money-like product on five features: liquidity transformation; threshold effects (a peg or $1 NAV that invites runs once broken); use as a money-like asset; contagion channels; reactive investors (JFC, "A Framework for Understanding the Vulnerabilities of New Money-Like Products," JFC 8(3), https://elischolar.library.yale.edu/journal-of-financial-crises/vol8/iss3/1/). Holding the peg under stress is not proof of safety: Tether briefly broke its peg in 2022 and recovered; reserve reports build reputation but do not remove run risk (Gorton, Yale Insights, https://insights.som.yale.edu/insights/stablecoins-survived-crypto-winter-but-that-doesnt-make-them-safe). Under the GENIUS Act (2025) payment stablecoins must be backed 1:1 by high-quality liquid assets, held for holders' benefit, audited, and not lent, pledged or rehypothecated (Circle FY2025 annual report, https://www.sec.gov/Archives/edgar/data/1876042/000187604226000116/a2025annualreport0331.pdf). CHECK: reserve composition at the instrument level, the attestation date and auditor, the custodian list, no encumbrance, and redemption terms and timing for non-retail holders.

### Prime brokers, custodians and derivatives counterparties

- CASE FILE, Credit Suisse, 2023. Client outflows in Q4 2022 and years of scandals came first. When a major shareholder said it would add no more capital, the shares fell 24% in a day and five-year CDS went above 1,000 bp; CS drew CHF 48B from standing facilities and CHF 120B from emergency ones before the UBS takeover (YPFS, JFC 7(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/18/). THE CHECK, as a counterparty, prime broker or custodian user: watch CDS, deposit and AUM outflows and shareholder support, and keep a documented plan to move assets and novate trades.
- CASE FILE, Lehman, 2008: ISDA documentation is not a resolution plan. At filing Lehman had 906,000 derivative transactions under 6,120 ISDA Master Agreements ($35T notional). Derivatives' exemption from the automatic stay let counterparties terminate and novate in a rush, destroying value; local law overrode standardized terms in several jurisdictions (YPFS, "Lehman Brothers Bankruptcy F" and "G," JFC 1(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/7/ and https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/8/). THE CHECK: for any borrower or fund with material hedges, map the counterparties, close-out netting, and whether the swap is secured pari passu under the credit agreement.
- Customer-asset segregation must be tested (Lehman broker-dealer, 0.5).
- Archegos (0.4): ask for aggregate exposure across ALL counterparties, not one prime broker's view, for any co-investment alongside a family office or levered vehicle.

### Collateral, margin and reinvestment

- CASE FILE, AIG, 2008. AIG's securities-lending program reinvested cash collateral in RMBS; when borrowers returned securities, AIG could not repay the cash, and the Fed lent up to $37.8B through the Securities Borrowing Facility. Separately, CDS written on CDOs produced collateral calls that drained liquidity; Maiden Lane III ($24.3B Fed loan plus $5B AIG equity) bought the CDOs to stop the calls (YPFS, AIG Modules B and E, JFC 3(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss1/3/ and https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss1/6/). THE CHECK: for insurers, lenders and funds, ask what cash collateral is invested in and what collateral-posting triggers (rating downgrade, mark-to-market) exist.
- Financing lines. For any levered credit fund, ABS warehouse or specialty lender: list every financing line with its haircut or advance rate, margin-call mechanics and term; stress haircuts to crisis levels (50% for non-Treasury structured collateral, 100% for esoteric assets); confirm the unencumbered liquidity that covers the call (Gorton and Metrick, JFE 2012). Stressed margins: from about 10% to above 40% in months (Geanakoplos, 0.10).
- Stress testing done right: run multiple scenarios, not one; disclose stressed fair value for all securities, including HTM; stress funding and liquidity, not only credit (JFC, "Stressing the Stress Tests," JFC 7(3), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss3/2/). CHECK: ask the manager for HTM and AFS fair-value marks and a liquidity stress, not only a loss-rate stress.

### Insurer and "permanent capital" counterparties

- Shadow reinsurance hides leverage. Life insurers ceded liabilities to affiliated, less-regulated "shadow" reinsurers (captives, often offshore), growing from about $11B (2002) to $370B (2013); by 2012 about 28 cents of every dollar insured was ceded to shadow reinsurers, up from 2 cents in 2002. Adjusting for it cut the average company's risk-based capital by about 53 percentage points and implied ratings about 3 notches lower (Koijen and Yogo, "Shadow Insurance," Econometrica 2016, NBER w19568, https://www.nber.org/papers/w19568). BOTH POSITIONS: industry critics (Harrington for ACLI) argue the effect is overstated (https://www.acli.com/-/media/acli/public/files/pdfs-public-site/public-public-policy/captives/captive_reinsurance_in_life_ins_harrington_2014.pdf). CHECK: when the counterparty, lender or LP is an insurer, or an asset manager whose permanent capital is an affiliated insurer, obtain statutory (not GAAP) statements of the operating company and its affiliated reinsurers, Schedule S ceded reinsurance, and recompute RBC on a consolidated basis including affiliated captives.
- Life-insurer private-placement lending reached about $849B (14% of balance sheets) in 2024, with PE-owned life insurers the main driver; their private placements in ABS and financial borrowers rose from 2% to 8% of assets, 2017 to 2024 (Meisenzahl, Overpeck and Polacek, Chicago Fed WP 2025-09, https://www.chicagofed.org/publications/working-papers/2025/2025-09). The manager may be lending policyholders' money into its own platform's deals. CHECK: affiliated-transaction policy, independent valuation of affiliated private placements, and the NAIC designation source (private letter ratings).
- Who holds the loan matters in a workout. Private credit holders (Fed, Q3 2025): private debt funds 54.7%, perpetual (non-traded) BDCs 18.7%, public BDCs 12.4%, middle-market CLOs 5.9%, private BDCs 5.4%, interval funds 3.0% (Federal Reserve FEDS Note, Aug. 11, 2026, URL in 0.9). A perpetual BDC with redemption queues behaves differently in a workout than a closed-end fund.

### Sponsor capacity as liquidity

- Sponsor dry powder is downside protection. In 2008 to 2009, PE-backed companies increased investment, raised more equity and debt, and gained share against peers, most strongly where the PE firm had more resources at the start of the crisis (Bernstein, Lerner and Mezzanotti, NBER w23626, https://www.nber.org/papers/w23626). CHECK: for lenders and co-investors, confirm the sponsor's uncalled capital and reserve policy in the fund that owns the company.
- Currency and peg mismatch. Schwarzman described an Argentina investment funded with dollar borrowing against a currency peg that lost every dollar (ECON 252 lecture 20). CHECK: identify any currency or peg mismatch between revenue and debt.

## 0.12 Decision hygiene and the IC bias audit

The committee is a failure point. These controls apply to every vote.

### Known biases with measured effects

- Sequence effects. In a field experiment with Indian loan officers paid a flat fee per approval, officers were 8 percentage points less likely to approve an application if they had just approved the previous one; US asylum judges were 3.3 points more likely to deny after a grant. The bias shrank when pay rewarded accuracy, and with experience (Chen, Moskowitz and Shue, "Decision-Making under the Gambler's Fallacy," QJE 2016, NBER w22026, https://www.nber.org/papers/w22026; NBER Digest, https://www.nber.org/digest/jun16/gamblers-fallacy). CHECK: score deals against fixed written criteria before discussion, randomize review order when batching, and pay reviewers (including credit staff) for accuracy, not volume.
- Pitch polish. Machine scoring of more than 1,100 accelerator pitch videos found teams with an above-average "pitch factor" (visual, vocal and verbal enthusiasm) were about 35% more likely to be funded and then did worse on follow-on financing and survival; for all-women teams, decisions were seven times more sensitive to pitch delivery (Song Ma and Allen Hu, via Yale Insights, https://insights.som.yale.edu/insights/passionate-startup-pitch-is-powerful-but-can-be-misleading). CHECK: score the written materials and data room before the live pitch, use a fixed rubric, and use more than one rater. RED FLAG: an investment case that rests on founder charisma rather than data-room evidence.
- Jargon. Opaque terms let directors and committee members approve what they do not understand. Sonnenfeld cites JPMorgan's 2012 "London Whale" losses (more than $6B, about $1B in fines), which investigations traced to governance confusion over a strategy described as "largely gibberish" (Sonnenfeld, "How Corporate Jargon Obscures the Truth and Fuels Disaster," Yale Insights, Sept. 2025, https://insights.som.yale.edu/insights/how-corporate-jargon-obscures-the-truth-and-fuels-disaster; YPFS London Whale collection, https://elischolar.library.yale.edu/ypfs-jpm-chase-london-whale/). CHECK (the jargon test): for every key term in the memo ("compute," "visibility," "risk-off," "synthetic," "hedge"), make the sponsor restate it in one plain sentence with a number attached. If no one in the approval chain can do that, the item is not approved. The memo carries a plain-language glossary annex (0.7 item 12).
- Miscalibration. Executives' 80% ranges captured outcomes only 36% of the time (Ben-David, Graham and Harvey 2013, 0.6). Answer "is the base case too optimistic" and "is the worst case bad enough" with an outside-view base rate (reference class: similar deals and their actual outcome distribution), not the sponsor's scenarios.
- Confirmation. Diligence run to confirm an answer already chosen is the most common M&A process failure. Keep deal champions separate from the valuation team; set the walk-away price before bidding; use cooling-off periods against auction fever (Feldman and Chunduru, KaW Dec. 8, 2025).
- Herding past operational warnings. DD reports are typically commissioned after strong performance and inflows; the operational-risk score built from them predicted later fund failure out of sample, yet operational risk did not reduce investor flows (Brown et al., NBER w15529). Run ODD to the same standard on a hot manager as on a cold one, and give the ODD team veto power.
- Social proof. "X and Y are already in" is not evidence (Soltes, 0.4; Brunnermeier and Nagel, 0.10).

### Governance of the process

- Go around the table, then run a post-mortem on every loss. Poll every deal team member at committee and record who disagreed and why; after losses, review which variables were misjudged and which outcomes were bad luck (Schwarzman, ECON 252 lecture 20, https://oyc.yale.edu/economics/econ-252-08/lecture-20).
- A risk framework on paper is not a control. Lehman had a framework its regulator considered compliant. From late 2006 it exceeded risk limits, raised limits to fit positions, kept risk staff out of key decisions, and in October 2007 replaced its chief risk officer with a dealmaker (YPFS, "The Lehman Brothers Bankruptcy B: Risk Limits and Stress Tests," JFC 1(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/3/). CHECK (of your own house and of any lender, fund or financial counterparty): ask for the limit-breach log and the record of limit changes for the last 24 months; ask who the CRO reports to and whether the CRO has been replaced recently.
- Diligence floor and intensity record (0.1, 0.7 item 7).
- Allocator governance. Who can terminate a manager and how fast, and is the decision-maker paid on assets retained? PRINCO staff hire and terminate managers without board sign-off while the board sets policy (PRINCO Organizational Model, https://princo.princeton.edu/about/organizational-model). CASE FILE, Connecticut state pension (about $40B): an estimated $5B less over five years and about $27B less over ten than at the 50-state median return; a plain 60/40 portfolio beat it by more than 1 point a year over the decade; eight CIOs and four interim CIOs; fees reported on total rather than actively managed assets (Sonnenfeld and Tian, Yale Insights, May 2023, https://insights.som.yale.edu/insights/why-connecticuts-investments-are-underperforming). THE CHECK: CIO tenure, fees as a share of actively managed assets, manager-level net performance against a passive alternative.

### 7A The written bias audit (Kahneman, Lovallo and Sibony)

The deal team answers in writing; the IC chair reads it before the vote (Kahneman, Lovallo and Sibony, "Before You Make That Big Decision," HBR June 2011; summary, https://fs.blog/before-you-make-that-big-decision; course copy, https://faculty.washington.edu/pathaksd/BBUS549/Required%20Readings/Before%20You%20Make%20that%20Big%20Decision.pdf). The form is A.4.

| # | Question | Bias |
|---|---|---|
| 1 | Does the team's compensation or pipeline target skew the call? | Self-interest |
| 2 | Is the team in love with the deal? | Affect |
| 3 | Were dissenting views recorded and explored? | Groupthink |
| 4 | Is the thesis an analogy to one memorable past win? | Saliency |
| 5 | Were credible alternatives (pass, smaller ticket, different structure) evaluated? | Confirmation |
| 6 | What would we want to know in a year, and can we get it now? | Availability |
| 7 | Where did each key number come from; is it the sponsor's figure re-labelled? | Anchoring |
| 8 | Are we assuming the sponsor's success in one asset class carries to this one? | Halo |
| 9 | Are we attached because of time already spent or a prior deal with this sponsor? | Sunk cost |
| 10 | Is the base case too optimistic? | Planning fallacy, competitor neglect |
| 11 | Is the worst case bad enough? | Disaster neglect |
| 12 | Is the team being too cautious? | Loss aversion |

Answer 10 and 11 with the outside-view base rate (0.6, 0.7 item 5).

## 0.13 Track-record and performance forensics

A track record is a sponsor's own exhibit. Treat it as a claim to test.

THE ONE CHECK

> Recompute the track record from cash flows you obtained yourself, show it with and without the top one or two outcomes, and benchmark it against a survivor-inclusive, vintage-matched, risk-matched public alternative.

### Manufactured performance

- Ratio metrics can be gamed. The Sharpe ratio, Jensen's alpha, the information ratio, the Sortino ratio and M-squared can all be manipulated, even with high transaction costs, by managers using derivatives or dynamic strategies; only a utility-based measure is manipulation-proof (Goetzmann, Ingersoll, Spiegel and Welch, "Portfolio Performance Manipulation and Manipulation-Proof Performance Measures," RFS 2007, https://repec.som.yale.edu/icfpub/publications/2471.pdf). CHECK: never accept a Sharpe or Sortino figure as evidence of skill. Ask for the return distribution, option-like exposures and drawdowns, and compute a manipulation-proof measure (MPPM) from monthly returns.
- Smoothness is the Ponzi tell (Madoff, 0.4). Appraisal-based marks also smooth: hold-to-maturity accounting makes a levered small-value portfolio's measured beta fall from about 2 to statistically zero (Stafford, RFS 2022, https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting). Treat low reported volatility and low correlation as an accounting artifact, not diversification.
- Short-volatility strategies look like alpha. The aggregate hedge-fund index's risk is matched by a mechanical S&P 500 index put-writing strategy; funds show 6% to 10% annual pre-fee alpha against linear factor models (1996 to 2012) yet are not reliably distinguishable from put writing; the working-paper version found the fee that would equate the put strategy to the index was about 3.6% a year (Jurek and Stafford, "The Cost of Capital for Alternative Investments," JF 2015, NBER w19643, https://www.nber.org/papers/w19643). CHECK: benchmark any strategy with short-volatility or crash exposure (credit, merger arb, levered carry, "market neutral") against a levered index put-writing series. A strategy earning a steady spread with rare large losses is selling insurance; its "alpha" in calm years is the premium.

### IRR hygiene

- Never compound an IRR, and never compare an IRR to a time-weighted index. Yale reported a 20-year venture IRR of 165.9% to June 2018 and said it should not be compounded because internet-boom distributions dominated it; the 20-year time-weighted figure was 24.6% (Yale News, Oct. 2018, https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion). Use PME or KS-PME for comparison, and report gross and net IRR with TVPI, DPI and a PME (Kaplan-Schoar PME; generalized PME, Korteweg-Nagel; Cordell, Roberts and Schwert methodology, Wharton lane).
- Venture is a right-tail business. The aggregate portfolio of all equity investments in 17,242 US ventures first funded 1980 to 2006 earned an IRR of about 22% and a generalized PME of 1.44, but dropping the best 5% of ventures makes the risk-adjusted return negative; returns decline after 1999 (Ouyang, Yu and Jagannathan, NBER w27690, https://www.nber.org/papers/w27690). CHECK: show every VC track record with and without its top one or two outcomes. A thesis of "consistent singles" contradicts the base rate.
- With and without fund leverage. The ILPA Performance Template (2025) standardizes gross and net IRR and TVPI with and without the fund-level subscription facility, and requires subscription-line interest as a separate expense line (ILPA Combined Overview, https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf; Katten, https://katten.com/insights/advisories/ilpa-publishes-updated-reporting-template-and-new-performance-template). ILPA's 2020 guidance identified 15% to 25% of commitments and 180 days outstanding as PE reference points for facility size and duration (ILPA, https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf). NAV loans can inflate interim IRR and DPI near a fundraise and pay carry on borrowed distributions (HLS Forum, "Private Equity and Net Asset Value Debt," 2024, https://corpgov.law.harvard.edu/2024/07/15/private-equity-and-net-asset-value-loans-ticking-time-bomb-or-ticking-all-the-right-boxes/). CHECK: ask every GP raising today for the ILPA Performance Template for each prior fund; refusal is a signal. Show performance with and without sub lines and NAV debt.
- Investor dollar-weighted returns can be far below fund returns. The ten best internet funds of 1997 to 2002 showed +1.5% a year time-weighted, but investors lost $9.9B of $13.7B invested (72%) because money came in near the top; Morningstar found dollar-weighted below time-weighted returns in all 17 equity categories, with a 13.4-point a year gap for tech funds (Swensen, ECON 252 lecture 9). For evergreen and semi-liquid funds, request investor-level returns and flow history.

### Database and benchmark bias

| Bias | Estimate | Source |
|---|---|---|
| Hedge fund backfill | over 500 bp a year (TASS 1994 to 2003) | Malkiel and Saha, Princeton CEPS WP 104 / FAJ 2005, https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf |
| Live vs dead funds | almost 750 bp a year (1996 to 2003) | same |
| Survivors vs all funds | 13.50% vs 9.71%, a 379 bp gap | same |
| End-of-life non-reporting | over 600 bp a year | Posthuma and van der Sluis, via Malkiel and Saha |
| Survivorship / backfill (Malkiel, as cited by Swensen) | about 4.4% / 7.3% a year | Swensen, ECON 252 lecture 9 |
| Survivorship / backfill (Ibbotson, about 3,500 funds) | 2.9% / 4.6% a year | same |

BOTH POSITIONS on the size of hedge-fund backfill bias: over 500 bp (Malkiel and Saha, primary paper) against about 7.3% (Malkiel's estimate as cited by Swensen). Different samples and periods; use the primary paper's figure and state the range.

- Attrition: of 604 funds reporting in 1996, fewer than 25% (124) still existed in 2004; LTCM lost 92% of its capital and reported none of it to the databases (Malkiel and Saha). A Russell manager universe fell from 307 to 177 reporters between 1996 and 2005, and the year-2000 domestic equity universe return was reported as -3.1% at the time and showed +1.2% in the 2005 database (Swensen, lecture 9).
- CHECK: any peer benchmark or "industry average" in a manager deck must state whether it excludes backfill and includes dead funds; otherwise haircut it by several hundred bp. Ask the GP for every fund and vehicle ever managed, including closed and abandoned ones.
- Benchmark the right risk. Buyout returns before fees can be largely replicated by a passive portfolio of small, low EV/EBITDA public stocks with about 2x leverage; after roughly 6% a year in fees, PE investors underperformed the replicating portfolio (Stafford, RFS 2022). Benchmark buyout GPs against a levered small-value index, not just the S&P 500 PME. Benchmark private funds against public factor exposures (size, value, leverage-adjusted equity) before crediting alpha (Goetzmann, Gourier and Phalippou, NBER w24941, https://www.nber.org/papers/w24941.pdf; abstract-level, preliminary, WEAK).

### Is there alpha at all? BOTH POSITIONS

| Position | Evidence |
|---|---|
| PE alpha is about zero for the average investor | Average public-pension risk-adjusted PE outperformance about zero (1995 to 2018); buyouts positive (partly value exposure), VC negative on average, real estate funds none; better picks reflected access, not selection skill (Korteweg, Panageas and Systla, HLS Forum, 2025, https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/). PE underperformed a replicating portfolio after fees (Stafford). Owner-held private equity returns were no higher than public equity (Moskowitz and Vissing-Jorgensen, AER 2002) |
| Alpha exists but is cyclical and selection-dependent | Endowments earned materially higher PE returns than other LPs (about 14% to 21% a year higher in different versions), mainly through better re-up decisions (Lerner, Schoar and Wongsunwai, JF 2007, https://www.nber.org/papers/w11136). The PE premium was positive in the first half of the LP cash-flow sample and negative later (Ang et al. 2018). Kartashova (Bank of Canada WP 2011-6) disputes Moskowitz and Vissing-Jorgensen beyond the 1990s |
| Cost of being an LP | In present-value terms roughly half of an LP's total cost is illiquidity, a quarter management fees, a quarter carry; the break-even alpha is comparable to the GP's total compensation (Sorensen, Wang and Yang, HLS Forum, 2014, https://corpgov.law.harvard.edu/2014/01/12/valuing-private-equity/) |

CHECK: before committing, write down the expected net alpha, the benchmark it is measured against (PME against a levered small-value index), and how prior predictions for this GP compared with outcomes (Siriwardane, HBS WK, https://www.library.hbs.edu/working-knowledge/rethinking-risk-why-pension-funds-are-betting-on-alternative-assets).

### Persistence, dispersion and attribution

- Manager dispersion makes selection the main decision. Ten-year first-to-third-quartile spreads to June 2005: fixed income 0.5 points a year; large-cap equity about 2; small-cap 4.7; hedge funds 7.1; real estate 9.3; leveraged buyouts 13.7; venture capital 43.2 (top vs bottom quartile) (Swensen, ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9). Choosing a median manager forfeits most of the reason to be in a private asset class.
- Persistence: BOTH POSITIONS. GPs whose fund beats the industry tend to beat it in the next fund (Kaplan-Schoar, via Metrick and Yasuda survey, NBER w16652); persistence is weaker in buyout because successful buyout GPs scale faster; Phalippou argues VC persistence is concentrated among funds backed by less sophisticated LPs. Top VC persistence comes from deal access that reputation unlocks, not better picking or advising, and reputation often sits with partners (Sorenson, Nanda and Samila, Yale Insights, https://insights.som.yale.edu/insights/for-top-venture-capital-firms-success-breeds-success). For hedge funds, persistence is close to a coin flip: about 50% of above-average funds repeat (about 55% if dead funds are excluded); about one third of top-quartile funds stay top quartile (Malkiel and Saha). CHECK: do not accept "top quartile" as evidence of skill for hedge or liquid-alternatives managers.
- Size is the enemy of performance (Swensen). CHECK: compare successor-fund size with the funds that produced the track record, with team size, and with deals per partner. RED FLAG: successor fund much larger than the funds that earned the record, without a matching increase in senior team.
- Attribute the record to the people. Attribute each realized deal to the partners who led it and test whether they are still there and still leading (Sorenson et al.). Carry allocation is driven by founder status, not track record: mean founder 19.2% of carry against 10.9% for non-founders; underprovision of carry predicts senior departures, which hurt the next fundraise (Ivashina and Lerner, "Pay Now or Pay Later?," JFE 2019, https://nber.org/system/files/working_papers/w22660/w22660.pdf). Detail in Chapter 10.
- Decompose each realized deal into revenue/EBITDA growth, leverage, and multiple change, and score the manager on the operating share (PRINCO principles, 0.7 item 6).
- Manager-selection principles from allocators. PRINCO (via a former 15-year staffer): "fewer, better, stronger" (after the GFC Princeton cut its roster because more managers diluted attention without adding safety); "who matters more than when" (pacing follows manager quality); prefer value creation through operations over leverage, multiple expansion or momentum; prefer managers who discuss problems openly. Named red flags: over-diversified rosters masking low conviction, returns driven by financial engineering, momentum mistaken for skill, opacity about problems ("Four Mantras from the Endowment," BU Insights, https://insights.bu.edu/four-mantras-from-the-endowment-a-personal-journey/; PRINCO Investment Strategy, https://princo.princeton.edu/about/investment-strategy). Yale: managers "maniacally focused on beating the markets," modest fund sizes, integrity weighed alongside numbers, and openness to emerging managers without formal records; Swensen called the standard 50-to-100-page questionnaire plus 5 to 10 years of audited history "not the richest pond" (Swensen, lecture 9; Yale Investments Office, https://investments.yale.edu/partners). Wharton: decline managers whose recent funds land consistently in the third or fourth quartile, and expect fund-size discipline after a bubble (Erickson, KaW, Mar. 13, 2023). The skill that separated endowments was the re-up decision, where the current fund's interim marks are a poor guide (Lerner, Schoar and Wongsunwai).
- Co-investments and side vehicles: assume adverse selection unless you are a top LP. In 392 direct investments by seven large institutions (1991 to 2011), co-investments underperformed the fund deals they sat beside (Fang, Ivashina and Lerner, JFE 2015, https://www.nber.org/papers/w19299); alternative vehicles (co-invest, SMAs, sidecars) reached about 40% of PE commitments by 2017 and underperform the sponsoring GP's main fund on average (Lerner, Mao, Schoar and Zhang, JFE 2022, https://www.nber.org/papers/w24941). CHECK: ask why the GP is syndicating and whether the main fund is taking its full pro rata.
- Interim marks are weak early. In 7,271 company-years in 536 US PE funds (2015 to 2020), interim returns predict final returns only weakly in years 1 to 2 (coefficient about 0.16), rising to 0.62 in years 3 to 4 and 0.78 later; a one-standard-deviation more positive tone in early GP commentary predicts about 3 to 4 points higher annualized final return (sample mean about 7%); commentary focused on cash flow and business model predicts better outcomes, focus on capital structure worse (HLS Forum, "Understanding Communications by Private Fund Managers," 2026, https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/). CHECK: read the GP's portfolio commentary history, not just the marks; flag companies where early letters dwell on refinancing, covenants or capital structure.
- Cherry-picked records are an SEC exam finding: track records shown gross of fees, without leverage effects, over selective periods, or borrowed from people not primarily responsible (HLS Forum, "SEC Identifies Private Fund Deficiencies," 2022, https://corpgov.law.harvard.edu/2022/02/17/sec-identifies-private-fund-deficiencies-signifying-increased-industry-scrutiny/).
- Operating-company forecast records count too: compare past projections with actuals (Schrand and Zechman, 0.2).

RED FLAGS: track record presented as a compounded IRR or compared with a time-weighted index; Sharpe or Sortino offered as proof of skill for a strategy using options or leverage; no ILPA Performance Template; "top quartile" without naming the benchmark, vintage and whether dead funds are included.

## 0.14 Leadership diligence

Run leadership as a full workstream, not a reference-call afterthought. Team is rated important by 95% of VCs and most important by 47%, ahead of business model (83%), product (74%), market (68%) and industry (31%); valuation ranks fifth; team is cited as the top factor in both successes (96%) and failures (92%) (Gompers et al. 2020, HLS summary, https://corpgov.law.harvard.edu/2019/08/20/how-do-venture-capitalists-make-decisions/). The founder workstream deserves the most hours, not the least.

### Base rates

| Measure | Value | Source |
|---|---|---|
| Buyouts with at least one CEO change during the hold | 69% (196 deals); a quarter of those changed more than once (2.4 transitions on average) | HLS Forum, "The CEO Decision," 2026, https://corpgov.law.harvard.edu/2026/09/23/the-ceo-decision-how-pe-investors-select-and-reassess-leaders-from-entry-to-exit/ |
| Exit CEOs appointed after year 2 | over 60% | same |
| Average hold: no change / two changes / four changes | 5.5 / 8.5 / 11.0 years | same |
| Replacements internal; external hires from the same sector | 30%; three-quarters | same |
| Top-quintile portfolio CEO performance | about 9 points a year above peers | same |
| PE firms recruiting own senior team before investing / after / at some point | about 31% / about 50% / 58% | Gompers et al. 2016, https://www.nber.org/papers/w21133 |
| Management and employee equity in PE deals (CEO) | 17% (8%); 15% (6%) at larger firms; public-company median CEO ownership about 1.6% | same |
| Portfolio boards | over 90% have 5 to 7 members; PE about 3 seats, management 1 to 2, outsiders 1 to 2 | same |
| Founder success rate: prior success / prior failure / first-time | about 30% / 20% / 18% | Gompers, Kovner, Lerner and Scharfstein, JFE 2010 |
| VC reference calls per deal | about 10 (13 late, 8 early) | Gompers et al. 2020 |

### The four entry questions (HLS CEO study)

1. Can the incumbent execute this specific plan?
2. Can gaps be closed fast enough?
3. Who are the credible internal and external successors?
4. How will requirements change across the hold?

CHECK: underwrite a CEO change as a base-case possibility and diligence the bench. Budget an extended hold in the downside case if a CEO change is likely (same source).

### Checks

- Forecast record: compare past projections and guidance with actuals; repeated optimistic misses are a precursor (Schrand and Zechman, 0.2). Overconfident executives were more likely to misreport and were not monitored more closely.
- Prior outcomes verified from filings and cap tables, not bios (Gompers, Kovner, Lerner and Scharfstein).
- Finance bench: a named CFO and controller with public-company or audited-company experience for late-stage and secondaries; an audit by a firm sized for the company; internal audit or equivalent; board not wholly founder-controlled (HLS Forum, "Untamed Unicorns," 2026, https://corpgov.law.harvard.edu/2026/11/04/untamed-unicorns-why-startup-finance-is-broken-and-how-to-fix-it/). Unicorns grew from about 40 (2013) to more than 1,500; median age at IPO rose from 9 to 13 years (2012 to 2024); the JOBS Act raised the 12(g) trigger from 500 to 2,000 holders, removing the pressure to build public-company finance functions (same source). Treat super-voting founder control plus no audit committee as a pricing item, not a footnote.
- Titles match the job; a "CFO" who is a controller is a gap (O'Dowd and McLarty, 0.2).
- Family and founder companies: an independent board with at least one director able to chair audit; a real CFO; a next generation that has worked outside the business (practitioners suggest 7 to 10 years and a C-level role, WEAK) before taking a board seat; a board reconfigured for a downturn (O'Dowd and McLarty, Yale Insights).
- Board expertise: map each director's domain expertise; a celebrity board with no domain experts is a red flag (Theranos, 0.2).
- Team integrity: background-check the CFO, controller and wire releaser (Barrios et al., 0.2).
- Incentives: management equity and vesting against the 17%/8% benchmark (Gompers et al. 2016).
- Lead investor's monitoring capacity. When a new direct flight cut VC travel time to a portfolio company, the company produced more and better-cited patents and was more likely to IPO or exit successfully (about 1.0 and 1.4 percentage points) (Bernstein, Giroud and Townsend, "The Impact of Venture Capital Monitoring," JF 2016, https://corpgov.law.harvard.edu/2014/01/30/the-impact-of-venture-capital-monitoring/). Diligence the lead's practical capacity to monitor (board load, distance, partner bandwidth), not just its brand.
- GP leadership succession (funds): about 6% of GP leaders transition over five years against more than 50% turnover for public-company CEOs; fewer than half of GPs have a formal transition plan; 96% of LPs say succession readiness is decisive for re-ups (HLS Forum, "Succession Planning in Private Equity," 2026, https://corpgov.law.harvard.edu/2026/02/21/succession-planning-in-private-equity-a-strategic-imperative-for-gps-and-lps/). Ask who actually makes investment decisions, who owns the LP relationship, what happens economically if a founder steps back, and whether the successor has led at scale.
- Interview discipline: write down every number management states and reconcile it to documents (Brown et al., 0.2); score materials before the pitch (Ma and Hu, 0.12).

## 0.15 Compliance and misconduct diligence

Public records show a fraction of misconduct. Diligence the internal record.

- Misconduct is far more frequent than enforcement data suggests: more than two internally substantiated instances of financial misconduct per firm per week, about 64 times the most expansive public database (Soltes, J. Financial Crime 2019, https://papers.ssrn.com/abstract=3347159). A clean SEC and litigation search on a target is weak evidence. CHECK: request the internal investigations log, the hotline log, and how each matter was closed, for 3 years.
- Test the whistleblower hotline; do not just confirm it exists. In a field study placing misconduct reports with nearly 250 firms, one-fifth had a non-functional channel (disconnected phone, bounced e-mail, wrong website), and firms with predicted internal-control weaknesses or recent sanctions were more likely to discourage anonymity. Tip-detected frauds ran a median 17 months against 24 (auditor) and 36 (law enforcement) (Soltes, "The Difficulty of Being Good: The Efficacy of Integrity Hotlines," 2018, https://www.stern.nyu.edu/sites/default/files/assets/documents/Eugene%20Soltes%20-%20The%20Difficulty%20of%20Being%20Good%20The%20Efficacy%20of%20Integrity%20Hotlines.pdf). Tips detect 43% of frauds (ACFE 2026). CHECK: call or e-mail the hotline during diligence; request hotline volume, categories and resolution times for 3 years.
- Prosecutors now expect compliance diligence. DOJ's Evaluation of Corporate Compliance Programs asks whether the acquirer performed comprehensive pre-acquisition compliance diligence (and if not, why), has a process for timely integration of the target into its controls, and audits acquired entities post-close (HLS Forum, 2020, https://corpgov.law.harvard.edu/2020/06/29/justice-department-updates-its-guidance-on-corporate-compliance-programs/). CHECK: document compliance diligence scope and gaps in the IC memo, and put a 100-day compliance integration and audit plan in the value-creation plan.
- FCPA successor liability. DOJ's M&A policy (2018, folded into its Corporate Enforcement Policy) gives a presumption of declination to an acquirer that discovers corruption through pre- or post-close diligence, promptly self-discloses, cooperates and remediates (HLS Forum, "FCPA Successor Liability," 2018, https://corpgov.law.harvard.edu/2018/08/14/fcpa-successor-liability/). Corruption appears in 45% of ACFE cases (ACFE 2026). CHECK: for any target with foreign sales agents, government customers or licences, run third-party and agent diligence, and plan the disclosure decision before signing.
- Control brings liability for the sponsor. (1) False Claims Act: DOJ named PE sponsor Riordan, Lewis & Haden alongside its portfolio pharmacy (Diabetic Care Rx) for financing a kickback scheme; settled 2019 for $21.36M. (2) ERISA multiemployer pension withdrawal liability: Sun Capital funds were held to be a trade or business under common control with a bankrupt portfolio company (D. Mass. 2018). (3) Control-person securities liability. (4) Veil-piercing. (5) FCPA (Och-Ziff 2016) (HLS Forum, "Secondary Liability Risks for Private Funds," 2019, https://corpgov.law.harvard.edu/2019/10/09/secondary-liability-risks-for-private-funds-recent-developments/). CHECK: in health care and government-contract targets, diligence billing and referral practices before close; map multiemployer pension exposure and structure ownership to avoid 80% common control where withdrawal liability exists; independent directors at portfolio level; corporate formalities; D&O coverage at both levels.
- Regulated-manufacturing data integrity. CASE FILE, Fresenius / Akorn (2017 to 2018): Fresenius's diligence flagged deficiencies in Akorn's testing and manufacturing, but it signed anyway; post-signing whistleblower letters led to an investigation that found falsified data and FDA submissions with false data. Delaware Chancery (2018) let Fresenius walk under the MAE clause, the first such ruling, but noted the agreement did not carve out diligence-disclosed matters; Akorn's CEO testified he never read the audit reports he received (Skadden, "Analyzing Akorn," https://www.skadden.com/insights/publications/2018/10/analyzing-akorn; opinion, https://law.justia.com/cases/delaware/court-of-chancery/2018/ca-2018-0300-jtl.html). THE CHECK: in pharma, food, supplements and medical devices, run an independent data-integrity audit of quality systems (raw lab data against reported data, FDA 483s and warning letters, audit trails), and draft specific closing conditions or indemnities for every known regulatory issue rather than relying on a general MAE.
- Labor-market antitrust. About 58% of major franchisors' 2016 franchise agreements contained no-poaching-of-workers clauses (examples: McDonald's, Burger King, Jiffy Lube, H&R Block); after the paper, the Washington State Attorney General and others forced their abandonment across many chains, and antitrust class actions followed (Krueger and Ashenfelter, "Theory and Evidence on Employer Collusion in the Franchise Sector," NBER w24831, https://www.nber.org/papers/w24831). CHECK: in franchise, multi-unit, staffing or roll-up targets, review franchise agreements, FDD Item 17, employment agreements and vendor contracts for no-poach, non-solicit and wage-fixing provisions; confirm removal and any open AG or class-action exposure; confirm non-compete enforceability by state for key employees.
- Antitrust on the exit. About 6% of pharma acquisitions (6.4% in the working paper) were "killer acquisitions" that shut down an overlapping project; they cluster just below HSR thresholds (Cunningham, Ederer and Ma, "Killer Acquisitions," JPE 2021, https://papers.ssrn.com/abstract=3241707). Expect growing FTC and DOJ scrutiny of sub-threshold deals in any strategic-exit thesis.
- Filing diffs (Lazy Prices, 0.4).
- Fund-level compliance (for GP diligence): SEC exam deficiencies are the test list (0.13, Chapter 10): LPAC consent skipped for conflicted transactions; post-commitment fees not stepped down; terms extended without approval ("zombie funds"); strategy and leverage outside limits; key-person events not followed; cherry-picked records; inadequate diligence on investments and service providers; hedge clauses purporting to waive fiduciary duty (HLS Forum 2022, URL above; SEC Division of Examinations risk alerts, June 2020 and Jan. 2022, https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf; Holland & Knight, https://www.hklaw.com/en/insights/publications/2022/02/division-of-examinations-publishes-risk-alert-for-private-fund). Fee case: TZP Management charged Aug. 15, 2025 with overcharging management fees by failing to offset portfolio-company transaction fees (SEC order; release number WEAK until confirmed). CHECK: recompute fee offsets from portfolio-company payments.
- Portfolio-level leakage. CASE FILE, Momentum Advisors (SEC 2025-53, Mar. 7, 2025, settled): the COO diverted about $223,000 from a private fund's portfolio companies via company debit cards and excess salary, concealed from the adviser, the bookkeeper and SEC staff; the managing partner failed to supervise and caused the fund to pay a $346,904 debt of an entity the two controlled; the fund was never audited; penalties $515,000 total (https://www.sec.gov/newsroom/press-releases/2025-53). THE CHECK: an unaudited fund is an automatic pass; test portfolio-company card and payroll spend for insiders, since a fund audit alone will not catch portfolio-level leakage.

## 0.16 Preserving legal remedies

Diligence is also evidence. Run it so that, if something goes wrong, you still have a claim, an insurer, or a price adjustment.

THE ONE CHECK

> Convert every hint into a written question, ask it, record the answer, re-run the model, and tie each unverified fact to a specific rep, indemnity or closing condition with a diarized deadline.

### Case files

| Case, year | What happened | THE CHECK |
|---|---|---|
| Paragon Metals Holdings v. Smith (Del. 2026) | A PE sponsor paid $100M for an auto-parts maker; the day after closing it learned two of the largest customers planned sharp volume cuts; it later defaulted on acquisition debt and injected $37M. The CEO had withheld a customer letter, stripped volume-reduction terms from a contract amendment, routed a $300K rebate through a foreign affiliate, and destroyed his phone. The buyer had seen hints, but its negotiator never asked the prepared questions in customer meetings, nobody read the CEO e-mail summarizing the letter, and the model was not updated. The Supreme Court revived the fraud claim, but only after years of litigation (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/07/30/are-hints-disclosures-delaware-supreme-court-revives-ma-fraud-claim-despite-buyers-red-flags/) | Convert every hint into a written question; ask it in customer meetings; document the answer; re-run the model; get customer-level volume forecasts directly from top customers |
| Cloudbreak Health / UpHealth de-SPAC (closed June 2021; Edwards v. GigAcquisitions2, Del. Ch. July 2025) | Cloudbreak merged with a SPAC and five struggling health-care companies on oral assurances and presentations prepared by the counterparty's banker; the presentations overstated revenue and contract value and omitted insolvency and an auditor resignation; the combined company went bankrupt. The fraud claim was dismissed as time-barred: the counterparties' agents owed no duty, the banker's disclaimers should have prompted independent work (HLS Forum, 2025, https://corpgov.law.harvard.edu/2025/08/26/chancery-decision-doubles-down-on-due-diligence/) | When you take stock as consideration, diligence the buyer as hard as a target (own QoE, call the auditors, ask about any auditor change); get specific reps on facts you cannot verify; diarize the fraud limitations period and indemnity survival dates |
| Fortis v. Johnson & Johnson (Auris Health; Del. Ch. 2024; Del. Supr. Jan. 2026) | Earnout milestones for a robotic-surgery product; Chancery found J&J breached its efforts obligations and fraudulently induced one milestone; the Supreme Court partly reversed, holding the negotiated "commercially reasonable efforts" definition let J&J calibrate effort for the first payment but not the rest (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/02/10/drafting-guidance-from-delaware-supreme-court-on-earnouts-efforts-obligations-and-fraud/) | The efforts definition is the asset. Read it, and draft objective metric definitions with worked examples, an explicit efforts standard or spend commitment, reporting and audit rights, and acceleration triggers |
| Fresenius / Akorn (Del. Ch. 2018) | MAE walk-away succeeded, but the agreement did not carve out diligence-disclosed matters (0.15) | Specific closing conditions or indemnities for each known issue, not a general MAE |

### Rules

- Anti-reliance clauses cut both ways. Delaware will not let a contract shield deliberate misrepresentations inside the agreement, and fraud claims based on diligence statements have survived non-reliance clauses in some cases. But do not rely on litigation as the remedy: reflect diligence findings in the price, the model, and specific indemnities (HLS Forum, "The Looming Specter: Post-Closing Fraud Claims in Private Company M&A Litigation," 2017, https://corpgov.law.harvard.edu/2017/07/19/the-looming-specter-post-closing-fraud-claims-in-private-company-ma-litigation/).
- R&W insurance excludes what you know. Typical limit 10% to 20% of deal value; retention about 1% of deal value; premium about 2% to 3% of the limit; over 95% of policies buy-side; used in roughly half of private-target deals, almost never public. In insured deals any seller indemnity tends to equal the retention (about 1%), against about 10% of deal value in uninsured deals. Policies exclude anything known to the buyer or its advisors, so whatever diligence finds is uninsured: price it or get a special indemnity. Moral hazard: insured buyers may diligence less (Griffith, "Deal Insurance," HLS Forum, 2019, https://corpgov.law.harvard.edu/2019/07/01/deal-insurance-representation-warranty-insurance-in-ma-contracting/). Underwriters review the buy-side QoE, legal and tax reports, and exclude matters not diligenced (general lane, 5.5).
- In a walk-away RWI deal the buyer's only recourse for a bad rep is the insurer, net of retention. Diligence quality therefore sets the coverage: what the QoE found is excluded; what it missed but should have found may be disputed (general lane, 5.4).
- Market terms (US private targets):

| Term | ABA 2025 Private Target Deal Points (139 deals, 2024 to Q1 2025) | SRS Acquiom 2025 Deal Terms (2,200+ deals, 2019 to 2024) |
|---|---|---|
| RWI used | 63% (55% prior study) | 42% of 2024 deals (44% in 2021) |
| Reps do not survive closing | 41% (30% prior study) | 33% of 2024 deals; 57% of RWI deals vs 11% of traditional-indemnity deals |
| Survival period where reps survive | 24 months most common (26%), then 12 (23%), 18 (19%) | Median 12 months |
| Basket | About two-thirds true deductibles, typically 0.5% to 1% of value | n/a |
| Indemnity cap | Mean about 16.8% of value (just over 6% in 2021), skewed by a minority of high-cap deals; use the median when published | n/a |
| Separate PPA escrow | n/a | Median 0.98% of value (1.00% in 2023) |

Sources: Business Law Today, https://businesslawtoday.org/?p=33407; K&L Gates, Dec. 19, 2025, https://www.klgates.com/2025-ABA-Private-Target-Mergers-Acquisitions-Deal-Points-Study-12-19-2025; Goulston & Storrs, https://www.goulstonstorrs.com/insights/article/2025-aba-private-target-m-and-a-deal-points-study-what-s-market; SRS Acquiom, https://media.taftlaw.com/wp-content/uploads/2025/04/15175412/2025-SRS-Acquiom-MA-Deal-Terms-Study-2-page-quick-reference.pdf. The ABA survival and deductible splits come via secondary summaries (WEAK until confirmed against the ABA PDF). BOTH POSITIONS on RWI penetration (63% ABA against 42% SRS Acquiom): different samples (ABA's 139 publicly available agreements against SRS Acquiom's 2,200+ deals it administered). Do not average; cite the sample.

- What actually goes wrong (claims data). About 18% of R&W policies bound 2019 to 2023 had at least one claim notification (historical 16% to 20%); 2025 North American R&W payments totalled about $440M across about 40 payments, median about $8.2M, average about $10.4M. Financial-statement breaches drove 38% to 40% of paid loss, material contracts 21%, compliance with laws 15.1%, IP 11%. 51% of claims were notified more than 12 months after closing and 24% more than 24 months. 20.6% of claims (2021 to 2025 policies) alleged loss on a multiple basis, and these made up 68% of 2025 paid loss (Aon 2026 Transaction Solutions Global Claims Study, https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study). AIG: about one claim per six policies (2012 to 2021); financial statements the leading breach (21%), then tax (19%) and compliance (16%) (AIG, https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2023-r-and-w.pdf.coredownload.pdf). BOTH POSITIONS on the financial-statement share: 38% to 40% of paid loss (Aon) against 21% of claims (AIG; also Marsh 2023, 13% of claim count but nearly half of claimed dollars). Count against dollars; both say financial statements dominate the money.
- Losses are claimed at the deal multiple. A $10M EBITDA overstatement at 12x can support about $120M of loss (Griffith 2019). The QoE, top-customer and supplier contract review, and regulatory compliance review together explain about three-quarters of insured loss; if budget is limited, those three workstreams come first.
- Timing. Because half of claims come more than 12 months after closing and a quarter after 24 months (Aon 2026), a 12-month survival period (SRS median) leaves a large share of discoveries uncovered. CHECK: diarize survival dates, the R&W policy period, and the fraud limitations period at signing.
- Earnouts. Outside life sciences, earnouts appear in about one in five private deals (15% in 2019, peak 30% to 37% in 2023, about 22% in 2024); median earnout about 31% of closing payments (2024) with a median 24-month period. In life sciences over 80% of private pharma deals use them, median about 61% of total consideration, often 3 to 5 years. Dispute risk rises with earnout share and length (HLS Forum, "The Art and Science of Earn-Outs in M&A," 2025, https://corpgov.law.harvard.edu/2025/07/11/the-art-and-science-of-earn-outs-in-ma/). Drafting checklist: objective metric definitions with worked examples; explicit efforts standard or fixed spend commitment; buyer reporting and audit rights; rules on cost allocation, staffing and working capital during the period; acceleration triggers; expert-not-arbitrator scope; records of efforts.
- LPs rarely sue. Of 153 lawsuits over four decades against the top and bottom 50 PE firms, only 6 (4%) were filed by fund investors and 3 (2%) by institutions; LPAs carry broad GP indemnification, exculpation, mandatory arbitration and limited information rights, and LPs fear losing allocations. A rare exception: the Abu Dhabi Investment Council sued a US PE firm in Delaware Chancery (Dec. 2025) over a continuation-fund transaction (HLS Forum, "Opting Out of Court?," 2026, https://corpgov.law.harvard.edu/2026/06/29/opting-out-of-court-reputation-and-informal-norms-in-private-equity/). The protection you get is what you negotiate before signing: information rights, LPAC composition, no-fault removal, consent rights on GP-leds and NAV loans. LPs generally cannot remove the manager except for egregious misconduct; the weaker the exit, the more the LPA must carry (key-person dissolution, for-cause removal standard, no-fault divorce threshold) (Morley, YLJ 123, 2014). Treat any fund with neither key-person dissolution nor a workable removal right as having no governance.
- No federal backstop since 2024. The SEC's Private Fund Adviser rules were vacated (0.18); quarterly statements, fund audits and fairness opinions on GP-led secondaries must be contracted for in the LPA or side letter.
- Investor-side liability. Veto rights used to harm the company create liability (Zync v. Porsche, Del. Ch. May 2026, pleading stage, https://corpgov.law.harvard.edu/2026/07/20/chancery-finds-potential-liability-for-blocking-company-financings-despite-contractual-veto-rights/); insider-led rescue financings face entire-fairness review (Guilbeau v. Footprint, Del. Ch. May 2026, pleading stage, https://corpgov.law.harvard.edu/2026/06/17/chancery-finds-funds-liable-for-aiding-directors-fiduciary-breaches/). CHECK: price insider rounds against your own recent marks and bridges, document every rejected alternative, give non-participants real time and data, and disclose insider benefits. Detail in Chapters 2 and 9.
- Lender counsel. Sponsor-designated lenders' counsel is the norm in US mid- and large-cap LBOs; designated counsel face pressure not to "over-lawyer" (HLS Forum, "Sponsor-Designated Lenders' Counsel," 2026, https://corpgov.law.harvard.edu/2026/04/16/sponsor-designated-lenders-counsel/). CHECK: have your own counsel review baskets, the EBITDA definition and unrestricted-subsidiary provisions (J.Crew blocker), Chapter 3.

## 0.17 Behavioral and governance red flags

The consolidated list. Each points to the section with its source and CHECK.

| RED FLAG | Section |
|---|---|
| One person decides, moves cash and reports | 0.4 |
| Returns smooth relative to the stated strategy, at any level; fixed "distribution rate" on an illiquid fund | 0.4, 0.13 |
| Repeated optimistic forecast misses in the sponsor's or management's history | 0.2, 0.14 |
| Founder super-voting control without a sunset; board of celebrities with no domain experts | 0.2, 0.14 |
| Verbal numbers that differ from documents; refused or deflected questions | 0.2 |
| Manager's description of cash controls differs from the administrator's | 0.5 |
| Non-Big 4 or undersized auditor combined with internal pricing | 0.4, 0.13 |
| No accounting function, no employee census, customer assets off balance sheet | 0.4 |
| A single key holder (crypto) | 0.4 |
| Multiple financing providers each seeing only their own collateral | 0.4, 0.5 |
| Period-end balances that differ from intra-quarter averages | 0.4 |
| "X and Y are already in" offered as diligence | 0.4, 0.12 |
| Small, explained-away irregularities (late audit, restatement, unbooked rebate) | 0.4 |
| Wire instructions or principal instructions received only by message | 0.4 |
| Seller-imposed deadline; competitive round used to cut the diligence floor | 0.1 |
| Lead investor cannot state hours, sites and references | 0.1 |
| Investment case resting on pitch delivery rather than the data room | 0.12 |
| Terms of art no one in the approval chain can restate with a number | 0.12 |
| Risk limits raised to fit positions; CRO replaced by a dealmaker | 0.12 |
| Deal champion also runs the valuation | 0.1, 0.12 |
| Sponsor deal pace doubling without the operating bench | 0.2 |
| Track record compounded, gross-only, cherry-picked, or attributed to people who have left | 0.13 |
| Successor fund far larger than the funds that earned the record | 0.13 |
| Non-functional or discouraged whistleblower hotline | 0.15 |
| Unaudited fund | 0.15 |
| Valuations prepared by the principal while an "independent expert" is claimed | 0.6 |
| Complex illiquid product sold to retail; heavy deployment pressure | 0.10 |
| Single uninsured bank; cash in pooled vehicles that can gate | 0.11 |
| "Proprietary deal" no one can corroborate | 0.1 |
| Strategic investor with a financing veto | 0.16 |

Behavioral base rate: 84% of fraud perpetrators displayed at least one behavioral red flag (ACFE 2026). Fraud is usually collusive: diligence the inner circle (0.2).

## 0.18 Regulatory status as of November 2026

What changed, and what it means for a data room. Re-check every line at signing.

| Item | Status (Nov. 2026) | What it means for diligence | Source |
|---|---|---|---|
| SEC Private Fund Adviser rules (Aug. 2023: quarterly statements, audit, restricted activities, adviser-led secondaries fairness opinion, preferential treatment) | Vacated in full by the Fifth Circuit, June 5, 2024 (National Association of Private Fund Managers v. SEC, No. 23-60471) | No federal rule requires a quarterly fee/performance statement, a fund audit beyond the Custody Rule's audit option, or a fairness opinion on a GP-led secondary. Contract for them in the LPA or side letter | Mofo, https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules; Paul Weiss, https://www.paulweiss.com/insights/client-memos/fifth-circuit-vacates-private-fund-adviser-rule |
| FinCEN Investment Adviser AML/CFT Rule (31 CFR Part 1032) | Compliance date postponed from Jan. 1, 2026 to Jan. 1, 2028; scope to be revisited; SEC/FinCEN adviser CIP proposal not final | Advisers have no federal AML program or SAR obligation until 2028. Ask who runs investor KYC and whether anyone files SARs | FinCEN, https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028; Federal Register, https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf |
| Corporate Transparency Act BOI reporting | Domestic companies and US persons permanently exempt (interim rule Mar. 26, 2025; final rule effective Aug. 14, 2026); only foreign registered companies report (about 28,000); previously filed US-person BOI to be deleted | No federal BOI record for US counterparties. Collect and verify ownership yourself | Mayer Brown, Aug. 20, 2026 (URL in 0.3); Federal Register 2026-16576 |
| FinCEN CDD Rule (31 CFR 1010.230) | Unchanged | 25% / control-person collection by covered financial institutions continues | 31 CFR 1010.230 |
| Rule 506(c) verification | SEC staff no-action relief (Mar. 12, 2025): minimum investment of $200,000 (natural persons) or $1,000,000 (entities), cash, not third-party financed, plus written representation, can be "reasonable steps" | High minimums are not a red flag alone; verify source of cash | General lane; letter citation WEAK until confirmed |
| OFAC 50 Percent Rule; Framework for OFAC Compliance Commitments (May 2019) | In force | Screen ownership chains and crypto addresses, not only names | OFAC, https://ofac.treasury.gov/ (document links WEAK until confirmed) |
| SEC crypto enforcement | SEC dismissed its civil action against Coinbase, Feb. 27, 2025, "not a judgment on the merits," to pursue rulemaking via its Crypto Task Force | Absence of an SEC case is not evidence of compliance; rely on custody, audit and on-chain verification | SEC 2025-47, https://www.sec.gov/newsroom/press-releases/2025-47 |
| GENIUS Act (2025), payment stablecoins | Enacted: 1:1 HQLA reserves, held for holders, audited, no lending, pledging or rehypothecation | Offshore or unregulated coins that cannot show this are a different, higher risk class | Circle FY2025 annual report (URL in 0.11) |
| Cannabis scheduling | DEA partial final rule (signed Apr. 22, published Apr. 28, 2026; challenges pending in the D.C. Circuit) moved FDA-approved marijuana products and marijuana under a qualifying state medical license to Schedule III; adult-use remains Schedule I; broader rescheduling went to a DEA ALJ hearing (June 29 to July 15, 2026), decision pending. No IRS 280E guidance located | "Cannabis is now Schedule III" is wrong for adult-use. Model full 280E as the downside; do not underwrite prior-year refunds | Federal Register, https://govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08176.htm; DOJ, https://www.justice.gov/opa/pr/justice-department-places-fda-approved-marijuana-products-and-products-containing-marijuana; Morgan Lewis, Sept. 2026 |
| One Big Beautiful Bill Act (July 2025) | Largely repealed IRA clean-electricity credits; REPEAT estimates about 29 GW less solar and 43 GW less wind through 2030 (approximate, not peer reviewed) | Tax counsel to confirm begin-construction and placed-in-service deadlines, FEOC restrictions and safe-harbor evidence; no-credit downside case | REPEAT, https://zenodo.org/records/15801701 |
| Retail access to private markets | 2025 executive order directed SEC and DOL to open 401(k) plans to private assets | Expect more semi-liquid vehicles; read gates, valuation frequency and fee layers (0.10, 0.11) | HLS Forum 2026 (URL in 0.10) |
| ILPA Reporting and Performance Templates (industry standard) | Published 2025; Reporting Template applies to funds in their investment period in Q1 2026 or launched on or after Jan. 1, 2026 | Ask for the Performance Template (with and without sub lines) for every prior fund | ILPA (URL in 0.13) |
| NVCA Model Legal Documents (industry standard) | Core financing set updated November 2026 | Diligence against the version in force at signing | https://nvca.org/model-legal-documents/ |
| CRE workouts | Interagency Policy Statement on Prudent CRE Loan Accommodations and Workouts (June 29, 2023; 88 FR 43115) replaced the 2009 statement | Ask whether each serial extension was a documented workout or deferred loss recognition | Fed SR 23-5, https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm |
| Leveraged lending | SR 13-3 (2013) remains the reference; 6x total leverage raises supervisory concern for most industries; 4.0x total / 3.0x senior is a common definition of "leveraged," not a cap (wording WEAK until checked against the letter) | Cite the primary, not intermediaries | https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm |
| HUD multifamily loan sizing | Mortgagee Letter 2025-03 (Jan. 8, 2025): 221(d)(4) market-rate new construction max 87% LTC (from 85%), min DSCR 1.15x (from 1.176x); affordable 90% at 1.11x | Insured-program ceilings, not private norms | HUD, https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf |
| GPB Capital founder | Sentence commuted late Nov. 2025 after 12 days served; conviction stands | Clemency does not change the diligence lesson; check the record, not the headline | NBC News (URL in 0.4) |

## 0.19 Physical-climate, water and insurability risk

A universal screen for long-lived real assets (real estate, infrastructure, agriculture, data centers). Detail lives in Chapters 1 and 6.

- Insurability is a diligence gate. In parts of California wildfire coverage is unavailable, and banks will not lend against uninsurable property, leaving cash-only buyers and lower values; in property-tax states falling values erode the municipal revenue base (Yale Insights, "Putting a Price on Climate Risk," https://insights.som.yale.edu/insights/putting-price-on-climate-risk). CHECK: obtain bindable insurance quotes (not indications) for the full hold, and stress a 2x premium. Flag any asset whose coverage depends on a state insurer of last resort. Premium repricing mirrors climate risk (Keys and Mulder, NBER w32579, https://www.nber.org/papers/w32579).
- Water certainty underpins Sun Belt development. The 1922 Colorado River Compact allocates 16.5M acre-feet a year, but 2000 to 2023 flows averaged about 12.5M (a structural deficit of about 4M a year); Lakes Mead and Powell are at about one-third of their 2000 levels, and further flow declines of 20% to 30% are projected (Cort, "The Colorado River Is Overdrawn," Yale Insights, May 2026, https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent). About 80% of Colorado River allocations go to agriculture. CHECK: for Phoenix, Las Vegas and Denver Front Range development and data centers, confirm the will-serve letter, water source and seniority (senior against junior rights), and cooling design; stress water cost at post-2026 tiered pricing. Water rights carried as permanent assets with no impairment for junior priority are a red flag.
- Grid-event exposure. ERCOT, Winter Storm Uri (Feb. 2021): about 30 GW of capacity missing against average non-summer load of about 45 GW; prices at the $9,000/MWh cap; losses estimated at about $140B (Hirs, "Why the Texas Power Market Failed," Yale Insights, https://insights.som.yale.edu/insights/why-the-texas-power-market-failed). CHECK: firm fuel, winterization, and scarcity-event modelling for any asset whose operations depend on the grid. Detail in Chapter 6.
- Rate sensitivity of long-duration assets: run +200 bp on debt and discount rate (Cheema-Fox et al., HBS WP 26-096, 0.7).

## 0.20 Policy and appropriation risk

Where a deal's cash flow depends on a government decision, the decision is a counterparty.

- Government tenancy carries termination-for-policy risk. DOGE listed 793 federal leases (about 9M sq ft) for cancellation in 2025; 384 were still listed by August 2025. GSA leases average 14 years against 5 to 10 for private tenants; early-termination options are typically exercisable after year 5 on 90 to 120 days' notice and were historically almost never used. In D.C. buildings with listed leases, landlord NOI fell 5% and junk-rated CMBS fell about 4% more than comparable GSA-backed bonds; Barclays put CMBS tied to government-leased buildings at about $12B (LaPoint and Choi, via Yale Insights, https://insights.som.yale.edu/insights/doges-lease-cancellations-are-already-hitting-the-commercial-real-estate-market). CHECK: read every government lease for ETOs and termination-for-convenience rights, model exercise on first date, and cap single-agency share of NOI.
- Legislative sweeps. In 2018 the Connecticut legislature redirected a substantial part of the Connecticut Green Bank's revenue to the general fund (Yale SOM case, "Connecticut Green Bank 2018," https://cases.som.yale.edu/connecticut-green-bank-2018). CHECK: where a program depends on a state green bank, a ratepayer charge or an appropriation, confirm whether the funds can legally be swept, and model their loss.
- Concession renegotiation is the norm. In about 1,000 Latin American concessions, 54% of transport and 74% of water contracts were renegotiated; Mexico's late-1980s toll-road concessions cost taxpayers over $8B (Gomez-Ibanez, Regulating Infrastructure, Harvard UP 2003, https://www.hks.harvard.edu/publications/regulating-infrastructure-monopoly-contracts-and-discretion; World Bank, https://documents1.worldbank.org/curated/en/678041468765605224/pdf/288160PAPER0Granting010renegotiating.pdf). CHECK: diligence counterparty political turnover, whether the tariff-adjustment mechanism has actually been honored, and termination compensation.
- Tax-credit dependence. OBBBA (July 2025) largely repealed IRA clean-electricity credits (0.18). CHECK: a no-credit downside case for any deal whose returns rely on 45Y, 48E or 45X credits or transferability.
- Ratepayer backlash. Data centers explained about 16% of industrial and 4% of residential price increases across 385 data centers and 42 utilities (2020 to 2025) (HBS WK, https://library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple); a 20% residential bill increase in parts of New Jersey became a 2025 governor's-race issue (Crosier, Onghai and Sircar, arXiv 2609.08166, https://arxiv.org/abs/2609.08166). CHECK: large-load tariff and cost-allocation rules, pending rate cases, and local moratorium risk. Detail in Chapter 6.
- Market-design risk: ERCOT generators had been urged to winterize after 2011 but were not paid to, and ERCOT had no enforcement power (Hirs, Yale Insights).

# 1 Real Estate

*Construction loans, bridge loans, development, syndications, note purchases, and real estate funds.*

Sub-playbooks: small construction loans ($1M to $2M), bridge loans, ground-up development, value-add, multifamily, commercial, office (including conversion), land and entitlement, hospitality, industrial, single-family rental and DSCR loans, equity syndications and JVs, note and loan-portfolio purchases, and real estate funds. Fund-level terms (LPA, fees, evergreen and NAV REIT liquidity, NAV lending) sit in Chapter 10 and the new funds chapters; this chapter cross-references them.

**THE ONE CHECK.** Re-underwrite the takeout yourself: at today's coupon (or the agency underwriting floor rate, whichever is higher), on leases in place, after a recurring capex reserve, at a value 30% below the current mark. If the refinance or sale does not repay the loan, name who writes the check for the gap and prove they have the cash.

## 1.1 How it works

- **Debt deals.** The lender advances against collateral. The borrower pays interest, often interest-only for bridge and construction. Repayment comes at sale or refinance (the takeout). Construction loans fund through draws tied to completed work.
- **Equity and syndication.** The sponsor (GP) raises LP equity, buys or builds, operates, and distributes cash flow and sale proceeds through a waterfall, usually after a preferred return and a promote.
- **Non-recourse debt is a put the lender writes.** The borrower's right to hand back the keys on a non-recourse loan is an option. In a competitive lending boom every lender rationally underprices it, and asset prices inflate (Pavlov and Wachter, Zell/Lurie working papers, https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/). Diligence on either side of the loan prices that put.
- **Lending terms move with the cycle, not just prices.** Advance rates and margins are a state variable: average margins on mortgage securities fell to about 10% from late 2005 to 2007, then jumped above 40% in late 2007 (Geanakoplos, "The Leverage Cycle," Cowles DP 1715 / NBER Macro Annual 2009, https://cowles.yale.edu/sites/default/files/2022-08/d1715.pdf). The takeout is underwritten in today's regime and executed in tomorrow's.
- **Short balloons are the historical norm in crises.** In the 1920s typical home loans were 60% LTV with roughly five-year balloons; the 30-year self-amortizing loan only became standard in the 1950s (Shiller, Yale ECON 252 lecture 12, https://oyc.yale.edu/economics/econ-252-08/lecture-12). Every bridge and construction loan is a balloon. Treat the refinance as the risk, not a formality.
- **Who lends matters.** Regional banks hold almost a third of US commercial mortgage dollars (over $1.6T) and are the lenders most likely to extend rather than enforce (Hinzen, Severino and Van Nieuwerburgh, "Too-Many-to-Ignore: Regional Banks and CRE Risks," Oct 2025, Wharton-hosted WFFI paper, https://wffi.wharton.upenn.edu/wp-content/uploads/2025/10/HSVRegional-Banks-and-CRE-Risks.pdf). See 1.11.

## 1.2 Regulatory anchor: supervisory LTV limits

These are bank supervisory ceilings under 12 CFR Part 34 / 365 (Interagency Guidelines for Real Estate Lending Policies). Private lenders vary, but these are the reference points.

| Loan category | Supervisory LTV ceiling |
|---|---|
| Raw land | 65% |
| Land development | 75% |
| Commercial / multifamily construction | 80% |
| 1-4 family residential construction | 85% |
| Improved property | 85% |

*FIGURE 3 Supervisory loan-to-value ceilings by property type (12 CFR Part 365, Appendix A).* Source: eCFR 12 CFR Part 365 Appendix A; FDIC; Fed SR 93-33. For multi-phase projects the limit applies to the final phase. Aggregate loans above these limits should not exceed 100% of a bank's total capital.

**Federal insured-program ceilings (the outer bound, not the norm).** HUD Mortgagee Letter 2025-03 (Jan 8, 2025) raised the Section 221(d)(4) market-rate new-construction maximum from 85% to 87% loan-to-cost and cut the minimum DSCR from 1.176x to 1.15x (7% vacancy factor). The same loosening applies to 223(f) acquisition and refinance. Affordable 221(d)(4) and 223(f) went to 90% LTC/LTV at 1.11x. These are government-insured, 40-year, fully amortizing, non-recourse loans. A private construction lender at or above these levels is lending at an insured-program ceiling without the insurance. Verify the current mortgagee letter before use: HUD issued further letters in 2025–26 (e.g. Middle Income Housing, ML 2025-02 / 2026-01) (HUD ML 2025-03, https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf; Nixon Peabody, Jan 14 2025, https://www.nixonpeabody.com/insights/alerts/2025/01/14/hud-adopts-relaxed-loan-sizing-standards-for-fha-insured-loans; HUD 2010 ML on Criterion 5 DSCR history, https://www.hud.gov/sites/documents/10-11hsgn.pdf).

**Agency takeout standards.** Fannie Mae multifamily DSCR and LTV are set in Form 4660 (Multifamily Underwriting Standards), tiered Tier 1 to 4. The Guide requires a Key Principal non-recourse guaranty on any fixed-rate loan underwritten below 1.35x DSCR, and underwritten debt service uses the HIGHER of the note rate or Fannie's underwriting rate floor (Fannie Mae Multifamily Selling and Servicing Guide, Sec. 203.02 and 311, https://mfguide.fanniemae.com/fnmf-pdf/download/9906).

**Workouts and extensions: the 2023 interagency standard.** The June 29, 2023 interagency Policy Statement on Prudent Commercial Real Estate Loan Accommodations and Workouts (OCC, Fed, FDIC, NCUA; 88 FR 43115) replaced the 2009 workout statement and added a section on short-term accommodations. Use it as the reference for what a "prudent" extend-and-amend looks like. When a sponsor's track record shows serial extensions, ask whether each was a documented workout under this framework or simply deferred loss recognition (Federal Reserve SR 23-5, https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm; FDIC FIL-34-2023, https://fdic.gov/news/financial-institution-letters/2023/fil23034.html; Federal Register, https://www.govinfo.gov/content/pkg/FR-2023-07-06/html/2023-14247.htm).

**Bank CRE concentration threshold.** CRE loans above 300% of total capital is the supervisory-attention threshold. The median regional bank runs about 312%; 54.8% of regional banks exceed 300%, up from 37.7% in 2015; outliers (NYCB/Flagstar) were above 500% (HSV 2025, URL above). Relevant whenever a bank is your lender, co-lender, A-note holder, or note seller (1.11).

## 1.3 Data room index

SPONSOR AND ENTITY
- Org chart, formation documents, operating agreement, good standing.
- Sponsor track record schedule: every prior deal, with outcomes. References.
- For every prior deal: original pro forma against actual results (forecast-miss history; see 0.2), every loan extension, modification, and workout, and whether each was documented under the 2023 interagency workout framework.
- Background and credit checks on principals and guarantors, and on the whole placement chain: COO, managing partners, sales agents (Drive Planning, 1.8).
- Schedule of every affiliate fee: acquisition, development, construction management, property management, leasing, refinancing, disposition. LPAC or investor approvals for each related-party arrangement (HLS Forum, SEC private fund deficiencies, 2022, https://corpgov.law.harvard.edu/2022/02/17/sec-identifies-private-fund-deficiencies-signifying-increased-industry-scrutiny/).

PROPERTY
- PSA, title commitment, ALTA survey.
- Current rent roll. T-12 and trailing-36 operating statements.
- Leases and estoppels. Service contracts.
- Lease expiry schedule by year, set against the loan maturity date (Gyourko, 1.11).
- Every government and anchor lease with its early-termination options (ETOs), termination-for-convenience rights, notice periods, and first exercise dates (LaPoint and Choi, via Yale Insights, https://insights.som.yale.edu/insights/doges-lease-cancellations-are-already-hitting-the-commercial-real-estate-market).
- MAI appraisal with prospective "as-complete" and "as-stabilized" values. The appraisal's cap rate stated as NOI- or cash-flow-based, current- or forward-year (1.12).
- Recurring capex history and reserve (actual spend, not budget), and a capex backlog estimate where value is below replacement cost.
- Environmental Phase I (Phase II if triggered).
- Property condition or engineering report.
- Zoning, entitlements, permits, certificate of occupancy.
- Insurance: property, liability, builder's risk, flood. Three-year premium history, a current bound quote (not an indication) at closing, deductibles, and named-storm, wind, and wildfire terms. Note any coverage that depends on a state insurer of last resort (1.13).
- Tax bills, and the municipality's revenue base where a property-tax spiral is possible (1.13).
- Water: will-serve letter, water source and seniority of rights for Sun Belt development (1.13).

CONSTRUCTION AND DEVELOPMENT
- Full project budget with hard and soft cost lines and contingency.
- GMP or fixed-price construction contract. Contractor qualifications and bonding.
- Draw schedule and sources-and-uses.
- Architect and engineer contracts and plans.
- Pro forma with absorption and lease-up.
- Entitlement timeline and fees, budgeted explicitly.
- For conversions: a costed per-square-foot conversion estimate and residential rent comps (1.4).
- Construction lender's identity, funding mix, and the draw-commitment survival terms if the lender fails (replacement lender, assignment rights) (First Republic, 1.8).
- Off-site dependencies (transit, utilities, infrastructure) and who funds each (Canary Wharf, 1.8).

FINANCIAL
- Debt terms, existing financing, payoff letters.
- Full amendment, extension, and forbearance history on existing debt.
- Underwriting model.
- Sponsor co-invest proof and liquidity. Verify the funds.
- Fund-level reserves and fund-level debt, not just asset-level (GGP, 1.8).

NOTE AND LOAN PURCHASES (added)
- Loan tape with current collateral values, not origination values.
- Payment history traced to bank deposits.
- Modification, extension, and forbearance history for each loan.
- County mortgage and deed records used to rebuild the seller's portfolio and LTVs where the seller discloses little (HSV 2025).

## 1.4 Diligence checklist by workstream

FINANCIAL
- Rebuild the pro forma. Do not accept sponsor NOI.
- Verify the rent roll against actual leases and bank deposits.
- **Underwrite on cash flow after recurring capex, not NOI.** NOI-based and cash-flow-based cap rates differ by the recurring capex reserve. Recurring capex as a share of NOI (NCREIF history): about 16% to 18% for institutional apartments (17% used), 31% industrial, 33% office, 36% retail. CHECK: ask whether the sponsor's cap rate is on NOI or cash flow, and current-year or next-year income. Apply the reserve before comparing (Linneman, "What Should Stabilized Multifamily Cap Rates Be?," Zell/Lurie WP 519, c. 2005, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf; reserve ratios are historical, use them as a method).
- **DSCR on leases in place only.** Never size debt on anticipated leases or market rent (the 2005–07 "pro forma" loan; 1.14).
- Check the exit cap assumption against the current market. An aggressive exit cap is the most common equity-killer. CHECK: run the Linneman framework rate and the REIT-implied cap for the same property type (1.12).
- **Do not underwrite real appreciation.** Shiller's index back to 1890 shows little long-run trend in real US home prices outside booms; similar series for Norway and the Netherlands agree, and real construction costs were flat or falling. Default to inflation-only growth unless a specific supply constraint is documented (Shiller, ECON 252 lecture 12, https://oyc.yale.edu/economics/econ-252-08/lecture-12).
- **Refinance gap.** For any loan maturing within 48 months, re-underwrite at the current market rate. Size the gap (new proceeds at the market DSCR minus the payoff) and name who funds it (Metrick, "Is Commercial Real Estate in for a Downturn... or a Crisis?," Yale Insights, Dec 2023, https://insights.som.yale.edu/insights/is-commercial-real-estate-in-for-downturnor-crisis).
- **Takeout sizing at the agency floor.** Size the takeout at the agency underwriting floor rate, not the current coupon. A bridge loan underwritten to exit at 1.25x on today's rate can fail at the agency floor. CHECK: ask which Fannie Mae tier the stabilized asset would size to at the floor rate (Fannie Mae Guide, Sec. 203.02 and 311, URL in 1.2).
- Confirm the construction budget has sufficient funds for completion. Approving a loan to finance partial construction without committed completion funds is a flagged unsafe practice (OCC Comptroller's Handbook, Commercial Real Estate Lending, https://occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-real-estate-lending/pub-ch-commercial-real-estate-previous.pdf).
- Developer profit should be funded only by sales, by construction loan funds upon completion and lease-up, or by subsequent term financing (OCC, same).
- **Income verification for residential credit, DSCR, and single-family rental deals.** Never underwrite borrower- or tenant-stated income. In 2002–05, in low-credit-score zip codes, mortgage-application income growth decoupled from IRS income growth; in the 18 zip codes rated most fraud-plagued, application income ran about 90% above average IRS income, and those zip codes later had the highest defaults. CHECK: IRS transcripts (Form 4506-C), payroll records, or bank-deposit verification on a statistically meaningful sample of the tape. Compare pool income growth with local IRS SOI income growth. Stated income growing faster than local IRS income is a fraud signal, not a credit improvement (Mian and Sufi, RFS 2017, NBER w20947, https://www.nber.org/papers/w20947; Princeton SPIA summary, https://spia.princeton.edu/news/how-income-fraud-made-housing-bubble-worse).
- **Affiliate fee trace.** Obtain the schedule of all affiliate fees and LPAC approvals. Real estate sponsors draw the same SEC exam findings as PE sponsors: unauthorized fees, no step-down after write-downs, extensions without consent, related-party property management or construction fees without LPAC consent (HLS Forum, 2022, URL in 1.3).

COMMERCIAL AND MARKET
- Independent sales and rent comps.
- Submarket vacancy and absorption.
- **Who set the comps, and how were they financed?** Cheap credit lets a small optimistic minority set the marginal price: after the 2003 surge in private-label securitization, transaction volume in exposed zip codes was driven almost entirely by a small group of speculators (repeat buyers, under about 1.5% of the population), followed by an amplified boom and bust. CHECK: ask what share of recent comparable sales were to investors or repeat buyers and how they were financed. If comps were set by levered investors financed by a lender class that has since pulled back (non-bank, private-label), the comp is not a durable value (Mian and Sufi, "Credit Supply and Housing Speculation," RFS 2022, NBER w24823, https://www.nber.org/papers/w24823).
- **Office: treat work-from-home as a permanent obsolescence shock.** Gyourko expects average attendance of 1 to 2 days a week, implying a 20% to 40% fall in office demand; elsewhere he estimates 15% to 20% (both positions stand; use the range). Class B vacancy typically runs 15% to 20%, some buildings above 30%. Some offices have traded at 25% to 50% of their pre-pandemic purchase price. Because office leases run 5 to 10 years, failure arrives at each lease expiry. CHECK: line up lease expiry against loan maturity and test the takeout on post-rollover occupancy for Class B. Do not assume historical occupancy. **WEAK** (podcast-sourced) (KaW Ripple Effect podcast, "Next Crisis: Empty Office Buildings | Joe Gyourko," May 14 2024, https://knowledge.wharton.upenn.edu/podcast/ripple-effect/next-crisis-empty-office-buildings-joe-gyourko/).
- **Office-to-residential conversion: verify the conversion math.** Gyourko cites conversion costs of about $300/sf in Philadelphia and about $500 to $600/sf in New York, where top Manhattan rents reach about $8/sf a month. He expects no more than about five conversions in Philadelphia this cycle; most failing Class B buildings are more likely demolished and replaced over the next decade. CHECK: a conversion plan needs a real cost per sf, residential rents that support it, and a basis low enough after the write-down. "Conversion optionality" is not a value floor. **WEAK** (podcast-sourced) (same podcast; related KaW coverage, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-going-to-happen-to-all-those-empty-office-buildings/).
- **Government tenancy is not credit-risk-free.** It carries termination-for-policy risk (1.8 GSA case file). CHECK: read every government lease for ETOs and termination-for-convenience rights, model the exercise case, and cap single-agency share of NOI (LaPoint and Choi, Yale Insights, URL in 1.3).
- **Single-infrastructure dependency.** Identify any single transport link, anchor-tenant sector, or public approval the value depends on, and run the "link delayed" case (Yale SOM case, "Canary Wharf: Financing and Placemaking," https://cases.som.yale.edu/canary-wharf).
- **Credit-cycle overlay.** For housing and consumer-demand-driven assets, record the 3-year change in household debt to GDP for the market (BIS / Fed Z.1). If it is in the top third of history, run a downside with revenue growth 2 points lower for 3 years: a one-standard-deviation rise (6.2 points over three years) predicts 2.1 points lower GDP growth over the next three (Mian, Sufi and Verner, QJE 2017, NBER w21581, https://www.nber.org/papers/w21581). Full overlay in Chapter 0.

LEGAL AND TITLE
- Title commitment, lien search, UCC, judgments.
- Survey review for encroachments and easements.
- Confirm zoning and entitlement independently with the municipality.
- **Entitlement cost.** Local land-use rules can raise the cost of a developed single-family lot by about 35% (Charlotte case study). CHECK: budget entitlement time and fees explicitly (Crosland, Zell/Lurie WP 659, via the realestate.wharton.upenn.edu working-paper index).
- **Foreclosure regime is a collateral variable.** In 21 US states a lender must sue in court before a foreclosure sale (judicial foreclosure). Non-judicial states were about twice as likely to foreclose on delinquent owners; moving from median to 90th-percentile foreclosure intensity was associated with about 9% lower house price growth (2007–09). CHECK: model time-to-recovery and carry by state (judicial states run materially longer, with legal cost and property deterioration during the delay), and model local price pressure when the collateral pool is geographically clustered (Mian, Sufi and Trebbi, JF 2015, NBER w16685, https://www.nber.org/papers/w16685).
- **Confirm every claimed LP interest and property.** Check claimed LP interests against the entity's own records and the county recorder (LeFever Mattson, 1.8).

CONSTRUCTION AND TECHNICAL
- Independent review of plans, budget, and schedule.
- Confirm GC bonding and insurance.
- Draw disbursement commensurate with improvements as of the inspection date (OCC).
- **Below replacement cost means deferred maintenance.** Owner-occupied homes worth less than construction cost spend about 50% less on renovation than comparable homes; land is about 30% of the value of the US housing stock. CHECK: on any asset trading below replacement cost, assume deferred maintenance and get a property condition report with a capex backlog estimate (Gyourko and Saiz, Zell/Lurie WP 407, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/407.pdf).

INSURANCE AND ENVIRONMENTAL
- Phase I ESA.
- Builder's risk and flood coverage for construction.
- **Underwrite the insurance reset, not last year's bill.** See 1.13 for the numbers. CHECK: three-year premium history, a current bound quote at closing, deductible and named-storm or wildfire terms; stress insurance expense in catastrophe-exposed markets (2x premium as the floor stress) and stress exit value for capitalization of higher premiums (Keys and Mulder, NBER w32579, https://www.nber.org/papers/w32579; Yale Insights, "Putting a Price on Climate Risk," https://insights.som.yale.edu/insights/putting-price-on-climate-risk).
- **Water certainty** for Phoenix, Las Vegas, and Denver Front Range development (1.13).

LENDER AND COUNTERPARTY (new workstream)
- Identify the construction or bridge lender, its funding mix, and its CRE concentration. Confirm the draw commitment survives a lender failure (First Republic, 1.8).
- When buying a property or note from a bank, or partnering with one, assume the existing loan has been extended to delay loss recognition. Re-mark it (HSV 2025; 1.11).

MANAGEMENT AND BACKGROUND
- Guarantor financial statements and liquidity verification. Recourse is only as good as the guarantor.
- Sponsor forecast-miss history: past projections against actual results on every prior deal. Repeated optimistic misses are a fraud precursor (Schrand and Zechman, JAE 2012; see 0.2).
- Background-check the second tier: COO, managing partners, and sales agents, not just the named principal (Drive Planning, 1.8).

## 1.5 The numbers

| Metric | Cited range | Strength |
|---|---|---|
| DSCR, stabilized income property | 1.20x to 1.35x minimum | Practitioner standard; corroborate per deal. Agency anchors: Fannie requires a Key Principal non-recourse guaranty on fixed-rate loans underwritten below 1.35x, with debt service at the higher of note rate or Fannie's underwriting floor (Fannie Mae Guide Sec. 203.02, 311). HUD 221(d)(4)/223(f) minimum 1.15x market-rate, 1.11x affordable (HUD ML 2025-03). Federal insured minimums are the floor, not the private norm |
| DSCR basis | Leases in place only, after a recurring capex reserve of about 17% (MF) to 36% (retail) of NOI | Levitin and Wachter 2013; Linneman WP 519 (c. 2005 reserve ratios) |
| Loan-to-cost, construction | 70% to 80% of total project cost | Consistent with sitting under both the 80% supervisory LTV ceiling for commercial/multifamily construction (12 CFR 365) and the HUD 221(d)(4) insured ceiling of 87% market-rate / 90% affordable (HUD ML 2025-03, Jan 2025). Ceiling resolved; the private norm by deal size remains **WEAK** until confirmed per lender |
| Preferred return | 6% to 9%, then promote to GP | Practitioner. **WEAK**: promote terms by deal size unresolved by any lane (HBS: Lietz frameworks not public). Verify per deal |
| RE fund fee benchmark | 1% to 2% of committed capital plus 20% promote; sponsor co-invest 2% to 25% | Linneman and Ross, KaW, Jul 31 2002 (dated: use as a reference, not a current market level) |
| Construction and bridge sizing | To as-complete value and takeout DSCR | Practitioner; test the takeout at the agency floor rate (1.4) |
| Stabilized NOI cap rate, multifamily, framework | 10-yr UST + risk premium (A ~210 bp, B ~260 bp, C ~350 bp), less g ~2%, grossed up for d = 17% capex | Linneman WP 519 (c. 2005; method, not levels). See 1.12 |
| REIT-implied vs appraisal cap gap | Nareit REIT-implied 5.74% against NCREIF ODCE appraisal 4.47%, Q2 2026: 127 bp | Nareit, context cited in the Wharton lane (non-Wharton). See 1.12 |
| CRE value-decline stress | 30% from current marks (Fed adverse, used in regional-bank CRE stress work); 40% (Fed 2024 severely adverse) | Hinzen, Severino and Van Nieuwerburgh, Oct 2025 (WFFI). Both figures stand; run 30% as base stress and 40% as severe |
| Foreclosure deadweight | About 5%, plus distressed-sale discounts of 20% to 30%; transfer taxes often paid twice | HSV 2025 |
| Latent distress vs reported delinquency | About 4 to 1 (loans with current LTV above 95% re-marked on location-by-property-type indices) | HSV 2025 |
| Historical CMBS delinquency | 30-day: under 2% pre-2008, about 9% in 2011, about 5% in 2014. CRE loan delinquency doubled to 7% by mid-2009 (Fed). Special servicer transfer at about 60 days delinquent | Zell/Lurie WRER CMBS papers, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/730.pdf; KaW podcast "On Shaky Ground," Jul 22 2009 (**WEAK** for the podcast figure) |
| Office value decline | About 30% (Metrick, late 2023); some trades at 25% to 50% of pre-pandemic purchase price (Gyourko, 2024) | Metrick, Yale Insights Dec 2023; Gyourko KaW podcast May 2024 (**WEAK**, podcast). Two measures, not a conflict: an average decline and the tail of individual trades |
| Office refinancing wall | About two-thirds of office CRE debt needed refinancing within about four years (late 2023); many legacy coupons near 1% against market near 7% | Metrick, Yale Insights Dec 2023 |
| Insurance reset | Average homeowners premiums +33% 2020–23 ($1,902 to $2,530); Florida +90% and Texas +50% by 2023 vs 2018; reinsurance costs roughly doubled 2017–23 | Keys and Mulder, NBER w32579 (residential data; same reinsurance channel prices commercial cover) |
| Private RE fund performance | No risk-adjusted outperformance for US public pensions, measured against their own portfolios (1995–2018) | Korteweg, Panageas and Systla, HLS Forum 2025, https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/ |

- **Fund-return claims need a public comparison.** Treat value-add and opportunistic RE fund return claims as needing a levered public-REIT comparison. Appraisal-based marks smooth volatility; low reported volatility is an accounting artifact, not diversification (Stafford, RFS 2022, https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting; see Chapter 10).

STRESS CASES TO RUN ON EVERY MODEL (Figure 4, now five cases)

| Exit cap | Cost overrun | Lease-up delay | Rates | Value decline (new) |
|---|---|---|---|---|
| +50 to +100 bps | +10% to +20% | 6 to 12 months | Interest rate shock: re-underwrite at current market rate and at the agency underwriting floor | -30% from current marks (-40% severe), plus about 5% foreclosure deadweight and 20% to 30% distressed-sale discount; recompute LTV and lender loss at loan level |

*FIGURE 4 The five standard real estate stress cases.* Add where relevant: insurance at 2x premium (1.13); every government or anchor ETO exercised on first date (1.8); advance-rate and margin cut at refinance (leverage cycle, 1.14); lender failure mid-draw (1.8).

## 1.6 Third parties

- MAI appraiser, with prospective values for construction. Ask the appraiser to state the cap rate basis (NOI or cash flow, current or forward).
- Phase I environmental consultant.
- Property condition or construction consultant, and an ongoing draw inspector. Capex backlog estimate on below-replacement-cost assets.
- Title company. Surveyor. Insurance broker (bound quotes, three-year premium history, cat-model view). Real estate counsel (judicial versus non-judicial foreclosure timing by state).
- Valuation firm or data provider able to re-mark loans with location-by-property-type price indices, for note and portfolio purchases (HSV 2025).
- Water-rights counsel or engineer for Sun Belt development (1.13).
- Background-check provider for the full placement chain.

## 1.7 Legal and structure

- Loan agreement, promissory note, mortgage or deed of trust.
- Assignment of rents and leases. UCC-1.
- Personal or corporate guaranty. Recourse versus non-recourse carve-outs ("bad boy" guaranties). Fannie requires a Key Principal non-recourse guaranty on fixed-rate loans underwritten below 1.35x (1.2).
- Title insurance (lender's policy), with endorsements and date-downs at each draw for construction.
- Intercreditor or subordination agreement if mezzanine is present.
- Construction loan assignment and replacement-lender provisions, so the draw commitment survives a lender failure (First Republic, 1.8).
- Foreclosure regime (judicial or non-judicial) by state, and its effect on recovery time and carry (Mian, Sufi and Trebbi 2015).
- Government and anchor leases: ETOs, termination for convenience, notice, and the lender's treatment of the termination case.
- For syndications: operating agreement, PPM, subscription documents, Reg D filing.
- **506(c) verification.** SEC staff no-action relief (Mar 12, 2025) lets a 506(c) issuer treat a high minimum investment (at least $200,000 for natural persons, $1,000,000 for entities), paid in cash and not third-party financed, plus a written representation, as "reasonable steps" to verify accredited status. A high minimum is no longer a red flag by itself, but it shifts the burden: verify the source of the cash. **WEAK** ([VERIFY] letter citation on sec.gov) (general lane; see 0.3).
- **Investor reporting standard to require in the operating agreement or LPA** (Linneman and Ross, KaW, "Towards Greater Transparency in Real Estate Private Equity Funds," Jul 31 2002, https://knowledge.wharton.upenn.edu/article/towards-greater-transparency-in-real-estate-private-equity-funds/):
  - Gross and net IRR, with fees, expenses, and carried interest shown.
  - For each asset: debt level, ownership percentage, and loan-covenant compliance, including partnership-level ventures.
  - Assets grouped as sold, stabilized (ahead of, on, or below underwriting), or non-stabilized.
  - Non-stabilized assets carried at cost and tested for impairment quarterly.
  - Asset-level cost, equity, reserves, debt, NOI, current value, IRR, and equity multiple.
  - 8-K-style notices for unusual events.
  - The same methods across all the sponsor's funds.
- Affiliate fees and LPAC consent mechanics for every related-party arrangement (HLS Forum 2022). The 2023 SEC Private Fund Adviser rules were vacated in June 2024, so quarterly statements and fee disclosure must be contracted for in the LPA or side letter (see Chapter 10).
- Fund-level vehicles (NAV REITs, evergreen RE funds, NAV facilities, subscription lines): see Chapter 10 and the NAV Lending chapter.

## 1.8 Failure modes and the check that catches each

| Case file | Year | What happened | THE CHECK |
|---|---|---|---|
| **Drive Planning** (land-development "bridge loan" Ponzi) | 2024; added charges Dec 30 2025 | Raised over $372M on "Real Estate Acceleration Loans" promising 10% per six months. New money paid old investors. In Dec 2025 the SEC also charged the former COO and a former managing partner, alleging they told investors the return was guaranteed and backed by collateral (SEC 2024-97, https://www.sec.gov/newsroom/press-releases/2024-97; SEC Lit. Rel. 26456, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26456; Bisnow, https://www.bisnow.com/national/news/commercial-real-estate/real-estate-firms-executives-hit-with-sec-charges-over-372m-ponzi-scheme-132575) | Proof of cash. Independent verification that loan proceeds funded the named projects. The guaranteed-return red flag. Background-check the whole placement chain: second-tier executives and sales agents are also defendants |
| **Wells Real Estate Investment** (fake portfolio and misappropriation) | 2024 | Claimed a $450M portfolio. Only about $11M of $56M raised was used to buy property (SEC, August 2024) | Independent title and asset confirmation of every claimed property |
| **Location Ventures** (Rishi Kapoor; understated costs inflating returns) | 2024 | A $93M fraud. Entities paid excessive fees, and higher returns were represented by understating cost estimates (SEC 2024-2, https://www.sec.gov/newsroom/press-releases/2024-2) | Independent construction budget review and a fee-flow trace |
| **First Liberty Building & Loan** (Georgia; bridge-loan Ponzi) | SEC Jul 10 2025 | At least $140M from about 300 investors via promissory notes and loan participations promising up to 18%, purportedly funding short-term business bridge loans "with few defaults." Most loans defaulted; from at least 2021 new money paid old investors; the founder allegedly spent $2.4M+ on credit cards and $335K on rare coins (SEC 2025-98, https://www.sec.gov/newsroom/press-releases/2025-98-sec-charges-georgia-based-first-liberty-building-loan-its-owner-operating-140-million-ponzi-scheme) | Loan-tape audit with borrower-level payment history traced to bank deposits. Any "few defaults" claim must be proven with a delinquency roll |
| **LeFever Mattson** (California; fake LP interests) | SEC May 22 2025 | Former CEO allegedly sold about 200 investors at least $46M of fake interests in real estate LPs and commingled funds (SEC 2025-76, https://www.sec.gov/newsroom/press-releases/2025-76-sec-charges-former-real-estate-investment-ceo-operating-multimillion-dollar-ponzi-scheme) | Confirm every claimed LP interest against the entity's own records and the county recorder for the property |
| **CMBS underwriting decay** | 2004–07 | See 1.14. IO share 47% to 86%; about $40B of "pro forma" loans sized on anticipated leases; flat stated LTVs while prices inflated | DSCR on in-place leases; amortization; compare underwritten metrics with a third party's stressed LTV and DSCR |
| **Underpriced non-recourse lending** | 1990s Asia; recurring | The walk-away put is underpriced in a competitive boom. Countries that curbed underpricing saw 30% to 40% value declines; those showing underpricing symptoms fell 80% or more. A 19-country study of 500+ REITs found deeper crashes where the put was underpriced (Pavlov and Wachter, https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/; https://realestate.wharton.upenn.edu/working-papers/real-estate-crashes-and-bank-lending/) | Lender-side red flag: spreads compressing while LTVs rise and recourse falls. Ask what the loan is worth if values fall 30% |
| **Canary Wharf / Olympia & York** | 1992 bankruptcy | A 14M sf project failed on a London property recession, competition from the City, poor transport links, few British tenants, complicated finances, and developer overconfidence. It succeeded only after the government linked it to the subway; it was built office-only. A new consortium took it out of bankruptcy in 1995; it went public in 1999 (Gordon, Zell/Lurie WP 418, https://realestate.wharton.upenn.edu/working-papers/the-crash-and-rebound-of-canary-wharf/; Yale SOM case, https://cases.som.yale.edu/canary-wharf) | Verify every off-site dependency (transit, infrastructure) and who funds it. Require pre-leasing. Map the full financing structure. Run the "link delayed" case. Discount the sponsor's conviction |
| **General Growth Properties** (refinancing wall) | 2009 | GGP filed after lenders refused to refinance $27B of debt. CRE maturities were estimated at $400B for 2009, growing past $1.8T by 2012. Wachter and Linneman named PE real estate funds, with thin reserves and short-term debt, as the most vulnerable owners. **WEAK** (podcast-sourced) (KaW podcast, "On Shaky Ground," Jul 22 2009, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/on-shaky-ground-commercial-real-estate-faces-financial-tremors/) | A maturity ladder against realistic refinance terms (rate, DSCR, proceeds at a stressed value). Count reserves at the fund level, not just the asset level |
| **2003–06 private-label mortgage boom** | 2003–09 | Credit expanded through non-core-deposit lenders; a small group of speculators set marginal prices; application income overstated up to about 90% above IRS income in the worst zip codes; then the bust (Mian and Sufi, NBER w24823, w20947) | Who set the comps and how were they financed; independent income verification; foreclosure-regime-adjusted recovery timing |
| **GSA-leased office and CMBS** | 2025 | DOGE listed 793 federal leases (about 9M sq ft) for cancellation; 384 were still listed by August 2025. GSA leases average 14 years against 5 to 10 for private tenants; ETOs typically exercisable after year 5 on 90 to 120 days' notice, historically almost never used. In D.C. buildings with listed leases, landlord NOI fell 5% and junk-rated CMBS fell about 4% more than comparable GSA-backed bonds, with spillovers to nearby properties. Barclays put CMBS tied to government-leased buildings at about $12B (LaPoint and Choi, via Yale Insights, URL in 1.3) | ETO and termination-right review lease by lease; model every ETO exercised on first date; cap single-tenant and single-agency share of NOI |
| **First Republic Bank** (as a lender to real estate) | 2023 | $212.6B of assets; a book of low-coupon jumbo mortgages funded by uninsured deposits. Lost $25B of deposits on March 10 and $40B more on March 13; borrowed up to $109B from the Fed; a $30B deposit from 11 banks bought only five weeks; failure cost the FDIC about $15.6B (YPFS, JFC 7(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/24/) | For any construction or bridge loan at a regional lender: confirm the lender's funding mix, and that the draw commitment survives a lender failure (replacement lender, assignment rights) |
| **Steward Health Care / Cerberus / MPT** (sale-leaseback) | 2016 SLB; Chapter 11 May 2024 | A 2016 sale-leaseback of hospital real estate to MPT ($1.25B for Massachusetts) funded dividends and left escalating rents (Brookings, https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/; lease-payment channel evidence in Gupta et al., NBER w28474, https://www.nber.org/papers/w28474). The healthcare-chapter lane flagged this case [VERIFY]; the Wharton lane sourced it to Brookings | For a net-lease landlord or its lender: model tenant rent coverage after the sale-leaseback, trace where the proceeds went, and treat escalators against an operating business with reimbursement risk as credit exposure to that business. See Chapter 5 and the healthcare chapter |

- **Development overrun, lien and completion risk.** The OCC notes risk of loss due to fraud and construction liens. CHECK: completion guaranty, funded interest reserve, lien waivers at each draw, title date-downs.
- **Guarantor illiquidity at the moment of recourse.** CHECK: verify guarantor liquidity, not just net worth.
- **Extend-and-pretend by the incumbent bank.** Borrowers at regional banks were more than 50% less likely to put in additional equity when their loans were underwater; where undercollateralization was worse, paydowns were smaller. Regional banks disproportionately hold loans on the oldest properties and in low-rent neighborhoods. CHECK: when buying a property or note from, or partnering with, a bank lender, assume the existing loan has been extended to delay loss recognition. Re-mark it (HSV 2025).
- **Latent distress in a "performing" loan.** A loan that locked in a low rate can stay current while deeply underwater. CHECK: for any loan purchase, note-on-note financing, or bank-portfolio deal, re-mark collateral to current value. Do not rely on payment status (HSV 2025).
- **Insurance shock and uninsurability.** CHECK: bound quotes for the full hold; 2x premium stress; flag state insurer-of-last-resort dependence (1.13).
- **Takeout fails at refinance because terms tightened, not because the asset failed.** CHECK: run the takeout with a lower advance rate and higher margin, as in late 2007 (Geanakoplos; 1.14).

## 1.9 Red flags and automatic passes

- Guaranteed returns, "can't lose," pooled funds with no segregation.
- Returns that are smooth relative to the strategy at any level, not just above-market returns (Antle, Yale Insights; see 0.4).
- Exit cap at or below the going-in cap in a rising-rate market.
- No independent appraisal, or an appraisal ordered only by the sponsor.
- Sponsor cannot prove co-invest funds.
- Round-number budgets with thin or no contingency.
- Related-party construction contracts at above-market pricing.
- Affiliate fees (acquisition, development, property management, refinancing, disposition) with no LPAC consent (HLS Forum 2022).
- DSCR built on anticipated leases or market rent rather than leases in place (the 2005–07 "pro forma" loan) (Levitin and Wachter 2013).
- Interest-only for the full term on a transitional or office asset (Levitin and Wachter 2013).
- LTV held flat while the market's cap rates compressed (Levitin and Wachter 2013).
- Class B office underwritten at historical occupancy, or a conversion exit with no costed plan (Gyourko, KaW May 2024).
- Insurance expense held flat in a coastal or wildfire market (Keys and Mulder 2024–26).
- Cap rate quoted without saying NOI or cash flow, or current or forward year (Linneman WP 519).
- A "few defaults" claim on a bridge-loan program with no delinquency roll (First Liberty).
- A government or anchor lease presented as 14-year locked income with no ETO analysis (LaPoint and Choi).
- Stated-income borrower or tenant pools with no IRS-transcript or bank-deposit verification (Mian and Sufi).
- Comps set mainly by levered investor buyers financed by a lender class that has since pulled back (Mian and Sufi 2022).
- Serial loan extensions in the sponsor's track record with no documented workout (2023 interagency statement).

## 1.10 Hard questions

- What is the takeout, and what happens if it is not there at maturity?
- At today's coupon, what refinance proceeds does the asset support, and who writes the check for the gap? (Metrick 2023)
- Which agency tier does the stabilized asset size to at the underwriting floor rate? (Fannie Mae Guide)
- Who controls the draw, and who inspects before each disbursement?
- If your construction lender fails mid-draw, who funds the remaining commitment? (First Republic)
- What is your real basis, and what are the related-party markups?
- Show me the signed leases behind this rent roll and the bank deposits behind this T-12.
- What is DSCR on leases in place, after a recurring capex reserve of about 17% (multifamily) to 36% (retail) of NOI?
- Is your exit cap NOI- or cash-flow-based? What spread to the 10-year Treasury does it imply? How does it compare with today's REIT-implied cap for the sector?
- What is the bound insurance quote today against your pro forma, and what did premiums do over the last three renewals? Is the property insurable at a bindable price for the full hold?
- What is the water source, and what is its priority?
- Show lease expiries by year against the loan maturity. What occupancy did you assume after rollover?
- What is the lease-by-lease termination-right schedule, and what is NOI if every government or anchor ETO is exercised on the first date?
- At a 30% lower value, what is the LTV, and who funds the paydown at maturity?
- Who bought the comps, and how were they financed?
- Show me every extension and modification on your prior loans, and whether each was a documented workout.
- Show me every affiliate fee you charged on your last three deals, and who approved it.

## 1.11 CRE distress 2023–26 and bank counterparties (new)

What changed, and how to underwrite it.

- **Office is structural, not cyclical.** Demand down 15% to 40% (Gyourko's two estimates); trades at 25% to 50% of pre-pandemic prices; distress arrives lease-roll by lease-roll over a five-year window (Gyourko, KaW 2024, **WEAK**, podcast). Metrick estimated office values down about 30% in late 2023, with about two-thirds of office CRE debt needing refinancing within four years and legacy coupons near 1% against market near 7% (Yale Insights, Dec 2023).
- **Reported delinquency understates distress about 4 to 1.** Re-marking each loan's collateral with granular location-by-property-type indices and flagging current LTV above 95% finds "latent distress" about four times reported delinquencies (HSV 2025).
- **Banks matter more than CMBS for mid-size loans.** Three measures, three denominators; none contradicts the others:
  - Regional banks hold almost a third of US commercial mortgage dollars, over $1.6T (HSV 2025).
  - Regional banks make up about 70% of bank lending to real estate (Wachter, KaW 2023, https://knowledge.wharton.upenn.edu/article/fallout-from-the-banking-crisis-whats-ahead).
  - About $3T of CRE sits on bank balance sheets, roughly two-thirds outside the 25 largest banks (Metrick, Yale Insights, Dec 2023).
- **Regional banks are the most likely to extend rather than enforce.** Borrowers at regional banks were more than 50% less likely to put in equity when underwater (HSV 2025).
- **Regional-bank CRE concentration.** Median about 312% of total capital; 54.8% of regional banks above the 300% supervisory-attention threshold (37.7% in 2015); outliers (NYCB/Flagstar) above 500%. Concentration leaves banks exposed to even local shocks, most often in multifamily and retail (HSV 2025).
- **Use, counterparty test.** When the counterparty is a regional bank (seller of notes, co-lender, A-note holder, construction lender), check:
  - CRE loans to total capital against the 300% threshold.
  - Uninsured share of deposits, unrealized securities losses against equity, and a 30-day outflow test (SVB and First Republic; see 4.12).
  - Whether the bank is a likely forced seller (opportunity) or slow enforcer (risk for a co-lender or B-note holder).
- **Bank-financed bubbles are the dangerous ones.** After a median real estate bust, systemic risk of banks with unfavorable characteristics rises by almost 70% of the median. CHECK: when a borrower or fund relies on bank or warehouse facilities concentrated in an asset class that has boomed, stress facility renewal (advance-rate cuts, non-renewal) at the same time as the asset-price decline. The lender will be under stress when you need it (Brunnermeier, Rother and Schnabel, RFS 2020, NBER w25775, https://nber.org/papers/w25775).
- **Discovery method for loan buyers.** Use county mortgage and deed records with property-type price indices to rebuild a lender's portfolio and LTVs when the lender discloses little (HSV 2025).
- **Workout standard.** Benchmark any extension against the June 2023 interagency CRE workout policy statement (1.2).
- **Value-decline stress.** 30% from current marks (Fed adverse), 40% severe (Fed 2024 severely adverse), plus deadweight and distressed-sale discounts (1.5).
- **Insurance and climate repricing is now a standing underwriting line** (1.13).
- **Policy risk is a tenant-credit line.** Government tenancy carries termination-for-policy risk (GSA 2025, 1.8).

**THE ONE CHECK (note and bank-portfolio deals).** Re-mark every loan's collateral to current value with a location-by-property-type index; count loans above 95% current LTV as distressed regardless of payment status.

## 1.12 Cap-rate sanity check (new)

**Linneman framework.** Forward cash-flow cap rate = r − g. NOI cap rate = cash-flow cap / (1 − d), where d is recurring capex as a share of NOI. Required return r = 10-year Treasury + a risk premium set by bond-equivalent credit quality (Linneman, Zell/Lurie WP 519, c. 2005, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf):

| Class (multifamily) | Bond-equivalent quality | Risk premium over 10-yr UST |
|---|---|---|
| A | About BB | About 210 bp |
| B | About BB− | About 260 bp |
| C | About B | About 350 bp |

With g of about 2% and d of 17%, the implied stabilized NOI cap rates are:

| 10-yr UST | Class A | Class B | Class C |
|---|---|---|---|
| 4.2% | 5.1% | 5.7% | 6.7% |
| 5.0% | 6.0% | 6.6% | 7.7% |

- In normal markets the forward cash-flow spread to the 10-year Treasury is about 0 bp for A, about 60 bp for B, and about 150 bp for C. Linneman found an unlevered beta for high-quality apartments of about 0.5.
- **Use.** If the sponsor's going-in or exit cap is below the framework rate for the current Treasury yield, the sponsor must show why growth or risk differs.
- **Dated.** The paper is c. 2005. Use the method, not the levels. Recompute with today's Treasury, a defended g, and the asset's own capex ratio (17% MF, 31% industrial, 33% office, 36% retail per NCREIF history in the same paper).

**Cross-checks.**
- **Credit-equivalent check.** Over roughly 25 years, cap rates showed little response to alternative investment returns, BBB corporate bonds excepted. Cross-check the direct-cap value with CAPM, a comparison with assets of similar credit risk (BBB/BB yields), and the Gordon growth model (Linneman and Rubenstein, "How Should Commercial Real Estate Be Priced?," WRER 12(1), 2008, Zell/Lurie WP 637, https://realestate.wharton.upenn.edu/working-papers/how-should-commercial-real-estate-be-priced/).
- **Public-market check on private marks.** Equity REIT returns predict later returns on the appraisal-based NCREIF index; the lead-lag first found by Gyourko and Keim (1992) persists in the modern REIT era. Compare the sponsor's exit cap and current appraisal cap against the REIT-implied cap for the same property type. A wide gap means the appraisal has not caught up (Gyourko, Zell/Lurie WP 470, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/441.pdf). Context (non-Wharton): Nareit reported REIT-implied caps at 5.74% against NCREIF ODCE appraisal caps of 4.47% in Q2 2026, a 127 bp gap.
- **Comps check.** Who bought, and how were they financed (Mian and Sufi 2022; 1.4).

**CHECK.** Write three numbers in the IC memo beside the sponsor's exit cap: the framework rate at today's Treasury, the REIT-implied cap for the sector, and the latest appraisal cap. Explain every gap above 50 bp.

## 1.13 Insurance, climate, water and insurability reset (new)

- **The premium reset.** Using more than 74M premiums inferred from mortgage escrow data (2014–2024), Keys and Mulder find average homeowners premiums rose about 33% from 2020 to 2023 ($1,902 to $2,530). Against 2018: Florida premiums up 90% by 2023, Texas up 50%. The pass-through from disaster risk into premiums doubled. Reinsurance costs roughly doubled from 2017 to 2023 and drove most of the rise (Keys and Mulder, NBER w32579, rev. Oct 2026, https://www.nber.org/papers/w32579; KaW, "How Higher Property Insurance Premiums Mirror Climate Risk," Sep 24 2024, https://knowledge.wharton.upenn.edu/article/how-higher-property-insurance-premiums-mirror-climate-risk/).
- **Premiums are capitalized into value.** Home price growth was more than $40,000 lower in the most exposed ZIP codes. An earlier version reported about 11% lower relative 2024 prices. Both versions are cited; use the latest (Keys and Mulder, same).
- **The data is residential, but the channel is not.** Reinsurance prices commercial property coverage too.
- **Insurability is a diligence gate.** In parts of California wildfire coverage is unavailable, and banks will not lend against uninsurable property, leaving cash-only buyers and lower values. In property-tax states, falling values erode the municipal revenue base: a possible "nasty spiral" of higher tax rates (Yale Insights, "Putting a Price on Climate Risk," https://insights.som.yale.edu/insights/putting-price-on-climate-risk).
- **Water certainty underpins Sun Belt development.** The 1922 Colorado River Compact allocates 16.5M acre-feet a year, but 2000 to 2023 flows averaged about 12.5M, a structural deficit of about 4M a year. Lakes Mead and Powell are at about one-third of their 2000 levels, and further flow declines of 20% to 30% are projected (Cort, "The Colorado River Is Overdrawn," Yale Insights, May 2026, https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent).

CHECKS
- Three-year premium history; a bound quote at closing (not an indication); bindable quotes for the full hold where available.
- Deductible, named-storm, wind, and wildfire terms read and modeled.
- Stress insurance expense at 2x premium in catastrophe-exposed markets. Stress exit value for capitalization of higher premiums.
- Flag any asset whose coverage depends on a state insurer of last resort.
- For Phoenix, Las Vegas, and Denver Front Range development: the will-serve letter, water-source seniority (senior versus junior rights), and water cost at post-2026 tiered pricing.
- For lenders: confirm the takeout lender will lend at the coverage actually available. An uninsurable asset has no takeout.

## 1.14 CMBS underwriting decay and the leverage cycle: case file (new)

**CASE FILE: CMBS underwriting decay, 2004–2007.**
- What happened: CRE CDOs outbid the experienced B-piece buyers who had policed conduit credit, and underwriting decayed.
- Interest-only loans rose from 47% of CMBS loans in 2004 to 86% in 2007. Conduit loans with partial or full IO went from 10% to 90% between 2003 and 2007 (Gyourko).
- About $40B of "pro forma" loans sized DSCR on anticipated, not in-place, leases: the CRE equivalent of NINJA loans.
- Stated LTVs stayed flat while prices inflated, which means standards were falling.
- Rating agencies' own stressed LTVs rose and stressed DSCRs fell, while AAA spreads tightened.
- Outcome: CMBS 30-day delinquency went from under 2% before 2008 to about 9% in 2011.
- THE CHECK: DSCR on in-place leases only. An amortization requirement. Compare underwritten LTV and DSCR with a third party's stressed LTV and DSCR. Treat flat LTVs in a rising market as loosening.
- Sources: Levitin and Wachter, "The Commercial Real Estate Bubble," Harvard Business Law Review 3, 2013, Zell/Lurie WP 747, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/747.pdf; Gyourko, NBER w14708, 2009, https://www.nber.org/papers/w14708; Zell/Lurie WRER CMBS paper, https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/730.pdf. Dated case (2004–07); the lesson is the pattern.

**The leverage cycle behind it.** In 2006 a AAA mortgage bond could be financed with a 1.6% haircut (about 60:1). Average leverage on the $2.5T of "toxic" mortgage securities was about 16:1, and about 1.2:1 by mid-2009. Ellington's average margins went from about 10% to above 40% in late 2007 (Geanakoplos, Cowles DP 1715, URL in 1.1). Implication: the refinance and takeout assumption must survive a regime where advance rates fall sharply at the moment you need them.

**Pattern signals to watch in any market (lender or LP side).**
- A new, less experienced buyer class outbids the incumbent credit police (B-piece buyers then; any new capital pool now).
- IO share rising.
- DSCR sized on pro forma rents.
- Stated LTVs flat while cap rates compress.
- Spreads compressing while LTVs rise and recourse falls (Pavlov and Wachter).
- Agency or third-party stressed metrics diverging from underwritten metrics.
- Xiong's four bubble features in the asset class at entry: an innovation story; frenzied trading and new, inexperienced investors; a coming increase in supply (new construction, new issuance); sudden bursts without a visible trigger. If three of four are present, the IC memo must name the exit buyer and price once supply arrives (Xiong, NBER w18905, https://www.nber.org/papers/w18905; full overlay in Chapter 0).

**THE CHECK.** Ask for the deal's or pool's IO share, the share sized on in-place leases, and the third-party stressed LTV and DSCR, by vintage. Two or more pattern signals present: underwrite to the stressed numbers, not the sponsor's.

# 2 Tech and Venture

Seed to growth, SaaS, games, AI, hardware, marketplace, fintech.

> **THE SPINE FOR THIS CHAPTER**
> The base case for a venture-backed company is failure. Rebuild every metric from raw data, reconcile every instrument on the cap table, test the core technical claim yourself, and price the security you are buying, not the headline post-money.

## 2.1 How it works

Equity in a priced round, or a SAFE or convertible note before one. The investor gets preferred stock with a liquidation preference, protective provisions, and pro rata rights. The return comes at exit: acquisition or IPO.

- **Base rates first.** Of about 2,000 VC-backed companies that raised at least $1M (2004 to 2010), about 75% never returned cash to investors; 30% to 40% liquidated with investors losing most or all; 70% to 80% missed projected ROI; 90% to 95% missed a declared projection. Excessive funding (it hides problems) and irreversible early commitments before demand is validated (Webvan) drive the largest failures (Ghosh, HBS Working Knowledge, https://www.library.hbs.edu/working-knowledge/why-companies-failand-how-their-founders-can-bounce-back). The IC memo must say what makes this company different from that base rate.
- **Returns are a right tail.** The aggregate portfolio of all equity in 17,242 US ventures first funded 1980 to 2006 (tracked to 2018 or exit) earned about 22% IRR and a generalized PME of 1.44, but dropping the best 5% of ventures makes the risk-adjusted return negative; returns decline after 1999 (Ouyang, Yu and Jagannathan, NBER w27690, https://nber.org/papers/w27690).
- **Manager dispersion is extreme.** Ten-year top-versus-bottom-quartile spread in venture was 43.2 points a year to June 2005, against 13.7 in buyouts and about 0.5 in fixed income. "There's absolutely no way" to index venture (Swensen, Yale ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9). Who leads the round matters more than the round.
- **What VCs say they weight.** Team is rated important by 95% and most important by 47%; business model 83%; product 74%; market 68%; valuation ranks fifth. Team is cited as the top factor in both successes (96%) and failures (92%) (Gompers, Gornall, Kaplan, Strebulaev, "How Do Venture Capitalists Make Decisions?", JFE 2020, HLS Forum summary https://corpgov.law.harvard.edu/2019/08/20/how-do-venture-capitalists-make-decisions/). The founder workstream deserves the most hours, not the fewest.
- **Required returns.** VCs require an average 31% IRR and a 5.0x median (5.5x mean) MOIC, higher for early stage and smaller funds; they market about 24% net IRR (median 20%) and 3.5x net MOIC (3.8x early, 2.8x late). MOIC is used by 63%, IRR by 42%; 9% use no quantitative metric and 20% do not forecast cash flows (Gompers et al. 2020, https://leeds-faculty.colorado.edu/bhagat/vc-decisions.pdf).
- **The standard screen.** Sahlman's People, Opportunity, Context, Deal. On people: "What do they know? Whom do they know? How well are they known?" On deal: the full set of contracts (investors, channels, employees), not just the term sheet. Entrepreneurs' projections are systematically padded (Sahlman, HBS Working Knowledge, https://www.library.hbs.edu/working-knowledge/how-to-write-a-great-business-plan).
- **Hot markets.** Startups first funded in hot VC markets are more likely to go bankrupt and more likely to be extreme successes, and are valued higher at IPO, even with experienced VCs (Nanda and Rhodes-Kropf, JFE 2013, https://corpgov.law.harvard.edu/2011/11/28/investment-cycles-and-startup-innovation/). In a hot market, widen the downside case. The round price is not validation.
- **Theme vehicles buy at the top.** Thematic ETFs lose about 30% risk-adjusted over their first five years because they launch holding stocks already overvalued after a run of performance, media attention and sentiment (Ben-David, Franzoni, Kim and Moussawi, RFS 2023, NBER w28369, https://nber.org/papers/w28369). The same logic applies to private theme SPVs (AI, crypto, space, climate) raised after a hype cycle. CHECK: compare entry valuation with the sector's own history and with the date the theme peaked in media and fund-launch counts. A wave of new vehicles in one theme is a late-cycle signal.
- **Financing cadence is slower than 2021.** Median time between rounds 696 days across stages; seed to Series A median 616 days (about 20 months); median seed pre-money a record $15.6M; median Series A pre-money $47.9M; seed deal count down 25% YoY and Series A down 18% (Carta, State of Private Markets Q2 2025, https://carta.com/data/state-of-private-markets-q2-2025/; Carta Series A Q2 2025, https://carta.com/data/series-a-fundraising-q2-2025). Down rounds were about 17% of new rounds in Q3 2025, just over 19% in Q1 2025 (Carta Q3 2025, https://carta.com/data/state-of-private-markets-q3-2025-full-report/). CHECK: runway must cover at least 24 months to the next round, not the 12 to 18 months of 2021.
- **Late-stage governance gap.** Unicorns grew from about 40 (2013) to more than 1,500; median age at IPO rose from 9 to 13 years (2012 to 2024); the JOBS Act raised the 12(g) trigger from 500 to 2,000 holders and excluded employees, removing pressure to build public-company finance functions (HLS Forum, "Untamed Unicorns," 2026, https://corpgov.law.harvard.edu/2026/11/04/untamed-unicorns-why-startup-finance-is-broken-and-how-to-fix-it/). Late-stage companies can be large and still lack a controller.

## 2.2 Data room index

- Core: pitch deck, 3 to 5 year financial model, fully diluted cap table (every share, option, RSU, SAFE, warrant, convertible note, and side letter).
- Corporate: charter, bylaws, board consents, prior financing documents including every SAFE and side letter, 83(b) elections.
- Investor rights map: every investor veto over financing, debt and M&A, who holds it, and every board designee (see 2.11).
- IP: assignments from every founder and contractor, patents, trademarks, open-source usage.
- Commercial: top customer contracts, cohort and retention data, pipeline.
- Cohort inputs: customers acquired per period, total active customers, and orders or transactions per period, by month or quarter (see 2.10) (Fader and McCarthy, Knowledge at Wharton, Feb. 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/).
- Financials: historicals, bank statements, revenue recognition policy.
- Treasury: list of bank accounts with balances by institution and insured share, and any loan covenant requiring exclusive banking (Song Ma, Yale Insights, https://insights.som.yale.edu/insights/whats-next-for-the-startups-that-banked-with-svb; Metrick, JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf).
- Team: org chart, key employee agreements, option plan, vesting, voting agreements and any super-voting class with its sunset.
- Data and privacy: data map, security posture, incident history.
- Technical validation: test protocols, error rates, complaint logs, regulator correspondence, and a list of every named validator, partner and government user (see 2.7, Theranos).
- Legal: litigation, material contracts, regulatory.

## 2.3 Diligence checklist by workstream

**PROCESS AND INTENSITY**
- Hold a diligence floor that does not shrink because a round is competitive. Diligence hours fall in hot markets, with distance, and as investors get busier or more experienced; thinner diligence widens the spread of outcomes, and doubling diligence is worth 2% to 6% of capital invested in the authors' model (Fu and Taylor, NBER w33987, 2025, rev. 2026, https://www.nber.org/papers/w33987; abstract-level). Record hours of in-person management contact, sites visited and references called in the IC memo.
- Benchmark effort: the average VC deal takes 83 days from first contact to close, about 118 hours of diligence, and about 10 reference calls (13 for late-stage firms, 8 early-stage) (Gompers et al. 2020, https://leeds-faculty.colorado.edu/bhagat/vc-decisions.pdf). A lead that spent a fraction of this is not a diligence anchor.
- Benchmark selectivity: per closed deal, a VC firm considers about 100 opportunities (151 in IT, 78 in healthcare); about 1 in 4 get a management meeting, a third of those reach a partners meeting, half of those go to diligence, and a third of diligenced deals get a term sheet; firms issue 1.7 term sheets per closed deal (Gompers et al. 2020, NBER w22587, https://www.nber.org/papers/w22587).
- Score the written materials and data room before the live pitch, with a fixed rubric and more than one rater. Teams with an above-average "pitch factor" were about 35% more likely to be funded and then did worse on follow-on financing and survival; for all-women teams, decisions were seven times more sensitive to delivery (Song Ma and Allen Hu, Yale Insights, https://insights.som.yale.edu/insights/passionate-startup-pitch-is-powerful-but-can-be-misleading).
- "Proprietary deal" is an assertion. VCs source more than 30% from professional networks, about 30% self-generated, about 20% from other investors, 10% inbound, 8% portfolio referrals (Gompers et al. 2020). Ask who else saw it.

**FINANCIAL AND METRICS**
- Rebuild ARR and MRR from contracts and billings, not the deck.
- Verify revenue against bank deposits.
- Validate churn, NRR, GRR, CAC, and gross margin from raw data.
- Ask for the cohort inputs behind any retention claim and rebuild cohort value (CBCV, see 2.10). Track the share of revenue from customers acquired in the period against prior cohorts: a "hockey stick made entirely of acquisition" needs ever-rising marketing spend (Fader on Wayfair, Knowledge at Wharton, Feb. 2018, URL above).
- Hold margins flat unless a named cost line falls. In 6,103 US IPO firms (53,079 firm-years, 1975 to 2016), median real sales growth exceeded 8% a year, yet cost-to-sales did not fall and profit-to-sales did not rise; the result held for all US public firms, firms worldwide and private European firms (Thomas, Ertan and Lewellen, "Do Profit Margins Expand for High Growth Firms?", Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows). See 5.14.
- Haircut the plan. Proven pattern: 70% to 80% of VC-backed companies miss projected ROI and 90% to 95% miss a declared projection (Ghosh, URL above). Widen management's ranges about 2x: realized outcomes fell inside CFOs' stated 80% confidence intervals only 36% of the time (Ben-David, Graham and Harvey, QJE 2013, NBER w16215, https://www.nber.org/papers/w16215).
- Reverse the valuation: divide the price by a fully diluted share count (options, RSUs, warrants, SAFEs, benefit-fund issuance) and state the margin, growth and pricing power the price requires. Adding RSUs and options moved one implied valuation from $1.25T to about $1.7T (Jacob Thomas, Yale Insights, https://insights.som.yale.edu/insights/is-anthropic-worth-125-trillion).
- Treasury: where is the cash held, what share is above the $250,000 FDIC limit, and is there a single-bank covenant? SVB had about 94% uninsured deposits; depositors withdrew $42B (almost a quarter of deposits) on March 9, 2023 (Metrick, JEP 2024, URL above). Require deposits spread across banks, insured sweeps, or Treasury MMFs.

**COMMERCIAL**
- Customer reference calls. Cohort retention analysis. Concentration.
- Confirm every named marquee customer, partner, validator or government deployment directly with that counterparty, not through the company (KaW, "What Silicon Valley Can Learn from the Theranos Fraud Case," Mar. 19, 2018, https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/).
- Test a random sample of claimed users or customers for live activity (logins, transactions, deliverable email) through production systems, with your own engineer present. Never accept a customer list as evidence (DOJ SDNY, Javice sentencing, https://www.justice.gov/usao-sdny/pr/startup-ceo-charlie-javice-sentenced-85-months-prison-175-million-fraud).

**LEGAL AND CORPORATE**
- Reconcile the cap table to signed documents, including every SAFE and side letter. This is the single biggest preventable mess.
- Walk the IP assignment chain. Confirm every founder and contractor assigned IP to the company. A missing assignment is a deal-killer.
- Map every investor veto over financing, debt and M&A, and every strategic investor's information, observer, ROFR or ROFN right (see 2.11).

**TEAM AND GOVERNANCE**
- Founder vesting status, key-person risk, references, background checks.
- Verify the founder's prior outcome from filings and cap tables, not the bio. Founders with a prior success succeed about 30% of the time, against 20% after a prior failure and 18% for first-timers (success = IPO or IPO filing, 1986 to 2003); top-tier VC backing raises odds only for first-time and previously failed founders (Gompers, Kovner, Lerner, Scharfstein, JFE 2010, https://corpgov.law.harvard.edu/2010/04/16/performance-persistence-in-entrepreneurship-and-venture-capital/). "Prior exit" is often inflated.
- Map voting control, board seats and each director's domain expertise. Theranos gave its founder 100 votes per share against 1, with full control of the board, and a board of politicians and military figures with no medical or financial expertise (Guay, KaW 2018, URL above). Treat founder super-voting control without a sunset as a risk factor and a pricing item.
- Late-stage and secondaries: require a named CFO and controller with public-company or audited-company experience, an audit by a firm sized for the company, internal audit or equivalent, and a board not wholly founder-controlled. FTX raised nearly $2B from VCs with no internal audit function and no experienced finance, accounting, HR or security leadership (HLS Forum, "Untamed Unicorns," 2026, URL above).
- Diligence the lead investor's practical capacity to monitor (board load, distance, partner bandwidth). When a new direct flight cut VC travel time to a portfolio company, it produced more and better-cited patents and was 1.0 to 1.4 points more likely to IPO or exit successfully (Bernstein, Giroud, Townsend, JF 2016, https://corpgov.law.harvard.edu/2014/01/30/the-impact-of-venture-capital-monitoring/).

**TECH AND CYBER**
- Code and architecture review. Security review. Open-source license exposure.
- Independently verify the core technical claim against a stated test protocol, on your samples, in your presence, by an expert you hire. Separate "a technology that did not work out" (ordinary venture risk) from "lying about what works today" (fraud) (KaW 2018; HLS Forum, Theranos, 2022, https://corpgov.law.harvard.edu/2022/01/30/theranos-the-limits-of-the-fake-it-till-you-make-it-strategy/).
- AI model and data provenance. NVCA 2025 added national-security and OISP representations: confirm foreign-person links, data categories, and compute locations.

## 2.4 The numbers: SaaS benchmarks

> **How to weight them by stage (resolves v1 gap B.1).** ICONIQ places real weight on the Rule of 40 only from about $25M ARR, because early growth rates inflate the score. Below about $25M ARR, underwrite growth plus NRR/GRR and burn. Above about $25M ARR, the Rule of 40 becomes a primary screen. Within the Rule of 40, a one-point increase in revenue growth has nearly twice the valuation impact of a one-point increase in FCF margin. The Rule of 40 (YoY ARR growth + FCF margin) became the metric most correlated with public-market multiples over the past year, outperforming growth alone and NRR (ICONIQ, State of Software 2025, https://www.iconiq.com/growth/reports/2025-state-of-software; ICONIQ Growth and Efficiency, https://www.iconiq.com/growth/insights/growth-and-efficiency). Yale sources do not settle the weighting but argue the same direction: projected margin expansion is not supported on average (Thomas, Ertan and Lewellen, URL above), so growth durability (NRR) deserves more weight than projected margins.

| Metric | Benchmark | Source |
|---|---|---|
| Rule of 40 (growth + FCF margin) | 40% or more. Primary screen above about $25M ARR; growth weighted about 2x margin (2025). | ICONIQ 2025 (URLs above) |
| Rule of 40, current median | Median 38% in Q1 2026. Target 50%+ above $10M ARR. **WEAK** (vendor aggregators) | networkcraft (https://networkcraft.net/2026-saas-metrics-benchmarks/); cxcash (https://cxcash.com/metrics/saas); designrevision (https://designrevision.com/blog/saas-growth-benchmarks) |
| Net revenue retention, private-company median | Just above 100%; 2024 survey median NDR 101%. Gross retention near 90%. | KeyBanc Capital Markets / Sapphire Ventures 2025 SaaS Survey (https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey) |
| Net revenue retention, scaled software | "Settling into a healthy ~110% to 120% range" (2025). | ICONIQ 2025 |
| Net revenue retention, v1 benchmark | Above 110% minimum, above 120% strong. Median about 117% in 2026. **WEAK** (vendor); this is a top-quartile public or late-stage figure, not a private median. | networkcraft; cfoadvisors.com |
| NRR by ARR band (top performers, 2021 vintage, refreshed 2024) | $1M to $10M ARR: median 125% (top 145%+). $10M to $25M: 117%. $100M+: 115%. | Bessemer, Scaling to $100 Million (https://www.bvp.com/atlas/scaling-to-100-million) |
| Gross revenue retention | Averages 85% to 90%. SMB can work at 70% to 80%. | Bessemer; KeyBanc/Sapphire (near 90%) |
| CAC payback | Median 16 months for B2B SaaS in 2025, IQR 10 to 24 months. Targets: SMB under 12 months, mid-market under 18, enterprise under 24. Under 12 months for PLG. | Benchmarkit via Growth Unhinged (https://kylepoyar.substack.com/p/2025-saas-benchmarks-report; practitioner dataset); Bessemer; re-cap.com (PLG figure, **WEAK**) |
| Magic number | Above 0.75 is efficient. **WEAK** (practitioner) | re-cap.com; David Skok |
| Burn multiple | Under 1.5x efficient. Above 3x is trouble. **WEAK** (practitioner; originator Craft Ventures, David Sacks; no primary retrieved) | vcbeast.com (https://vcbeast.com/nvca-model-legal-documents-startup-forms) |
| LTV:CAC | Above 3:1. **WEAK** (partly replaced: Bessemer uses a CLTV/CAC framing) | jumpstartpartners.finance; Bessemer |
| Gross margin | Long-run aim 65% to 70%; top performers 80%+. v1: above 70% to 75% (practitioner). | Bessemer; v1 practitioner |
| ARR growth, private median | About 20% projected for 2025 (15% in 2024). | KeyBanc/Sapphire 2025 |
| ARR growth by band (top performers, 2021 vintage) | $1M to $10M ARR: median 165% (top 230%+). $10M to $25M: 87%. $100M+: 57%. v1: 100%+ early, 40% to 60% later. | Bessemer; re-cap.com (v1, **WEAK**) |
| Round cadence | 696 days median between rounds; 616 days seed to A (Q2 2025). | Carta (URLs in 2.1) |
| Down rounds | About 17% of new rounds (Q3 2025); just over 19% (Q1 2025). | Carta |

**Reading the table.**
- **Conflict on NRR, presented, not averaged.** v1's "median about 117% in 2026" (networkcraft; cfoadvisors) conflicts with the private-company median of just above 100% (KeyBanc/Sapphire 2025; 101% in 2024). Bessemer's 117% is the $10M to $25M ARR band median among top-performing 2021-vintage companies. ICONIQ puts scaled software at 110% to 120%. Rule: benchmark a private company against KeyBanc/Sapphire for the median and Bessemer for the top-performer bar. A private company at 117% is top quartile, not average.
- **Vintage warning.** Bessemer figures are 2021 vintage (zero-rate era). Use them as the top-performer bar only (Bessemer, URL above).
- **Last-round valuation is not a mark.** FTX raised $400M at a $32B valuation, up from $25B six months earlier, before it collapsed; Stripe was reported raising about $4B at about $55B, roughly half its 2021 valuation of $95B (Erickson, KaW, Mar. 13, 2023, https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/). Reprice any 2021-vintage mark against current comparables and model a down round.
- **Headline post-money is biased upward.** Later-stage post-money valuations overstate value when the round carries liquidation preferences, ratchets or participation (Gornall and Strebulaev, as confirmed in Ouyang et al., NBER w27690, URL above). Value the specific security.
- **High-growth DCF discipline.** Start from the expected long-run state of the market and the company's share of it, work back to today, and benchmark the path against historical high-growth companies. Do not extrapolate history (Wessels, KaW, https://knowledge.wharton.upenn.edu/article/kicking-tires-ubers-17-billion-valuation-worth-much/).

## 2.5 Third parties

Tech and security diligence firm. QoE provider for growth-stage rounds (scope per 5.5: an agreed-upon-procedures or consulting engagement, no assurance). IP counsel. Background-check provider. Independent technical validator hired by you, not the company, for any core scientific or hardware claim (HLS Forum, Theranos, 2022, URL above). An engineer of your own to sample production user and transaction data (DOJ SDNY, Javice, URL above).

## 2.6 Legal and structure

- NVCA model suite: Term Sheet, Stock Purchase Agreement, Amended Charter (Certificate of Incorporation), Investors' Rights Agreement, Voting Agreement, ROFR and Co-Sale, plus Management Rights Letter and Indemnification Agreement. Free at nvca.org (NVCA Model Legal Documents, https://nvca.org/model-legal-documents/).
- **Version dates, two sources.** v1: NVCA updated five models in October 2025 (tranched financing, national-security reps) and revised the ROFR (April 2026) and voting agreement (June 2026) (1752.vc, https://www.1752.vc/learn/venture-capital-deal-documents-explained; **WEAK**, aggregator). NVCA's own page now lists the core financing set as "Updated November 2026," plus a July 2020 LPA insert on CFIUS and 2025 model PIPE sets (nvca.org, URL above). Cite nvca.org directly and diligence against the version in force at signing.
- Liquidation preference: 1x non-participating is founder-friendly. 2x participating is not.
- Anti-dilution: broad-based weighted average is standard. Full ratchet is punitive.
- Also watch board composition, drag-along, and protective provisions (vcbeast.com, URL above).
- **Negotiability map.** VCs are least flexible, in order, on pro rata rights, liquidation preference, anti-dilution, valuation, board control and vesting; more flexible on option pool, participation, investment amount, redemption rights and dividends (Gompers et al. 2020, URL above). A lead that concedes on preference or board control but fights on dividends is atypical: ask why.
- **Investor vetoes create liability and catch-and-kill risk.** See 2.11 (Zync v. Porsche; Footprint).
- **Strategic and corporate VC investors.** A drop in the parent's innovation raised the odds of launching a CVC unit by about 26%; the median CVC lasted four years (against 10 to 12 for traditional VC), usually ending once the parent recovered; parents often cite the startup's patents afterward (Song Ma, "The Life Cycle of Corporate Venture Capital," Yale Insights, https://insights.som.yale.edu/insights/companies-invest-in-startups-to-repair-weaknesses). Do not count on CVC follow-on support. Review information rights, observer rights, and ROFR or ROFN clauses for technology leakage and exit blocking.
- **Strategic-exit antitrust.** About 6% of pharma acquisitions (6.4% in the working paper) were "killer acquisitions," clustered just below HSR thresholds; as many as 50 a year in pharma (Cunningham, Ederer and Ma, JPE 2021, Yale Insights, https://insights.som.yale.edu/insights/when-corporate-acquisitions-affect-healthcare). An exit thesis that relies on a strategic with an overlapping product faces FTC/DOJ scrutiny of sub-threshold deals, and the buyer may shelve the asset (relevant to milestones and earnouts, see 5.11).

## 2.7 Failure modes

- Cap-table disasters from unpapered pre-seed SAFEs and grants surfacing at Series A. CHECK: reconcile every instrument before the term sheet.
- Missing IP assignment. A founder or contractor who never assigned IP. CHECK: full assignment chain.
- Revenue-quality fiction. "ARR" that is non-recurring or not collected. CHECK: proof of cash and a contract-level rebuild.
- Metric gaming. NRR that excludes churned logos. Blended CAC that hides paid CAC. CHECK: recompute from raw cohorts.
- Fabricated users or customers. CHECK: sample live activity in production systems with your own engineer.
- Technology that does not do what is claimed. CHECK: independent validation on your samples, in your presence.
- Growth bought with marketing, with collapsing cohorts. CHECK: cohort-level CBCV before pricing (2.10).
- Marking off the last round. CHECK: reprice to current comparables; value the specific security.
- Uninsured cash at one bank. CHECK: treasury map with insured share by institution.
- Projected margin expansion with no named driver. CHECK: line-by-line cost bridge or flat margins (5.14).

**Case files.**

| Company, year | What happened | THE CHECK that would have caught it |
|---|---|---|
| Theranos, 2003 to 2018 | Raised about $700M (KaW 2018) or close to $1B at a $9B valuation (HLS Forum 2022; "Untamed Unicorns" 2026): sources differ on the total. 2014 revenue projected to investors at $100M; actual just over $100,000. The analyzer, promised to run about 200 tests, ran about a dozen on its own hardware; tests ran on third-party analyzers presented as Theranos devices. Investor materials carried pharma logos without authorization. Investors were told the device was used on military medevac helicopters; DoD never used it. Founder held 100 votes per share; board of former cabinet officials and generals with no lab-science expertise. Employees raised repeated internal warnings. One investor testified he invested in 2006 and 2013 on his relationship with the founder (KaW, https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/; HLS Forum, https://corpgov.law.harvard.edu/2022/01/30/theranos-the-limits-of-the-fake-it-till-you-make-it-strategy/). | (1) Independent technical validation by your expert, on your samples, in your presence. (2) Call every named validator, partner and government user directly. (3) Error rates, complaint logs, regulator correspondence. (4) Reconcile projections to invoices and cash. (5) Treat a celebrity board with no domain experts and founder super-voting control as red flags. (6) No investment on "relationship" without audited financials and data-room access. |
| Frank / JPMorgan, 2021 acquisition; sentenced Sept. 29, 2025 | Founder claimed 4.25 million users when Frank had about 300,000, and had a synthetic list of 4M+ fake customers generated to pass diligence. JPMorgan paid $175M. When JPMorgan emailed 400,000 "customers," about 70% bounced. Sentence 85 months; restitution over $287M. The judge said JPMorgan had "a lot to blame themselves" for weak diligence (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/startup-ceo-charlie-javice-sentenced-85-months-prison-175-million-fraud). | Never accept a user list as evidence. Test a random sample for live activity (logins, transactions, deliverable email) through production systems with your own engineer present. |
| Blue Apron IPO, 2017 | Growth bought with marketing; about 70% of acquired customers churned within six months; declining cumulative net revenue per recent cohort. IPO range cut from $15 to $17 to $10 within days of a cohort analysis; shares later fell about 70% more (Fader and McCarthy, KaW, Feb. 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/). | Cohort-level CBCV before pricing (2.10). |
| Wayfair, 2018 analysis | CBCV value under $10 per share while the stock traded around $64; "a hockey stick made entirely of acquisition," repeat rates below Amazon's two decades earlier. Stock fell about 10% the day the paper posted (Fader and McCarthy, KaW, URL above). | Share of revenue from newly acquired customers by period; repeat-purchase curve against the category leader. |
| FTX, 2022 | Raised $400M at $32B, up from $25B six months earlier (KaW 2023, URL above). Nearly $2B raised from VCs with no internal audit, no accounting department, no complete employee list, customer deposits off the main balance sheet (HLS Forum, "Untamed Unicorns," 2026; Antle, Yale Insights, https://insights.som.yale.edu/insights/did-crypto-cause-the-ftx-collapse). | Controls first: in-house CFO/controller, employee census reconciled to payroll, customer assets and liabilities on the balance sheet, independent audit. Do not treat the last round as validation. See Chapter 11 for crypto. |
| SVB depositors, March 2023 | Hundreds of startups held large uninsured balances at SVB, threatening payroll; $42B withdrawn on March 9, 2023 (Metrick, JEP 2024; Song Ma, Yale Insights, URLs in 2.2). | Treasury map: balances by bank, insured share, single-bank covenants. "If your bank closed this morning, how many weeks of payroll could you meet?" |
| Zync v. Porsche, Del. Ch. May 2026 (pleading stage) | See 2.11. A strategic's board designee used a financing veto; company shut down. | Investor-rights map; treat a strategic with a financing veto as a red flag. |
| Footprint, Del. Ch. May 2026 (pleading stage) | See 2.11. Insider-led rescue round at about half the funds' own implied value; aiding-and-abetting claims survived. | Price insider rounds against your own marks; document alternatives. |

Other recent late-stage convictions named in the same source: Nikola (Milton), Ozy Media (Watson) (HLS Forum, "Untamed Unicorns," 2026, URL above).

## 2.8 Red flags

- Founder will not give raw data room access. "Trust the deck" metrics.
- Unreconciled cap table. Side letters surfacing late.
- Concentrated revenue (one customer above 25%) presented as ARR.
- No IP assignments.
- Company cannot or will not give customers acquired and active customers by period (Fader and McCarthy, KaW 2018, URL above).
- Investment case rests on founder charisma rather than data-room evidence (Ma and Hu, Yale Insights, URL in 2.3).
- Celebrity board with no domain experts; founder super-voting control with no sunset; no audit committee at late stage (KaW 2018; HLS Forum 2026).
- Named validators, partners or government users the company will not let you call (HLS Forum, Theranos, 2022).
- A strategic investor holding a veto over financing or M&A (HLS Forum, Zync, 2026, URL in 2.11).
- Insider-led round priced below the insiders' own recent marks or bridge terms, with a short decision window for non-participants (HLS Forum, Footprint, 2026, URL in 2.11).
- Revenue growth that is almost entirely new-customer acquisition, with each new cohort worth less than the last (KaW 2018).
- More than one quarter of payroll in uninsured deposits at one bank (Metrick, JEP 2024).
- Valuation justified by the last round, or by a theme at its media peak (KaW 2023; Ben-David et al., NBER w28369).
- Model where margins expand with scale and no cost line is named (Thomas, Ertan and Lewellen, Yale Insights).

## 2.9 Hard questions

- Show the cohort data behind NRR, by month.
- Which founders or contractors have NOT assigned IP?
- What is paid CAC, unblended, and the payback by segment?
- What is the real cash position and the default-alive runway?
- How many customers did you acquire each quarter, and how many are active today? Show orders per period (Fader and McCarthy).
- Name each specific cost line that falls as a share of revenue, and why (Thomas, Ertan and Lewellen).
- At today's price and fully diluted count, what margin and growth must be true at steady state (Thomas)?
- Who can block the next financing or a sale, and has anyone ever used that right (Zync)?
- If your bank closed this morning, how many weeks of payroll could you meet (Song Ma; Metrick)?
- May we call every named validator, partner and government user directly (Theranos)?
- What did your founders' prior companies actually return to investors, per the cap table (Gompers et al. 2010)?
- At the current 616-day seed-to-A cadence, does the runway reach the next round with six months to spare (Carta 2025)?

## 2.10 Customer-cohort valuation (CBCV) for SaaS, subscription and repeat-purchase businesses

New in v2. Applies to SaaS, DTC (see 7.6), marketplaces and consumer subscription.

- **Method.** Value the company as existing customers plus future cohorts. Forecast acquisition, retention, purchase frequency and spend separately, then sum (Fader and McCarthy, KaW, Feb. 12, 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/; McCarthy, Fader and Hardie, J. Marketing 2017).
- **Minimum data request.** Customers acquired per period and total active customers per period. Non-subscription businesses also need orders placed per period. Ideally: spend per order and gross margin by cohort.
- **What good looks like.** Strong retainers (Harry's, Dollar Shave Club) show flattening cohort curves (Fader and McCarthy, KaW 2018). What bad looks like: Blue Apron's declining cumulative net revenue per recent cohort and about 70% six-month churn (same).
- **Tests to run.**
  - Plot each cohort's cumulative revenue (or gross profit) by period since acquisition. Each new cohort should be at least as valuable as the last.
  - Compute the share of period revenue from customers acquired in the period. Rising share with flat repeat means growth is being bought.
  - Compare repeat rates to the category leader at the same age.
  - Rebuild NRR and GRR from the cohort file, including churned logos, and compare to the deck.
  - Reconcile cohort revenue to billings and bank deposits.
- **Use with SaaS benchmarks.** Below about $25M ARR, cohort retention and NRR/GRR carry more weight than the Rule of 40 (ICONIQ 2025, URL in 2.4).
- **THE ONE CHECK.** If the company cannot produce acquired and active customer counts by period, you cannot value it on fundamentals. Most non-subscription firms disclose none of this (Fader and McCarthy).

## 2.11 Insider rounds, investor vetoes and control conflicts

New in v2. Applies to venture and to minority growth equity (Chapter 9).

| Case | What happened | Lesson and CHECK |
|---|---|---|
| Zync v. Porsche (Del. Ch. May 2026, pleading stage) | Porsche's venture arm held 5% via a $2.9M convertible note, one of three board seats, and a director-approval right over new debt. Its designee voted down a $10M Series A; Porsche withheld a promised bridge after obtaining a confidential competitor agreement, and conditioned a $50M PE offer on indemnities. The company shut down. Claims for director disloyalty, aiding and abetting, and breach of the implied covenant survived; exculpation did not cover bad faith (HLS Forum, https://corpgov.law.harvard.edu/2026/07/20/chancery-finds-potential-liability-for-blocking-company-financings-despite-contractual-veto-rights/). | Veto rights used to harm the company create liability; directing your board designee is risky. CHECK: list every investor veto over financing and M&A and who holds it. Treat a strategic with a financing veto as a red flag ("catch-and-kill" risk for other investors). |
| Footprint (Guilbeau v. Footprint, Del. Ch. May 2026, pleading stage) | A near-insolvent packaging company raised $500M of new Class F preferred, $450M (about 90%) from three insider funds that each had a board designee. Pre-money allegedly about half what the funds' own earlier bridge loans implied; higher-valuation alternatives set aside; Class A holders had three weeks to decide; disclosures omitted the valuation, insider benefits and rejected offers. Entire-fairness review applied; aiding-and-abetting claims against the funds survived (HLS Forum, https://corpgov.law.harvard.edu/2026/06/17/chancery-finds-funds-liable-for-aiding-directors-fiduciary-breaches/). | If you lead or join an insider down round or rescue: price it against your own recent marks and bridges, document every rejected alternative, give non-participants real time and data access, and disclose insider benefits. If you are the non-insider: demand the same. |

- **Checklist for any round where insiders are on both sides.**
  - Who on the board is conflicted, and is there an independent committee?
  - What third-party price discovery was run (outside lead, competing term sheets)?
  - How does the price compare with each insider's latest fund mark and any bridge conversion terms?
  - How long do non-participants have, and what information do they get?
  - What happens to non-participants (pay-to-play, conversion to common, preference stacking)?
  - What do the minutes record on alternatives?
- **Corporate VC exits.** Median CVC life is four years (Song Ma, Yale Insights, URL in 2.6). A strategic that leaves can leave a veto behind.
- Cross-reference: Chapter 9 (minority growth), Chapter 10 (GP-led secondaries and continuation-vehicle conflicts).

## 2.12 Base rates and track-record tests for the venture IC memo

New in v2.

- State the prior before the argument: about 75% of VC-backed companies never return cash; 30% to 40% lose most or all (Ghosh, HBS WK, URL in 2.1). Only one or two in ten VC investments succeed (Sorenson, Nanda and Samila, Yale Insights, https://insights.som.yale.edu/insights/for-top-venture-capital-firms-success-breeds-success).
- Show any VC manager's or co-investor's track record with and without its top one or two outcomes; a "consistent singles" thesis contradicts the base rate (Ouyang et al., NBER w27690).
- Attribute track record to the partners who led each deal, and test whether they are still there. Top-VC persistence comes from access to later-stage, larger, syndicated deals that reputation unlocks, not from better picking or advice (Sorenson, Nanda and Samila, URL above). Fund-level diligence: Chapter 10.
- Never compound an IRR or compare it with a time-weighted index. Yale's 20-year venture IRR to June 2018 was 165.9%, dominated by internet-boom distributions; the 20-year time-weighted figure was 24.6% (Yale News, Oct. 2018, https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion). Use PME.
- Required versus delivered: VCs require 31% IRR and 5.0x median MOIC on deals, and market about 24% net (Gompers et al. 2020).

# 3 Debt to Businesses

*Senior, mezzanine, unitranche, ABL, venture debt, revenue-based financing.*

**THE ONE CHECK.** Put three leverage numbers side by side in the IC memo: leverage on unadjusted EBITDA, leverage including every factoring, supply-chain-finance, and receivables-sale facility, and the maximum senior secured leverage the documents permit once every basket and add-back is used. Underwrite to the worst of the three (Ivashina and Vallee, NBER w27316; Harker, KaW Apr 2026).

## 3.1 How it works

The lender advances principal. The borrower pays interest, fixed or floating over SOFR, and repays principal through amortization or at maturity. The loan is secured by collateral, cash flow, or both. Priority is set by lien and intercreditor agreement.

| Rank | Layer | Position |
|---|---|---|
| 1 (paid first, lowest return) | Senior secured / first lien | |
| 2 | Unitranche | Blended first-lien / second-lien economics in one instrument |
| 3 | Second lien / mezzanine | |
| 4 | Preferred equity | |
| 5 (paid last, absorbs losses first, highest return) | Common equity | |

*FIGURE 6 The capital stack. Lien and intercreditor terms decide who is paid first.* In practice, the documents decide more than the figure: baskets, unrestricted-subsidiary capacity, and open-market purchase language can move collateral or priority after closing (3.10, 3.11).

- **The contract will be renegotiated.** Over 90% of long-term private credit agreements are renegotiated before stated maturity, usually early and usually not because of distress. A typical bank loan is renegotiated about five times, roughly every nine months, with pricing, maturity, amount, and covenants all changing. The amendment trail is the real credit history (Roberts and Sufi, JFE 93, 2009, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf; Roberts, JFE 116, 2015, https://www.nber.org/papers/w20484).
- **Not all of the spread is credit risk.** Matching syndicated loans with the same firm's bond spreads on the same day, banks earn a premium over the market price of credit risk of about 142 to 172 bp of an average all-in drawn spread of 279 bp: about half, and up to 61% in one model, for secured term loans to non-investment-grade firms (Schwert, JF 2020, Rodney White WP 03-18, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/04/03-18.schwert.pdf). When comparing a private loan's yield with bonds or a fund's "illiquidity premium," do not treat the whole spread as pay for default risk.
- **Who holds private credit** (Fed, Q3 2025): private debt funds 54.7%, perpetual (non-traded) BDCs 18.7%, public BDCs 12.4%, middle-market CLOs 5.9%, private BDCs 5.4%, interval funds 3.0%. About 70% of small firms' new borrowing is in private credit. A perpetual BDC with redemption queues behaves differently in a workout than a closed-end fund (Federal Reserve FEDS Note, "Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution," Aug 11 2026, Figs. 2 and 4, https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html).
- **Private lenders can forbear indefinitely.** A private lender that holds a borrower's entire debt need not mark or trade it. Market prices that once gave early warning largely disappear, and forbearance can create "zombie" borrowers (Elias and de Fontenay, "The Credit Markets Go Dark," Yale Law Journal 134(3), https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark). See 3.13.

## 3.2 Data room index

- Financials for 3 years plus TTM, audited if available. Monthly management accounts.
- AR and AP agings, customer concentration, borrowing-base detail (ABL).
- Debt schedule, existing liens (UCC search), intercreditor agreements.
- **The complete amendment, waiver, and consent history for every credit facility since origination**, including PIK elections and maturity extensions (Roberts and Sufi 2009; Elias and de Fontenay).
- **Every factoring, supply-chain finance, receivables-sale, inventory-finance, and other off-balance-sheet obligation**, with counterparties and balances. First Brands: about 5x stated leverage against about 20x all-in (Harker, KaW, Apr 22 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).
- UCC searches across ALL affiliates and the founder's personally owned entities, not just the borrower (First Brands; 3.12).
- List of every SPV, JV, guarantee, keepwell, and "moral obligation" support (Shiller, ECON 252 lecture 8, https://oyc.yale.edu/economics/econ-252-08/lecture-8).
- Average daily or intra-quarter balances of debt, cash, and assets, not only period-end figures (Lehman Repo 105; 3.12).
- Hedging: every ISDA Master Agreement, counterparty, close-out netting terms, and whether swaps are secured pari passu under the credit agreement (YPFS, Lehman F and G, https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/7/ and /8/).
- Cash location: banks holding operating cash, share above insured limits, any covenant forcing a single bank (SVB; see 0.5 and 4.12).
- Sponsor model and projections. The sponsor's or management's prior projections against actuals.
- Collateral appraisals and field exam (ABL).
- Material contracts, legal, tax.
- QoE engagement letter and scope section (what was and was not tested).
- For recurring-revenue borrowers: ARR by cohort, seat counts, and pricing history, for an AI-substitution stress (3.3).
- Last 8 quarters of public filings, or management letters for private borrowers, for a text diff (Cohen, Malloy and Nguyen, "Lazy Prices," JF 2020, NBER w25084, https://www.nber.org/papers/w25084).

## 3.3 Diligence checklist by workstream

FINANCIAL AND CREDIT
- Independent QoE: adjusted EBITDA, add-back validation, proof of cash, net working capital.
- **QoE is not an audit.** A QoE carries no assurance: it is typically an agreed-upon procedures engagement (SSAE No. 19, AT-C 215, effective for reports dated on or after July 15, 2021: "no opinion or conclusion," and the engaging parties accept responsibility for the sufficiency of procedures) or a consulting engagement under CS 100. CHECK: read the engagement letter and scope first; ask what was NOT tested and whether proof of cash covered every bank account in the bank confirmations (Journal of Accountancy, Sept 2020, https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html; PCAOB AT 601, https://pcaobus.org/oversight/standards/attestation-standards/details/AT601).
- Leverage and coverage at entry. Projections stress-tested. Equity cushion.
- **Maximum permitted leverage.** Compute maximum permitted senior secured leverage by summing all incurrence baskets, ratio debt, and EBITDA add-backs. Put it beside closing leverage (3.10).
- **All-in leverage.** Add every factoring, SCF, and receivables-sale facility to debt (3.12).
- **Maturity wall against a secular-decline case**, not a cyclical one. Count the capex the business needs to stay competitive before debt service (Toys "R" Us, 3.7).
- **AI-exposed software borrowers.** About one-fifth of loans in semi-liquid private credit funds are to software firms. AI disruption of SaaS led to sharp revisions in their default probabilities in 2026 (a "software crisis"). CHECK: for recurring-revenue loans, stress ARR for AI substitution (seat compression, price pressure) and test the debt on downside ARR, not on ARR multiples (KaW, "Why Semi-Liquid Private Credit Funds Are in Fragile Territory," Oct 26 2026, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/).
- **Widen management ranges.** Realized outcomes fell inside executives' stated 80% confidence intervals only 36% of the time. Treat a management downside case as a midpoint; widen sponsor ranges about 2x before stress testing and build the downside from base rates (Ben-David, Graham and Harvey, QJE 2013, NBER w16215, https://www.nber.org/papers/w16215).
- **Margins do not expand with scale on average.** Any model where EBITDA margin rises with scale needs a line-by-line cost bridge; otherwise hold margins flat (Thomas, Ertan and Lewellen, Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows).
- **Text-diff the filings.** For a public borrower or a carve-out from a public parent, diff the last 8 quarters of filings (risk factors, MD&A, legal proceedings) and require management to explain each material edit. Firms that materially change filing language later show lower earnings and higher bankruptcy risk (Lazy Prices, URL in 3.2).

COLLATERAL (ABL)
- Field exam before booking and periodically after (OCC Comptroller's Handbook, Asset-Based Lending, https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf).
- Third-party appraisal of inventory (NOLV) and equipment.
- Borrowing-base eligibility rules and reserves.
- **Item-level collateral dedupe** (invoice number, serial number, VIN) against every other lender's and factor's borrowing base. UCC sweep across all secured parties and affiliates (3.12).
- **Direct verification of receivables** with account debtors, with remittance to a lender-controlled lockbox (First Brands; DOJ SDNY).
- **Customer-side channel-stuffing test.** For the top 10 account debtors, compare the borrower's invoiced sales to each customer with that customer's purchase, inventory, or AP trend. Large year-over-year jumps in a debtor's inventory and AP signal pre-billing or channel stuffing; that single variable carried about half the predictive power of the 11-variable Dechow model across about 30,000 supplier-years (Zhang, Li and Li, via Yale Insights, https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms). Pair with verification calls.

LEGAL
- Loan agreement, security agreement, UCC-1 perfection, guaranties, intercreditor.
- Scrutinize the EBITDA definition and its add-back caps.
- Read the investments, unrestricted-subsidiary, IP-transfer, non-guarantor, and asset-sale provisions as a set (3.10, 3.11).
- **Who chose lender counsel?** Sponsor-designated lenders' counsel is the norm in US mid- and large-cap LBOs: the sponsor picks (and the borrower pays) the lenders' lawyers, who run one central diligence process shared with all lenders, and face pressure not to "over-lawyer." CHECK: have your own counsel review the baskets, EBITDA definition, and unrestricted-subsidiary provisions independently (HLS Forum, "Sponsor-Designated Lenders' Counsel," Apr 16 2026, https://corpgov.law.harvard.edu/2026/04/16/sponsor-designated-lenders-counsel/).
- **Same-sponsor lending.** PE sponsors increasingly run private credit funds and normally avoid lending to their own portfolio companies because of the conflict. CHECK: confirm whether the lender is affiliated with the equity sponsor, and how amendments and waivers are approved (Elias and de Fontenay, YLJ).
- **Hedges.** Map swap counterparties, close-out netting, and whether the swap is secured pari passu. At Lehman's filing it had 906,000 derivative transactions under 6,120 ISDA Master Agreements ($35T notional); derivatives' exemption from the automatic stay let counterparties terminate and novate in a rush, and local law overrode standardized terms in several jurisdictions (YPFS, Lehman F and G, URLs in 3.2).

PROCESS (credit committee)
- **Sequence bias.** Indian loan officers paid a flat fee per approval were 8 percentage points less likely to approve an application if they had just approved the previous one; paying per approval amplified the bias, and accuracy-based pay shrank it. CHECK: score credits against fixed written criteria before discussion, randomize review order when batching, and pay credit staff for accuracy, not volume (Chen, Moskowitz and Shue, QJE 2016, NBER w22026, https://www.nber.org/papers/w22026).
- **Deployment pressure.** Ask how much the lender must deploy this year. The largest perpetual private-credit fund must deploy about $43B a year, more than a quarter of annual US direct lending; very large deployment targets make selective underwriting hard (Harker, KaW Apr 2026).
- **Do not "be wrong twice."** Be careful about buying more debt in a company where you already hold equity (Harvest Partners, 2009 Wharton PE conference; KaW, Aug 5 2009, https://knowledge.wharton.upenn.edu/article/continuing-defaults-by-private-equity-portfolio-companies-transform-the-middle-market/).

## 3.4 The numbers

CASH-FLOW LENDING AND PRIVATE CREDIT

| Metric | Cited figure | Source and strength |
|---|---|---|
| Unitranche leverage, stable sponsor-backed | 4.0x to 5.5x EBITDA | coyotewealth.com. **WEAK** (vendor); no primary replacement retrieved. Consistent with the Fed median of 5.0x below |
| Median private-credit borrower debt (2025 issuance) | 5.0x EBITDA (3.2x for leveraged loans) | Federal Reserve FEDS Note, Aug 11 2026 (primary; replaces "Fed data via botminds.ai") |
| Interest cover (EBITDA / cash interest), 2025 issuance | 2.2x (3.7x for leveraged loans). **Correction:** the Fed reports this as an AVERAGE, not a median as v1 stated | Federal Reserve FEDS Note, Aug 11 2026 |
| Median borrower revenue | $223M (IQR $35M to $700M) for private credit vs $902M for leveraged loans | Federal Reserve FEDS Note, Aug 11 2026 |
| Median borrower size (IMF) | About $0.5B for private credit vs $4.6B for leveraged-loan issuers | IMF GFSR Apr 2024 Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md |
| Leverage covenant cushion | 25% to 35% to sponsor-model EBITDA | Sidley, https://www.sidley.com/en/insights/newsupdates/2026/03/financial-covenants-in-private-credit-transactions; coyotewealth.com |
| Unitranche pricing | About SOFR + 475 to 650 bps | coyotewealth.com. **WEAK** (vendor; still practitioner per the source-replacement review) |
| Supervisory "leveraged" definition | Total debt above 4.0x or senior above 3.0x EBITDA is a common definition of "leveraged," not a cap. SR 13-3's 6x total-leverage marker raises supervisory concern for most industries | Interagency Guidance on Leveraged Lending, Federal Reserve SR 13-3, Mar 2013, https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm (primary; replaces ctacquisitions.com). **WEAK** on the exact 4x/3x wording until confirmed against the SR letter text |
| Loan spread that is not credit risk | About 142 to 172 bp of a 279 bp average all-in drawn spread (about half; up to 61%) | Schwert, JF 2020 |
| Covenant baskets | 96% of 1,240 leveraged agreements have at least one basket; median 8 baskets; average 79 carve-outs (22 on liens); average debt basket more than 2.3x EBITDA; collateral and asset-sale baskets average 35% and 39% of EBITDA | Ivashina and Vallee, NBER w27316 / Management Science 2025 |
| Permitted vs closing leverage | About half of borrowers close below 5x, yet over 70% of contracts permit later senior secured debt above 5x; over three-quarters of 5x borrowers can go above 6x; a similar share of 6x borrowers can go above 7x | Ivashina and Vallee |
| PIK | PIK interest's share of BDC interest income has doubled since 2019 | IMF GFSR Apr 2024 Ch. 2 |
| Rate structure | Private credit almost exclusively floating rate | IMF GFSR Apr 2024 Ch. 2 |
| Marks | Private credit marked quarterly on internal or third-party models; leveraged loans priced daily. BDC marks lag B-rated leveraged loans; price and NAV take at least four quarters to converge after a shock | Fed FEDS Note 2026; IMF GFSR 2024 |

DEFAULTS, LOSSES AND RECOVERIES

| Metric | Cited figure | Source |
|---|---|---|
| Private credit default rate (covenant + payment defaults) | 1.76% Q2 2025; 1.84% Q3 2025 (705 loans, $141B original principal); 2.46% Q4 2025; 2.73% Q1 2026; 2.41% Q3 2026 | Proskauer Private Credit Default Index, https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-184-for-q3-2025; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-246-for-q4-2025; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-273-for-q1-2026; https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-241-for-q3-2026 |
| Defaults by borrower size | Q3 2025: $25M to $49.9M EBITDA band 2.6% vs 1.2% for $50M+ | Proskauer, Q3 2025 |
| Realized loss, direct lending | Long-run about 1.0% a year since 2004 (1.03% through 2023); 0.70% for 2025. Trailing-four-quarter income exceeded realized losses in every quarter since 2005, including the GFC. Use 1% a year as base-case loss and 2% to 3% as stress | Cliffwater, Report on U.S. Direct Lending, https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf; 2025 results release on a Cliffwater staging host, https://cliffwaterdev-staging.azurewebsites.net/files/docs/CliffwaterPressRelease_CDLI_2025_Results.pdf (**WEAK** for the 2025 figure until confirmed on cliffwater.com) |
| Average recovery by priority (bankruptcies of firms with loans and bonds, Moody's URD 1995–2013) | Loans 84%; secured bonds 60%; senior unsecured bonds 38% | Schwert, JF 2020. Commentators expect lower loan recoveries next cycle given covenant-lite and thinner junior cushions. Use as the base for LGD in 0.6 |
| Middle-market distress reference (2009) | Senior debt traded at 60 to 80 cents; predicted middle-market default rates 10% or more over 12 months; lack of DIP financing made Chapter 11 a likely route to liquidation | KaW, Aug 5 2009 (dated: a downside anchor, not a forecast) |

- **Default definitions differ; ask which one.** "Headline default rates are relatively high because they include covenant defaults that often lead to renegotiation" (IMF GFSR Apr 2024 Ch. 2). Proskauer counts covenant and payment defaults; Cliffwater counts realized losses; rating-agency indices count payment and selective defaults. These produce very different numbers. CHECK: when a sponsor quotes a default rate, ask which definition, and ask for realized loss alongside.

ASSET-BASED LENDING ADVANCE RATES (OCC Comptroller's Handbook, Asset-Based Lending, primary; vendor corroboration from ranfunding, donclarkeenterprises, and eqfunding dropped)

| Collateral | Advance rate |
|---|---|
| Eligible receivables | 80% to 85% typical (OCC range 70% to 85%) |
| Inventory, % of book (cost) | Up to about 65% |
| Inventory, % of NOLV | About 80% |
| Equipment, appraised value | 50% to 80% |

*FIGURE 7 Asset-based lending advance rates by collateral type.*

- Single-customer concentration caps: typically 15% to 25% of the AR pool (OCC notes 10% to 20%).
- Over-advance: most banks cap at 10% to 15% of the borrowing base (OCC).
- **Advance rates are a state variable, not a constant.** Repo haircuts on non-Treasury collateral went from about zero in early 2007 to nearly 50% at the late-2008 peak (Gorton and Metrick, JFE 2012); mortgage-security margins went from about 10% to above 40% in months (Geanakoplos 2009). Underwrite the borrower's liquidity at the stressed advance rate (see 4.9).
- **An advance rate is meaningless without collateral dedupe** (Tricolor; 3.12, 4.5).

VENTURE DEBT AND REVENUE-BASED FINANCING (all **WEAK**: no primary replacement retrieved by any lane; the Stifel deck remains the best source)

| Term | Cited figure | Source |
|---|---|---|
| Venture debt size | 25% to 35% of the last equity round | ratiotech.com; founderpath.com, https://founderpath.com/blog/venture-debt |
| Venture debt interest | About SOFR + 700 to 950 bps, or Prime + 25 to 100 bps at banks | ctacquisitions.com, https://ctacquisitions.com/what-is-venture-debt-financing/; Stifel, https://www.stifel.com/Newsletters/AdGraphics/FlipBooks/_GRP/Macolino-WMG/Past-Events/VentureDebtWebinarSlides.pdf |
| Warrant coverage | 0.5% to 2% equity | founderpath.com; Stifel |
| Lender all-in target | 12% to 25% via interest plus warrants | Wikipedia, https://en.wikipedia.org/wiki/Venture_debt, sourced to industry |
| Recurring-revenue advance | 3x to 12x MRR | beancount.io, https://beancount.io/blog/2026/05/14/venture-debt-recurring-revenue-loans-series-a-b-startups-runway-extension-warrant-coverage-mrr-financing-non-dilutive-growth-capital-guide |
| RBF repayment | 5% to 15% revenue share to a cap of about 1.2x to 1.6x | kadenwoodgroup.com, https://kadenwoodgroup.com/perspectives/revenue-based-financing-vs-venture-debt |

- **Venture debt borrowers' cash sits at banks.** SVB had about 94% of deposits uninsured; a $42B one-day run on March 9, 2023 (Metrick, JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf). CHECK: where the borrower's cash sits, what share is above the $250,000 insured limit, and whether a covenant forces a single bank. Require spread deposits, insured sweeps, or Treasury MMFs.
- **AI-substitution stress applies to MRR-based advances** (3.3).

## 3.5 Third parties

- QoE accountant (read the engagement letter: AUP or consulting, no assurance).
- ABL field examiner. Inventory and equipment appraiser.
- Lender's counsel: your own, independent of sponsor-designated counsel, for baskets, EBITDA definition, and unrestricted-subsidiary review.
- Background-check provider, covering the CFO, controller, and the person who releases wires, not only the named principal (Barrios, Guo and Zhu, via Yale Insights, https://insights.som.yale.edu/insights/remote-work-is-linked-to-decline-in-financial-misconduct).
- Independent collateral agent or backup servicer able to dedupe collateral across facilities (3.12).
- UCC and lien search provider, covering all affiliates and the founder's personal entities.
- Independent valuation agent for Level 3 marks where the lender is a fund (IMF recommends mandatory independent external valuations).

## 3.6 Legal and structure

- Credit agreement, security agreement, UCC filings, guaranties.
- Intercreditor and subordination agreements.
- Deposit account control agreements (DACA) and lockbox for ABL. Lockbox under lender control, not borrower control.
- Maintenance covenants (leverage, coverage) versus covenant-lite. **Covenants have measurable teeth:** after a financial covenant violation, capital expenditure falls by about 1% of capital per quarter, a 13% drop against pre-violation levels (Chava and Roberts, JF 2008, https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/CovenantInvestmentJF2008.pdf). Violations are followed by cuts to acquisitions, leverage, and shareholder payouts, and by more forced CEO turnover; operating and stock performance improve after violations on average (Nini, Smith and Sufi, RFS 2012, https://ideas.repec.org/a/oup/rfinst/v25y2012i6p1713-1761.html). The Chicago Booth summary of Nini, Smith and Sufi puts the rate at about 1.5% before a violation and about 8% four quarters after (the finding places this beside forced CEO turnover; confirm which variable against the RFS paper before quoting). In a covenant-lite deal the lender gives up an early-intervention right that, on average, adds value. Ask what the spread pays for that loss.
- **Covenant baskets** (Ivashina and Vallee): the median agreement has 8 baskets and the average 79 carve-outs. Price and negotiate them; see 3.10.
- **J.Crew blocker:** no transfer of material IP to unrestricted subsidiaries; caps on investments in non-guarantors (3.11).
- Equity cure provisions: number, frequency, and whether cure equity counts as EBITDA.
- Swap documentation: ISDA terms, close-out netting, and whether hedges share the collateral pari passu (Lehman).
- Same-sponsor lending: amendment and waiver approval process where lender and equity sponsor are affiliated.
- **Lender counsel independence** (HLS Forum 2026; 3.3).

## 3.7 Failure modes

- **EBITDA inflated by aggressive add-backs**, so real leverage is higher than underwritten. CHECK: QoE with validated add-backs, and caps in the EBITDA definition.
- **Borrowing-base fraud and phantom receivables.** CHECK: field exam, verification calls to account debtors, lockbox, customer-side channel-stuffing test (3.3).
- **Equity cure abuse.** The sponsor cures a covenant breach with equity counted as EBITDA, hiding a trend. CHECK: limit consecutive cures and watch the trend (botminds.ai, **WEAK**, vendor; Sidley).
- **Covenant-lite with no maintenance test.** 48% of larger deals in 2025 per Proskauer, via botminds.ai. **WEAK**: the share needs the Proskauer primary, and default and covenant statistics depend on definitions (IMF GFSR 2024). Covenant-lite also delays the signal: lenders may not see trouble until full default, and the lack of covenants can make problem deals worse over time (practitioners at the 2009 Wharton PE and VC conference, KaW Aug 5 2009). CHECK: demand at least one maintenance covenant with a defined cushion and step-downs.
- **Permitted leverage far above closing leverage.** Baskets, ratio debt, and add-backs let a 5x borrower go above 6x without lender consent (Ivashina and Vallee). CHECK: maximum permitted leverage in the IC memo (3.10).
- **Collateral stripped through baskets** (J.Crew). CHECK: J.Crew blocker; investment caps; unrestricted-subsidiary limits (3.11).
- **Off-balance-sheet leverage and double-pledged collateral** (First Brands). CHECK: 3.12.
- **Forbearance hides losses** in a private loan no one marks or trades. CHECK: amendment, PIK, and extension history by loan; compare the mark with other BDCs' marks on the same loan (3.13).
- **Dividend recaps priced like LBO leverage.** In 2006–07, Wharton lender roundtables reported recaps priced at little discount to LBO leverage; some lenders refused to finance them. CHECK: in a recap, underwrite the loan as if it were a fresh LBO with no equity added, and split recap returns from earnings growth in the sponsor's track record (KaW, "Lender Roundtable: Outlook on Debt Markets," https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/).
- **Bank failure at the borrower's or lender's bank.** CHECK: cash location and insured share; for revolvers, the lender's own funding (SVB, First Republic; 4.12).

| Case file | Year | What happened | THE CHECK |
|---|---|---|---|
| **First Brands Group** (auto parts) | Chapter 11 Sept 2025; indictment unsealed Jan 29 2026 | SDNY charged founder Patrick James and his brother with bank fraud, wire fraud, and a continuing financial crimes enterprise, alleging billions in purported customer receivables sold to factoring partners that did not exist, collateral double- and triple-pledged, and massive off-balance-sheet inventory financing through entities James owned. At filing: $12M cash in corporate accounts against more than $9B of liabilities. A former executive pleaded guilty and is cooperating; defendants deny the charges (DOJ SDNY, https://justice.gov/usao-sdny/pr/first-brands-executives-charged-multibillion-dollar-fraud; IRS-CI, https://irs.gov/compliance/criminal-investigation/first-brands-executives-charged-with-multibillion-dollar-fraud). Lenders thought leverage was about 5x; counting off-balance-sheet factoring and SCF it was closer to 20x. Per Cambridge Associates, high-quality private-credit managers saw the warning signs and avoided it; banks, broadly syndicated loan funds, and rating agencies did not (Harker, KaW Apr 22 2026) | (1) UCC search across ALL affiliates and the founder's personally owned entities; (2) direct verification of a sample of receivables with the account debtor, remittance to a lender-controlled lockbox; (3) reconcile total supply-chain, factoring, and inventory financing in the footnotes to what the company tells each lender; (4) cash proof at the parent. See 3.12 |
| **J.Crew** | 2016–17; Chapter 11 May 2020 | Owned by TPG and Leonard Green since 2011. Used an investment basket plus a carve-out to move about $250M of brand IP out of lenders' collateral into an unrestricted subsidiary, then used it to back new debt that refinanced junior notes. Senior loan prices dropped on announcement (Ivashina and Vallee, NBER w27316, https://www.nber.org/papers/w27316) | Read the investments, unrestricted-subsidiary, and IP-transfer provisions; require a J.Crew blocker and caps on investments in non-guarantors. See 3.11 |
| **Toys "R" Us** | 2005 LBO; Chapter 11 Sept 2017 | A $7.5B LBO by Bain Capital, KKR, and Vornado. Debt service and 2018–19 maturities, combined with failure to adapt to e-commerce, ended in Chapter 11 and liquidation. **WEAK** (podcast-sourced) (KaW podcasts, "The Demise of Toys R Us," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-demise-of-toys-r-us/, and "Can Toys R Us Recapture Its Glory Days?") | A maturity wall tested against a secular-decline revenue case, not a cyclical one. Count the capex the business needs to stay competitive before debt service |
| **Paragon Metals Holdings v. Smith** (cross-ref Chapter 5) | Del. 2026 | A PE sponsor paid $100M for an auto-parts maker; the day after closing it learned two of the largest customers planned sharp volume cuts, and it later defaulted on acquisition debt (HLS Forum, https://corpgov.law.harvard.edu/2026/07/30/are-hints-disclosures-delaware-supreme-court-revives-ma-fraud-claim-despite-buyers-red-flags/) | For an acquisition loan: lender-side customer calls with the top customers before closing, not reliance on the sponsor's diligence |

## 3.8 Red flags

- EBITDA definition with uncapped, vague add-backs.
- No field exam and no appraisal on an ABL.
- Receivables concentration above caps presented as fully eligible.
- Second lien without an intercreditor.
- Maximum permitted senior secured leverage two or more turns above closing leverage (Ivashina and Vallee).
- No J.Crew blocker; uncapped investments in non-guarantors or unrestricted subsidiaries.
- A borrower with multiple warehouse, factoring, or inventory-finance providers who each see only their own collateral, and no single party that sees all of it (First Brands; Tricolor).
- Factoring or supply-chain finance excluded from leverage.
- Recurring financing that unwinds just after period-end (Repo 105 pattern).
- Lender counsel chosen by the sponsor and no independent review by your own counsel.
- Lender affiliated with the equity sponsor, with amendments approved inside the same group.
- PIK toggles, serial amend-and-extend, or maturity extensions with no paydown.
- Default rate quoted with no definition.
- A lender under deployment pressure (very large annual deployment target).
- Recurring-revenue loan sized on ARR multiples with no AI-substitution downside.

## 3.9 Hard questions

- What is leverage on unadjusted EBITDA, and on the lender's own number?
- What is the maximum senior secured leverage the documents permit, using every basket, ratio debt, and add-back?
- Is there a maintenance covenant, at what cushion, and does it step down?
- What is the equity cushion in a downside case, and who funds a cure?
- Show every amendment, waiver, PIK election, and maturity extension since origination, and what each one changed. What is the mark on this loan in other lenders' books?
- List every factoring, supply-chain-finance, and receivables-sale facility. What is leverage including them?
- Is any collateral, invoice, or VIN pledged under another facility? Show the dedupe.
- Can material IP or assets move to an unrestricted subsidiary or non-guarantor? Under which baskets, and how much?
- Who chose lender counsel, and what did your own counsel change?
- Is the lender affiliated with the sponsor? Who approves waivers?
- Which default definition does your track record use, and what were realized losses?
- What happens to ARR if AI cuts seats by a third?
- Where is the company's cash held, and what share is uninsured?

## 3.10 Covenant capacity: maximum permitted leverage (new)

Headline covenants are hollowed out by baskets and carve-outs. In 1,240 leveraged credit agreements: 92% restrict liens and 87% restrict additional debt, but 96% contain at least one deductible ("basket"); the median agreement has 8 baskets and the average 79 distinct carve-outs (22 on liens). The average debt basket equals more than 2.3x EBITDA; collateral and asset-sale baskets average 35% and 39% of EBITDA (Ivashina and Vallee, "Weak Credit Covenants," NBER w27316 / Management Science 2025, https://www.nber.org/papers/w27316).

- **Headline leverage understates permitted leverage.** About half of borrowers close below 5x total debt/EBITDA, yet over 70% of contracts permit later senior secured debt above 5x. Over three-quarters of 5x borrowers can go above 6x, and a similar share of 6x borrowers above 7x.
- **Non-bank loans have weaker contracts, priced only modestly higher.** LBO loans and loans with more non-bank funding have significantly weaker contracts. The market reprices the risk only after a public event (J.Crew 2016–17).
- **Covenants add value when they bite** (Chava and Roberts 2008; Nini, Smith and Sufi 2012; 3.6). A lender that gives them away should be paid for it.

PROCEDURE
1. List every incurrence basket (general, ratio, incremental/accordion, free-and-clear, refinancing, acquisition, purchase-money, capital lease, non-guarantor, foreign subsidiary).
2. List every lien basket and every investment basket, including investments in unrestricted subsidiaries and non-guarantors.
3. Apply the EBITDA definition as written, with every permitted add-back and run-rate adjustment at its cap (or uncapped).
4. Compute maximum permitted senior secured and total leverage, and the collateral that can leave the box.
5. Put closing leverage, maximum permitted leverage, and all-in leverage including off-balance-sheet financing (3.12) side by side in the IC memo (HBS lane IC memo addition).
6. Price the gap or negotiate it down. Have your own counsel, not sponsor-designated counsel, do steps 1–4.

**CHECK.** If maximum permitted senior secured leverage exceeds closing leverage by two turns or more, underwrite recovery at the permitted level, not the closing level.

## 3.11 Liability management exercises (new)

Liability management exercises (LMEs) are now a main out-of-court workout tool. In an LME, the borrower and a group of creditors use the existing documents to prime, strip, or move value away from non-participating creditors: drop-downs of assets into unrestricted subsidiaries or non-guarantors, and uptiers that subordinate non-participants. Diligence must map which creditors can be primed or stripped under the existing documents (Hotchkiss roundtable, WFFI Policy Series, "The Ambiguous Economics of Out-of-Court Workouts," Apr 16 2026, https://wffi.wharton.upenn.edu/policy-series-topics/). **WEAK**: roundtable listing only; no white paper reviewed. The Wharton lane flagged that this section needs non-Wharton primary sources (law-firm and court materials); none were retrieved by any lane. Uptier and non-pro-rata case law is not covered by the findings and must be sourced before this section anchors a posted deal.

**The anchor case: J.Crew (2016–17).** See 3.7. About $250M of brand IP moved through an investment basket and a carve-out to an unrestricted subsidiary, then backed new debt that refinanced junior notes. Senior loans fell on announcement; Chapter 11 followed in May 2020 (Ivashina and Vallee).

CHECKS
- **Drop-down capacity.** Sum investment capacity into unrestricted subsidiaries and non-guarantors (3.10). Require a J.Crew blocker: no transfer of material IP to unrestricted subsidiaries.
- **Uptier capacity.** Read the voting thresholds for amendments that subordinate liens or payment priority, and whether pro rata sharing can be amended by a majority. [Mechanics drawn from the WFFI framing; confirm against document-level sources.]
- **Who sits on which side.** Map the lender group: which holders could form a majority and participate, and whether you would be inside or outside.
- **Recovery haircut.** Loan recoveries averaged 84% in 1995–2013 (Schwert 2020), but commentators expect lower loan recoveries in the next cycle given covenant-lite and thinner junior cushions. Underwrite recovery after the worst LME the documents allow.
- **Distressed buyers.** In the capital-structure map (4.2 distressed row), identify which tranche can be primed and price the fulcrum after an LME, not before.

## 3.12 Collateral integrity and off-balance-sheet leverage (new)

A standalone procedure anchored on First Brands and Tricolor (2025). Both collapsed within days of each other in September 2025, with allegations of collateral pledged to more than one lender (Harker, KaW Apr 22 2026). The general lesson is the spine of this book: independent verification of what secures the loan. A borrower with multiple warehouse, factoring, or inventory-finance providers who each see only their own collateral, and no single party that sees all of it, is the red flag (DOJ SDNY First Brands and Tricolor releases). Archegos is the same failure at a prime-broker level: no counterparty saw the whole book (see Chapter 10).

PROCEDURE
1. **UCC sweep across all secured parties**, all affiliates, and the founder's personally owned entities, not just the borrower.
2. **Inventory of every factoring, supply-chain-finance, receivables-sale, and inventory-finance facility.** Add all of it to leverage. First Brands: about 5x stated, about 20x all-in.
3. **Reconcile financing disclosures**: footnote totals against what the company tells each lender.
4. **Item-level dedupe** (invoice number, serial number, VIN) against other lenders' borrowing bases, run by an independent collateral agent or backup servicer.
5. **Direct debtor verification** of a sample of receivables, with notification and acknowledgment of assignment where the structure allows.
6. **Lockbox control**: remittances to a lender-controlled account under a DACA.
7. **Cash proof at the parent**, not only at the borrower.
8. **Custodial possession** of original titles and notes for consumer or auto paper (Tricolor; 4.5).
9. **Static-pool reconciliation**: charge-offs from the servicing system tied to trustee and lender reports (Tricolor).
10. **Window-dressing test**: request average daily or intra-quarter balances of debt, cash, and assets. Lehman used "Repo 105" transactions to move up to $50B of assets off its balance sheet at quarter-ends; its auditor knew and did not force disclosure. Flag any recurring financing that unwinds just after period-end (YPFS, Lehman C and D, https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/4/ and /5/).
11. **Off-balance-sheet vehicles and implied support**: list every SPV, JV, guarantee, keepwell, and "moral obligation" support, and require a consolidated look-through (Enron partnerships, bank SIVs; Shiller, ECON 252 lecture 8).
12. **Customer-side test**: compare invoiced sales to each top debtor with that debtor's own purchase, inventory, or AP trend (Zhang, Li and Li; 3.3).

Add a "Collateral dedupe" line to the A.2 diligence report: UCC sweep done, item-level dedupe done, by whom (Wharton lane template addition).

**THE ONE CHECK.** No single party sees all the collateral: fix that before funding, or pass.

## 3.13 Renegotiation, forbearance and marks: the loan's real history (new)

- **The amendment trail is the credit history.** Over 90% of private credit agreements are renegotiated before maturity; a typical bank loan about five times, roughly every nine months (Roberts and Sufi 2009; Roberts 2015).
- **Opacity lets forbearance hide losses.** Assets in private-credit strategies grew from about $300B in 2010 to an estimated $1.6T in 2023. Loans held by private-credit BDCs rose from 1,395 to 20,182 between 2010 and 2022. BDC filings are one of the few public windows: lender identity, rate, amount, maturity, and book value for a subset of borrowers (Elias and de Fontenay, YLJ).
- **Marks lag.** Private credit is marked quarterly on models; BDC marks lag B-rated leveraged loans and take at least four quarters to converge after a shock. The IMF recommends mandatory independent external valuations and more frequent valuation reviews (IMF GFSR Apr 2024 Ch. 2).
- **Observable index marks are defensible; model-only marks that ignore them are not.** Subprime index (ABX) prices in 2008–09 had significant fundamental components despite claims of irrationality (JFC 3(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss2/1/).
- **"Third-party pricing" can be gamed.** Infinity Q's CIO manipulated inputs to the supposedly independent Bloomberg BVAL models (see 0.6).

CHECKS
- Track amend-and-extend, PIK toggles, and maturity extensions loan by loan.
- Compare the manager's mark with the same loan's mark in other BDCs' Schedules of Investments.
- Ask who has write access to pricing inputs, and get the administrator's or valuation agent's independent price on a sample of Level 3 loans.
- Ask which vehicle holds the loan (Fed holder mix, 3.1): a perpetual BDC under redemption pressure is a different workout counterparty.

# 4 Credit of All Kinds

*Direct lending, specialty finance, receivables, trade, litigation, royalties, consumer, structured, distressed, and the funding behind them.*

**THE ONE CHECK.** Independently verify that the loan assets exist, are pledged only to you, and perform as reported: a loan-level tape traced to cash, deduped across every facility, with a third party holding the collateral documents. Then stress the lender's own funding: what happens to its warehouse lines and redemptions in the same month its losses peak.

## 4.1 How it works

Non-bank lenders originate and hold loans (direct lending), or buy and finance pools of receivables, royalties, legal claims, or structured tranches. The return comes from spread, fees, and recovery. Most of these lenders are themselves levered by banks, warehouse lines, repo, or redemption-funded vehicles, so the lender's funding is part of the credit (4.9).

**Market size: the figures differ by definition and date. Do not average them.**

| Measure | Figure | Source |
|---|---|---|
| v1 figure (superseded) | "Exceeds $1.7 trillion globally" | coyotewealth.com (**WEAK**, vendor; replaced) |
| Global assets plus dry powder, 2023 | About $2.1T; US managers $1.6T AUM (June 2023); growing about 20% a year over five years | IMF GFSR Apr 2024 Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md |
| Private-credit strategy assets | About $300B (2010) to an estimated $1.6T (2023) | Elias and de Fontenay, YLJ 134(3), https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark |
| Industry size, post-2008 growth | Roughly $2T | Ivashina, HBS Working Knowledge, https://library.hbs.edu/working-knowledge/how-private-debt-became-2-trillion-industry |
| Industry size, 2026 commentary | About $1.8T to $2T | Goldstein, KaW, "Five Things to Know About Private Credit," May 5 2026, https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit |
| Global private credit market, end-2025 | $3.5T (semi-liquid net assets $300B of it) | Fang, Goldstein and Zeng, via KaW Oct 26 2026, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/ |
| Private-credit debt outstanding to US nonfinancial private corporations, Q1 2026 | About $1.4T | Federal Reserve Financial Accounts, via FEDS Note Aug 11 2026, Fig. 1 |

Use the Fed figure for US corporate debt outstanding; the IMF figure for global AUM including dry powder; the $3.5T figure for the broadest global market definition. State which one any memo uses.

- **Why it grew.** Banks shed high-LTV leveraged loans after 2008, and PE needed leverage to hit about 20% promised returns. Ivashina's main concerns: uncertain valuations (marks drive jumpy flows), high leverage and credit risk, and interconnection with banks and the rest of the system (Ivashina, HBS WK).
- **Opacity.** Pricing and risk are visible only to a few parties, marks are model-based, and regulators have limited system-wide data. Labels such as "alternative assets," "direct lending," or "multi-strategy income" can hide private-loan exposure. CHECK: look through to holdings and to how marks are set (Goldstein, KaW May 2026).
- **Bank leverage behind private credit.** Bank lending to private-credit vehicles rose from about $8B (2013) to about $95B (end-2024). Bank commitments to PE and private-credit sponsors are about 14% of bank lending to nonbanks, up from about 1% a decade earlier (Harker, KaW Apr 22 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).
- **Cycle signal.** A complex, illiquid product marketed to unsophisticated investors usually means the cycle is near its peak. Late entrants understand least why the strategy worked, and very large deployment targets make selective underwriting hard (Harker, same).
- **A steady spread with rare large losses is selling insurance.** Benchmark short-volatility credit strategies against levered index put-writing; their "alpha" in calm years is the premium (Jurek and Stafford; Princeton lane; see 10.5).

## 4.2 Diligence by sub-strategy: what changes

| Strategy | What to verify |
|---|---|
| Direct lending | As Chapter 3. Sponsor quality, documentation, covenants, EBITDA definition, leverage cushion. Maximum permitted leverage under the baskets (3.10). Same-sponsor conflicts (3.3). Which vehicle holds the loan and its redemption profile (3.1, 4.11) |
| Factoring and receivables | Receivables exist and are collectible. Debtor creditworthiness. Dilution history. Notification vs non-notification. Recourse vs non-recourse. Advance rates 70% to 90% of eligible AR. On notification deals, verify every account debtor's acknowledgment of assignment (general lane). Item-level dedupe against other factors and lenders (3.12). Customer-side channel-stuffing test (3.3) |
| Trade finance | Underlying goods, shipping documents, letters of credit, counterparty and country risk. Dedupe documents across financiers (3.12) |
| Equipment finance | Collateral value, residual, lessee credit, lien perfection. Serial-number dedupe. Equipment residual norms still a gap (needs lender interviews) |
| Litigation finance | Case merits (independent legal opinion by counsel not involved in the case), damages model and collectability, duration (model IRR at 1.5x expected duration), capital adequacy to see cases through, portfolio diversification and cross-collateralization, non-recourse to claimant, funder control rights versus state ethics rules, Level 3 marks and the auditor's approach. No federal statute regulates litigation funding and there is no nationwide disclosure requirement; GAO found public data too limited to size the market; commercial deals run into the millions, consumer advances usually under $10,000 (GAO-23-105210, Dec 2022, https://www.gao.gov/products/gao-23-105210). Court-level disclosure is spreading (e.g. D. Del. standing orders since 2022) (**WEAK**, [VERIFY] current federal rulemaking status). Full outline: Litigation Finance chapter |
| Royalty finance | The royalty stream itself (music, pharma, mineral), title to the royalty, payor creditworthiness, duration and decline curve. Music: Copyright Royalty Board rate determinations and listed royalty funds' NAV write-downs as comparables (suggested primary sources; not yet researched) |
| Consumer credit | Pool stratification, FICO bands, charge-off and delinquency vintages, servicer quality. Bunching or performance jumps at eligibility cutoffs (4.8). Income verified against IRS transcripts or bank deposits (4.8). Household-debt cycle position (Mian, Sufi and Verner; 4.8). Custodial possession of titles; VIN-level dedupe (Tricolor) |
| Structured credit (ABS, CLO) | Tranche attachment and detachment, underlying collateral, waterfall, rating-agency assumptions, correlation. For CLOs: obligor (typically 2%) and industry (typically 15%) limits; AAA break-even default rate at a stated recovery; manager after-fee PME by vintage (4.3). Warehouse risk and manager incentives (YPFS "Inside the CDO Machine" and "Anatomy of a Trade," JFC 4(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol4/iss1/10/ and /12/). Mark to observable indices where they exist (ABX lesson, 3.13) |
| Distressed and special situations | Capital structure map, fulcrum security, recovery and liquidation analysis, bankruptcy process, collateral valuation. Map which creditors can be primed or stripped under the existing documents (LMEs, 3.11). Recovery base: loans 84%, secured bonds 60%, senior unsecured 38% (Moody's URD 1995–2013 via Schwert 2020), with a haircut for covenant-lite. In a weak DIP market, Chapter 11 can mean liquidation: plan for out-of-court, equity-funded restructuring (KaW 2009) |
| Note and CRE loan purchases | Re-mark collateral to current value; latent distress about 4x reported delinquency; extension history of the selling bank (1.11) |
| Insurance-linked balance sheets and PE-owned insurers (new row) | Statutory statements (not GAAP) of the operating company and affiliated reinsurers; Schedule S ceded reinsurance; RBC recomputed on a consolidated basis including affiliated captives; affiliated-transaction policy; independent valuation of affiliated private placements; NAIC designation source (private letter ratings). See 4.10 |
| Semi-liquid vehicles as lenders (new row) | Liquidity coverage against the redemption cap; gate and queue history; fund leverage response to outflows; stale-NAV risk. See 4.11 and Chapter 10 |
| Specialty and bank-like lenders funded by deposits or short-term money (new row) | Uninsured or flighty funding share; unrealized loss to equity; IRRBB; 30-day outflow coverage; pre-positioned collateral. See 4.12 |
| Tokenized private credit and real-world assets (new row; cross-ref Chapter 11) | About $29B of tokenized RWAs on public chains (April 2026), plus $16.9B of private-credit tokens on Figure's Provenance chain, about $46B in total. The token is usually a contractual or beneficial claim on an off-chain asset, not direct title. Verify the legal right conveyed, the custodian and bankruptcy remoteness, redemption timing and gates, oracle and NAV rules, and independent audit of the underlying loans. A token's trading speed should match the speed at which the underlying asset can honor redemptions (Cong, Mayer and Rabetti, WFFI 2026, https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf) |
| NAV lending and fund finance (cross-ref) | Initial LTV 10% to 30%, max about 40%; structural subordination to portfolio-company debt; recallable distributions. Full treatment: NAV Lending and Fund Finance chapter |

## 4.3 The numbers

- **Direct lending:** as Chapter 3 (3.4): median leverage 5.0x, average interest cover 2.2x (Fed 2026); realized loss about 1.0% a year long run, 2% to 3% as stress (Cliffwater); default indices by definition (Proskauer, IMF).
- **Specialty finance:** focus on loss rates, net yield after losses, advance rates, and overcollateralization. An advance rate is meaningless without collateral de-duplication (Tricolor).
- **Factoring versus ABL cost:** factoring runs 18% to 36% equivalent, against about 10% to 18% for ABL on average usage (ranfunding.com, https://ranfunding.com/asset-based-lending/). **WEAK**: no primary replacement retrieved.
- **Factoring advance rate:** 70% to 90% of eligible AR (keep; practitioner, consistent with OCC ABL receivables range of 70% to 85%).
- **Advance rates are a state variable.** Gorton and Metrick's repo-haircut index (nine non-Treasury collateral classes) went from about zero in early 2007 to nearly 50% at the late-2008 peak; several classes could not be repo'd at all, equivalent to a 100% haircut. Margins went from about 10% to above 40% in months (Geanakoplos). Underwrite at the stressed advance rate: 50% for non-Treasury structured collateral, 100% for esoteric assets (Gorton and Metrick, JFE 2012, https://repec.som.yale.edu/icfpub/publications/2358.pdf; Geanakoplos, Cowles DP 1715).

CLO AND STRUCTURED CREDIT

| Metric | Figure | Source |
|---|---|---|
| CLO collateral pool performance | Like loan mutual funds with similar risk and fees: gross PME about 0.97 | Cordell, Roberts and Schwert, "CLO Performance," Nov 2020, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf |
| CLO equity | Average PME about 2.47 before management fees; after fees, outside equity earns about what its systematic risk predicts. Returns eroded as the market grew | Same |
| CLO management fee | Typically about 50 bp of collateral balance; falling since 2017 | Same |
| CLO share of leveraged loan funding | Two-thirds of leveraged loan issuance since 2008 (about $2.1T) | Same |
| AAA break-even | With 40% recovery, about 60% of loans in the pool must default before AAA loses money. For comparison, the cumulative 1931–33 default rate for risky debt was 31% | Roberts and Schwert, KaW, Aug 10 2020, https://knowledge.wharton.upenn.edu/article/clos-will-not-cause-next-financial-crisis/ |
| Concentration limits | 15% per industry; 2% per obligor | Same |
| Track record | Pre-2008 AAA CLO tranches lost nothing (S&P); pre-2008 AAA CDO tranches lost $325B (Cordell et al. 2019) | Same |

CHECK: for any CLO or CLO-like vehicle, confirm obligor and industry limits and the AAA break-even default rate at a stated recovery. Underwrite CLO managers on after-fee PME by vintage, and on how much of the gross outperformance the manager keeps.

RECOVERY AND LOSS ANCHORS
- Loans 84%, secured bonds 60%, senior unsecured 38% (Moody's URD 1995–2013, via Schwert 2020). Expect lower loan recoveries next cycle.
- Direct lending realized loss about 1.0% a year since 2004 (Cliffwater).
- Consumer subprime, mean two-year default rate about 5% in the Keys et al. sample (2010; dated).

**B.1 gap status (advance-rate and loss-rate norms by sub-strategy): partly resolved.** Direct lending loss (Cliffwater), recovery by priority (Schwert), CLO AAA break-even (Roberts and Schwert), ABL advance rates (OCC), NAV LTVs (Sidley), and stressed advance rates (Gorton and Metrick; Geanakoplos) are now sourced. Consumer installment and equipment residual norms still need lender interviews.

## 4.4 Third parties

- Collateral or portfolio auditor. Loan-tape auditor tracing borrower-level payments to bank deposits.
- Servicer review, and a backup servicer able to step in.
- Independent collateral agent or custodian holding original titles and notes; able to dedupe collateral across facilities (VIN, invoice, serial number).
- Independent legal opinion (litigation finance), by counsel not involved in the case.
- Rating agency (structured). Read the agency's stressed assumptions, not just the rating.
- Valuation firm, with a direct engagement letter and a call to confirm it actually did the work (SQN Capital, SEC Lit. Rel. 26671, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671).
- Statutory-accounting specialist or insurance regulator contact for insurer-affiliated platforms (Schedule S, consolidated RBC) (4.10).
- Bank-funding analyst for deposit-funded lenders (IRRBB, LCR-style outflow test) (4.12).

## 4.5 Failure modes

- **Fake or over-pledged collateral.** The "market maker loan and dump" pattern is the crypto analog. The general lesson is independent verification of what secures the loan.
- **Servicer failure and commingling in specialty finance.** CHECK: backup servicer and segregated collection accounts.
- **Origination gaming at eligibility cutoffs.** CHECK: plot the tape around every cutoff (4.8).
- **Funding run on the lender.** Warehouse haircuts rise, lines are pulled, or redemptions exceed liquidity at the moment losses peak. CHECK: 4.9 and 4.11.
- **Forbearance and stale marks hiding losses.** CHECK: amendment history and cross-BDC mark comparison (3.13).

| Case file | Year | What happened | THE CHECK |
|---|---|---|---|
| **The Adam brothers** (a lending pool that did not exist) | 2024 | Promised up to 13.5% monthly from a "lending pool" (SEC 2024-107, https://www.sec.gov/newsroom/press-releases/2024-107) | Independent verification that the loan assets exist. Proof of cash. The guaranteed-return red flag |
| **Tricolor Holdings** (subprime auto lender) | Collapsed Sept 2025; DOJ charges Dec 2025; SEC civil charges Aug 18 2026 | DOJ charged the CEO and COO; the CFO and senior director of finance pleaded guilty and are cooperating. Alleged schemes: double-pledging the same auto loans to multiple warehouse lenders and ABS deals; altering loan descriptions to meet eligibility; booking charged-off loans in a fictitious dealer-management-system "portfolio company" so they looked current. The SEC called it a "$1.9 billion collapse." One report: about $2.2B of collateral pledged against about $1.4B of real collateral by Aug 2025. A forensic review cited by ABA Business Law Today found about 40% of roughly 70,000 Tricolor loans shared VINs or attributes with at least one other loan (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/ceo-cfo-coo-charged-connection-billion-dollar-collapse-tricolor-auto; SEC 2026-77, https://www.sec.gov/newsroom/press-releases/2026-77-sec-charges-former-executives-fraud-connection-19-billion-collapse-subprime-auto-lender-tricolor; SEC Lit. Rel. 26612, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26612; Harker, KaW Apr 2026; ABA, https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-october/seeing-red-flags-in-tricolor-collateral-interests) | Loan-level collateral de-duplication across ALL facilities (VIN-level for autos) by an independent collateral agent or backup servicer; custodial possession of original titles and notes; static-pool charge-off reconciliation from the servicing system to the trustee reports; independent verification of each pledged receivable. See 3.12 |
| **First Brands Group** (factoring counterparty view) | 2025 | Purported customer receivables sold to factoring partners allegedly did not exist; collateral double- and triple-pledged (DOJ SDNY). See 3.7 | For a factor or SCF provider: confirm the receivable with the account debtor, require notification and acknowledgment of assignment, and dedupe against other factors (3.12) |
| **First Liberty Building & Loan** (bridge-loan pool Ponzi) | SEC Jul 10 2025 | $140M of notes and loan participations promising up to 18%, "few defaults"; most loans defaulted; new money paid old investors from at least 2021. See 1.8 | Loan-tape audit traced to bank deposits; delinquency roll behind any "few defaults" claim |
| **Silicon Valley Bank** (lender and depository) | 2023 | 94% uninsured deposits; long securities funded by demand deposits; a $17B unrealized loss larger than $15B book equity by Dec 31 2022, all in public filings; a $42B one-day run on March 9 2023 (Metrick, JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf). One JFC analysis argues the Basel IRRBB standard would have flagged the strategy 10 quarters before failure, and the LCR would have forced tens of billions more liquidity at least 4 quarters before (JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/12/) | Uninsured-funding share, unrealized loss to equity, IRRBB, and a 30-day outflow test. See 4.12 |
| **Credit Suisse** (counterparty) | 2023 | Client outflows in Q4 2022 after years of scandals. When a major shareholder said it would add no more capital, shares fell 24% in a day and five-year CDS went above 1,000 bp. CS drew CHF 48B from standing facilities and CHF 120B from emergency ones before the UBS takeover (YPFS, JFC 7(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/18/) | As a counterparty, prime broker, or custodian client: watch CDS, deposit and AUM outflows, and shareholder support. Keep a documented plan to move assets and novate trades |
| **Reserve Primary Fund** ("cash" that was credit) | 2008 | A $62.5B fund holding $785M of Lehman paper got more than $40B of redemption requests in two days, broke the buck on September 16, 2008, and suspended redemptions. Investors got about 50 cents within six weeks, 99 cents after two years; the final distribution (99.1 cents) came in 2014 (YPFS, JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/9/) | Look through "cash" and "cash management" vehicles to the credit underneath; model a 6-to-24-month gate on any pooled cash vehicle |
| **AIG** (securities lending and CDS collateral) | 2008 | AIG reinvested securities-lending cash collateral in RMBS; when borrowers returned securities it could not repay the cash, and the Fed lent up to $37.8B through the Securities Borrowing Facility. CDS written on CDOs produced collateral calls that drained liquidity; Maiden Lane III ($24.3B Fed loan plus $5B AIG equity) bought the CDOs to stop the calls (YPFS, AIG Modules B and E, JFC 3(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss1/3/ and /6/) | For insurers, lenders, and funds: what is the cash collateral invested in, and what collateral-posting triggers (rating downgrade, mark-to-market) exist? See 4.10 |
| **Pre-2008 CDOs vs CLOs** | 2008 | Pre-2008 AAA CDO tranches lost $325B; pre-2008 AAA CLO tranches lost nothing (S&P; Cordell et al. 2019, via Roberts and Schwert 2020) | Do not treat "structured" as one risk class. Test the collateral, obligor and industry limits, and AAA break-even for the specific vehicle |
| **Semi-liquid private credit run dynamics** (cross-ref Chapter 10) | 2026 | Stale marks, a 5% gate, and thin cash produced gating, rising fund leverage, and deferred payments. Q2 2026: $7.1B of repurchases against $3.8B of inflows, the sector's first aggregate net outflow; $10.7B of requests unmet (KaW Oct 26 2026). See 4.11 | Liquidity coverage ratio (cash + NII + maturities against the redemption cap), mark-lag tests, redemption queue history |

## 4.6 Red flags

- Yields far above the risk-free rate with "no risk."
- Returns that are smooth relative to the strategy at any level (Antle; 0.4). A steady spread with no losses is either insurance premium not yet paid out (put-writing) or a mark not yet taken.
- No independent audit of the loan tape or collateral.
- Manager also services, values, and reports, with no third party.
- A borrower or originator with several warehouse lenders or factors, none of whom sees all the collateral (Tricolor; First Brands).
- Collateral pledged without custodial possession of titles or notes.
- Bunching of loans just above an eligibility cutoff, or a performance jump at the cutoff (Keys et al.).
- Stated-income consumer pools whose income growth outruns local IRS income growth (Mian and Sufi).
- "Few defaults" with no delinquency roll or static-pool data (First Liberty).
- "Independent valuation" the manager cannot evidence with the valuation firm's engagement letter (SQN).
- Labels ("alternative assets," "multi-strategy income") that hide private-loan exposure (Goldstein).
- Lender leverage stack (subscription line, NAV facility, asset-based facility, repo) with no disclosed margin-call triggers (Harker).
- A redemption-funded vehicle whose redemption cap exceeds its liquidity coverage (Fang, Goldstein and Zeng).
- An insurer-affiliated platform lending policyholder money into its own deals with no independent valuation of affiliated placements (4.10).
- Default rate quoted without a definition (IMF).
- Very large deployment targets (Harker).

## 4.7 Hard questions (new)

- Show me the loan tape at loan level, and the bank deposits behind its payment history.
- Who holds the original titles and notes? Who has run a collateral dedupe across every facility, and when?
- Plot defaults around every eligibility cutoff. Is there a bunch or a jump?
- How was borrower income verified, and on what sample?
- What is the static-pool charge-off history by vintage, reconciled from the servicing system to trustee reports?
- List every financing line with its haircut or advance rate, margin-call mechanics, and term. What happens if haircuts go to 50%?
- What unencumbered liquidity covers a margin call?
- Who values the Level 3 loans, and who has write access to the pricing inputs? Show me the same loans' marks in other managers' books.
- Which default definition does your track record use? What were realized losses?
- What is the redemption cap against cash, NII, and maturities per quarter? What did you do the last time requests exceeded the cap?
- For a CLO: what is the AAA break-even default rate at 40% recovery? What are the obligor and industry limits? What is your after-fee PME by vintage?
- For insurer-affiliated capital: show the statutory statements, Schedule S, and consolidated RBC including affiliated captives. Who values the affiliated private placements, and who rated them?
- For a deposit-funded lender: what share of funding is uninsured, what is the unrealized loss to equity, and what is the 30-day outflow coverage?
- For litigation finance: what is IRR at 1.5x the expected duration, and can the defendant pay?

## 4.8 Loan-tape and portfolio diligence (new)

A procedure for any pool: consumer, SMB, auto, bridge loans, receivables, or a loan portfolio purchase.

DATA ROOM
- Loan-level tape with origination data (FICO, DTI, LTV, income, documentation type) and current status.
- Payment history by loan traced to bank deposits.
- Static-pool data: delinquency roll rates, charge-offs, and recoveries by vintage.
- Modification, extension, PIK, and forbearance history by loan.
- Servicing agreement, backup servicer agreement, and collection-account structure.
- Custodian receipts for original titles and notes.
- Every warehouse, forward-flow, ABS, and participation agreement the originator has signed, for dedupe.
- Eligibility criteria for each facility.

TESTS
- **Cutoff test.** Plot the tape's FICO and DTI distribution, and default rates, around every eligibility cutoff. Low-documentation subprime loans just above the 620 FICO threshold, where securitization was easier, defaulted about 10% to 25% more than loans just below it (about 20% in one version), against a mean two-year default rate of about 5%. The authors attribute this to lax screening when loans could be sold; the interpretation is contested (Bubb and Kaufman point to underwriting rules of thumb), but the diligence test holds either way. A bunch or a performance jump at the cutoff signals origination gaming (Keys, Mukherjee, Seru and Vig, QJE 2010, https://corpgov.law.harvard.edu/2009/06/08/did-securitization-lead-to-lax-screening/).
- **Income test.** IRS transcripts (Form 4506-C), payroll, or bank-deposit verification on a statistically meaningful sample. Compare pool income growth with local IRS SOI zip-code income and BLS wages. Application income ran about 90% above IRS income in the worst zip codes in 2002–05, and those zip codes defaulted most (Mian and Sufi, NBER w20947, https://www.nber.org/papers/w20947).
- **Existence and dedupe test.** VIN, invoice, or serial-number dedupe across all facilities; custodial possession; static-pool reconciliation to trustee reports (Tricolor).
- **Payment-trace test.** Borrower-level payments traced to bank deposits; delinquency roll behind any low-default claim (First Liberty).
- **Re-mark test** for secured pools: current collateral value, not origination value; count current LTV above 95% as distressed (HSV 2025; 1.11).
- **Cycle test.** Record the 3-year change in household debt to GDP for the market; if in the top third of history, run a downside with 2 points lower growth for 3 years (Mian, Sufi and Verner, QJE 2017, https://www.nber.org/papers/w21581).
- **Geography and foreclosure regime.** For secured consumer and residential pools, model recovery timing by judicial versus non-judicial state and local price pressure from clustered foreclosures (Mian, Sufi and Trebbi 2015; 1.4).
- **Servicer test.** Backup servicer named and tested; segregated collection accounts; who can move cash out of them (0.5 wire-signature check).

## 4.9 Funding fragility: haircuts, margins, warehouse and bank leverage (new)

Specialty lenders, ABS warehouses, levered credit funds, and NAV-financed vehicles fail through their funding before their assets. Short-term secured funding runs through haircuts (Gorton and Metrick, JFE 2012).

- **Repo haircut index:** about zero in early 2007 to nearly 50% at the late-2008 peak; some classes unfinanceable (100%). Illustration: with $10T of repo and a 20% average haircut, borrowers face a $2T shortfall.
- **Margins are procyclical:** about 10% to above 40% in months; AAA haircuts from 1.6% to multiples of that (Geanakoplos).
- **Liquidity spirals:** market liquidity and funding liquidity reinforce each other. Falling prices raise margins (margin spiral) and inflict losses on levered holders (loss spiral), so liquidity can vanish suddenly and across assets at once (Brunnermeier and Pedersen, RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf).
- **Bank-financed bubbles:** lenders with high loan growth in a boomed asset class are under the most stress in the bust (Brunnermeier, Rother and Schnabel, RFS 2020).
- **The leverage stack behind private credit:** bank lending to private-credit vehicles about $8B (2013) to about $95B (end-2024) (Harker 2026).

CHECKS
- List every financing line (warehouse, repo, subscription line, NAV facility, asset-based facility, forward flow) with its haircut or advance rate, margin-call mechanics, eligibility criteria, and term.
- Stress haircuts to crisis levels: 50% for non-Treasury structured collateral, 100% for esoteric assets.
- Model a simultaneous 20% to 30% collateral price fall plus a haircut increase. Identify what is sold first and whether a forced sale breaches covenants elsewhere.
- Stress facility renewal (advance-rate cuts, non-renewal) at the same time as the asset decline.
- Confirm the unencumbered liquidity that covers the call.
- Stress funding and liquidity, not only credit losses: run multiple scenarios; ask for HTM and AFS fair-value marks and a liquidity stress, not only a loss-rate stress (JFC, "Stressing the Stress Tests," JFC 7(3), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss3/2/).
- For ISDA-hedged lenders: map counterparties and close-out netting (Lehman; 3.3).

## 4.10 Insurer-affiliated private credit capital (new)

Life insurers, many PE-owned, are now a main source of "permanent capital" for private credit platforms. When the manager's capital is an affiliated insurer, the manager is lending policyholders' money into its own platform's deals.

- **Size.** Life-insurer private-placement lending reached about $849B (14% of balance sheets) in 2024, with PE-owned life insurers the main driver. Their private placements in ABS and financial borrowers rose from 2% to 8% of assets, 2017–2024 (Meisenzahl, Overpeck and Polacek, Chicago Fed WP 2025-09, https://www.chicagofed.org/publications/working-papers/2025/2025-09; non-Princeton context cited in the Princeton lane).
- **Shadow reinsurance hides leverage.** Life insurers ceded liabilities to affiliated, less-regulated "shadow" reinsurers (captives, often offshore), growing from about $11B (2002) to $370B (2013). By 2012 about 28 cents of every dollar insured was ceded to shadow reinsurers, up from 2 cents in 2002. Adjusting for it cut the average company's risk-based capital by about 53 percentage points and implied ratings about 3 notches lower, with expected impairment probability rising severalfold (Koijen and Yogo, "Shadow Insurance," Econometrica 2016, NBER w19568, https://www.nber.org/papers/w19568).
- **The opposing view.** Industry critics (Harrington, for ACLI) argue the effect is overstated (https://www.acli.com/-/media/acli/public/files/pdfs-public-site/public-public-policy/captives/captive_reinsurance_in_life_ins_harrington_2014.pdf). Both positions stand; do the consolidated computation yourself.
- **Collateral reinvestment risk.** AIG's securities-lending cash collateral, reinvested in RMBS, needed up to $37.8B of Fed lending (4.5).

CHECKS
- When the counterparty, lender, LP, or co-investor is an insurer, or an asset manager whose permanent capital is an affiliated insurer: obtain statutory statements (not GAAP) of the operating company and its affiliated reinsurers, and Schedule S ceded reinsurance.
- Recompute RBC on a consolidated basis including affiliated captives.
- Read the affiliated-transaction policy. Who approves the insurer buying the affiliated manager's loans?
- Require independent valuation of affiliated private placements.
- Identify the NAIC designation source (private letter ratings) for each affiliated placement.
- Ask what the cash collateral is invested in and what collateral-posting triggers (downgrade, mark-to-market) exist.
- **Gap:** consolidated RBC for insurer-affiliated private-credit platforms still needs an interview with an insurance regulator or rating analyst (Princeton lane). Suggested primaries: NAIC statutory filings and RBC ratios, AM Best methodology, state insurance department exam reports.

## 4.11 Semi-liquid private credit vehicles: the credit view (new)

Full fund-level treatment (BDCs, interval funds, NAV REITs, evergreen PE, retail and 401(k) access) belongs in Chapter 10 and the evergreen-vehicle section. This section covers what a lender, co-lender, borrower, or credit analyst needs when the counterparty or loan holder is a redemption-funded vehicle.

- **Scale.** Semi-liquid private credit net assets grew from $10B (2019) to $300B (end-2025), within a $3.5T global private credit market. Perpetual (non-traded) BDCs hold 18.7% of private credit and interval funds 3.0% (Fed, Q3 2025; 3.1).
- **The 2026 stress.** Q2 2026: $7.1B of repurchases against $3.8B of inflows, the sector's first aggregate net outflow; $10.7B of requests unmet (gated). Blue Owl Capital Corp II received redemption requests for about 22% of shares and Blue Owl Credit Income Corp about 40%; Blackstone, BlackRock, and Apollo vehicles also saw requests above the cap. Earlier in 2026, Blue Owl ended quarterly redemptions from the $1.6B OBDC II, and Blackstone met record redemptions of about 8% of its flagship credit fund (Fang, Goldstein and Zeng, via KaW Oct 26 2026; Harker, KaW Apr 22 2026).
- **Liquidity coverage is thin.** Redemption cap typically 5% of shares a quarter. Average cash about 5.5% of total net assets; net investment income about 2.5% a quarter (mostly paid out, since BDCs must distribute 90%); loan maturities under 0.5% a quarter. Recurring 5% redemptions exhaust this quickly.
- **Secondary liquidity is poor.** About 80% of loans are unrated, and fewer than 20% are held by 10 or more fund families, so forced sales mean fire-sale discounts.
- **Leverage-redemption loop.** Net debt issuance rises 0.38 percentage points of TNA for each 1-point increase in net outflows. "Repurchases payable" (deferred redemption payments) work like trade credit owed to exiting investors.
- **Stale NAV creates a run incentive.** If marks lag, redeeming investors exit above economic value at remaining holders' expense. BDC marks take at least four quarters to converge after a shock (IMF GFSR 2024).
- **Concentration.** About one-fifth of loans in semi-liquid private credit funds are to software firms, exposed to the 2026 AI repricing (KaW Oct 2026; 3.3).
- **Gates recur and carry stigma.** Suspensions work like bank holidays: they only pause the run, and stigma makes managers reluctant to use them until late. Read the gate, suspension, and in-kind provisions and assume they will be used (JFC, "Survey of Bank Holidays and Fund Suspensions," JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/1/).
- **Sponsor support** (insiders buying in) is discretionary and may not scale.
- **Retail access** tends to erode the illiquidity and contracting advantages that made private markets work, keeps higher fees, and creates liquidity mismatch (HLS Forum, "Private Equity for All," Feb 28 2026, https://corpgov.law.harvard.edu/2026/02/28/private-equity-for-all-the-paradoxical-push-to-democratize-private-markets/).

CHECKS (credit view)
- **Liquidity coverage ratio:** quarterly cash + NII + maturities against the redemption cap.
- Mark-lag test: the vehicle's marks against the same loans in other BDCs' schedules and against leveraged-loan indices.
- Redemption queue and gating history; whether unmet requests carry forward.
- Fund-level leverage stack and margin triggers (4.9).
- **As a borrower's lender or co-lender:** if the loan holder is a perpetual BDC under redemption pressure, expect pressure to sell, to resist new money in a workout, or to favor PIK. Factor that into intercreditor dynamics.

## 4.12 Bank and bank-like lenders and counterparties (new)

Applies to any bank, credit union, fintech lender, or specialty finance company that funds with deposits or short-term money, and to any bank that is your counterparty: construction lender (1.8), A-note holder or note seller (1.11), revolver lender, custodian, or depository for a borrower's cash.

TESTS
- Uninsured share of funding (SVB: about 94%).
- Unrealized losses on securities against equity (SVB: about $17B against $15B book equity at Dec 31 2022).
- IRRBB: economic value of equity under rate shocks. The Basel IRRBB standard would have flagged SVB's strategy 10 quarters before failure, by one JFC analysis.
- An LCR-style 30-day outflow test. The LCR would have forced tens of billions more liquidity at least 4 quarters before (JFC 7(2)).
- Pre-positioned collateral at the Fed. Signature Bank was "particularly unprepared": it lacked collateral pre-positioned at the Fed (Metrick, JEP 2024).
- CRE concentration against the 300% supervisory threshold (HSV 2025; 1.11).
- For a large counterparty: CDS, deposit and AUM outflows, and shareholder support (Credit Suisse). Keep a documented plan to move assets and novate trades.
- Risk governance: the limit-breach log and the record of limit changes for the last 24 months; who the CRO reports to and whether the CRO was replaced recently. Lehman raised limits to fit positions and in October 2007 replaced its CRO with a dealmaker (YPFS, Lehman B, https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/3/).

THE 2023 RUN, IN NUMBERS
- SVB: $42B withdrawn on March 9, 2023, almost a quarter of deposits. Signature lost about $10B and First Republic about $25B the next day (Metrick, JEP 2024; Song Ma, Yale Insights, https://insights.som.yale.edu/insights/whats-next-for-the-startups-that-banked-with-svb).
- First Republic: $40B more on March 13; up to $109B borrowed from the Fed; FDIC cost about $15.6B (1.8).
- Credit Suisse: CHF 48B from standing facilities and CHF 120B from emergency ones (4.5).

**CHECK.** For every operating company, fund, and borrower in the deal: where is the cash held, what share is above insured limits, and does any covenant force a single bank? Require deposits to be spread across banks, or kept in insured sweeps or Treasury MMFs, and look through any MMF to its holdings (Reserve Primary, 4.5). Full counterparty framework: proposed new Chapter 0 section on counterparty, treasury, and liquidity risk.

# 5 Private Equity and M&A

LBOs, lower middle market, search funds, roll-ups, carve-outs, growth equity.

> **THE SPINE FOR THIS CHAPTER**
> Buy earnings you have proven to cash, at a multiple you would accept at exit, with leverage the downside case can carry. Whatever diligence finds is uninsured, so price it. Whatever diligence misses, the claim will be made at the deal multiple.

## 5.1 How it works

The sponsor acquires a company using equity plus debt (an LBO), improves it, and exits in 3 to 7 years. The return comes from three places: EBITDA growth, debt paydown, and multiple change. An IC memo must split the return into these three sources (goreuben.com, https://www.goreuben.com/templates/ic-memo-buyout). See 5.14.

- **Funnel.** For every 100 opportunities considered, the average PE firm deeply investigates fewer than 24, signs an LOI or agreement with fewer than 14, and closes about 6 (Gompers, Kaplan, Mukharlyamov, "What Do Private Equity Firms Say They Do?", JFE 2016, NBER w21133, https://www.nber.org/papers/w21133). A sponsor claiming to close a much larger share is either not screening or not seeing competitive flow.
- **Sourcing.** PE firms call about 48% of closed deals "proprietary" in some sense (36% self-generated, 7.4% from management, 8.6% executive network), but 33% come from investment banks, 8.6% from brokers and 4.3% from other PE firms (same). Ask who else saw it and whether a banker ran a process.
- **How sponsors value.** Gross IRR and MOIC; over 70% also use comparable multiples; fewer than 20% use DCF/APV; at least 55% do not use WACC; about 96% use a 5-year horizon; exit value set off comparables (fewer than 30% use a perpetuity; 16% assume exit multiple = entry multiple) (same).
- **Target returns.** Target gross IRR averages 22% (most 20% to 25%; survey-table median 25%; smaller firms higher); target MOIC median 2.5x, mean 2.85x; net IRR marketed to LPs mostly 20% to 25% (25% to 30% gross); over 85% adjust targets for risk (same).
- **Value-creation levers, by sponsors' own account** (share of deals where important, pre-deal): revenue growth over 70%; incentives 61%; follow-on acquisitions over 50%; facilitating a high-value exit about 50%; governance 47%; buying cheap 44% to 47%; cost reduction only 36% (47% post-deal) (same). A plan that relies on cost cuts or multiple arbitrage relies on the industry's weaker levers.
- **Exit routes.** Sponsors expect about 50% of exits to strategics, about 30% to financial buyers, fewer than 20% via IPO (26% large firms, 11% small), matching realized exits of 53/30/17 (same, citing Stromberg 2008). An IPO-dependent exit is a minority outcome.
- **M&A base rate.** 70% to 90% of acquisitions underperform their own expectations across multiple studies; high premiums are hard to recover through synergies (Feldman and Chunduru, "Why Many M&A Deals Fail and How to Beat the Odds," KaW, Dec. 8, 2025, https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/).
- **Do buyouts beat public markets?** Present both positions. (a) Buyouts showed positive risk-adjusted performance for 1995 to 2018 public pensions, partly value exposure, while the average plan's overall risk-adjusted PE outperformance was about zero (Korteweg, Panageas, Systla, HLS Forum, 2025, https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/). (b) Pre-fee buyout returns can largely be replicated by a passive portfolio of small, low EV/EBITDA public stocks with about 2x leverage; after about 6% a year in fees, PE investors underperformed it; mark-at-cost accounting makes measured beta fall from about 2 to near zero (Stafford, RFS 2022, https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting). (c) Owner-held entrepreneurial private equity returned no more than public equity despite extreme concentration (Moskowitz and Vissing-Jorgensen, AER 2002, NBER w8876, https://www.nber.org/papers/w8876); a Bank of Canada follow-up disputes robustness beyond the 1990s (Kartashova, Bank of Canada WP 2011-6). In lower-middle-market deals, do not assume an illiquidity premium appears on its own. Fund-level benchmarking: Chapter 10.
- **Sponsor pace and depth.** Effects differ persistently across PE groups; rapid growth in a group's deal volume is associated with lower employment growth at its targets; employment falls about 12% over two years after public-to-private buyouts and rises about 15% after private-to-private (Davis, Haltiwanger, Handley, Lipsius, Lerner, Miranda, NBER w26371, https://www.nber.org/papers/w26371). In 2008 to 2009, PE-backed companies raised more capital, invested more and gained share versus peers, most where the sponsor had more resources (Bernstein, Lerner, Mezzanotti, NBER w23626, https://www.nber.org/papers/w23626). CHECK: chart the sponsor's deals per year against team size; confirm uncalled capital and reserve policy in the fund that owns the company.

## 5.2 Data room index

- CIM. 3 to 5 years of financials plus TTM. Monthly management accounts, trial balances, tax returns.
- Sell-side QoE if any, with its engagement letter and scope section. EBITDA bridge and add-back schedule.
- Bank statements for every account (36 months) and bank confirmations, for proof of cash.
- Average daily or intra-quarter balances of debt, cash and receivables, not only period-end (YPFS, Lehman Repo 105, JFC 1(1), https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/4/).
- Every factoring, supply-chain-finance and receivables-sale agreement; UCC search results across all secured parties (Harker, KaW, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).
- Customer and supplier lists, contracts, concentration; customer-level volume forecasts and any correspondence on volume reductions or cancellations (Paragon, 5.7).
- Org chart, management bios, employment and compensation, option and phantom plans; historical budgets versus actuals for three years (Schrand and Zechman, J. Accounting and Economics 2012, https://repository.upenn.edu/accounting_papers/119).
- Legal: corporate records, litigation, IP, real estate, permits, compliance; internal investigations log; hotline log with volumes, categories and resolution times for three years (Soltes, HBS, https://www.stern.nyu.edu/sites/default/files/assets/documents/Eugene%20Soltes%20-%20The%20Difficulty%20of%20Being%20Good%20The%20Efficacy%20of%20Integrity%20Hotlines.pdf).
- Regulated targets: FDA 483s and warning letters, quality-system audit trails, raw lab data (Akorn, 5.7).
- HR: union contracts, open grievances, multiemployer pension and withdrawal-liability estimates (Blumenthal, Yale Insights, https://insights.som.yale.edu/insights/how-does-private-equity-create-value; Sun Capital, 5.12).
- Franchise, staffing and multi-unit targets: franchise agreements, FDD Item 17, and every no-poach or non-solicit clause (7.8).
- IT systems and cyber posture, incident history.
- Sponsor and affiliate fee agreements charged to the target: transaction, monitoring, director, exit (Metrick and Yasuda, Wharton WP 2007, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf).
- Insurance, environmental, ESG.
- Public or carve-out targets: the last 8 quarters of 10-K/10-Q filings or parent segment disclosures (Lazy Prices, 5.3).

## 5.3 Diligence by workstream: the full institutional set

**PROCESS DISCIPLINE**
- Set a walk-away price from conservative cash flows before bidding starts. Keep deal champions separate from the valuation team. Probability-weight synergies and model dis-synergies (lost customers and talent). Use cooling-off periods against auction fever. Treat a seller-imposed deadline as a red flag, not a reason to skip work. Diligence run to confirm an answer already chosen is the most common M&A process failure (Feldman and Chunduru, KaW 2025, URL in 5.1).
- Synergy table in the IC memo: cost synergies separate from revenue synergies, each with probability and timing, plus a dis-synergy line. Cost synergies typically take 1 to 2 years; revenue synergies 2 to 3+ years (same).
- Convert every hint in the data room into a written question, ask it in customer meetings, record the answer, and re-run the model on what you learned (Paragon, 5.7).
- The opposite error exists. A pure DCF treats uncertainty only as downside and can underbid: value a target as NPV of core cash flows plus option value of growth businesses plus abandonment value. In one example a bank's $800M DCF cap lost to an $840M bid that abandonment value would have justified at $849M (MacMillan, van Putten and Baghai, KaW, Mar. 30, 2011, https://knowledge.wharton.upenn.edu/article/mas-overlooked-pitfall-the-false-negative/). Use only with explicit, ranged assumptions, never to rationalize a price.
- Do not "be wrong twice": be careful buying more debt in a company where you already hold equity (Harvest Partners, 2009 Wharton PE conference, KaW, Aug. 5, 2009).

**FINANCIAL AND QOE**

The Quality of Earnings walk: reported net income (from the books) → reported EBITDA (+ interest, tax, D&A) → adjusted EBITDA (+/- validated add-backs) → pro forma EBITDA (+/- pro forma items). Each step must be independently validated.

- Independent QoE walking reported net income to reported EBITDA to adjusted EBITDA to pro forma EBITDA.
- Read the QoE engagement letter and scope first. A QoE carries no assurance: it is an agreed-upon-procedures engagement under SSAE No. 19 (AT-C 215, effective for reports dated on or after July 15, 2021; "no opinion or conclusion"; the engaging parties own the sufficiency of procedures) or a consulting engagement under CS 100. Ask what was NOT tested and whether proof of cash covered every account in the bank confirmations (Journal of Accountancy, Sept. 2020, https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html; PCAOB AT 601, https://pcaobus.org/oversight/standards/attestation-standards/details/AT601).
- A 3-year EBITDA bridge showing each adjustment category. Every management add-back independently validated, not accepted (v7labs.com, https://www.v7labs.com/blog/quality-of-earnings-analysis).
- Haircut management's forecast. The median and mean PE discount to management's EBITDA forecast is 20% (Gompers, Kaplan, Mukharlyamov, NBER w21133). Show the haircut explicitly in the base case.
- Compare the last three budgets with actuals. About a quarter of misstatements in 49 SEC AAER firms began as unintentional, optimistic errors before sliding into intentional misreporting; overconfident executives misreported more and were not monitored more closely (Schrand and Zechman 2012, URL in 5.2). A pattern of optimistic misses is a fraud precursor.
- Proof of cash: reconcile bank deposits to reported revenue for 36 months (notveryprivateequity.com).
- Forensic revenue testing of the target, not a review of the seller's QoE alone. HP paid $11B for Autonomy (2011) and wrote down $8.8B in 2012 over alleged accounting problems (Feldman and Chunduru, KaW 2025).
- Customer-side revenue test: for the top 10 customers, compare the target's reported sales to each customer with the customer's own purchase, inventory or AP trend (filings, confirmations, or ask). Across about 30,000 supplier-years (1976 to 2018), the gap between supplier sales growth and major customers' purchase growth, and sharp jumps in customers' inventory and payables, predicted revenue fraud; the customer-inventory/AP variable alone carried about half the power of the 11-variable Dechow model (Zhang, Li and Li, Yale Insights, https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms).
- Ask for average daily or intra-quarter balances; flag any financing that unwinds just after period-end. Lehman's Repo 105 moved up to $50B off balance sheet at quarter-ends; its auditor knew (YPFS, JFC 1(1), URL in 5.2).
- Add every factoring, supply-chain-finance and receivables-sale facility to leverage. First Brands' lenders thought leverage was about 5x; counting off-balance-sheet factoring and SCF it was closer to 20x (Harker, KaW 2026, URL in 5.2). See Chapter 3.
- Net working capital peg. Set from a trailing 12-month average of normalized NWC. The SPA trues up the price dollar for dollar against it. It is negotiated, not measured, and it quietly moves a turn of value (v7labs.com; modusalliance.com, https://modusalliance.com/insights/buy-side-vs-sell-side-qoe/).
- NWC = current assets minus current liabilities, excluding cash, debt, and income tax.
- Revenue recognition policy documented and compared with prior years.
- Related parties listed, with arm's-length testing.
- Currency or peg mismatch between revenue and debt. Blackstone's Argentina investment, funded with dollar borrowing against a currency peg, lost every dollar (Schwarzman, Yale ECON 252 lecture 20, https://oyc.yale.edu/economics/econ-252-08/lecture-20).

**COMMERCIAL**
- Customer interviews, market study, competitive position, pricing power, pipeline.
- In middle-market deals, commercial diligence happens on management calls, not just in documents (f2.ai, https://f2.ai/blog/how-ai-is-rewriting-the-diligence-to-close-playbook-for-pe-deal-teams).
- Get customer-level volume forecasts directly from the top customers (Paragon, 5.7).
- Ask former employees, vendors and customers directly whether they were ever asked to do something with invoices, payments or records that felt wrong. 43% of occupational frauds are detected by tips; more than half of tips come from employees and almost a third from vendors and customers; owner/executive frauds have a median loss of $475,000, more than 9x employee frauds (ACFE, Occupational Fraud 2026, https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf).

**LEADERSHIP (a full workstream, not a reference call)**
- Base rates: in 196 buyouts, 69% had at least one CEO change during the hold; a quarter of those changed more than once (2.4 transitions on average); over 60% of exit CEOs were appointed after year 2; average holds were 5.5 years with no change, 8.5 with two changes, 11.0 with four. Only 30% of replacements were internal; three-quarters of external hires came from the same sector. Top-quintile portfolio CEOs deliver about 9 points a year above peers (HLS Forum, "The CEO Decision," 2026, https://corpgov.law.harvard.edu/2026/09/23/the-ceo-decision-how-pe-investors-select-and-reassess-leaders-from-entry-to-exit/).
- About 31% of PE firms recruit their own senior team before investing; about 50% after; 58% at some point (Gompers, Kaplan, Mukharlyamov, NBER w21133).
- Four questions: can the incumbent execute this specific plan; can gaps be closed fast enough; who are credible internal and external successors; how will requirements change across the hold. Budget an extended hold in the downside case if a CEO change is likely (HLS Forum 2026, URL above).
- Background-check the CFO, controller and whoever releases wires, not only the CEO. Remote-capable public firms saw misconduct fall about 2 points more after 2020, roughly half the baseline, consistent with collusion being harder to sustain (Barrios, Guo and Zhu, Yale Insights, https://insights.som.yale.edu/insights/remote-work-is-linked-to-decline-in-financial-misconduct). Frauds with three or more perpetrators have a median loss of $324,000 against $55,000 for one (ACFE 2026).

**TAX**
- Historical returns, deferred liabilities, transfer pricing, structuring.

**LEGAL AND COMPLIANCE**
- Confirmatory: corporate, contracts, litigation, IP, employment, real estate, permits.
- Contingent liabilities: model litigation, mass-tort and successor exposure. Bayer-Monsanto ($63B, 2018) erased more than $50B of shareholder value on underestimated litigation risk; BofA-Countrywide (about $4B, 2008) led to at least $17B of mortgage settlements (Feldman and Chunduru, KaW 2025).
- Compliance diligence is expected by prosecutors. DOJ's Evaluation of Corporate Compliance Programs asks whether the acquirer performed comprehensive pre-acquisition compliance diligence (and if not, why), integrated the target into its controls promptly, and audits acquired entities post-close (HLS Forum, 2020, https://corpgov.law.harvard.edu/2020/06/29/justice-department-updates-its-guidance-on-corporate-compliance-programs/). Document scope and gaps in the IC memo; put a 100-day compliance integration and audit plan in the value-creation plan.
- FCPA successor liability: DOJ's M&A policy (2018, folded into its Corporate Enforcement Policy) gives a presumption of declination to an acquirer that finds corruption through pre- or post-close diligence, promptly self-discloses, cooperates and remediates (HLS Forum, 2018, https://corpgov.law.harvard.edu/2018/08/14/fcpa-successor-liability/). For targets with foreign agents, government customers or licences, run agent diligence and plan the disclosure decision before signing.
- Test the whistleblower hotline: call or email it during diligence. In a field study of nearly 250 firms, one-fifth had a non-functional channel; firms with predicted control weaknesses or recent sanctions were more likely to discourage anonymity; tip-detected frauds run a median 17 months against 24 (auditor) and 36 (law enforcement) (Soltes, HBS 2018, URL in 5.2).
- A clean public search is weak evidence. Internal records at large multinationals show more than two substantiated misconduct instances per firm per week, about 64 times the most expansive public database (Soltes, J. Financial Crime 2019, https://papers.ssrn.com/abstract=3347159). Request the internal investigations log and how each matter closed.
- Public targets, take-privates and carve-outs: diff the last 8 quarters of filings (risk factors, MD&A, legal proceedings) and require an explanation of each material edit. Firms that change filing language later show lower earnings and returns and higher bankruptcy risk; a short-changers/long-non-changers portfolio earned up to 188 bp a month for up to 18 months (1995 to 2014) (Cohen, Malloy, Nguyen, "Lazy Prices," JF 2020, NBER w25084, https://www.nber.org/papers/w25084).
- Regulated manufacturing (pharma, food, supplements, devices): independent data-integrity audit of quality systems (raw lab data against reported data, FDA 483s and warning letters, audit trails) (Akorn, 5.7).
- Antitrust on serial add-ons: sub-HSR deals are not safe (killer acquisitions cluster below thresholds, Cunningham, Ederer and Ma, JPE 2021; FTC suit against U.S. Anesthesia Partners and Welsh Carson, 2023 [VERIFY dates and order terms on ftc.gov]). Healthcare roll-ups: see the Healthcare Services chapter.

**HR AND LABOR**
- Union contracts, open grievances, and pension or withdrawal liability. One Yale SOM-affiliated sponsor walks away when it cannot reach a workable union agreement (Blumenthal, Yale Insights, URL in 5.2).
- Multiemployer pension exposure and the fund's common-control position (5.12).
- No-poach, non-solicit and wage-fixing provisions in franchise agreements, employment agreements and vendor contracts; non-compete enforceability by state (Krueger and Ashenfelter, NBER w24831, https://www.nber.org/papers/w24831; see 7.8).

**IT AND CYBER**
- Budget cyber diligence before signing. Verizon cut $350M from the Yahoo price after late discovery of undisclosed breaches (Feldman and Chunduru, KaW 2025).

**HEALTHCARE AND GOVERNMENT-REIMBURSED TARGETS**
- PE ownership of nursing homes raised short-term patient mortality by about 10% to 11% (about 1.7 points, within 15 days of discharge); frontline nursing-assistant hours per patient-day fell about 3%; costs shifted to monitoring fees, interest and lease payments (1,674 acquisitions in 128 deals among 12,400 for-profit homes) (Gupta, Howell, Yannelis and Gupta, NBER w28474, https://www.nber.org/papers/w28474; KaW, Jul. 22, 2024, https://knowledge.wharton.upenn.edu/article/how-to-align-private-equity-motives-with-nursing-home-outcomes/). CHECK: model regulatory and reputational exposure from staffing and quality metrics (government pays about 75% of nursing-home revenue), and fee, lease and interest leakage to the sponsor or landlord. Full sub-playbook: Healthcare Services and Physician-Practice Roll-Ups chapter.

**OTHER WORKSTREAMS**
- IT and cyber. HR and benefits. Insurance. Environmental. ESG.

## 5.4 The numbers

| Metric | Cited figure | Source |
|---|---|---|
| Entry multiples, middle market | 6x to 10x EBITDA. Higher for strategic or growth targets. **WEAK** (advisor blog; no primary such as GF Data or PitchBook-LCD retrieved) | soferadvisors.com (https://soferadvisors.com/insights/blog/what-is-a-leveraged-buyout-lbo-structure-explained/) |
| Lower anchor: small-company acquisitions | Median international search-fund acquisition: $12M price, $8M revenue, 26% EBITDA margin, 5.7x EBITDA, 1.4x revenue (2026 study) | IESE, International Search Funds 2026, https://www.iese.edu/media/research/pdfs/ST-0689-E |
| Direct lender share of middle-market LBOs | About 70% in 2024. **WEAK** (Bain via an advisor blog) | Bain via ctacquisitions.com (https://ctacquisitions.com/lbo-meaning/) |
| Private credit vs leveraged loans (2025 issuance) | Private-credit borrowers: median debt/EBITDA 5.0x, average interest coverage 2.2x; leveraged-loan borrowers 3.2x and 3.7x | Federal Reserve FEDS Note, Aug. 11, 2026, https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html (see Chapter 3) |
| "Leveraged" threshold | Above 4.0x total or 3.0x senior is a common definition of "leveraged," not a cap. SR 13-3 flags 6x total leverage as raising supervisory concern for most industries. [confirm wording against the SR letter text] | Federal Reserve SR 13-3 (Interagency Guidance on Leveraged Lending, March 2013), https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm |
| Survey leverage (2012 market) | Median target debt/total capital 60%, debt/EBITDA 4.0x (against 70% and 5.2x in Axelson et al. 2013 data). About two-thirds set leverage "as much as the market will bear"; fewer than 10% cite financial flexibility. | Gompers, Kaplan, Mukharlyamov, NBER w21133 |
| Historic buyout structure | "About three dollars of debt for every one dollar of equity" (Blackstone, 2008). Dated. | Schwarzman, Yale ECON 252 lecture 20 |
| Permitted vs closing leverage | About half of borrowers close below 5x, yet over 70% of contracts permit later senior secured debt above 5x; over three-quarters of 5x borrowers can go above 6x | Ivashina and Vallee, "Weak Credit Covenants," NBER w27316, https://www.nber.org/papers/w27316 |
| When a QoE is commissioned | Above about $5M EBITDA or $20M to $30M enterprise value. **WEAK** (advisor) | modusalliance.com |
| LMM diligence timeline | 60 to 90 days from LOI to close. **WEAK** (advisor) | ctacquisitions.com (https://ctacquisitions.com/lower-middle-market-private-equity-2026/) |
| Management forecast haircut | 20% median and mean | Gompers, Kaplan, Mukharlyamov, NBER w21133 |
| Target returns | Gross IRR about 22% (20% to 25%); MOIC median 2.5x, mean 2.85x | same |
| Management equity | 17% of equity to management and employees on average, about 8% to the CEO (15% and 6% at larger firms); public-company median CEO ownership about 1.6% | same |
| Portfolio boards | Over 90% have 5 to 7 members: PE about 3 seats, management 1 to 2, outsiders 1 to 2 | same |
| CEO change during hold | 69% of buyouts | HLS Forum 2026 (5.3) |
| Exit routes | About 50% strategic, 30% financial, under 20% IPO | Gompers et al.; Stromberg 2008 |
| M&A underperformance | 70% to 90% of deals underperform expectations | Feldman and Chunduru, KaW 2025 |
| Sponsor fees charged to targets | Monitoring fees 1% to 5% of portfolio-company EBITDA a year, typically offset 80/20 in LPs' favor; about 80% of buyout LPAs share transaction fees with LPs (a third return 100%, a third split 50/50); median buyout fund PV of GP revenue $19.36 per $100 committed ($10.34 management fees, $5.35 carry, $1.44 entry transaction fees, $2.11 monitoring and exit fees); median lifetime management fees 12% of committed capital (IQR 10% to 13.5%); 93.1% of buyout funds had a hurdle (8% modal) (1992 to 2006 sample) | Metrick and Yasuda, Wharton WP 2007 / RFS 2010, URL in 5.2 |
| R&W, indemnity, escrow and earnout terms | See 5.10 and 5.11 | ABA 2025; SRS Acquiom 2025; Aon 2026 |

- Model: a full LBO with base and downside cases. The downside is built to test the debt package and the covenants.
- Show leverage at close beside maximum permitted senior secured leverage, computed by summing all incurrence baskets, ratio debt and EBITDA add-backs (Ivashina and Vallee, URL above). The average credit agreement has 79 carve-outs and a debt basket above 2.3x EBITDA (same).
- Justify leverage by the target's cash-flow volatility, not by what lenders will provide (Gompers et al.).
- Widen management's scenario ranges about 2x before stress testing; build the downside from base rates, not the sponsor's scenario tab (Ben-David, Graham and Harvey, QJE 2013, NBER w16215, https://www.nber.org/papers/w16215).
- Show the exit multiple against entry, and a case at entry minus 1 to 2 turns (Gompers et al.; see 5.14).
- Search funds and ETA: aggregate U.S./Canada pre-tax IRR 33.9% and ROI 4.75x across 382 acquisitions (Stanford GSB 2026 Search Fund Study as cited by IESE, https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations); international median acquisition returned only 1.1x and about 21% of concluded funds lost money (IESE 2026). The 2007 figures (about 37% average IRR, $4M to $11M EV) are superseded (KaW podcast, 2007, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/looking-for-a-company-to-run-search-funds-could-be-the-answer/; **WEAK**, dated). Full sub-playbook: Search Funds and ETA chapter.

## 5.5 Third parties

QoE from a Big Four firm or A&M or Grant Thornton (ctacquisitions.com; **WEAK** as a provider list). The provider's brand matters less than the scope: proof of cash on every account, NWC, and revenue cut-off, under a stated SSAE 19 AUP or CS 100 engagement (Journal of Accountancy 2020, URL in 5.3). The R&W underwriter will review the buy-side QoE, legal and tax reports and exclude matters not diligenced, so the scope you buy sets the coverage you get (Aon 2026, https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study).

Also: commercial diligence firm. Legal, tax, IT and cyber, environmental, and insurance advisors. R&W insurance broker. Background checks on management, CFO, controller and wire releasers. Regulatory counsel and an independent data-integrity auditor in regulated manufacturing. FCPA/agent diligence provider for foreign-exposed targets. Healthcare regulatory counsel and coding auditor for government-reimbursed targets.

## 5.6 Legal and structure

- Purchase agreement (SPA or APA), reps and warranties, disclosure schedules.
- Indemnities, escrow or holdback, earnouts, R&W insurance.
- NWC true-up mechanism.
- Debt commitment papers, equity rollover, management incentive plan (benchmarks in 5.4).
- Reference the ABA deal points studies for market terms. Now quantified in 5.10.
- **Anti-reliance clauses cut both ways.** Delaware will not let a contract shield deliberate misrepresentations inside the agreement, and fraud claims based on diligence statements have survived non-reliance clauses in some cases. Do not rely on litigation as the remedy: put findings in the price, the model and specific indemnities (HLS Forum, "The Looming Specter," 2017, https://corpgov.law.harvard.edu/2017/07/19/the-looming-specter-post-closing-fraud-claims-in-private-company-ma-litigation/).
- **Specific indemnities and closing conditions for every known regulatory issue.** Do not rely on a general MAE. In Akorn, the agreement did not carve out diligence-disclosed matters (Skadden, https://www.skadden.com/insights/publications/2018/10/analyzing-akorn).
- **Diarize remedies.** Keep a dated list of fraud limitations periods and indemnity-survival deadlines; for every unverified fact, name the rep or indemnity that covers it (Cloudbreak, 5.13).
- **Sponsor fee agreements with the target.** Ask for every transaction, monitoring, director and exit fee and the LPA offset. A monitoring agreement with acceleration on exit is a red flag: SEC fined four affiliated PE advisers $12.5M plus $37.5M disgorgement (2015 to 2016) for accelerating monitoring fees on exit without adequate disclosure (HLS Forum, 2016, https://corpgov.law.harvard.edu/2016/12/19/the-year-in-review-sec-enforcement-actions-against-investment-advisers/; Metrick and Yasuda).
- **Sale-leasebacks and dividend recaps.** Model rent coverage after any sale-leaseback and trace where proceeds went (Steward, 5.7). In 2006 to 2007, lender roundtables reported recaps priced at little discount to LBO leverage; some lenders refused them (KaW, "Lender Roundtable," https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/). Split recap-driven IRR from earnings growth (5.14).
- **Lender documents.** If you are a lender into the LBO: ask who chose lenders' counsel (sponsor-designated counsel is the norm in US mid- and large-cap LBOs), and have your own counsel review baskets, the EBITDA definition and unrestricted-subsidiary provisions; require a J.Crew blocker (HLS Forum, "Sponsor-Designated Lenders' Counsel," 2026, https://corpgov.law.harvard.edu/2026/04/16/sponsor-designated-lenders-counsel/; Ivashina and Vallee). See Chapter 3.
- New subsections: R&W insurance and claims data (5.10); earnouts (5.11); sponsor liability (5.12); SPACs, de-SPACs and PIPEs (5.13); return attribution and the flat-margin base case (5.14).

## 5.7 Failure modes

- Buying inflated EBITDA. Weak add-backs mean the buyer underwrites $7M on $8M marketed, which changes debt capacity and price (privateequitybro.com, https://privateequitybro.com/top-lower-middle-market-investment-banks-to-watch-in-2026/). CHECK: independent QoE with a bridge. Under R&W, a $1M EBITDA miss at 10x becomes a $10M multiple-basis claim (5.10).
- NWC peg set on a favorable month, requiring a Day 1 cash injection. CHECK: peg from a genuine TTM average with seasonality modeled.
- Unrecorded liabilities: deferred revenue, accrued PTO, gift cards, warranty. CHECK: balance-sheet diligence and proof of cash.
- Customer concentration and key-person risk surfacing after close. CHECK: commercial diligence and reference calls; customer-level volume forecasts from the customers.
- Off-balance-sheet leverage (factoring, SCF) and double-pledged collateral. CHECK: every facility added to leverage; UCC sweep; item-level dedupe (First Brands, 2025; Chapter 3).
- Hints in the data room that nobody asks about. CHECK: written question log (Paragon).
- Known regulatory defects papered by a general MAE. CHECK: data-integrity audit and specific closing conditions (Akorn).
- Stock consideration from an undiligenced buyer. CHECK: diligence the buyer as hard as a target (Cloudbreak).
- Return that depends on multiple expansion or margin expansion with no named driver. CHECK: flat-margin, exit-equals-entry case (5.14).

**Case files.**

| Company, year | What happened | THE CHECK that would have caught it |
|---|---|---|
| Paragon Metals Holdings v. Smith (Del. Supr. 2026) | Sponsor paid $100M for an auto-parts maker; the day after closing learned two of the largest customers planned sharp volume cuts; later defaulted on acquisition debt and injected $37M. The CEO withheld a customer letter, stripped volume-reduction terms from a contract amendment, routed a $300K rebate through a foreign affiliate to keep it off the books, and destroyed his phone. The buyer had seen hints (references to volume declines and a cancellation letter), but its negotiator never asked the prepared questions in customer meetings, nobody read the CEO email summarizing the letter, and the model was not updated. The fraud claim was revived only after years of litigation (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/07/30/are-hints-disclosures-delaware-supreme-court-revives-ma-fraud-claim-despite-buyers-red-flags/). | Convert every hint into a written question, ask it in customer meetings, document the answer, re-run the model. Get customer-level volume forecasts directly from top customers. |
| Fresenius / Akorn, 2017 to 2018 | Fresenius's diligence flagged testing and manufacturing deficiencies; it signed anyway. Post-signing whistleblower letters led to an investigation finding falsified data and FDA submissions with false data. Delaware Chancery (2018) let Fresenius walk under the MAE clause, the first such ruling, but noted the agreement did not carve out diligence-disclosed matters. Akorn's CEO testified he never read the audit reports he received (Skadden, URL in 5.6; Del. Ch. opinion, https://law.justia.com/cases/delaware/court-of-chancery/2018/ca-2018-0300-jtl.html). | Independent data-integrity audit (raw lab data against reported, 483s, warning letters, audit trails); specific closing conditions or indemnities for each known regulatory issue. |
| Cloudbreak Health / UpHealth de-SPAC, closed June 2021 (Edwards v. GigAcquisitions2, Del. Ch. July 2025) | See 5.13. Fraud claim dismissed as time-barred. | Diligence the buyer as hard as a target; diarize limitations periods. |
| Toys "R" Us, $7.5B LBO 2005 (Bain Capital, KKR, Vornado); Chapter 11 Sept. 2017, then liquidation | Debt service and 2018 to 2019 maturities, combined with failure to adapt to e-commerce (KaW podcast, "The Demise of Toys R Us," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-demise-of-toys-r-us/). | Maturity wall tested against a secular-decline revenue case, not a cyclical one; count the capex needed to stay competitive before debt service. |
| Steward Health Care / Cerberus; Chapter 11 May 2024 | A 2016 sale-leaseback of hospital real estate to MPT ($1.25B for Massachusetts) funded dividends and left escalating rents (Brookings, https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/; lease channel evidence in Gupta et al., NBER w28474). | Model rent coverage after any sale-leaseback and trace where the proceeds went. |
| J.Crew (TPG and Leonard Green, from 2011), 2016 to 2017; Chapter 11 May 2020 | Investment basket plus a carve-out used to move about $250M of brand IP to an unrestricted subsidiary, backing new debt; senior loan prices fell on announcement (Ivashina and Vallee, NBER w27316). | For lenders: read investments, unrestricted-subsidiary and IP-transfer provisions; require a J.Crew blocker. |
| Verizon / Yahoo, 2017 | $350M price cut after late discovery of undisclosed data breaches (Feldman and Chunduru, KaW 2025). | Cyber diligence before signing. |
| HP / Autonomy, 2011 to 2012 | $11B purchase; $8.8B write-down over alleged accounting problems (same). | Forensic revenue testing, not reliance on the seller's numbers. |
| Bayer / Monsanto, 2018 | $63B deal; more than $50B of shareholder value erased on underestimated litigation (same). | Contingent-liability model including mass tort. |
| BofA / Countrywide, 2008 | About $4B deal; at least $17B of mortgage settlements (same). | Successor-liability model. |
| Premium-driven value destruction | Tyson-Hillshire (70% premium, about $2B destroyed against fair value near $47/share); GE-Alstom ($22B impairment); Kraft Heinz (more than $28B of write-downs); Microsoft-Nokia ($7.6B impairment on a $7.2B deal); Sprint-Nextel (nearly $30B goodwill impairment); Quaker-Snapple (bought $1.7B, sold $300M); Yahoo-Tumblr (bought $1.1B, sold about $3M) (same). | Walk-away price set before bidding; probability-weighted synergies; dis-synergy line. |
| Frank / JPMorgan, 2021 | Strategic acquirer paid $175M for a startup with fabricated users (see 2.7). | Sample live users in production systems. |
| Riordan, Lewis & Haden / Diabetic Care Rx, settled 2019 | See 5.12. Sponsor named in FCA suit; $21.36M. | Pre-close billing and referral diligence. |
| Blackstone Argentina investment (pre-2008) | Dollar debt against a currency peg; lost every dollar (Schwarzman, Yale ECON 252 lecture 20). | Currency-mismatch test. |

## 5.8 Red flags

- Adjusted EBITDA with no bridge.
- Cash-basis books, no audited or reviewed financials, inconsistent monthly close.
- Seller refuses a buy-side QoE or customer calls.
- Retrade risk: valuation and financing not qualified before the LOI.
- A seller-imposed deadline used to cut diligence (Feldman and Chunduru, KaW 2025).
- Deal champion also owns the valuation model (same).
- A history of budgets missed optimistically (Schrand and Zechman 2012).
- Factoring or supply-chain finance excluded from leverage (Harker, KaW 2026).
- Period-end balances that differ sharply from intra-quarter averages (Repo 105, YPFS).
- References in the data room to volume declines, cancellation letters or rebates nobody has asked about (Paragon).
- A non-functional whistleblower hotline, or no hotline log (Soltes).
- A known regulatory defect handled only by the general MAE (Akorn).
- Monitoring agreement with fee acceleration on exit (SEC 2015 to 2016 via HLS Forum).
- A return case that needs exit multiple above entry, or margin expansion with no named cost line (5.14).
- Stock consideration from a buyer whose auditor recently resigned (Cloudbreak).
- No-poach clauses in franchise or vendor agreements (Krueger and Ashenfelter).
- Sponsor doubling deal pace without doubling its operating bench (Davis et al., NBER w26371).

## 5.9 Hard questions

- Which reported earnings survive the close? Show the bridge.
- How was the NWC peg built, and what was excluded?
- Split the return: how much is growth, paydown, and multiple? How much is from recaps?
- What happens to the debt in the downside case?
- What is our walk-away price, who set it, and is that person on the deal team (Feldman)?
- Which synergies are cost and which are revenue? What is each one's probability and timing? What are the dis-synergies?
- What contingent liabilities (litigation, data breach, product) did diligence price, and how?
- What did the QoE engagement letter exclude, and which bank accounts were not in proof of cash?
- How do the last three budgets compare with actuals?
- For every hint in the data room, what question did we ask, who asked it, and what was the answer (Paragon)?
- What is maximum permitted senior secured leverage under the baskets, against closing leverage (Ivashina and Vallee)?
- What does the return look like with exit multiple equal to entry and margins flat (Thomas; Wasserstein and Thomas)?
- Can this CEO execute this plan, and who is the successor (HLS CEO study)?
- What did diligence find that the R&W policy will therefore exclude, and how is it priced?
- When did we last call the hotline, and what happened?
- How much uncalled capital does the owning fund hold for this company in a downturn (Bernstein et al.)?

## 5.10 R&W insurance: market terms and what claims data say goes wrong

New in v2. Resolves v1's "Reference the ABA deal points studies."

**Market terms.**

| Term | Figure | Source |
|---|---|---|
| RWI used (ABA sample) | 63% of deals (55% in prior study) | ABA 2025 Private Target M&A Deal Points Study (139 agreements, 2024 to Q1 2025): Business Law Today, https://businesslawtoday.org/?p=33407; K&L Gates, Dec. 19, 2025, https://www.klgates.com/2025-ABA-Private-Target-Mergers-Acquisitions-Deal-Points-Study-12-19-2025; Goulston & Storrs, https://www.goulstonstorrs.com/insights/article/2025-aba-private-target-m-and-a-deal-points-study-what-s-market |
| RWI used (SRS sample) | 42% of 2024 deals (44% in 2021) | SRS Acquiom 2025 Deal Terms Study (2,200+ deals, $505B, closed 2019 to 2024), https://media.taftlaw.com/wp-content/uploads/2025/04/15175412/2025-SRS-Acquiom-MA-Deal-Terms-Study-2-page-quick-reference.pdf; https://www.srsacquiom.com/our-insights/reps-warranties-findings/ |
| Reps do not survive closing | 41% of deals (30% prior study) (ABA); 33% of 2024 deals "no survival" (SRS); 57% of RWI deals versus 11% of traditional-indemnity deals (SRS) | ABA 2025; SRS 2025 |
| Survival period where reps survive | 24 months most common (26%), then 12 (23%) and 18 (19%) (ABA); median 12 months (SRS) | ABA 2025 (secondary summaries; confirm with the ABA PDF); SRS 2025 |
| Basket | About two-thirds are true deductibles, typically 0.5% to 1% of transaction value | ABA 2025 (secondary summaries) |
| Indemnity cap | Mean about 16.8% of transaction value (just over 6% in 2021), skewed by a minority of high-cap deals; use the median when published | ABA 2025 |
| PPA escrow | Median 0.98% of transaction value (1.00% in 2023) | SRS 2025 |
| RWI policy limit | Typically 10% to 20% of deal value | Griffith, HLS Forum, 2019, https://corpgov.law.harvard.edu/2019/07/01/deal-insurance-representation-warranty-insurance-in-ma-contracting/ |
| Retention | About 1% of deal value | same |
| Premium | About 2% to 3% of the limit | same |
| Buy-side share | Over 95% of policies; used in roughly half of private-target deals, almost never public | same |
| Seller indemnity | Insured deals: tends to equal the retention (about 1%); uninsured: about 10% of deal value | same |

- **Sources differ on RWI usage (63% ABA versus 42% SRS).** The samples differ (139 ABA agreements; 2,200+ SRS deals). Present both; do not average.

**Claims data.**

| Finding | Figure | Source |
|---|---|---|
| Claim frequency | About 18% of policies bound 2019 to 2023 had at least one claim notification (historical 16% to 20%); AIG: about one claim per six policies (2012 to 2021); underwriters report mid-to-high teens | Aon 2026 Transaction Solutions Global Claims Study, https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study; AIG, https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2023-r-and-w.pdf.coredownload.pdf; Griffith 2019 |
| Payments, North America 2025 | About $440M across about 40 payments; median about $8.2M; average about $10.4M; 41% in the eight-figure range | Aon 2026 |
| What breaches drive paid loss | Financial statements 38% to 40%; material contracts 21%; compliance with laws 15.1%; IP 11% | Aon 2026 |
| Same question, other insurers | AIG W&I sample by count: financial statements 21%, tax 19%, compliance with laws 16%; financial-statement and material-contract breaches grow with claim size. Marsh 2023: financial statements 13% of claim count but nearly half of claimed dollars | AIG (URL above; 2021 edition https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2021-r-and-w.pdf); Marsh via Griffith/HLS Forum |
| Timing | 51% of claims notified more than 12 months after closing; 24% more than 24 months | Aon 2026 |
| Multiple-basis claims | 20.6% of claims (2021 to 2025 policies) alleged loss on a multiple basis; they made up 68% of 2025 paid loss | Aon 2026 |
| Small deals | Deals under $100M were 41% of claims but 34% of deals | Aon 2026 |

**What it means for diligence.**
- Policies exclude anything known to the buyer or its advisors. Whatever diligence finds is uninsured: price it or get a special indemnity (Griffith 2019). What diligence missed but should have found may be disputed (derived from Aon 2026 and Griffith 2019).
- In a walk-away deal the buyer's only recourse for a bad rep is the insurer, net of retention.
- Damages can be multiplied. A $10M EBITDA overstatement at 12x can support about $120M of loss (Griffith 2019). That is why financial-statement reps dominate paid loss.
- The QoE (financial statements), top customer and supplier contract review (material contracts) and regulatory compliance review together explain about three-quarters of insured paid loss (Aon 2026). If budget is limited, those three workstreams come first.
- Half of claims arrive after 12 months, so 12-month survival on any seller indemnity misses most of them (Aon 2026; SRS 2025).
- Moral hazard: insured buyers may diligence less (Griffith 2019). Hold the same floor.
- THE ONE CHECK: read the policy's exclusions against the diligence reports before signing, and list every finding the exclusions will carve out.

## 5.11 Earnouts

New in v2.

- **Frequency.** Outside life sciences, earnouts appear in about one in five private deals (15% in 2019, peak 30% to 37% in 2023, about 22% in 2024); median earnout about 31% of closing payments (2024); median period 24 months. Life sciences: over 80% of private pharma deals, median about 61% of total consideration, often 3 to 5 years. Revenue is the most common metric, then EBITDA. Dispute risk rises with earnout share and length (HLS Forum, "The Art and Science of Earn-Outs in M&A," 2025, https://corpgov.law.harvard.edu/2025/07/11/the-art-and-science-of-earn-outs-in-ma/).
- **Drafting checklist** (same): objective metric definitions with worked examples; explicit efforts standard or a fixed spend commitment; buyer reporting and audit rights; rules on cost allocation, staffing and working capital during the period; acceleration triggers; expert-not-arbitrator scope; records of efforts.
- **Case file: Fortis v. Johnson & Johnson (Auris Health), Del. Ch. 2024; Del. Supr. Jan. 2026.** Earnout milestones for a robotic-surgery product. Chancery found J&J breached its efforts obligations and fraudulently induced one milestone; the Supreme Court partly reversed, holding the negotiated "commercially reasonable efforts" definition let J&J calibrate effort for the first payment but not the rest (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/02/10/drafting-guidance-from-delaware-supreme-court-on-earnouts-efforts-obligations-and-fraud/). CHECK: the efforts definition is the asset; read it before valuing any earnout receivable.
- **Buyer with an overlapping product.** Killer acquisitions (about 6% of pharma deals, clustered below HSR thresholds) put milestone payments at risk when the buyer shelves the asset; require development-effort covenants (Cunningham, Ederer and Ma, JPE 2021).
- **Owner-run and search-fund deals.** Tie seller notes or earnouts to customer retention when relationships are personal to the seller (Search Funds chapter).

## 5.12 Sponsor liability for portfolio companies

New in v2. Control brings liability. For LPs, co-investors and lenders, this is a diligence item on the sponsor as well as the target.

| Channel | Case or rule | CHECK |
|---|---|---|
| False Claims Act | DOJ named PE sponsor Riordan, Lewis & Haden alongside its portfolio pharmacy (Diabetic Care Rx) for financing a kickback scheme; settled 2019 for $21.36M (HLS Forum, "Secondary Liability Risks for Private Funds," 2019, https://corpgov.law.harvard.edu/2019/10/09/secondary-liability-risks-for-private-funds-recent-developments/). | In healthcare and government-contract targets, diligence billing and referral practices before close; FMV support for referral-source arrangements. |
| ERISA multiemployer withdrawal liability | Sun Capital funds held to be a trade or business under common control with a bankrupt portfolio company (D. Mass. 2018), because of active management, GP control of hiring and pay, and board control (same). | Map multiemployer pension exposure; structure fund ownership to avoid 80% common control where withdrawal liability exists. |
| Control-person securities liability | (same) | Independent directors at portfolio level. |
| Veil piercing | (same) | Observe corporate formalities; separate accounts and boards. |
| FCPA | Och-Ziff, 2016 (same). DOJ M&A policy gives a declination presumption for prompt self-disclosure (HLS Forum 2018, URL in 5.3). | Agent and third-party diligence; disclosure decision planned before signing. |
| Board designee conduct | Zync v. Porsche and Footprint (Del. Ch. 2026): aiding-and-abetting and disloyalty claims against investors and designees survived (2.11). | Do not direct designees; document conflicts and alternatives. |
| Healthcare roll-up antitrust | FTC 2023 suit against U.S. Anesthesia Partners and Welsh Carson; Welsh Carson later entered a consent order requiring prior notice of certain acquisitions [VERIFY dates and order terms on ftc.gov] (see the Healthcare Services chapter). | Local market share by specialty; state notice laws. |
| Franchise no-poach | State AG actions and class actions followed the 2018 Krueger-Ashenfelter findings (7.8). | Clause review and open-exposure check. |

- Confirm D&O coverage at both portfolio and fund level (HLS Forum 2019).
- DOJ compliance-program guidance makes the acquirer's pre-acquisition diligence and post-close integration part of how prosecutors judge the company (HLS Forum 2020, URL in 5.3).

## 5.13 SPACs, de-SPACs and PIPEs

New in v2. Applies when you are a target taking SPAC stock, a PIPE investor, or a lender or co-investor in a de-SPACed company.

- **Net cash per share is the number.** For SPACs that merged between January 2019 and June 2020, cash actually delivered per $10 share averaged $4.10 (median $5.70) after redemptions, sponsor promote, warrants and fees ($7.50 before redemptions). Later deals were higher but far below $10 (Klausner, Ohlrogge and Ruan, "A Sober Look at SPACs," Yale Journal on Regulation 39 (2022), https://openyls.law.yale.edu/entities/publication/44dd0075-0956-44d1-bb2e-ea326755b4b5; Yale JREG bulletin, https://www.yalejreg.com/bulletin/net-cash-per-share-the-key-to-disclosing-spac-dilution/). A Harvard Forum critique disputes how much net cash per share predicts returns (reported alongside the Klausner et al. findings; critique not retrieved directly, **WEAK**); present both.
- **Compute it.** Net cash per share = (cash in trust after redemptions minus merger costs minus warrant value) / shares outstanding including sponsor promote. Treat headline EV as unreliable.
- **Diligence the buyer as hard as a target.** Own QoE on the counterparty, call its auditors, ask about any auditor change, and get specific reps on facts you cannot verify.
- **Case file: Cloudbreak Health / UpHealth (closed June 2021; Edwards v. GigAcquisitions2, Del. Ch. July 2025).** Cloudbreak merged with a SPAC and five struggling healthcare companies on oral assurances and management presentations prepared by the counterparty's banker. Documents later showed the presentations overstated revenue and contract value and omitted insolvency and an auditor resignation; the combined company went bankrupt. The fraud claim was dismissed as time-barred: counterparties' agents owed Cloudbreak no duty, the banker's disclaimers should have prompted independent work, and Cloudbreak could have diligenced more (HLS Forum, "Chancery Decision Doubles Down on Due Diligence," 2025, https://corpgov.law.harvard.edu/2025/08/26/chancery-decision-doubles-down-on-due-diligence/). THE CHECK: independent diligence of the stock you receive; diarize the fraud limitations period and indemnity survival dates.
- **PIPE documents.** NVCA published 2025 model PIPE sets (NVCA Model Legal Documents, https://nvca.org/model-legal-documents/). Diligence against the version in force at signing.
- **Hard questions.** What is net cash per share after expected redemptions? Who prepared the projections, and who owes us a duty on them? Has the counterparty's auditor changed in three years? When does our fraud claim expire?

## 5.14 Return attribution and the flat-margin base case

New in v2. Applies to buyouts, ETA, growth equity (Chapter 9) and venture models (Chapter 2).

- **Split every base-case return** into EBITDA growth (itself split into revenue growth and margin change), debt paydown, multiple change, and recap or dividend proceeds. A memo that cannot separate these is asking the committee to approve a hope (goreuben.com; KaW Lender Roundtable on recaps, URL in 5.6).
- **Margins do not expand with scale on average.** In 6,103 US IPO firms (53,079 firm-years, 1975 to 2016), median real sales growth exceeded 8% a year, yet cost-to-sales did not fall and profit-to-sales did not rise; the same held for all US public firms, firms worldwide and private European firms. "If you are going to project efficiency, you have to have some concrete story" (Thomas, Ertan and Lewellen, Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows). **CONTRADICTS** the implicit margin-expansion assumption in many buyout, growth (9.3) and SaaS (2.4 Rule of 40) models. Rule: hold EBITDA margin flat in the base case. Margin expansion only with a line-by-line cost bridge naming each efficiency, with supplier quotes or contracts where volume drives it.
- **Multiple expansion dominates small-buyout outcomes.** In search-fund acquisitions later sold, aggregate enterprise value rose from about $1B to $4B; about 80% came from multiple expansion (6.3x at entry to 15.6x at exit) and about 20% from EBITDA growth; margins fell from 25% to 19%; holds about five years (Wasserstein and Thomas, Yale Insights, Apr. 2026, https://insights.som.yale.edu/insights/do-search-fund-ceos-improve-performance). Returns are back-end-loaded and depend on exit conditions.
- **Do not underwrite multiple expansion.** Buying at 4x and selling at 6x because markets rise "is not a version of value creation that we feel is predictable" (Blumenthal, Yale Insights, URL in 5.2). Base cases exit at or below entry. Sixteen percent of sponsors simply assume exit = entry, which is not conservative if entry was at a cyclical peak; show entry minus 1 to 2 turns (Gompers, Kaplan, Mukharlyamov, NBER w21133).
- **Required cases in every IC memo.**

| Case | Margin | Exit multiple | Other |
|---|---|---|---|
| Sponsor case | As modeled | As modeled | As modeled |
| Base case | Flat at current, plus only named and costed drivers | Equal to or below entry | Management forecast haircut about 20% (Gompers et al.) |
| Attribution test | Flat | Equal to entry | Report how much of the sponsor-case return survives |
| Downside | Flat or lower | Entry minus 1 to 2 turns | Revenue from base rates; ranges widened about 2x (Ben-David et al.); secular-decline case where relevant (Toys "R" Us) |

- **Red-team step.** "Recompute the return with exit multiple equal to entry multiple and margins flat; report how much of the base case survives" (from Thomas et al. and Wasserstein and Thomas).
- **Value-creation reality check.** Sponsors themselves rate cost reduction important in only 36% of deals pre-deal (Gompers et al.). A plan that is mostly cost cuts and multiple expansion leans on the weaker levers.

# 6 Energy and Infrastructure

*Power generation, turbines, gensets, transmission-dependent projects, concessions, carbon capture, project finance. Data centers now have their own chapter (6A); this chapter supplies the contract suite and the numbers that 6A relies on.*

This is live deal flow: data center power islands, gensets, and gas-to-power.

> **WHAT CHANGED IN V2**
>
> - **DSCR.** v1's single "S&P illustrative minimum senior DSCR 1.70x" is wrong as a universal minimum. S&P's current criteria (Dec. 2022, Table 8) set the investment-grade minimum DSCR as a function of operating risk, from 1.10x to 5.00x. Fitch's 'BBB' renewables table and Morningstar DBRS's merchant figures added. See 6.5.
> - **Interconnection timing.** v1's "8 to 12 years in primary hubs" (Goldman via gi-advisors, WEAK) now sits beside 3 to 7 years typical (Princeton ZERO Lab, Dec. 2025), "more than 5 years, and 7+ in places" (Kleinman Center, 2025), and a 61-month median from request to operation (LBNL, 2026). All four shown with sources. See 6.4.
> - **"Executed LGIA" is no longer the finish line.** LBNL: 41% of capacity that signed an interconnection agreement (2000 to 2022) still withdrew by end-2025. The check is revised. See 6.4, 6.7.
> - **Availability-guarantee GAP resolved.** Entergy CCGT toll term sheet (98% summer and winter months, 96% otherwise) and DOE wind O&M checklist (95%). See 6.5.
> - **New sections.** Pre-FID risk capital, transmission and build-rate realism, ERCOT Winter Storm Uri, merchant cannibalization, spark-spread valuation, OBBBA/FEOC tax-credit risk (6.10), concessions and regulated-tariff assets (6.11), carbon capture and CO2 storage (6.12).

---

## 6.1 How it works

In project finance, a special-purpose entity (SPV) borrows non-recourse against the project's contracted cash flows. Equity plus senior debt fund construction. The project repays from offtake revenue (a PPA, a tolling agreement, a lease, or a regulated or concession tariff). Lenders rely on the contract suite and an independent engineer.

**Debt is sized by coverage, not by gearing.** S&P, Fitch and Morningstar DBRS size debt by minimum DSCR and downside resilience; gearing is an OUTPUT of DSCR sculpting, not an input (general-lane review of S&P 2022, Fitch 2012 and DBRS 2025 criteria; see 6.5). Underwrite the coverage table first and let leverage fall out of it.

**Risk capital runs to COD, not to financial close.** Princeton's Net-Zero America defines risk capital as pre-FID capital plus everything committed before the Commercial Operation Date (COD), exposed to development, market, construction and technology-performance risk (Net-Zero America Final Report Summary, Oct. 2021, "Capital mobilization", https://netzeroamerica.princeton.edu/img/Princeton%20NZA%20FINAL%20REPORT%20SUMMARY%20(29Oct2021).pdf).

**Pre-FID capital is 100% at risk.** Pre-FID development spend (interconnection studies, permitting, site control, deposits) is typically incurred 2 to 10 years before COD and is fully lost if the project does not reach FID. Net-Zero America sizes it at about $185B to $190B against about $2.6T of supply-side capital committed in the 2020s, roughly 7% (NZA Final Report Summary, 2021, URL above).

| Capital phase | Typical timing | Risks carried | Who usually funds | How to price it |
|---|---|---|---|---|
| Pre-FID (development) | 2 to 10 years before COD (NZA 2021) | Interconnection, permitting, site control, offtake not signed. Total loss if no FID | Developer equity, development capital | Venture-like. Never at a construction-loan or operating-asset return (NZA 2021) |
| Construction (FID to COD) | 18 to 48 months by technology (Kleinman 2025-26; see 6.4) | Cost overrun, schedule, equipment delivery, energization | Sponsor equity, construction debt, tax equity bridges | Construction risk premium. EPC wrap and LDs move part of it |
| Operations (post-COD) | Life of the PPA or lease | Availability, resource or fuel, price (merchant tail), counterparty | Term debt, institutional equity | DSCR-sized per 6.5 |

CHECK: split the capital stack into pre-FID, construction (pre-COD) and operating dollars and price each separately. The model shows a cash-at-risk curve by month through COD, and the IC memo states the maximum cumulative exposure before first revenue (NZA 2021).

**What kind of asset is it?** Underwrite the one you are actually offered.

| Asset type | What carries the revenue | Binding risk | Read first |
|---|---|---|---|
| Contracted renewables (solar, wind, storage) | PPA with utility or corporate offtaker | Resource (P50 vs P90), curtailment, tax-credit eligibility | 6.5 Fitch table; 6.10 |
| Contracted thermal (CCGT, peaker) | Tolling agreement: offtaker pays capacity, supplies or pays for fuel | Availability, heat rate | 6.5 availability; Entergy toll |
| Merchant or hedged thermal | Spot energy, capacity payments, hedges, revenue puts | Spark spread, scarcity events, cannibalization | 6.5 spark spread; 6.7 Panda Temple, Uri |
| Contracted baseload / nuclear PPAs | Long-tenor PPA with hyperscaler | Counterparty, regulatory challenge to cost shifting | 6.2; 6A |
| Behind-the-meter power island | Lease or energy services contract with data-center tenant | Air permit, fuel, equipment provenance, curtailment interface | 6.4 equipment; 6A |
| Concession, PPP, availability-payment, regulated tariff | Public counterparty or regulator-set tariff | Renegotiation, political turnover, appropriation | 6.11 |
| Carbon capture and CO2 storage | Offtake, tax credit, transport-and-storage tariff | No contracted sink, storage-site characterization | 6.12 |

---

## 6.2 The contract suite and what each protects

*Figure 10 (v1), as a table. Each agreement moves one risk off the SPV.*

| Agreement | Risk moved off the SPV | Counterparty | Read, at minimum |
|---|---|---|---|
| EPC contract | Cost and schedule | EPC contractor | Fixed price, completion date, delay LDs and cap, performance tests, contractor credit and parent guaranty |
| PPA / offtake / toll / lease | Revenue | Utility, corporate, hyperscaler | Tenor vs debt tenor (merchant tail), price, termination rights, credit support, curtailment compensation, change-in-law |
| Interconnection agreement (LGIA) | Grid access | Transmission provider / RTO | Network-upgrade cost allocation, posted security, milestone dates, withdrawal penalties |
| O&M agreement / LTSA | Availability and performance | O&M provider, OEM | Availability definition, exclusions, LDs and LD cap |
| Fuel supply and transport | Fuel cost and availability | Gas supplier, pipeline | Firm vs interruptible transport, backup fuel, compressor power |
| Lenders' documents and IE | Debt, draw certification | Lenders, independent engineer | Draw conditions, DSRA, distribution lock-up, covenant DSCR |
| Tax-credit transfer or tax equity | Credit monetization | Transfer buyer, tax equity investor | Recapture indemnity, begin-construction and FEOC reps (6.10) |
| Concession / availability-payment agreement | Revenue set by public body | Government entity | Tariff-adjustment mechanism, termination compensation (6.11) |
| CO2 transport-and-storage agreement | Disposal of captured CO2 | Pipeline and Class VI operator | Per-tonne tariff, capacity, monitoring (6.12) |
| Hedge or revenue put | Price floor for merchant output | Bank or trading counterparty | Settlement in scarcity events, collateral calls, counterparty credit (6.7 Panda Temple, Uri) |

- **EPC (turnkey, fixed-price).** Transfers cost and schedule overrun to a creditworthy contractor. Mintz calls the EPC contractor's creditworthiness and experience "a critical factor" in lenders' willingness to finance (Mintz, International Project Finance Fundamentals).
- **O&M agreement.** A reputable, experienced operator maintains availability and performance (Mintz). For the availability guarantee, read the definition before the percentage: time-based availability leaves the owner holding the resource and most performance risk; energy-based or production-based guarantees put more on the provider and run lower than time-based. CHECK: the definition, the exclusions (grid outages, force majeure, scheduled maintenance) and the LD cap, not just the headline percentage (U.S. DOE, O&M Agreement Checklist for On-Site Wind Energy, 2023, https://www.energy.gov/sites/default/files/2023-07/om-agreement-checklist-on-site-wind-energy.docx; Definitions of Availability Terms for the Wind Industry, white paper, 2017, https://www.ourenergypolicy.org/wp-content/uploads/2017/08/Definitions-of-availability-terms-for-the-wind-industry-white-paper-09-08-2017.pdf). Benchmarks in 6.5.
- **PPA or offtake.** "The single most important document in the file" (ibinterviewquestions.com, https://ibinterviewquestions.com/blog/project-finance-explained). Watch the merchant tail: a 12-year PPA against an 18-year loan leaves 6 years uncontracted.
  - **Tolling agreement (thermal).** The utility pays a capacity payment conditioned on availability. Entergy's 2020 CCGT toll term sheet requires 98% monthly availability in summer (June to August) and winter (December to February) months and 96% in all other months, and discounts the capacity payment 2% for each 1% shortfall (1% per 1% if the shortfall is force majeure), capped at 100% of the monthly capacity payment (Entergy Services, 2020 ETI CCGT RFP, Appendix B-2 Term Sheet - Toll, https://rfp.entergy.com/ENTRFP/SEND/2020ETICCGTRFP/Documents/04282020/Appendix%20B-2%20-%20Term%20Sheet%20-%20Toll.pdf). The O&M/LTSA guarantee must sit at or above what the toll demands, or the SPV carries the gap.
  - **Long-tenor baseload PPAs with hyperscalers (offtake comparables).** Constellation-Microsoft: a 20-year PPA tied to the restart of Three Mile Island Unit 1 (Crane). Talen-AWS: up to 1,920 MW front-of-meter through 2042, which Talen says significantly reduces its market risk. Kleinman flags two risks: data-center demand that never shows up stranding grid build-out, and behind-the-meter deals shifting costs to other ratepayers, which is regulatory risk to the deal (Kleinman Center podcast, "The Future of Electricity Demand in the AI Era," https://kleinmanenergy.upenn.edu/commentary/podcast/the-future-of-electricity-demand-in-the-ai-era/; company 8-Ks via SEC EDGAR). WEAK on the risk framing (podcast-sourced); the deal terms are in the 8-Ks.
- **Fuel supply agreement.** Secures fuel cost and availability. Critical for gas and thermal. Firm transport, on-site backup fuel, and compressor power that is not on the utility's curtailable list are what kept plants running in Winter Storm Uri (Yale Insights, Hirs, https://insights.som.yale.edu/insights/why-the-texas-power-market-failed; see 6.7).
- **Interconnection agreement.** Secures grid access and queue position. An executed LGIA is necessary but not sufficient: verify network-upgrade cost allocation, posted security, and milestone deadlines (LBNL, Queued Up: 2026 Edition, https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf). Post-agreement permitting and transformer procurement are their own schedule risk (6.4).
- **Independent Engineer (IE) report.** Lenders require it to confirm that the technology is commercially viable, budget assumptions are reasonable, there are no serious environmental issues, permits are in order, and projections are realistic (Wilson Sonsini, Project Finance Primer, https://www.wsgr.com/PDFSearch/ctp_guide.pdf). The IE is selected by the lender but paid by the developer, and certifies each construction drawdown against physical progress. v2 additions: the IE's energy case for renewables is a ONE-YEAR P90 rating case with availability and O&M haircuts, not P50 (Fitch 2012; see 6.5); for any partly merchant plant the IE or market advisor delivers spark-spread distributions, not a single forward curve, and the model must reproduce the plant's historical capacity factor before it is trusted (Princeton ORFE, Carmona and Coulon, https://ar5iv.labs.arxiv.org/html/1205.2299).
- **Concession or availability-payment agreement.** Renegotiation is the norm, not the exception (6.11).

---

## 6.3 Data room index

v1 items:

- Site control: land lease or ownership.
- Interconnection agreement and queue position (LGIA, facilities study).
- PPA, offtake, or hyperscaler lease.
- EPC contract. O&M agreement. Fuel supply agreement.
- Permits and environmental.
- IE report. Financial model.
- Equipment supply contracts and warranties. Insurance.

v2 additions:

- **Interconnection detail.** Cluster assignment and readiness status under FERC Order 2023, readiness deposits posted, network-upgrade cost allocation, security posted, milestone schedule with withdrawal-penalty exposure (LBNL 2026; Kleinman Center, "Will Interconnection Reform Unlock the Grid?," Jul. 8, 2025, https://kleinmanenergy.upenn.edu/commentary/podcast/will-interconnection-reform-unlock-the-grid/). The executed agreement itself, because public queue data often omits or overwrites signed-agreement dates (Kleinman, Jul. 2025).
- **Post-agreement schedule.** Permitting plan and the transmission owner's procurement schedule for high-voltage transformers (Kleinman, Jul. 2025).
- **Surplus or replacement interconnection rights** if the site is a brownfield (existing coal, gas or nuclear site) (NZA 2021).
- **Capital-at-risk curve** by month through COD, split pre-FID / construction / operations (NZA 2021).
- **Energy yield report** with P50 and one-year P90 (renewables) (Fitch 2012).
- **Market advisor report** with spark-spread and capture-price distributions, including other announced capacity in the same zone (Princeton; Crosier, Onghai and Sircar, arXiv 2609.08166, Sept. 2026, https://arxiv.org/abs/2609.08166).
- **Tolling agreement or hedge/revenue-put documents**, with scarcity-event settlement terms.
- **LTSA/O&M availability definitions**, exclusions and LD caps.
- **Fuel:** firm transport contracts, on-site backup fuel capacity, compressor power arrangements, winterization plan and its cost (Yale Insights, Hirs).
- **Tax credits:** begin-construction (safe-harbor) evidence, FEOC supply-chain trace with supplier certifications, tax opinion, transfer agreement with recapture protection (Kleinman, Draves, Apr. 27, 2026, https://kleinmanenergy.upenn.edu/commentary/blog/the-landscape-of-renewable-energy-in-the-united-states-in-an-era-of-subsidy-scrutiny/; REPEAT, Zenodo, Jul. 2025, https://zenodo.org/records/15801701).
- **Water source, priority and cooling design** (Yale Insights, Cort, https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent).
- **Large-load tariff, cost-allocation rules and pending rate cases** of the serving utility, where the project serves a data center (HBS Working Knowledge, https://library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple).
- **Concession agreement**: tariff-adjustment formula, history of adjustments actually granted, termination compensation (Gomez-Ibanez; World Bank; see 6.11).
- **Public funding dependencies**: green-bank, ratepayer-charge or appropriation sources, and whether they can legally be swept (Yale SOM case, Connecticut Green Bank 2018, https://cases.som.yale.edu/connecticut-green-bank-2018).
- **CO2 transport-and-storage agreement** or Class VI permit and storage-site characterization (NZA 2021; see 6.12).
- **Insurance**: bound quotes (not indications) for the hold, named-storm, wildfire and freeze terms (Yale Insights, "Putting a Price on Climate Risk," https://insights.som.yale.edu/insights/putting-price-on-climate-risk; see 11.5).
- **Equipment**: firm purchase orders with serial numbers, FAT and load-bank certificates, delivery dates and deposits (v1 6.4).

---

## 6.4 Diligence checklist

### TECHNICAL

- IE review of technology, budget, schedule, availability, and heat rate.
- Renewables: debt sized on a one-year P90 rating case with availability and O&M haircuts. Wind gets a higher base-case bar because Fitch's portfolio data show most wind projects underperform their P50 (Fitch Ratings, "Rating Renewable Energy Projects," CDFA course deck, July 2012, https://www.cdfa.net/cdfa/cdfaweb.nsf/ord/iefc12-joassin.html/$file/Joassin.%20Fitch%20CJ%20-%20CDFA%20Intro%20Course%207-31-12.pdf).
- Thermal: the plant model reproduces historical capacity factor and heat rate before projections are trusted (Carmona and Coulon).
- Availability guarantee meets or exceeds what the offtake contract demands (Entergy toll: 98%/96%), with definitions and exclusions read (DOE 2023).

### POWER AND GRID

- **Revised v2 check.** Verify an executed interconnection agreement (LGIA) backed by funded substation and network-upgrade commitments, not an early-stage queue filing. Then go further, because 41% of capacity with SIGNED interconnection agreements (2000 to 2022) had still withdrawn by end-2025 (LBNL 2026):
  - network-upgrade cost allocation, and whether the project can afford its share;
  - security posted, and the withdrawal-penalty exposure;
  - milestone deadlines, and whether each is met or at risk;
  - the permitting plan and the transformer procurement schedule (Kleinman, Jul. 2025);
  - the cluster and readiness status under FERC Order 2023 (below).
- Stress the energization timeline against debt-service covenants (plausity.com, https://plausity.com/en/news/ai-data-center-power-due-diligence-grid-cooling-energy-risk). WEAK, vendor source; the practice is standard.
- **Grid connection timelines. Sources disagree; present all and verify per market and per utility.**

| Source | Figure | Scope | Status |
|---|---|---|---|
| Goldman Sachs via gi-advisors.com (v1) | 8 to 12 years | "Primary hubs" for data-center connection | WEAK (secondhand via advisor blog, https://gi-advisors.com/data-center-project-finance-development-commercial-structuring-power-constraints-and-bankability/). Princeton reads it as the worst primary hubs, not the norm |
| Camus, encoord and Princeton ZERO Lab, Dec. 2025 | 3 to 7 years typical, against an 18 to 24 month data-center build | U.S. data-center grid connection | Primary study, but funded by Google, which reviewed it before publication (https://www.rtoinsider.com/wp-content/uploads/2025/12/Whitepaper-dec-2025.pdf) |
| Kleinman Center (Penn), Jul. 2025 | Under 2 years before 2008 to more than 5 years, and 7+ in places | Generator interconnection, U.S. | WEAK (podcast-sourced) (https://kleinmanenergy.upenn.edu/commentary/podcast/will-interconnection-reform-unlock-the-grid/) |
| LBNL, Queued Up: 2026 Edition (data through end-2025) | Median 61 months from interconnection request to COD for projects built in 2025 (36 months in 2015; 22 in 2008). Median request-to-agreement 45 months; agreement-to-COD 31 months (21 in 2008). Projects of 200 MW+ about 59 months | Generator interconnection, U.S. | Primary (https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf) |
| Kleinman Center, Jul. 2025, PJM data | PJM's 2018 to 2020 entry cohort received interconnection agreements only in April 2025 | PJM | WEAK (podcast-sourced) |

  Reading: the LBNL median (about 5 years) and the ZERO Lab range (3 to 7 years) agree in magnitude; 8 to 12 years is a tail, not a base case. Large-load (data center) interconnection is a separate process from generator queues and varies by utility (LBNL 2026, via the general-lane data-center draft). CHECK: get the utility's or RTO's own current timeline for the specific substation, in writing.

- **Completion base rates. A queue position is not power.**

| Source | Base rate |
|---|---|
| LBNL Queued Up 2026 | About 19% of projects (13% of capacity) that requested interconnection 2000 to 2020 reached commercial operation |
| LBNL Queued Up 2026 | 41% of capacity that SIGNED an interconnection agreement 2000 to 2022 had withdrawn by end-2025 |
| LBNL, via Kleinman, Jul. 2025 | About 20% of projects requesting interconnection 2000 to 2018 reached commercial operation by end-2023 (consistent with the 2026 edition) |
| PJM data, via Kleinman, Jul. 2025 | Of projects entering PJM's queue 2014 to 2023, 67% withdrew and 16% are operating. WEAK (podcast-sourced) |

- **Post-agreement delay is its own line item.** In PJM data, permitting delays averaged more than 14 months, and transmission-owner procurement (largely high-voltage transformers) added nearly 20 months. Public queue data often omits or overwrites signed-agreement dates, so get the executed agreement itself (Kleinman, Jul. 2025). WEAK (podcast-sourced; confirm against PJM queue records).
- **FERC Order 2023 checks.** Studies moved to a "first-ready, first-served" cluster process, with readiness deposits that scale with project size. The required maximum cluster-study duration is 150 days. Regions may get variations; PJM, for example, proposed "reasonable efforts" instead of delay penalties. CHECK: the project's cluster, its readiness status, and the region's compliance posture (Kleinman, Jul. 2025). WEAK on the specifics (podcast-sourced); confirm against the FERC order and the RTO's compliance filing.
- **Transmission is the system bottleneck.** Princeton ZERO Lab's REPEAT finds U.S. transmission has expanded about 1% per year; it must rise about 50% faster just to carry current-policy wind and solar growth, and about double for a 2035 net-zero target. If transmission stays at about 1% per year, the low-carbon share of 2030 generation falls from about 75% to about 61%, and roughly half the expected emissions reduction is forfeited (Utility Dive on the REPEAT transmission report, https://www.utilitydive.com/news/repeat-project-carbon-emissions-transmission-report/687446/; REPEAT, https://repeatproject.org). CHECK: any project whose economics need a new or upgraded line (network upgrades in the LGIA, a merchant HVDC line, a renewable energy zone) gets a "no new transmission" downside case with curtailment and basis risk applied.
- **Macro frame only.** Net-Zero America: transmission capacity about doubles by 2050 in the least-cost case, rises to about 5x in the 100%-renewables case, and grows 60% by 2030 in the high-electrification case (interim) (NZA Final Report Summary; NZA Annex F, HV Transmission, https://netzeroamerica.princeton.edu/img/NZA%20Annex%20F%20-%20HV%20Transmission.pdf). Do not cite as project-level demand.
- **Brownfield siting is usually the fastest route to the grid.** Most new thermal capacity could be sited at existing coal, gas and nuclear plant sites, which already hold interconnection rights and water (NZA 2021). CHECK: for a new thermal or data-center power-island project, ask whether the site reuses an existing interconnection (surplus interconnection service, or replacement of a retiring unit).
- **Firm versus curtailable service** for data-center load: see 6A.3.

### MARKET THESIS AND BUILD-RATE REALISM

- **Build-rate realism test.** Net-Zero America's constrained case capped U.S. wind plus solar additions at 35 GW per year, about 30% above the single-year historical record; the historical solar-plus-wind peak used was 21 GW per year (2015). REPEAT later modeled solar needing 44 to 51 GW per year (2023 to 2030) against 19 GW installed in 2021 (NZA 2021; Utility Dive on REPEAT). CHECK: when a sponsor's market thesis assumes national build rates far above any historical year, treat the supply side (EPC crews, transformers, modules, interconnection approvals) as the binding constraint and haircut the schedule.
- **Models assume perfect foresight; your deal does not.** NZA explicitly warns its least-cost pathways assume "rational and efficient markets" with investors responding instantly, while real capital mobilization needs long lead times under deep uncertainty (technology cost, future policy, public acceptance) (NZA 2021). CHECK: when a sponsor cites a national decarbonization or load-growth model as its demand case, ask which assumptions (perfect foresight, unconstrained siting, unlimited transmission) the project actually depends on.
- **Point forecasts of load are not acceptable; ask for a distribution** and for the "everyone builds" case (Crosier, Onghai and Sircar, Princeton, arXiv 2609.08166, 2026; see 6.5).

### OFFTAKE

- PPA or lease tenor versus debt tenor (the merchant tail).
- Offtaker or tenant creditworthiness. For data centers the hyperscaler lease is the collateral. An investment-grade tenant supports high leverage. v2: confirm the lease is with, or guaranteed by, the hyperscaler parent, not an SPV or JV with a terminable lease (Yale Insights, "Who Will Finance the AI Revolution?," https://insights.som.yale.edu/insights/who-will-finance-the-ai-revolution; see 6A).
- Offtake that depends on a data-center customer: hyperscaler-owned versus colocation tenant changes ratepayer and regulatory exposure (HBS Working Knowledge; see 6A.3).
- Merchant or partly merchant: capture-price deck must include other announced capacity in the zone (Princeton arXiv 2609.08166).

### FUEL

- Supply agreement, price, flare or direct-line gas feasibility.
- Firm fuel: firm pipeline transport, on-site backup fuel, and compressor power not on the curtailable list (Yale Insights, Hirs; Uri, 6.7).
- Winterization standard met, and its cost funded.

### WEATHER, SCARCITY AND MARKET DESIGN

- Scarcity-event modelling for a merchant or hedged generator in both directions: the cost of being short a hedge at the price cap, and counterparty default by retailers (Yale Insights, Hirs). In Uri, prices hit the $9,000/MWh cap and some ancillary services $25,000/MWh (same).
- Market-design risk in deregulated power is policy risk: generators were urged to winterize after 2011 but were not paid to, and ERCOT had no enforcement power (same). See 6.10, 11.6.

### RATES

- Run every renewable project model at +200 bp on the debt and the discount rate, and show IRR sensitivity explicitly. Clean-energy assets behave like long-duration growth assets (value falls when rates rise, because capex is upfront and payback spans decades); during the 525 bp Fed tightening, higher financing costs offset much of the data-center demand boost to clean energy (HBS AI Institute summary of Cheema-Fox, Czasonis, Kontu, Serafeim, "The AI-Energy Nexus," HBS WP 26-096, https://aiinstitute.hbs.edu/forget-the-algorithms-follow-the-electricity/).

### POLICY AND TAX CREDITS

- See 6.10: begin-construction evidence, FEOC trace, transfer recapture protection, no-credit downside case.

### EQUIPMENT PROCUREMENT: VERIFY LEAD TIMES AND PROVENANCE

*Figure 11 (v1), as a table, with v2 corroboration. A reservation slot is not a firm order.*

| Equipment | Lead time | Source | Status |
|---|---|---|---|
| New heavy gas turbine | 3 to 7 years; OEMs booking into 2028 to 2029 | nextlerllc.com; semianalysis.com (https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power) (v1) | Corroborated by the two rows below |
| New gas turbine | 4 to 6 years | Kleinman Center podcast, Feb. 2026 (https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/) | WEAK (podcast-sourced) |
| New gas turbine | 5 to 7 years | S&P Global, May 2025, cited by Princeton ORFE (Crosier, Onghai and Sircar, arXiv 2609.08166) | Secondhand from a preprint; consistent with v1 |
| Aeroderivative turbine | 18 to 36 months | semianalysis.com (v1) | WEAK (newsletter) |
| Diesel genset above 2.5 MW | 18 to 24 months | safeguard.sh (v1) | WEAK (vendor) |
| Gensets, industry-wide | Toward about 107 weeks | Power Magazine 2026, via savrn.com (https://savrn.com/blog/ai-data-center-supply-chain) (v1) | WEAK (via vendor blog) |

**Build times by technology (development to operation).** Solar plus storage 12 to 18 months (other Kleinman pieces say 18 to 24 months for solar; the two figures conflict and are shown both). Wind about 2 years. Combined-cycle gas 3 to 4 years. The cost of new gas generation roughly doubled over five years (Kleinman, Draves, Apr. 2026; Kleinman podcast, Feb. 2026; Kleinman, Ying and Hu, "RE+ 2025," Oct. 9, 2025, https://kleinmanenergy.upenn.edu/commentary/blog/re-2025-navigating-the-u-s-power-systems-current-challenges/). WEAK where podcast-sourced.

- New gas turbine lead times now run 3 to 7 years. OEMs are booking into 2028 to 2029 (nextlerllc.com; semianalysis.com). Aeroderivatives run 18 to 36 months (semianalysis.com).
- One major OEM sold out of high-horsepower gensets through 2028 (February 2026 capacity announcement, via savrn.com). Large diesel gensets above 2.5 MW run 18 to 24 months (safeguard.sh). Industry-wide genset lead times stretch toward about 107 weeks (Power Magazine 2026, via savrn.com). WEAK (vendor and aggregator sourcing).
- **Secondary and "grey market."** Used gas turbines run about $1.5M per MW against $2M+ new (Reuters, via startupfortune.com). A secondary market is emerging from canceled and speculative orders tied to failed projects (semianalysis.com). One large buyer canceled about 13 GW of reservations and took a reported loss of about $3.7B (Tom's Hardware). WEAK (secondhand reporting).
- **CHECK provenance.** A slot reservation is a paid option, not firm or installed equipment (Yahoo Finance). Verify the FAT (factory acceptance test per ISO 8528-5), the load-bank test certificate with serial number, and warranty terms for new-surplus versus refurbished (depco.com; cigroup-us.com).
- **Transformers are on the critical path twice:** in the project's own substation and in the transmission owner's network upgrades (nearly 20 months of added delay in PJM data, Kleinman, Jul. 2025, WEAK). CHECK: the project's in-service date is later than both transformer delivery dates.

---

## 6.5 The numbers

### DEBT SERVICE COVERAGE IN PROJECT FINANCE

> **CORRECTION TO V1.** v1 listed "S&P illustrative minimum senior DSCR 1.70x" as a single benchmark (citing the 2017 S&P criteria hosted by Maalot, https://maalot.co.il/Publications/MT20171116151537.pdf). That is wrong as a universal minimum. Under S&P's current General Project Finance Rating Methodology (Dec. 14, 2022), the minimum DSCR consistent with investment grade depends on the Operations Phase Business Assessment (OPBA, 1 = lowest operating risk, 12 = highest) and ranges from 1.10x to 5.00x. A 1.70x minimum DSCR is investment grade for a mid-risk asset (OPBA 5 to 8) and is not enough for a high-risk one (OPBA 9 to 12). The threshold is a function of asset risk, not a constant.

**S&P Global Ratings, General Project Finance Rating Methodology, Dec. 14, 2022, Table 8: forecast MINIMUM DSCR needed for a 'bbb' (investment-grade) outcome** (https://maalot.co.il/Publications/MT20221215151143.PDF)

| OPBA (operating risk) | Minimum DSCR for 'bbb' | Typical fit (judgment, not S&P's mapping) |
|---|---|---|
| 1 to 2 | 1.10x to 1.20x | Availability-based or fully contracted, simple technology, strong counterparty |
| 3 to 4 | 1.175x to 1.40x | Contracted renewables, contracted thermal with tolls |
| 5 to 6 | 1.30x to 1.75x | Contracted with more volume or operating risk |
| 7 to 8 | 1.60x to 2.50x | Partly merchant |
| 9 to 10 | 2.50x to 5.00x | Largely merchant |
| 11 to 12 | No investment-grade outcome; 3.00x or more only gets 'bb' | Highest-risk merchant |
| Any (even OPBA 1 to 2) | Below 1.05x maps to 'b' | |

The "typical fit" column is this bible's illustration of how asset types tend to map, not S&P's table; S&P assigns OPBA from its own operating-risk analysis. Ask the sponsor or its rating adviser for the OPBA it expects and why.

**S&P downside resiliency (Table 9).** "Very high" resiliency requires DSCR always above 1.0x in the downside scenario AND downside DSCRs mapping to at least 'bbb' in most periods; "Low" means liquidity reserves are depleted by year three. "Stronger liquidity reserves" are defined as at least one year of debt service or at least 5% of total project debt (S&P 2022, Table 9). CHECK: ask the sponsor for the downside case and the year in which the DSRA is exhausted.

**S&P liquidity notching.** Liquidity is "less than adequate" (minus at least one notch) if sources do not cover next-12-month debt service 1x, if there is no dedicated DSRA, or if a 10% CFADS decline (OPBA 1 to 4) or 15% decline (OPBA 5 to 12) would breach a covenant. Strong liquidity (plus one notch) needs sources/uses above 2.0x (OPBA 1 to 6) or 2.5x (OPBA 7 to 12) and reserves covering 12 months (OPBA 1 to 6) or 18 months (OPBA 7 to 12) of debt service (S&P 2022, liquidity section).

**Fitch Ratings, indicative 'BBB' coverage for fully contracted renewable projects with investment-grade offtakers (average DSCR)** (Fitch, "Rating Renewable Energy Projects," CDFA course deck, July 2012, URL in 6.4)

| Technology | Base case | Rating case (one-year P90 plus availability and O&M haircuts) |
|---|---|---|
| Solar PV | 1.40x or more | 1.30x or more |
| Concentrated solar (CSP) | 1.50x or more | 1.40x or more |
| Wind | 1.60x or more | 1.30x or more |
| Biomass / geothermal | 1.60x or more | 1.40x or more |

Dated (2012) but primary; later Fitch rating actions continue to cite 1.30x rating-case minima (general-lane review). Wind's higher base-case bar reflects Fitch's portfolio data showing most wind projects underperform their P50.

**Morningstar DBRS (Feb. 2025, discussing its Dec. 2024 project-finance methodology).** A merchant hydro, wind or solar project may need a DSCR of about 1.5x to 1.7x to reach minimum investment grade, and a merchant THERMAL project roughly three times that (Morningstar DBRS, "Takeaways From the Evolution of Project Finance Event," Feb. 4, 2025, https://dbrs.morningstar.com/research/447217).

> **CONFLICT: what "fully merchant" needs.** v1 (Credit Agricole CIB) says merchant cash flows need 2.00x minimum, and the practitioner band says "2.00x and above." DBRS (2025) says merchant renewables may reach minimum investment grade at about 1.5x to 1.7x, below the 2.00x floor, while merchant thermal needs roughly three times that, far above it. S&P 2022 puts largely merchant assets (OPBA 9 to 10) at 2.50x to 5.00x. Do not average. Read 2.00x as a floor for merchant renewables in bank practice, and as far too low for merchant gas. Size merchant thermal off the S&P OPBA 9 to 12 rows and the DBRS thermal comment, and test at the 10th-percentile spark spread (below).

**Moody's.** Moody's Power Generation Projects methodology (Jan. 2022) sits outside its generic project-finance methodology; its scorecard grid is behind registration and was not retrieved (Moody's generic PF methodology scope, https://ratings.moodys.com/api/rmc-documents/361401; Moody's rating action on Longview Power citing the Jan. 2022 methodology, https://www.yahoo.com/video/longview-power-llc-moodys-upgrades-191706199.html). GAP, WEAK. Until pulled, use S&P Table 8 and the Fitch table as primary anchors.

**v1 benchmark table, retained with v2 status**

| Benchmark | Figure | Source | v2 status |
|---|---|---|---|
| S&P illustrative minimum senior DSCR | 1.70x | S&P Global Ratings project finance criteria (2017, Maalot host) | CORRECTED. Replace with S&P 2022 Table 8 (1.10x to 5.00x by OPBA) |
| S&P illustrative minimum total DSCR | 1.20x. At least 1.05x generally for 'BB' | S&P Global Ratings (2017) | Consistent with 2022 Table 8: below 1.05x maps to 'b' even at OPBA 1 to 2 |
| Contracted cash flows | 1.40x minimum | Credit Agricole CIB, Project Bond Focus (https://www.ca-cib.com/sites/default/files/2020-10/Project%20Bond%20Focus%20-%20Wind%202020%20VF.pdf) | Bank practice; sits inside S&P OPBA 3 to 6 and matches Fitch solar base case |
| Merchant cash flows | 2.00x minimum | Credit Agricole CIB | See CONFLICT box: floor for merchant renewables, too low for merchant thermal |
| Contracted renewables (practitioner) | 1.20x to 1.35x | gridlines.com | WEAK (practitioner); superseded by Fitch (1.30x to 1.40x rating case / 1.40x to 1.60x base case) and S&P OPBA 3 to 4 |
| Partly merchant (practitioner) | 1.40x to 1.75x | gridlines.com | WEAK (practitioner); superseded by S&P OPBA 5 to 8 (1.30x to 2.50x) |
| Debt service reserve account | 6 to 12 months | Credit Agricole CIB | Qualified: S&P "stronger" reserves are at least 1 year of debt service or 5% of debt; "strong" liquidity needs 12 months (OPBA 1 to 6) or 18 months (OPBA 7 to 12). 6 months is the floor |

*Figure 12 (v1), as a table: minimum DSCR rises with merchant exposure.*

| Revenue profile | v1 practitioner band | v2 primary anchor |
|---|---|---|
| Contracted renewables | 1.20x to 1.35x (gridlines, WEAK) | Fitch 'BBB': solar 1.40x base / 1.30x rating case; wind 1.60x / 1.30x. S&P OPBA 3 to 4: 1.175x to 1.40x |
| Contracted cash flows | 1.40x minimum (CA-CIB) | S&P OPBA 1 to 6: 1.10x to 1.75x |
| Partly merchant | 1.40x to 1.75x (gridlines, WEAK) | S&P OPBA 5 to 8: 1.30x to 2.50x |
| Fully merchant | 2.00x and above (CA-CIB) | DBRS: renewables about 1.5x to 1.7x; thermal roughly 3x that. S&P OPBA 9 to 10: 2.50x to 5.00x; OPBA 11 to 12: not investment grade |

**Agency digest (v1), now qualified.** v1: a digest of agency scorecards puts power projects above 1.4x to avoid sub-investment-grade, and contracted solar with a PPA above 1.2x for investment grade (publicenterprise.org digest of Moody's and Fitch, https://publicenterprise.org/wp-content/uploads/Project-Finance-September-2024.pdf). WEAK: verify against primary criteria. v2: Fitch's own table puts contracted solar at 1.40x base case / 1.30x rating case for 'BBB', above the digest's 1.2x. The digest figure may reflect a rating-case or a different agency's metric; use Fitch's primary figures. The "above 1.4x" figure for power projects broadly is consistent with S&P OPBA 3 to 6.

**Gearing.** Senior debt about 60% to 80% of project cost. Equity about 20% to 40%, pushed to 20% to 30% for merchant (uspeglobal.com, https://uspeglobal.com/articles/what-is-an-independent-power-producer-ipp-business-models/; jakenenergy.com, https://jakenenergy.com/knowledge/merchant-power-plant-financing.html). WEAK, vendor-sourced. No primary source fixes these percentages in the rating criteria reviewed (general-lane review). v2 rewrite: size debt to the DSCR table (S&P Table 8 / Fitch indicative) on a P90 rating case; gearing of 60% to 80% is the typical RESULT for contracted assets (practitioner, WEAK), lower for merchant. If the gearing was set first and the DSCR backed into, that is the red flag.

> **WEAK note on v1's equity band.** "Pushed to 20% to 30% for merchant" reads as lower equity for riskier assets, the opposite of what DSCR sizing implies. Treat as unverified; merchant projects should carry MORE equity, not less, at the coverage levels above.

### OPERATING METRICS

| Metric | Figure | Source | Status |
|---|---|---|---|
| Capacity factor, gas peaker | About 10% historical average utilization | EIA AEO 2022 (https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf) | Primary |
| Capacity factor, combined cycle | About 30% to 90% by dispatch | EIA | Primary |
| Heat rate, combined cycle | About 6,150 to 7,500 Btu/kWh | Lazard; EIA; World Bank | Primary/institutional |
| Heat rate, simple-cycle turbine | About 8,000 to 10,450 Btu/kWh | Lazard; EIA; World Bank | Primary/institutional |
| Heat rate, lean-burn reciprocating engine | About 7,000 to 8,100 Btu/kWh | Lazard; EIA; World Bank | Primary/institutional |
| Simple-cycle efficiency | Recip 42% to 49%. Aeroderivative 38% to 42%. Older heavy frame 33% to 36% | Prismecs (vendor) (https://prismecs.com/blog/technical-comparison-between-the-gas-turbine-and-combustion-engine) | WEAK (vendor) |
| LCOE, gas combined cycle | About $39 to $101 per MWh (2023) | Lazard LCOE+ v16, April 2023 (https://www.lazard.com/media/2ozoovyg/lazards-lcoeplus-april-2023.pdf) | Dated; Kleinman reports new gas cost roughly doubled over five years (2026) |
| Availability guarantee, LTSA or O&M, gas | About 95% to 98% | Entergy 2020 CCGT toll term sheet: 98% summer/winter months, 96% other months; capacity payment cut 2% per 1% shortfall | RESOLVED (v1 GAP, WEAK removed). Below 95% is off-market |
| Availability guarantee, wind O&M | About 95% (time-based, during hours with sufficient wind) | U.S. DOE O&M Agreement Checklist for On-Site Wind, 2023 | RESOLVED. Higher guarantees cost more; energy-based availability runs lower than time-based |

### MARKET AND DEMAND NUMBERS

- **Merchant generation into data-center demand: the cannibalization trap.** Because each new plant lowers the clearing price earned on the investor's entire fleet, optimal build intensity falls toward zero as capacity accumulates, even while load keeps arriving; uncertainty in load forecasts and execution risk weakens incentives further. Under ERCOT calibration, with no supply response the average wholesale price roughly doubles in a decade; with optimal investment it rises from about $30 to about $46 to $49/MWh over six years, with a wide distribution of outcomes (Crosier, Onghai and Sircar, Princeton ORFE/Bendheim/Andlinger, "AI for AI," arXiv 2609.08166, Sept. 2026; preprint, not peer reviewed). CHECK: a merchant plant underwritten on "AI demand" must show the price deck with other announced capacity in the same zone included (the "everyone builds" case), not just its own MW added to today's stack.
- **Valuing a merchant gas plant.** A gas-fired plant is economically a strip of spark-spread call options (power price minus heat rate times gas price, minus variable O&M and, where applicable, carbon cost), one per dispatch hour across its life (Carmona and Coulon, "Electricity price modeling and asset valuation: a multi-fuel structural approach," https://ar5iv.labs.arxiv.org/html/1205.2299; Carmona, Coulon and Schwarz, "The Valuation of Clean Spread Options," https://ar5iv.arxiv.org/html/1205.2302). CHECK: DSCR is tested at the 10th-percentile spark spread. Panda Temple (6.7) failed on exactly this variable.
- **PJM capacity price shock** (merchant revenue and data-center cost input). Total PJM capacity bills went from about $2.2B for 2023 and 2024 combined to more than $14B in a single year. Capacity costs were about $40B over three years; the market monitor attributes about half to data centers; NRDC cites $47B. The last auction cleared about $16B under a price collar, against about $26B uncapped. About 6.5 GW a year of data-center load is being added through 2030 (Kleinman Center podcast, "How PJM Is Grappling With Data Center Power Demand," Feb. 3, 2026, https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/). WEAK until confirmed with PJM and Independent Market Monitor primary reports (podcast speaker figures; the $40B and $47B figures conflict and are shown both). Use: merchant revenue models that rely on capacity payments need a collar-extension case and a collar-expiry case.
- **Load growth and retail rates.** Retrospective studies saying load growth lowered retail rates (LBNL/Brattle 2019 to 2024; EPRI/Watershed 2015 to 2024) were measured in a period of spare capacity; they say little about wholesale energy and capacity prices once supply is tight (Princeton arXiv 2609.08166). Do not let a sponsor use them to dismiss ratepayer or political backlash risk. See 6A.3 for the HBS utility-level evidence.
- **Data-center load context**: see 6A.2.
- **Secondary-market pricing of infrastructure fund stakes.** LP portfolio pricing H1 2026: infrastructure about 91% of NAV, against all strategies about 87%, buyout 91%, credit 89%, real estate 68% (Jefferies, Global Secondary Market Review, July 2026, https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf). Context for valuing an infrastructure fund interest; cross-reference the Secondaries chapter.

### POLICY AND CARBON NUMBERS

- OBBBA impact sizing: 6.10. CCS cost benchmarks: 6.12.

---

## 6.6 Third parties

Independent engineer. Environmental consultant. Interconnection and grid consultant. Fuel and market advisor. Insurance advisor. Equipment inspector (FAT). Project-finance counsel.

v2 additions:

| Third party | What they deliver | Why (source) |
|---|---|---|
| Market advisor (merchant or partly merchant) | Spark-spread and capture-price distributions, "everyone builds" zone case, capacity-price collar cases | Carmona and Coulon; Princeton arXiv 2609.08166; Kleinman Feb. 2026 |
| Energy-yield consultant (renewables) | P50 and one-year P90, curtailment and basis assumptions | Fitch 2012 |
| Interconnection counsel / RTO specialist | Cluster status, readiness deposits, network-upgrade allocation, withdrawal-penalty exposure | LBNL 2026; Kleinman Jul. 2025 |
| Tax counsel | Begin-construction and placed-in-service deadlines, FEOC "material assistance" analysis, transferability and recapture | Kleinman Apr. 2026; REPEAT Jul. 2025 |
| Supply-chain tracing firm | FEOC trace with supplier certifications | Kleinman Apr. 2026 |
| Weather and winterization engineer | Winterization standard, freeze-event dispatch study | Yale Insights, Hirs |
| Regulatory and political-risk counsel | Concession tariff-adjustment history, termination compensation, appropriation sweep risk | Gomez-Ibanez; World Bank; Yale CT Green Bank case |
| Water-rights counsel | Source, seniority, curtailment priority | Yale Insights, Cort |
| Storage geologist (CCS) | Injectivity, capacity, monitoring plan, Class VI status | NZA 2021 |
| Rating adviser (if debt is rated or to be rated) | Expected OPBA and downside case under S&P 2022 | S&P 2022 |

---

## 6.7 Failure modes

> **CASE FILE: MERCHANT POWER WITHOUT AN OFFTAKE**
>
> **Panda Temple I (2017).** A 758 MW ERCOT combined-cycle plant financed with about $377M of debt and $375M of equity. Filed Chapter 11 in April 2017 after breaching its debt-service reserve covenant. Low spark spreads despite a revenue-put hedge (Pillsbury; Utility Dive, https://www.utilitydive.com/news/panda-temple-bankruptcy-could-chill-new-gas-plant-buildout-in-ercot-market/442582/).
>
> **THE CHECK** Contracted offtake. Merchant-tail stress. DSRA sizing. v2: spark-spread distributions from the market advisor, DSCR at the 10th-percentile spark spread, and the model reproducing historical capacity factor (Princeton ORFE, Carmona and Coulon).

> **CASE FILE: MERCHANT COAL**
>
> **Homer City Generation (2017).** Chapter 11 in January 2017 (Cole Schotz, https://www.coleschotz.com/new-delaware-chapter-11-filing-homer-city-generation-l-p/).
>
> **THE CHECK** Merchant exposure and fuel economics.

> **CASE FILE: SCARCITY EVENT AND FUEL FAILURE**
>
> **ERCOT, Winter Storm Uri (February 2021).** About 30 GW of capacity was missing, against average non-summer load of about 45 GW. Prices hit the $9,000/MWh cap, with some ancillary services at $25,000/MWh. Losses are estimated at about $140B: about $50B in ERCOT charges and about $90B in property and casualty losses. Generators had been urged to winterize after 2011 but were not paid to, and ERCOT had no enforcement power. Gas compression and delivery failed, partly because rolling blackouts cut power to compressors, leaving plants without fuel (Ed Hirs interview, "Why the Texas Power Market Failed," Yale Insights, https://insights.som.yale.edu/insights/why-the-texas-power-market-failed).
>
> **THE CHECK** Firm fuel supply (firm transport, on-site backup fuel, and compressor power not on the curtailable list). Winterization standard and the cost of meeting it. Scarcity-event modelling for a merchant or hedged generator in both directions: the cost of being short a hedge at the cap, and counterparty default by retailers.

> **CASE FILE: CONCESSION RENEGOTIATION**
>
> **Mexico toll-road concessions (late 1980s) and a Brazilian water concession (1996).** Mexico's late-1980s toll-road concessions cost taxpayers over $8B after renegotiation. A Brazilian water concession was abandoned (1996) after a new local government refused a contractual tariff adjustment. Across about 1,000 Latin American concessions, 54% of transport and 74% of water contracts were renegotiated, typically delaying investment, raising tariffs or extending terms (Gomez-Ibanez, Regulating Infrastructure: Monopoly, Contracts and Discretion, Harvard UP 2003, https://www.hks.harvard.edu/publications/regulating-infrastructure-monopoly-contracts-and-discretion; World Bank, Granting and Renegotiating Infrastructure Concessions, https://documents1.worldbank.org/curated/en/678041468765605224/pdf/288160PAPER0Granting010renegotiating.pdf).
>
> **THE CHECK** Counterparty political turnover, the tariff-adjustment mechanism's track record of actually being honored, and termination compensation (6.11).

> **CASE FILE: APPROPRIATION SWEEP**
>
> **Connecticut Green Bank (2018).** The Connecticut legislature redirected a substantial part of the Connecticut Green Bank's revenue to the general fund (Yale SOM case, "Connecticut Green Bank 2018: Finance and Marketing After the Raid," https://cases.som.yale.edu/connecticut-green-bank-2018).
>
> **THE CHECK** Where a program depends on a state green bank, a ratepayer charge or an appropriation, confirm whether the funds can legally be swept, and model their loss (6.10, 11.6).

> **CASE FILE: SPECULATIVE EQUIPMENT RESERVATIONS**
>
> **Large-buyer turbine reservation cancellation (reported).** One large buyer canceled about 13 GW of reservations and took a reported loss of about $3.7B (Tom's Hardware). The buyer and year are not identified in the v1 source. WEAK (secondhand reporting).
>
> **THE CHECK** Slot reservation versus firm order. Equipment provenance and FAT.

**Failure modes and the check that catches each**

| Failure mode | Evidence | CHECK |
|---|---|---|
| Signed interconnection agreement, project still dies | 41% of capacity with signed IAs (2000 to 2022) withdrew by end-2025 (LBNL 2026) | Network-upgrade cost allocation, posted security, milestone deadlines, permitting and transformer schedule, not just the executed LGIA |
| Interconnection delay destroying economics | About 20% of the U.S. data-center pipeline faces power and grid delays (plausity.com, WEAK, vendor). Median 61 months request-to-COD (LBNL 2026) | Executed LGIA with funded upgrades (v1), plus the revised check above. Energization date stressed against covenants |
| Post-agreement delay | Permitting more than 14 months and transformer procurement nearly 20 months in PJM data (Kleinman Jul. 2025, WEAK) | Permitting plan and transformer procurement schedule in the data room |
| Speculative and canceled equipment orders | 13 GW reservation cancellation, about $3.7B reported loss (Tom's Hardware, WEAK) | Slot reservation versus firm order. Equipment provenance and FAT |
| Merchant spark-spread collapse | Panda Temple 2017 | Spark-spread distribution; DSCR at P10 spark spread |
| Scarcity event, fuel failure | ERCOT Uri 2021 | Firm fuel, winterization, two-way scarcity modelling |
| Cannibalization by the market's own response | Princeton arXiv 2609.08166 (2026) | "Everyone builds" zone case |
| No new transmission | REPEAT (transmission at about 1% a year) | "No new transmission" case with curtailment and basis |
| Pre-FID dollars lost | NZA: $185B to $190B pre-FID across the 2020s (2021) | Price pre-FID separately; cash-at-risk curve to COD |
| Tax credit lost or FEOC failure | OBBBA 2025 (6.10) | Begin-construction evidence, FEOC trace, no-credit downside case |
| Public funding swept | Connecticut Green Bank 2018 | Legal sweepability review; model loss of funds |
| Concession renegotiated | Mexico toll roads; Brazil water 1996 | Tariff-adjustment track record; termination compensation |
| Capture plant with no sink | NZA 2021 (6.12) | Signed transport-and-storage agreement or owned Class VI permit |
| Curtailable service sold as firm | PJM 2026 proposals (6A.3) | Written firm/non-firm terms and an hourly curtailment study |

---

## 6.8 Red flags

**RED FLAG** list. v1 items first, then v2 additions.

- A queue position filing presented as secured power.
- A slot reservation presented as owned turbines.
- A merchant project with contracted-level DSCR.
- Used or refurbished gensets with no FAT, no serialized load-bank certificate, and unclear warranty.
- No independent engineer report.
- An executed LGIA presented as certainty of COD, with no network-upgrade cost allocation, posted security, or milestone status (LBNL 2026: 41% of signed capacity withdrew). [v2]
- An interconnection agreement with no permitting plan and no transformer procurement schedule (Kleinman Jul. 2025). [v2]
- A data-center site marketed as having "secured power" whose service is non-firm or curtailable (Kleinman Feb. 2026). [v2]
- A "fast-track" data-center interconnection with no written non-firm or flexible service terms and no curtailment study (Princeton ZERO Lab). [v2]
- A renewable project relying on credits with no begin-construction evidence or FEOC trace (Kleinman Apr. 2026). [v2]
- A demand case built from a single national or ISO load forecast with no distribution and no competing-supply case (Princeton arXiv 2609.08166). [v2]
- Pre-FID development dollars priced as if they were construction or operating dollars (NZA 2021). [v2]
- A sponsor citing the 8-to-12-year or the 2-year timeline as a general rule, rather than a site-specific utility study. [v2]
- Gearing set first and DSCR backed into, or a DSCR quoted without the OPBA or rating case behind it (S&P 2022). [v2]
- Renewables debt sized on P50 rather than a one-year P90 rating case (Fitch 2012). [v2]
- A merchant thermal plant at a merchant-renewables DSCR (DBRS 2025: thermal needs roughly three times the merchant-renewables level). [v2]
- A DSRA below 6 months, or no dedicated DSRA (S&P 2022 liquidity notching). [v2]
- An availability guarantee below 95%, or one that sits below the offtake contract's availability requirement (Entergy 2020; DOE 2023). [v2]
- Gas supply on interruptible transport with no backup fuel, or compressors on the curtailable list (Yale Insights, Hirs). [v2]
- A merchant revenue model that assumes today's PJM capacity collar persists, with no collar-expiry case (Kleinman Feb. 2026, WEAK). [v2]
- A concession with no record of tariff adjustments actually granted (Gomez-Ibanez). [v2]
- A capture project with no contracted CO2 sink (NZA 2021). [v2]

---

## 6.9 Hard questions

v1, with the first question revised:

- Show the executed interconnection agreement and the substation funding. v2: and show the network-upgrade cost allocation, the security posted, the milestone schedule and status, the permitting plan and the transformer delivery dates.
- Is the power contracted, for how long, and against what debt tenor?
- Is the equipment firm-ordered and inspected, or a reservation?
- What is the DSCR in the merchant or downside case, and what is the DSRA?

v2 additions:

- What OPBA do you expect S&P to assign, and does your minimum DSCR clear the Table 8 range for it? In the downside case, in which year is the DSRA exhausted? (S&P 2022)
- Is the energy case P50 or one-year P90? Show both DSCRs. (Fitch 2012)
- What does the availability guarantee define as "available," what is excluded, and what is the LD cap? Does it match the offtake contract's requirement? (DOE 2023; Entergy 2020)
- Is the service firm or curtailable? If curtailed, what runs the load, under what permit, and for how many hours? (Kleinman Feb. 2026; ZERO Lab Dec. 2025)
- What has the queue done to your cluster? What is your withdrawal-penalty exposure? (Kleinman Jul. 2025)
- Who pays for network upgrades and incremental capacity costs, and is that in the lease or PPA? (Kleinman Feb. 2026)
- How much of your capital is pre-FID, how much pre-COD, and what is the maximum cumulative cash at risk before first revenue? (NZA 2021)
- How many MW of other generation are announced or in the queue in your zone, and what happens to your capture price if half of it is built? (Princeton arXiv 2609.08166)
- If the tax credit disappears or the FEOC test fails, what is the equity IRR and does the debt still size? (REPEAT 2025; Kleinman Apr. 2026)
- What happens in a Uri-type freeze: where does the fuel come from, and what do you owe on your hedges at the cap? (Yale Insights, Hirs)
- What is the IRR at +200 bp on debt and discount rate? (HBS WP 26-096)
- Does the site reuse an existing interconnection? If not, why not? (NZA 2021)

---

## 6.10 Policy, tax-credit and appropriation risk (new)

**Tax credits after the One Big Beautiful Bill Act (OBBBA, July 2025).** Status as summarized by the Kleinman Center, April 2026: wind and solar had to begin construction before July 2026, with a four-year completion window, or be placed in service before 2028. Credits phase out starting in 2028 and end by 2032. Transferability was preserved (Kleinman Center, Draves, Apr. 27, 2026, https://kleinmanenergy.upenn.edu/commentary/blog/the-landscape-of-renewable-energy-in-the-united-states-in-an-era-of-subsidy-scrutiny/). Verify against current Treasury and IRS guidance; the deadlines differ by credit and technology, and this is a secondary summary.

**FEOC.** Foreign-entity-of-concern "material assistance" rules apply to facilities beginning construction after December 31, 2025. They can effectively disqualify projects using Chinese-sourced supply or IP, and developers warn PPA prices will rise (Kleinman, Draves, Apr. 2026; Kleinman, Ying and Hu, "RE+ 2025," Oct. 9, 2025, https://kleinmanenergy.upenn.edu/commentary/blog/re-2025-navigating-the-u-s-power-systems-current-challenges/).

**Size of the policy shock.** Princeton REPEAT estimated that the OBBBA, by largely repealing IRA clean-electricity credits, cuts U.S. additions by about 29 GW of solar and 43 GW of wind through 2030 (about 140 GW and 160 GW through 2035), cuts cumulative electricity and clean-fuels investment by about $0.5T over 2025 to 2035, and raises household energy costs about $165 a year in 2030 and $280 a year in 2035. Results are approximate and not peer reviewed (REPEAT Project, "Impacts of the One Big Beautiful Bill Act," Zenodo, July 2025, https://zenodo.org/records/15801701).

CHECK, for any deal whose returns depend on 45Y, 48E or 45X credits or on transferability:

- tax counsel confirms the begin-construction and placed-in-service deadlines under current Treasury guidance;
- safe-harbor evidence (physical work or 5% spend) is in the data room (REPEAT 2025);
- a FEOC supply-chain trace with supplier certifications (Kleinman Apr. 2026);
- the transfer buyer has recapture protection, and who bears recapture is in the transfer agreement;
- a no-credit downside case: equity IRR, and whether the debt still sizes.

**Appropriation and public-funding risk.** Connecticut Green Bank, 2018: the legislature redirected a substantial part of its revenue to the general fund (Yale SOM case). CHECK: where a program depends on a state green bank, a ratepayer charge or an appropriation, confirm whether the funds can legally be swept, and model their loss.

**Ratepayer and political backlash.** A 20% residential bill increase in parts of New Jersey became a 2025 governor's-race issue (Princeton arXiv 2609.08166). Behind-the-meter deals shifting costs to other ratepayers are regulatory risk to the deal (Kleinman podcast, WEAK). See 6A.3 for the HBS utility-level evidence and large-load tariffs.

**Market-design risk.** ERCOT did not pay generators to winterize and had no power to require it before Uri (Yale Insights, Hirs). PJM's capacity collar and its 2026 large-load proposals are rule changes in progress (6A.3). Treat market rules as a variable, not a constant.

Cross-reference 11.6 (policy and appropriation risk across asset classes).

---

## 6.11 Concessions, PPPs, availability-payment and regulated-tariff assets (new)

**How it works.** Revenue is set by a public counterparty (availability payments) or by a regulator or contract formula (tariffs, tolls), not by a market. Harvard's Gomez-Ibanez frames the core risk as the choice between regulation by contract and regulation by discretion: either the contract fixes the tariff path and the government later wants out, or a regulator sets it and can change its mind (Gomez-Ibanez, Regulating Infrastructure, Harvard UP 2003).

**Base rate.** Renegotiation is the norm, not the exception. In about 1,000 Latin American concessions, 54% of transport and 74% of water contracts were renegotiated, typically delaying investment, raising tariffs or extending terms (World Bank, Granting and Renegotiating Infrastructure Concessions, URL in 6.7). Data are Latin American; U.S. availability-payment and regulated assets carry the same structural risk through appropriations and rate cases.

**Diligence checklist.**

- Counterparty: who signs, who pays, and from which budget line. Is payment subject to annual appropriation? (Yale CT Green Bank case; 11.6)
- Political turnover: election calendar of the counterparty over the debt tenor (Gomez-Ibanez).
- Tariff-adjustment mechanism: formula, indexation, and its track record of actually being honored (Gomez-Ibanez; World Bank).
- Termination compensation: on default, on convenience, on force majeure; whether it covers senior debt and equity.
- Availability-payment deductions: definition, measurement, cap (compare the Entergy toll mechanics in 6.5 for the private-offtaker analog).
- Change-in-law and relief events.
- Demand risk retained (tolls) versus transferred (availability payments).

**Failure cases.** Mexico toll roads (late 1980s; over $8B taxpayer cost after renegotiation). Brazilian water concession abandoned (1996) after a new local government refused a contractual tariff adjustment (Gomez-Ibanez; World Bank). See 6.7.

**Red flags.** A concession model that assumes every scheduled tariff increase is granted. Payment dependent on annual appropriation with no termination compensation. A counterparty facing an election before COD with the project as a campaign issue.

**Hard questions.** Show every tariff adjustment the counterparty has granted and refused in the last decade. What do we receive on termination for convenience? Which budget line pays, and can it be swept?

---

## 6.12 Carbon capture and CO2 infrastructure (new)

**Benchmarks (for carbon-capture, blue-hydrogen and Class VI storage deals).** Net-Zero America: CO2 transport and storage cost averages about $17 to $23 per tonne stored, depending on scale. A national build needs over 100,000 km of new CO2 pipelines costing about $170B to $230B. About $13B of storage-site characterization, appraisal and permitting is needed before 2035 to enable expansion. Most sequestration is on the Texas Gulf Coast (NZA Final Report Summary, Oct. 2021, Pillar 4, https://netzeroamerica.princeton.edu/img/Princeton%20NZA%20FINAL%20REPORT%20SUMMARY%20(29Oct2021).pdf). Model-based, 2021 dollars; not a quote.

CHECK: a capture project's model must show a signed transport-and-storage agreement (or owned Class VI permit) with a per-tonne tariff in this range or a justified premium, and storage-site characterization evidence (injectivity, capacity, monitoring plan). Tax-credit dependence gets the 6.10 checks.

**RED FLAG** A capture plant with no contracted sink is a stranded asset (NZA 2021).

**Hard question.** Where does each tonne go, under what signed agreement, at what tariff, and who owns the injection permit?

---

> **THE ONE CHECK**
>
> Delivered power and contracted revenue, sized to a downside case. An executed interconnection with upgrades funded, security posted and milestones met (not merely signed); an offtake that outlasts the debt from a creditworthy counterparty; and DSCR that clears the S&P Table 8 range for its risk class on a P90 or 10th-percentile spark-spread case, with a DSRA that survives the downside. That combination would have caught Panda Temple, and it goes past the signed agreement that 41% of withdrawn capacity in LBNL's 2026 data already had.

---

# 6A Data Centers and Digital Infrastructure

*New in v2. Split from Chapter 6. Hyperscale campuses, powered land, colocation, and the power that decides all three. Uses Chapter 6 for the contract suite, DSCR tables and equipment checks, and Chapter 1 for real-estate mechanics.*

## 6A.1 How it works

**Three distinct risk products share the label.** Underwrite the one you are actually being offered (general-lane draft, primary sources as cited below).

| Product | What you are really buying | Collateral | Binding risk |
|---|---|---|---|
| Powered land and development | Entitlements, interconnection position, power | Option value until power is executed | Power deliverability, energization date, permits |
| Build-to-suit / leased hyperscale campus | A long lease to an investment-grade hyperscaler | The lease and its guaranty (real estate / infrastructure credit) | Who the tenant really is (parent vs SPV), termination and contraction rights, delivery-date LDs |
| Colocation / retail | An operating business | EBITDA | Churn, pricing, power pass-through, ratepayer exposure |

**The financing is moving off balance sheet.** Hyperscaler capex was about $116B in 2022 and nearly $200B in 2024, with 2025 plans of about $80B (Microsoft), $65B (Meta), $75B (Alphabet) and $100B (Amazon). Deals such as Intel's roughly $11B joint venture with Apollo raise capital off balance sheet. Falling model costs (DeepSeek) were flagged as a risk to the economics (Goldman Sachs bankers at Yale, "Who Will Finance the AI Revolution?," Yale Insights, https://insights.som.yale.edu/insights/who-will-finance-the-ai-revolution). Worldwide data-center capex rose about 51% to about $455B in 2024 (HBS AI Institute summary of "The AI-Energy Nexus," HBS WP 26-096, https://aiinstitute.hbs.edu/forget-the-algorithms-follow-the-electricity/). The more of this sits in SPVs and JVs, the more the credit question becomes "who actually owes the rent."

**Power is the binding constraint.** A data center builds in 18 to 24 months; the grid connection typically takes 3 to 7 years (Camus, encoord and Princeton ZERO Lab, Dec. 2025, Google-funded, https://www.rtoinsider.com/wp-content/uploads/2025/12/Whitepaper-dec-2025.pdf). Every other part of the diligence is subordinate to when, and on what terms, the MW arrive.

---

## 6A.2 Demand numbers

The figures differ by year, scope and author. Do not blend them; cite the one that matches your question.

| Metric | Figure | Source | Note |
|---|---|---|---|
| U.S. data-center electricity, 2023 | About 176 TWh, about 4.4% of U.S. electricity | U.S. DOE / LBNL, 2024 United States Data Center Energy Usage Report, Dec. 20, 2024 (https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers) | Primary |
| U.S. data-center electricity, 2028 projection | 325 to 580 TWh, about 6.7% to 12% of U.S. electricity | DOE / LBNL 2024 | The width of the range IS the demand risk |
| U.S. data-center electricity, 2018 to 2025 | 76 TWh (1.9%) in 2018 to more than 200 TWh (4.8%) by 2025 | Crosier, Onghai and Sircar (Princeton), "AI for AI," arXiv 2609.08166, Sept. 2026 (https://arxiv.org/abs/2609.08166) | Preprint |
| U.S. data-center share, 2030 | Up to 15% of U.S. electricity | LBNL projection as cited by HBS Working Knowledge (https://library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple) | Secondhand; different horizon from the DOE/LBNL 2028 range. Confirm the underlying LBNL figure |
| Utility peak demand | Data centers expected to raise peak demand 20% to 40% or more over a decade in the Midwest, Southeast, Southwest and Texas | Princeton arXiv 2609.08166 | Utility forecasts |
| ERCOT | 33 GW of new data-center and crypto-mining demand forecast by 2031 (36% of its 91 GW all-time peak); peak demand of 175 GW by 2032 floated | Princeton arXiv 2609.08166 | Forecasts, not contracts |
| PJM | About 6.5 GW a year of data-center load added through 2030 | Kleinman Center podcast, Feb. 3, 2026 (https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/) | WEAK (podcast-sourced) |
| Global | About 460 TWh, about 2% of global electricity | HBS AI Institute, WP 26-096 | |
| Campus size | Heavily right-skewed: most Texas campuses under 0.5 GW, a few multi-GW | Princeton arXiv 2609.08166 | |

CHECK: underwrite tenant contracts, not the projection. Ask what share of the sponsor's demand case is signed leases, LOIs, and forecast, in MW and by year.

---

## 6A.3 Power: firm versus flexible, the PJM 2026 proposals, and tariff risk

### Firm versus non-firm service

- **PJM, January 2026.** PJM's board letter of January 16, 2026 proposed: "bring your own generation" for firm service; "connect and manage," meaning curtailable service that may force a switch to diesel backup; and a new-supply-only backstop auction with longer-term pricing, subject to FERC approval. In PJM, network service does not prevent curtailment because dispatch is cost-based. In ERCOT, connect-and-manage projects can be curtailed under grid stress (Kleinman Center, "How PJM Is Grappling With Data Center Power Demand," Feb. 3, 2026). WEAK (podcast-sourced); confirm against the PJM Board letter and any FERC filing before relying on the terms. Proposals, not final rules, as of the source date.
- **Most tariffs today offer only firm or non-firm service, often no non-firm option at all,** so a flexible structure frequently does not yet exist (Camus/encoord/ZERO Lab, Dec. 2025). Flexible or conditional-firm large-load tariffs are being written utility by utility (Princeton lane, open gap).
- CHECK: whether the site's power is firm or curtailable, the backup-generation permit and fuel, and who bears incremental transmission and capacity costs (Kleinman Feb. 2026).

### The ZERO Lab flexible-interconnection study

**Source and its limits.** Brancucci, Cutler and Jenkins, "Flexible Data Centers: A Faster, More Affordable Path to Power" (Camus, encoord and Princeton ZERO Lab, Dec. 2025). **Funded by Google, which reviewed it before publication.** Six real 500 MW candidate sites in ONE PJM utility. Critics dispute that AI loads will actually curtail (whitepaper, https://www.rtoinsider.com/wp-content/uploads/2025/12/Whitepaper-dec-2025.pdf; Canary Media summary, https://www.canarymedia.com/articles/data-centers/pjm-needs-flexible-data-centers; EnergyConnects/Bloomberg, https://www.energyconnects.com/news/gas-lng/2025/december/flexible-power-accelerates-data-center-projects-princeton-says).

**Findings** (all from the whitepaper, Dec. 2025):

| Item | Result |
|---|---|
| Baseline | Data centers face 3 to 7 years to connect against an 18 to 24 month build |
| Sites modeled | Six real 500 MW sites in one PJM utility, all 8,760 hours; four were transmission-constrained |
| Time to full operation with flexible connection plus bring-your-own-capacity (BYOC) | About 2 years, 3 to 5 years faster |
| Grid power availability | More than 99% of hours |
| On-site resources dispatched (batteries, generators, compute flexibility) | 40 to 70 hours a year |
| Transmission curtailment | 7 to 35 hours a year, in events of 4 to 16 hours; peak curtailment up to 281 MW at the worst site |
| Generation shortfalls | About 32 additional hours a year, concentrated in extreme weather |
| Firm-only service, per GW of new data-center load | Adds about $764M of annual system supply cost (2.17 GW of nameplate additions) |
| 20% conditional-firm service | Avoids 273 MW of new build ($78M) |
| BYOC | Internalizes $326M of capacity cost |
| Energy payments | Cover $329M |
| Net | The data center covers about $733M per GW |

**How to use it.** As evidence that flexible connection CAN shorten timelines at constrained sites, not as evidence that any given site will connect in two years.

- CHECK for a data-center power deal claiming a "fast-track" grid connection: obtain the utility's written flexible / non-firm interconnection terms, the hourly curtailment study (hours per year, MW curtailed, which hours), and evidence that on-site generation and storage are sized to cover the curtailment window. A non-firm connection is a different collateral from firm service: the hyperscaler lease must tolerate curtailment, or the BYOC assets must be in the security package (Princeton lane).
- **RED FLAG** A sponsor citing the Princeton/Camus result as proof its site will connect in two years. The study covered six PJM sites in one utility territory, was funded by Google, and critics dispute that AI loads will actually curtail. Ask for the site-specific study.

### Grid timelines and queue base rates

Use Chapter 6.4's timeline table (8 to 12 years, Goldman via gi-advisors, WEAK; 3 to 7 years, ZERO Lab; more than 5 and 7+ years, Kleinman, WEAK; 61-month median, LBNL 2026). Large-load (data center) interconnection is a separate process from generator queues and varies by utility; a "will-serve" letter is not an executed electric service agreement (LBNL, Queued Up: 2026 Edition, https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf, via the general-lane draft).

### Tariff, ratepayer and political risk

- **Who pays.** In 385 data centers across 42 utilities (2020 to 2025), data centers explained about 16% of industrial and 4% of residential price increases (about $5.40/MWh industrial, $1.70/MWh residential). Colocation (third-party leased) centers raised consumer costs while hyperscaler-owned ones did not; utilities built for large industrial loads passed through less (HBS Working Knowledge, "Blaming Data Centers for Higher Electric Bills? It's Not That Simple," https://library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple).
- **Retrospective "load growth lowers rates" studies** (LBNL/Brattle 2019 to 2024; EPRI/Watershed 2015 to 2024) were measured in a period of spare capacity and say little once supply is tight. A 20% residential bill increase in parts of New Jersey became a 2025 governor's-race issue (Princeton arXiv 2609.08166).
- **Capacity-cost pass-through.** PJM capacity costs of about $40B over three years, about half attributed to data centers by the market monitor; NRDC cites $47B (Kleinman Feb. 2026). WEAK (podcast speaker figures; confirm against PJM and IMM reports).
- **Behind-the-meter deals** shifting costs to other ratepayers are regulatory risk to the deal (Kleinman podcast, "The Future of Electricity Demand in the AI Era," https://kleinmanenergy.upenn.edu/commentary/podcast/the-future-of-electricity-demand-in-the-ai-era/). WEAK (podcast-sourced).
- CHECK for any data center or power deal serving one: the large-load tariff and cost-allocation rules of the specific utility, pending rate cases, local moratorium risk, and whether the offtaker is a hyperscaler or a colocation tenant (HBS Working Knowledge).

### Merchant generation built for data-center demand

See 6.5: the cannibalization trap (Princeton arXiv 2609.08166). A merchant plant underwritten on "AI demand" must show the "everyone builds" price deck.

### Faster routes to power

- **Brownfield reuse.** Existing coal, gas and nuclear sites already hold interconnection rights and water (NZA 2021, https://netzeroamerica.princeton.edu/img/Princeton%20NZA%20FINAL%20REPORT%20SUMMARY%20(29Oct2021).pdf). Ask about surplus interconnection service or replacement of a retiring unit.
- **Front-of-meter contracted baseload.** Talen-AWS (up to 1,920 MW through 2042) and Constellation-Microsoft (20-year PPA, Crane restart) (Kleinman podcast; company 8-Ks). See 6.2.
- **Behind-the-meter power island.** Chapter 6 contract suite (EPC, LTSA availability 95% to 98%, fuel supply) plus air permits; equipment lead times and provenance per 6.4.

### Water

Phoenix and Front Range data centers depend on Colorado River-linked water certainty. Add "water source, priority and cooling design" to the data room (Todd Cort, Yale Insights, May 2026, https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent). The 1922 Compact allocates 16.5M acre-feet a year against 2000 to 2023 flows of about 12.5M (same). See 11.4 and 11.5.

---

## 6A.4 The contract suite and the lease

| Document | What it protects | Read, at minimum |
|---|---|---|
| Lease (build-to-suit or hyperscale) | Rent, which is the collateral | Term vs debt tenor; early termination and contraction rights; assignment rights; rent escalators; delivery-date LDs and tenant walk rights if late; power pass-through; whether the lease tolerates curtailment |
| Parent guaranty | That the investment-grade parent, not an SPV, owes the rent | Guarantor entity, scope, caps, release triggers (general draft; Yale Insights) |
| Electric service agreement / large-load interconnection agreement | MW deliverable by date | Executed (not a will-serve letter); load ramp schedule; firm vs curtailable; upgrade cost allocation; security posted; energization date with LDs (general draft; LBNL 2026) |
| Flexible / non-firm service terms | Curtailment exposure | Hours and MW the utility may curtail, notice, compensation (ZERO Lab 2025) |
| Behind-the-meter generation contracts | On-site power | EPC, LTSA, fuel supply, air permit (Chapter 6.2) |
| Development agreement and GMP | Cost and schedule | GMP, contingency, contractor's data-center track record |
| Long-lead equipment purchase orders | Delivery | Transformers, switchgear, generators, chillers: delivery dates, deposits, serial numbers (Chapter 6.4) |
| Fiber and carrier agreements | Connectivity | Route diversity |
| Water rights / permits | Cooling | Source, seniority, curtailment priority (Yale Insights, Cort) |
| Property tax abatement | Opex | Clawbacks and job or investment conditions |
| SLAs (operating assets) | Revenue retention | Uptime commitments and credits |

---

## 6A.5 Data room index

- Site control and zoning (is data-center use permitted by right?).
- Utility service agreement, load ramp schedule and tariff; utility facilities study; upgrade cost allocation and security posted.
- Flexible / non-firm service terms and the hourly curtailment study, if any (ZERO Lab 2025).
- Large-load tariff, cost-allocation rules, pending rate cases, local moratorium history (HBS Working Knowledge).
- Behind-the-meter generation: EPC, LTSA, fuel supply, air permit, backup-generation permit and fuel (Kleinman Feb. 2026).
- Fiber route diversity and carrier agreements.
- Water rights / permits, source priority, and cooling design (Yale Insights, Cort).
- Lease(s) with tenant, guaranty, and termination / contraction rights.
- Development budget and GMP.
- Long-lead equipment orders (transformers, switchgear, generators, chillers) with delivery dates and deposits.
- Commissioning plan (Level 1 to 5).
- SLAs and uptime history (operating assets).
- Power pass-through mechanics.
- Property tax abatements and their clawbacks.
- Insurance: bound quotes for the hold (11.5).
- Engineer's report on rack density, cooling (air vs liquid), and retrofit cost.

(Base list from the general-lane draft; additions as cited.)

---

## 6A.6 Diligence checklist

### TENANT AND LEASE

- Identity and credit of the LEASE GUARANTOR (parent vs SPV), lease term vs debt tenor, early termination or contraction rights, rent escalators, delivery-date LDs and tenant walk rights if the building is late (general draft).
- Who is the credit: the hyperscaler parent, or an SPV or JV with a terminable lease? What are the lease term, termination and assignment rights against the debt tenor? (Yale Insights, "Who Will Finance the AI Revolution?")
- Does the lease tolerate curtailment, or must BYOC assets cover it? (ZERO Lab 2025)
- Hyperscaler-owned versus colocation: changes ratepayer exposure (HBS Working Knowledge).

### POWER

- MW contracted vs MW deliverable by date; who bears the cost of upgrades; curtailment or interruptible provisions in the tariff (general draft).
- Executed electric service agreement or large-load interconnection agreement with the utility, the utility's facilities study, upgrade cost allocation and the security posted, energization date with LDs (general draft; LBNL 2026).
- Firm or curtailable; if curtailable, the backup permit, fuel, and hours (Kleinman Feb. 2026).
- Who pays incremental transmission and capacity costs, and is that in the lease? (Kleinman Feb. 2026)
- Brownfield interconnection reuse available? (NZA 2021)
- For behind-the-meter generation, the Chapter 6 contract suite (EPC, LTSA availability 95% to 98%, fuel supply) plus air permits.

### CONSTRUCTION

- Equipment provenance and lead times (Chapter 6.4: a reservation is not an order); contractor's data-center track record; contingency.
- Delivery date later than the transformer delivery date, and later than energization.

### TECHNOLOGY AND OBSOLESCENCE

- Rack density the shell supports (air vs liquid cooling); cost to retrofit if the tenant leaves.
- What happens to the asset if compute demand per dollar falls? (Yale Insights; DeepSeek flagged as a risk to economics)

### OPERATING ASSETS

- PUE trend, uptime/outage incidents, churn and renewal spreads, power cost pass-through percentage.

### WATER, CLIMATE, INSURANCE

- Water source, seniority, cooling design (Yale Insights, Cort).
- Bindable insurance quotes for the hold (Yale Insights, "Putting a Price on Climate Risk"; 11.5).

### RATES

- Run the model at +200 bp on debt and discount rate (HBS WP 26-096).

---

## 6A.7 The numbers

- **Leverage on hyperscale build-to-suit** tracks the tenant's credit and lease term (rated-equivalent); **colocation** trades on EBITDA like an operating company (general draft).
- **Use S&P Table 8 logic** (Chapter 6.5): an investment-grade long lease with no merchant tail is a low-OPBA asset (low DSCR needed, 1.10x to 1.40x range for OPBA 1 to 4); speculative / colocation is higher OPBA and needs far more coverage (S&P General Project Finance Rating Methodology, Dec. 14, 2022, Table 8, https://maalot.co.il/Publications/MT20221215151143.PDF). Mapping a data-center lease to a specific OPBA is judgment; ask the rating adviser.
- **Flexible-connection economics** per GW (ZERO Lab 2025): see 6A.3 table.
- **Hyperscaler capex** and global capex: see 6A.1.
- **PUE benchmarks.** GAP: industry PUE benchmarks (Uptime Institute annual survey) to be added after primary retrieval (general draft).
- **Lease and cap-rate benchmarks.** GAP: no primary source retrieved in this research pass.

---

## 6A.8 Third parties

| Third party | Deliverable |
|---|---|
| Utility / interconnection consultant | Facilities study review, firm vs non-firm terms, hourly curtailment study, upgrade allocation |
| Independent engineer | Construction budget, schedule vs equipment and energization, density and cooling retrofit cost |
| Power-island IE (if behind-the-meter) | Chapter 6 scope: technology, availability, heat rate, air permit |
| Lease counsel | Guaranty, termination, contraction, delivery LDs, curtailment tolerance |
| Regulatory counsel | Large-load tariff, rate cases, moratorium risk |
| Water-rights counsel | Source, seniority, curtailment |
| Insurance advisor | Bindable quotes for the hold |
| Equipment inspector | FAT, serial numbers, load-bank certificates |

---

## 6A.9 Failure modes and the check that catches each

| Failure mode | CHECK | Source |
|---|---|---|
| Powered-land story without power | Executed utility agreement and energization schedule; treat queue position or will-serve letters as option value only | General draft; LBNL 2026 |
| Tenant walk right on late delivery | Read the delivery-date and termination clauses against the realistic equipment and energization timeline | General draft |
| SPV tenant, not the hyperscaler parent | Obtain and read the guaranty | General draft; Yale Insights |
| Stranded asset on design obsolescence | Engineer's report on density and cooling retrofit cost | General draft |
| Speculative or canceled equipment orders | Firm PO, serial numbers, FAT (Chapter 6.7) | v1 6.7 |
| Curtailable service sold as firm | Written firm/non-firm terms; hourly curtailment study; BYOC in the security package | Kleinman Feb. 2026 (WEAK); ZERO Lab 2025 |
| Ratepayer backlash, tariff change, moratorium | Large-load tariff, cost allocation, rate cases, moratorium history | HBS Working Knowledge; Princeton arXiv 2609.08166 |
| Demand that never shows up | Signed leases vs forecast; stranded grid build-out | Kleinman podcast (WEAK); DOE/LBNL 2024 range |
| Compute economics fall (cheaper models) | Re-lease case; residual value on tenant exit | Yale Insights (DeepSeek) |
| Merchant generation cannibalized by others serving the same load | "Everyone builds" price deck | Princeton arXiv 2609.08166 |
| Water curtailed | Source seniority; cooling alternatives | Yale Insights, Cort |
| Interconnection delay | About 20% of the U.S. data-center pipeline faces power and grid delays (plausity.com, WEAK, vendor, https://plausity.com/en/news/ai-data-center-power-due-diligence-grid-cooling-energy-risk). CHECK: executed agreement with funded upgrades, milestones, energization date stressed against covenants | v1 6.7; LBNL 2026 |

No named data-center project failure case was sourced in this research pass. GAP.

---

## 6A.10 Red flags

**RED FLAG** list:

- "Up to X GW" of power with no executed agreement.
- Lease signed by an SPV with no parent guaranty.
- Tenant LOI presented as a lease.
- Behind-the-meter gas plan with no air permit.
- Delivery date earlier than the transformer delivery date.
- (General-lane draft for the five above.)
- "Secured power" that is non-firm or curtailable (Kleinman Feb. 2026).
- A "fast-track" interconnection with no written flexible terms and no curtailment study (Princeton ZERO Lab).
- The ZERO Lab two-year result cited as proof for this site (Princeton lane).
- A will-serve letter presented as an electric service agreement (LBNL 2026, general draft).
- A demand case that is a national forecast, not signed leases (DOE/LBNL 2024 range).
- A colocation business with no view on its utility's rate case or large-load tariff (HBS Working Knowledge).
- No water source or seniority in a Colorado River-dependent market (Yale Insights, Cort).

---

## 6A.11 Hard questions

- Show the executed utility agreement and the energization schedule by MW.
- Who guarantees the lease?
- What happens if delivery is six months late?
- What density does the building support, and what does a liquid-cooling retrofit cost?
- Which equipment is on firm order with serial numbers?
- (General-lane draft for the five above.)
- Is your interconnection firm or flexible? How many hours per year can the utility curtail you, and what carries the load during those hours? (Princeton ZERO Lab; Kleinman)
- Who pays for network upgrades and incremental capacity costs, and is that in the lease? (Kleinman)
- Which large-load tariff applies, what rate cases are pending, and has the county or state considered a moratorium? (HBS Working Knowledge)
- If the tenant leaves at the first termination option, who re-leases it, at what rent, and what does the debt look like? (Yale Insights)
- What is your water source and its priority? (Yale Insights, Cort)

> **THE ONE CHECK**
>
> Executed power by MW and date, firm or with curtailment the lease tolerates, matched to a lease the hyperscaler PARENT guarantees for longer than the debt. Power without a lease is a development bet; a lease without delivered power is a walk right.

---

# 7 CPG and Consumer Brands

DTC, food and beverage, retail, franchise.

> **THE SPINE FOR THIS CHAPTER**
> Volume that is not repeat purchase is rented. Prove repeat from cohorts, prove sell-through from retailer POS, and compare channels on contribution margin after trade spend and CAC.

## 7.1 How it works

The brand sells product through DTC, marketplaces, and wholesale or retail. Returns come from volume times contribution margin. Equity value comes from velocity, distribution, and durable margin.

- Consumer demand is cyclical and credit-driven. Across 30 countries (1960 to 2012), a one-standard-deviation rise in household debt to GDP over three years (6.2 points) predicts 2.1 points lower GDP growth over the next three years; forecasters systematically over-predicted growth at the end of these booms (Mian, Sufi and Verner, QJE 2017, NBER w21581, https://www.nber.org/papers/w21581). CHECK: record the 3-year change in household debt to GDP (BIS / Fed Z.1) for the brand's markets; if it is in the top third of history, run a downside with revenue growth 2 points lower for 3 years. (Full macro overlay: Chapter 0.)
- M&A in the category has a poor record: Quaker bought Snapple for $1.7B and sold it for $300M; Kraft Heinz took more than $28B of write-downs; Tyson paid a 70% premium for Hillshire, about $2B destroyed against fair value near $47/share (Feldman and Chunduru, KaW, Dec. 8, 2025, https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/). Brand acquisitions need the walk-away discipline in 5.3.

## 7.2 Diligence checklist

**FINANCIAL**
- Revenue recognition.
- Gross-to-net: trade spend, deductions, chargebacks, returns.
- Normalized EBITDA, inventory, working capital, cash conversion.
- Proof of cash and an independent QoE where EBITDA supports one (5.3, 5.10). Financial-statement breaches drive 38% to 40% of R&W paid loss (Aon 2026, https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study).
- Hold gross margin flat in the base case. CPG decks almost always assume gross-margin gains from volume; across 6,103 high-growth firms, margins did not expand with scale on average (Thomas, Ertan and Lewellen, Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows). Require co-packer and supplier quotes at the higher volume before crediting any COGS improvement.

**COMMERCIAL**
- Category growth, velocity, repeat rate, customer and retailer concentration, channel economics.
- Reconcile ACV distribution with door count, retailer authorizations, velocity against the category set, and repeat (auxocapitaladvisors.com, https://auxocapitaladvisors.com/cpg-m-and-a-advisory/; **WEAK**, advisor).
- ACV growth alone is not enough. It must connect to velocity and repeat.
- DTC: rebuild customer-based value from cohorts (7.6). Check whether growth is acquisition-led (Fader and McCarthy, KaW, Feb. 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/).
- Wholesale: request sell-through (POS) against sell-in by account and weeks of inventory at each distributor and retailer (7.7).

**REGULATED PRODUCT (food, beverage, supplements, personal care)**
- Independent data-integrity audit of quality systems: raw lab data against reported, FDA 483s and warning letters, audit trails. Akorn's falsified data let Fresenius walk away (2018) (Skadden, https://www.skadden.com/insights/publications/2018/10/analyzing-akorn; see 5.7). Apply the same audit to food and supplement makers.

**FRANCHISE AND MULTI-UNIT**
- See 7.8 (no-poach, FDD).

**DEAL TERMS**
- Revenue-based earnouts are common in brand acquisitions; apply the 5.11 drafting checklist (HLS Forum, 2025, https://corpgov.law.harvard.edu/2025/07/11/the-art-and-science-of-earn-outs-in-ma/).

## 7.3 The numbers

Compare channels on contribution margin, not gross margin.

| Channel | Contribution margin | Source |
|---|---|---|
| DTC | 35% to 55% | logicagencyinc.com (https://www.logicagencyinc.com/guides/cpg-channel-economics); **WEAK** (vendor) |
| Marketplace | Single digits to about 34% | same; **WEAK** |
| Wholesale | About 33% | same; **WEAK** |

- Velocity = units sold divided by number of stores (or per $MM ACV). The clearest demand signal (trustcultivar.com, https://www.trustcultivar.com/resources/cpg-financial-kpis-emerging-brands; marginvelocity.com; **WEAK**, vendor).
- ACV distribution = weighted percentage of retail volume where the SKU sells (alloy.ai, https://alloy.ai/cpg-analytics; **WEAK**, vendor definition).
- LTV:CAC for DTC above 3:1. Track CAC payback by channel. **WEAK** (practitioner). Recompute LTV from cohorts; never use company-defined LTV (7.6).
- Gross margin: emerging brands often target 30% to 40% early, higher at scale (trustcultivar.com; **WEAK**). Higher at scale is an assumption to prove with supplier quotes, not a default (Thomas, Ertan and Lewellen).
- Watch trade spend as a percentage of revenue, inventory turns, and spoilage for perishables.
- Company-defined unit economics are marketing. Allbirds' S-1 (2021) framed CAC payback against first-purchase contribution on a $124 AOV, and the top-25% cohort's lifetime spend at $446: company projections, not audited (Allbirds S-1, SEC EDGAR, as cited by the Wharton lane; confirm on EDGAR).

## 7.4 Failure modes

- Headline gross margin hiding thin contribution after trade spend and CAC. CHECK: contribution margin by channel.
- Revenue growth from promoted volume that loses money. CHECK: promo lift measured net of baseline.
- ACV growth with weak velocity: distribution that will be delisted. CHECK: velocity and repeat by retailer.
- Channel mix masking: blending high-margin DTC with low-margin marketplace sales. CHECK: channel-level P&Ls.
- Trade loading and channel stuffing: shipments into distributors and retailers ahead of consumer demand. CHECK: sell-in against POS sell-through by account; weeks of inventory at distributors (7.7).
- Growth bought with marketing; collapsing cohorts. CHECK: CBCV (7.6).
- Margin plan that assumes scale efficiencies. CHECK: supplier quotes at volume; flat-margin base case (5.14).
- No-poach clauses in franchise agreements creating antitrust exposure. CHECK: FDD and agreement review (7.8).

**Case files.**

| Company, year | What happened | THE CHECK |
|---|---|---|
| Blue Apron IPO, 2017 | About 70% of acquired customers churned within six months; declining cumulative net revenue per recent cohort; IPO range cut from $15 to $17 to $10 within days; shares later fell about 70% more (Fader and McCarthy, KaW 2018). | Cohort CBCV before pricing. |
| Wayfair, 2018 analysis | CBCV under $10 per share against a stock near $64; growth "made entirely of acquisition"; repeat below Amazon's two decades earlier; stock fell about 10% the day the paper posted (same). | Share of revenue from new customers; repeat curve against the category leader. |
| Quaker / Snapple | Bought for $1.7B, sold for $300M (Feldman and Chunduru, KaW 2025). | Walk-away price; distribution and repeat tested before paying for "brand." |
| Kraft Heinz | More than $28B of write-downs (same). | Brand-value impairment test against velocity and share trends, not cost-cutting plans. |
| Tyson / Hillshire | 70% premium; about $2B of value destroyed against a fair value near $47/share (same). | Premium justified only by probability-weighted, timed synergies. |
| Franchise no-poach, 2016 to 2018 | About 58% of major franchisors' 2016 agreements contained no-poach clauses; state AGs forced their abandonment and class actions followed (Krueger and Ashenfelter, NBER w24831, https://www.nber.org/papers/w24831). | Clause review; open AG and class-action exposure (7.8). |

## 7.5 Red flags

- Only blended metrics. No channel-level contribution.
- Distribution wins with no velocity data.
- Trade spend and deductions not disclosed.
- The company cannot or will not give customers acquired and active customers by period. Most non-subscription firms disclose none of this (Fader and McCarthy, KaW 2018).
- LTV and CAC payback defined by the company on first-purchase contribution (Allbirds S-1 pattern).
- Distributor or retailer weeks of inventory rising quarter over quarter while POS is flat (Zhang, Li and Li, Yale Insights, https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms).
- Gross-margin expansion in the plan with no supplier quotes.
- No-poach or wage-fixing language in franchise or vendor agreements.
- Regulated product with no recent independent quality-system audit.

## 7.6 Customer-cohort diligence for DTC and subscription brands

New in v2. Method and data request as in 2.10; DTC specifics here.

- **Data request.** By month or quarter: customers acquired, active customers, orders, revenue and gross margin per order, by acquisition channel and by cohort. Marketing spend by channel by month.
- **Fit retention and repeat.** Plot cumulative gross profit per cohort by month since acquisition. Strong retainers (Harry's, Dollar Shave Club) show flattening cohort curves; Blue Apron showed each recent cohort worth less (Fader and McCarthy, KaW 2018).
- **Acquisition-led test.** Share of revenue from customers acquired in the period. A rising share with flat or falling repeat means growth needs ever-rising marketing spend (Fader on Wayfair, same).
- **Rebuild LTV and CAC yourself.** Contribution after COGS, fulfillment, returns, payment fees and discounts, on the repeat curve you fitted, against fully loaded CAC by channel. Never use the company's lifetime-spend projection (Allbirds S-1, 2021).
- **Benchmark against the category leader** at the same cohort age.
- **Reconcile** cohort revenue to the P&L and to bank deposits (payment processor settlements).
- **THE ONE CHECK.** No cohort file, no valuation on fundamentals.

## 7.7 Sell-in versus sell-through: the trade-loading test

New in v2.

- Apply the customer-side test: sharp jumps in retailers' or distributors' inventory and payables against the brand's shipments predict revenue fraud. In about 30,000 supplier-years (1976 to 2018), the customer-inventory/AP signal alone carried about half the predictive power of the 11-variable Dechow model (Zhang, Li and Li, Yale Insights, URL in 7.5).
- Request: retailer POS (sell-through) by account and week; brand shipments (sell-in) by account; distributor inventory reports; retailer deductions and chargebacks by account.
- Flag: weeks of inventory at distributors rising quarter over quarter while POS is flat; quarter-end shipment spikes; rising deductions and returns in the following quarter.
- Confirm directly with the top retailers and distributors where possible (5.3 commercial).

## 7.8 Franchise and multi-unit: no-poach liability and the FDD

New in v2.

- **No-poach clauses are a liability, not a moat.** About 58% of major franchisors' 2016 franchise agreements contained no-poaching-of-workers clauses (examples: McDonald's, Burger King, Jiffy Lube, H&R Block), most common in low-wage, high-turnover sectors. Following the paper, the Washington State Attorney General and others forced their abandonment across many chains, and antitrust class actions followed (Krueger and Ashenfelter, NBER w24831 / Journal of Human Resources 2022, https://www.nber.org/papers/w24831).
- **CHECK** in any franchise, multi-unit, staffing or roll-up target: review franchise agreements, FDD Item 17, employment agreements and vendor contracts for no-poach, non-solicit and wage-fixing provisions; confirm removal and any open AG or class-action exposure; confirm non-compete enforceability by state for key employees (same).
- **FDD as a diligence source (suggested primaries, not yet verified in this edition).** FTC Franchise Rule (16 CFR Part 436) and the Franchise Disclosure Document: Item 19 (financial performance representations), Item 20 (outlet openings, closings, transfers: unit turnover), Item 21 (audited franchisor financials); SBA Franchise Directory (suggested primaries; not retrieved). **WEAK** until checked against the rule text.
- **Hard questions.** Show every agreement with a no-poach or non-solicit clause and when it was removed. What does Item 20 show about closures and transfers over five years? Are Item 19 figures system-wide or a selected subset?

## 7.9 Hard questions

- Show contribution margin by channel after trade spend, fulfillment and CAC.
- Show velocity by retailer against the category set, and repeat by retailer.
- How many customers did you acquire each month, how many are active, and how many orders did they place?
- What is POS sell-through against sell-in by account for the last eight quarters?
- What are weeks of inventory at each distributor today, and a year ago?
- Which COGS reductions in the plan are backed by signed supplier or co-packer quotes?
- What share of revenue was promoted, and what was lift net of baseline?
- Show trade spend, deductions and chargebacks by retailer.
- Has any retailer delisted a SKU in the last two years, and why?

## 7.10 Open gaps

- No institutional or academic source was found for channel contribution-margin bands, velocity benchmarks, trade spend as a share of revenue, or emerging-brand gross margin targets; all 7.3 figures remain **WEAK** (vendor). Candidate primaries to pull: Circana/NielsenIQ category data, public CPG 10-K gross-to-net disclosures, retailer slotting and deduction policies.
- No HBS, Wharton, Yale or Princeton CPG-specific diligence material beyond cohort valuation and the trade-loading test (none found in the HBS, HLS Forum, HKS, Wharton, Yale or Princeton sources reviewed).
- Franchise primaries (FTC Franchise Rule, FDD items) are suggested, not verified.
- No data on DTC CAC inflation by channel, marketplace fee economics, or retail-media costs from a primary source.
- Interview 3 to 5 CPG investors and lenders (B.2) on velocity thresholds for retention of shelf space and on trade-spend norms by category.

# 8 Cannabis and Hemp

Licensing, 280E, state compliance, cultivation, retail.

> **THE SPINE FOR THIS CHAPTER**
> Model federal tax at full 280E unless the operator proves otherwise with a DEA registration, a tax opinion and an audit-proof medical apportionment. Confirm the license with the regulator. Confirm the bank. Price exit off a buyer pool that is legally allowed to own the asset.

## 8.1 How it works

State-licensed cultivation, processing, distribution, and retail. Adult-use remains federally Schedule I, so banking and tax are constrained. As of November 2026, only FDA-approved marijuana products and marijuana under a qualifying state medical license have moved to Schedule III (8.6).

## 8.2 The 280E anchor

This is the central diligence issue.

| | Normal business | Under 280E |
|---|---|---|
| COGS | Deductible | Deductible (IRC 471 direct costs only) |
| Operating expenses | Deductible | Not deductible: taxed federally |
| Federal tax base | Profit | Profit plus operating expenses |

- IRC 280E denies all ordinary business deductions and credits to a business "trafficking" in a Schedule I or II controlled substance. Only COGS under IRC 471 is deductible (cannabisindustrylawyer.com; greengrowthcpas.com, https://greengrowthcpas.com/irc-280e-cannabis-tax-guide/). Effective federal rates can exceed 70% (peasebell.com, https://www.peasebell.com/insights/cannabis-280e-deductions-2026/; **WEAK**, CPA-firm marketing).
- Harborside: 280E applies to state-legal cannabis; COGS is limited to 471(a) direct costs; 263A is not available (Patients Mutual Assistance Collective Corp. v. Commissioner, 151 T.C. 176 (2018), aff'd 995 F.3d 671 (9th Cir. 2021); greengrowthcpas.com; cannabizguide.com, https://cannabizguide.com/guides/280e-tax-basics).
- **Correction to v1.** v1 said: "April 2026: FDA-approved marijuana products and marijuana under a state medical license moved to Schedule III, which can lift 280E for medical-only operators" (getmeadow.com; greengrowthcpas.com). The status as of November 2026 is narrower and less settled; see 8.6. No IRS guidance on 280E after the partial rule was located. Law-firm readings say qualifying medical operators are no longer subject to 280E for that activity, but this is not IRS guidance (Foley, Apr. 2026; Morgan Lewis, Sept. 2026; URLs in 8.6).
- State conformity varies. Some states (for example California) conform to 280E. Others (Colorado, Oregon, New York, New Jersey, Minnesota) decouple and allow state deductions (bluecloudcpa.com; greengrowthcpas.com). **WEAK** (CPA-firm sources; confirm each state's current statute per deal).

## 8.3 Diligence checklist

- License. Verify it is real, current, in good standing, and transferable. Confirm with the state regulator. Check ownership-change approval requirements.
- 280E tax exposure. Model the real effective tax. Verify COGS methodology under 471. Check dual medical and adult-use apportionment.
- 280E relief claims (any operator claiming Schedule III treatment): require (a) a DEA registration under the new expedited pathway, (b) a tax opinion, (c) a dual-license apportionment method (medical against adult-use COGS, revenue and overhead) that would survive audit, and (d) a model at full 280E treatment as the downside. Do not underwrite refund claims for prior years (derived from Federal Register 2026-08176 and law-firm readings: Foley, Apr. 2026; Morgan Lewis, Sept. 2026).
- Litigation status of the rescheduling: consolidated challenges to the partial rule are pending in the D.C. Circuit (8.6).
- State compliance. Seed-to-sale tracking, testing, packaging and labeling, security.
- Banking. How cash is handled. Banking relationship or cash-management risk. Check the operator's depository relationship, its tenure, any account-closure history, and the bank's own regulatory standing; require a contingency plan for a sudden de-banking. A Federal Reserve master-account denial after an eight-month review was called "a death sentence" for a cannabis-serving institution (KaW podcasts, "CannaBusiness: Marijuana Regulations and Banking Concerns," https://knowledge.wharton.upenn.edu/podcast/this-week-in-business/cannabusiness-marijuana-regulations-banking-concerns/; "The Pot Paradox," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/policy-paradox-legalized-marijuana/; **WEAK**, 2018 to 2019 podcast commentary, update for 2026 status).
- Real estate. Local approval, zoning, landlord consent.
- Public MSOs: diff the last 8 quarters of filings for changed risk-factor and legal language (Lazy Prices, NBER w25084, https://www.nber.org/papers/w25084).
- Cash controls: a cash-heavy business needs the full 0.4/0.5 proof-of-cash and segregation-of-duties work (Chapter 0).

## 8.4 Failure modes

- License not transferable or not in good standing. CHECK: regulator confirmation.
- 280E understated in projections, deducting operating expenses it cannot. CHECK: rebuild tax at Schedule I treatment.
- COGS overstated beyond 471 by claiming 263A. CHECK: the Harborside standard.
- Schedule III relief assumed for adult-use revenue, or for medical revenue without a DEA registration. CHECK: registration evidence, tax opinion, apportionment method, full-280E downside (8.6).
- Prior-year refund claims booked as an asset. CHECK: exclude from value.
- Exit valued at consumer-staples multiples. CHECK: buyer pool and sin-stock discount (8.7).
- Sudden de-banking. CHECK: bank tenure, closure history, contingency.

## 8.5 Red flags

- Projections that deduct normal opex federally.
- License in a name different from the operating entity.
- No seed-to-sale compliance trail.
- A deck that says "cannabis is now Schedule III." That is wrong for adult-use and incomplete for medical (registration and pending litigation) (Federal Register 2026-08176).
- Refund claims for prior-year 280E taxes counted in value or liquidity.
- No apportionment method between medical and adult-use for a dual licensee.
- Exit comps drawn from consumer staples or alcohol with no discount.
- One bank, short tenure, no backup.

## 8.6 Federal status as of November 2026

New in v2. Corrects v1 8.2.

| Item | Status (Nov. 2026) | Source |
|---|---|---|
| FDA-approved marijuana drug products | Schedule III | DEA partial final rule, signed April 22, 2026, published April 28, 2026: Federal Register 2026-08176, https://govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08176.htm; DOJ, https://www.justice.gov/opa/pr/justice-department-places-fda-approved-marijuana-products-and-products-containing-marijuana |
| Marijuana manufactured, distributed or dispensed under a qualifying state medical license | Schedule III, with an expedited DEA registration pathway for state medical licensees | same; Foley, Apr. 2026, https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/ |
| Adult-use (recreational) marijuana | Schedule I | same |
| Legal challenges to the partial rule | Consolidated challenges pending in the D.C. Circuit | Morgan Lewis, Sept. 2026; Foley, Apr. 2026 |
| Broader rescheduling of all marijuana | New DEA ALJ hearing held June 29 to July 15, 2026; post-hearing briefs filed; ALJ recommended decision and final Administrator determination pending | Morgan Lewis, Sept. 2026, https://www.morganlewis.com/pubs/2026/09/high-time-for-a-change-post-dea-hearing-broader-marijuana-rescheduling-questions-remain |
| IRS guidance on 280E after the partial rule | None located as of Nov. 2026 [GAP] | Search of IRS releases reported in the 2026 findings |

- **Underwriting rule.** Adult-use revenue: full 280E. Medical revenue: full 280E in the base case unless the operator shows the DEA registration, a tax opinion and an audit-proof apportionment; model relief as upside only. Prior-year refunds: zero.
- **THE ONE CHECK.** Rebuild federal tax at full 280E on every dollar of revenue, then credit relief only for medical revenue backed by a DEA registration under the new pathway.
- **Re-verify at signing.** The ALJ decision, the Administrator's final determination, the D.C. Circuit outcome and any IRS notice can each move the answer.

## 8.7 Valuation and exit

New in v2.

- **The neglected-stock discount is structural.** "Sin" stocks (alcohol, tobacco, gaming) have lower institutional ownership and fewer analysts and earn about 2.5% a year higher risk-adjusted returns than comparables, because norm-constrained investors (pensions, endowments, many banks) avoid them and litigation risk is higher; later work questions the size of the premium (Hong and Kacperczyk, "The Price of Sin," JFE 2009, https://w4.stern.nyu.edu/sternfin/mkacperc/public_html/sin.pdf; NYU Stern summary, https://www.stern.nyu.edu/experience-stern/news/uat_024862). Implication: fewer eligible buyers and lenders mean a higher cost of capital and lower exit multiples than a comparable consumer company, persisting until institutional constraints lift.
- **CHECK.** The exit case names realistic buyers actually permitted to own the asset (federal-illegality constraints on US-listed acquirers, bank lenders and exchanges) and applies a discount to consumer-staples comps rather than borrowing their multiples (same).
- Hold margins flat in the base case (5.14); a price-compressing state market makes expansion less likely, not more.

## 8.8 Hard questions

- What is federal tax at full 280E, and what does the model assume?
- Which revenue is medical, which adult-use, and how is overhead apportioned?
- Do you hold a DEA registration under the new pathway? Show it.
- Who wrote the tax opinion, and what does it assume about IRS treatment?
- Are any prior-year refund claims in the numbers?
- May we call the state regulator to confirm license standing and change-of-control approval?
- Who is your bank, for how long, and what happens if it closes the account tomorrow?
- Who can legally buy this company at exit, and at what multiple?

## 8.9 Hemp

- No findings file contained hemp-specific material (2018 Farm Bill hemp definition, intoxicating hemp-derived THC products, state restrictions, FDA position on CBD). Diligence by analogy only: license and registration status confirmed with the regulator; testing certificates of analysis from an accredited lab; total-THC compliance at harvest; labeling claims. All **WEAK** (no source in this edition). See 8.10.

## 8.10 Open gaps

- No IRS guidance on 280E after the April 2026 partial rule; track IRS notices and any Tax Court cases.
- Outcome of the DEA ALJ hearing (June to July 2026), the Administrator's final determination, and the D.C. Circuit challenges.
- State 280E conformity list rests on CPA-firm sources (**WEAK**); verify each state's current statute.
- Effective 280E rate figure ("can exceed 70%") is **WEAK** (CPA firm); rebuild per deal.
- Banking: Wharton material is 2018 to 2019 podcast commentary (**WEAK**); no current primary on bank access, SAFE Banking status or FinCEN cannabis SAR guidance was found.
- Hemp: no sources (8.9).
- No cannabis-specific failure cases with primary sources in this edition (HBS, Wharton, Yale lanes found none). Candidate sources: SEC filings and enforcement on cannabis issuers; state regulator disciplinary actions; MSO restatements.
- Interview 3 to 5 cannabis lenders and operators on apportionment practice, bank tenure, and license-transfer timelines.

# 9 Operating Company Growth Equity

The catch-all for inbound raises.

> **THE SPINE FOR THIS CHAPTER**
> Growth equity carries little leverage, so the return must come from revenue growth and the exit multiple. Underwrite flat margins, a haircut forecast, and an exit at or below entry. As a minority holder, diligence who can block or reprice the next round.

## 9.1 How it works

Minority or control equity into a small or mid-size private company for growth. The return comes from growth and an eventual exit.

- Growth equity sits inside the PE survey population (about 75% of respondents invest in growth equity). Use the same benchmarks: 20% management-forecast haircut; 22% to 25% target gross IRR; about 2.5x MOIC; exits about 50% strategic, 30% sponsor, under 20% IPO (Gompers, Kaplan, Mukharlyamov, NBER w21133, https://www.nber.org/papers/w21133).
- Growth deals carry less leverage, so return attribution must come from revenue growth and exit multiple. Show the multiple at which the deal still returns 2x (same).
- Owner-held private equity has not reliably beaten public equity (Moskowitz and Vissing-Jorgensen, AER 2002, NBER w8876, https://www.nber.org/papers/w8876; disputed beyond the 1990s by Kartashova, Bank of Canada WP 2011-6). Do not assume an illiquidity premium.

## 9.2 Diligence checklist

- Financial: QoE-lite, proof of cash, revenue quality, margins, unit economics, working capital.
- Commercial: market, customers, concentration, pipeline, competition.
- Legal and corporate: cap table, charter, prior financings, IP, material contracts, litigation.
- Management: references, background checks, key-person risk.
- Use of proceeds and the path to the next round or to profitability.
- **Forecast-record test.** Compare the last three budgets with actuals. Management with a history of optimistic misses is the population where unintentional errors become intentional misreporting (Schrand and Zechman, J. Accounting and Economics 2012, https://repository.upenn.edu/accounting_papers/119).
- **Widen the ranges.** Realized outcomes fell inside CFOs' 80% confidence intervals only 36% of the time; treat management's downside as a midpoint (Ben-David, Graham and Harvey, QJE 2013, NBER w16215, https://www.nber.org/papers/w16215).
- **Customer-cohort data request** (2.10, 7.6): customers acquired, active customers, orders per period (Fader and McCarthy, KaW 2018, https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/).
- **Customer-side revenue test** for the top 10 customers (Zhang, Li and Li, Yale Insights, https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms; see 5.3).
- **Family and founder governance.** Before investing, require: an independent board with at least one director able to chair audit; a real CFO, not a controller with a CFO title; a next generation that has worked outside the business (practitioners suggest 7 to 10 years and a C-level role) before taking a board seat; a board reconfigured for a downturn. Sloppy numbers signal broader governance problems even where financials are unaudited (O'Dowd and McLarty, Yale Insights, https://insights.som.yale.edu/insights/even-small-businesses-need-corporate-governance).
- **Preference stack and control.** Diligence the existing preference stack, who can block or lead future rounds, and what happened in every prior bridge or down round (HLS Forum cases Footprint and Zync, 2.11).
- **Strategic investors on the cap table.** Median CVC life is four years; do not count on follow-on (Song Ma, Yale Insights, https://insights.som.yale.edu/insights/companies-invest-in-startups-to-repair-weaknesses; 2.6).
- **Treasury.** Bank map with insured share; single-bank covenants (Metrick, JEP 2024, https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf).
- **Theme timing.** If the company is in a hot theme, compare entry valuation with the sector's history and the theme's media peak (Ben-David, Franzoni, Kim and Moussawi, NBER w28369, https://nber.org/papers/w28369).
- **Diligence floor.** Record in-person management hours, sites visited and references called; do not shrink them in a competitive round (Fu and Taylor, NBER w33987, https://www.nber.org/papers/w33987).

## 9.3 The numbers

Match to the sector: SaaS metrics in Chapter 2, CPG in Chapter 7, and so on. Always: default-alive runway, burn, growth, gross margin, retention.

- **Flat-margin base case.** No average margin expansion across 6,103 high-growth firms (Thomas, Ertan and Lewellen, Yale Insights, https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows). **CONTRADICTS** the implicit expansion in most growth models. Base case holds the current EBITDA margin; expansion only with a named, costed driver (5.14).
- **THE ONE CHECK.** Re-run the return with flat margins, a 20% forecast haircut and exit at entry multiple. If it no longer clears the hurdle, the deal is a bet on the multiple.
- **Forecast haircut.** About 20% off management EBITDA (Gompers et al.).
- **Target returns.** 22% to 25% gross IRR; about 2.5x MOIC (same).
- **The 2x test.** Solve for the exit multiple at which the deal returns 2x on flat margins and haircut revenue; compare with entry (Gompers et al.).
- **Runway at today's cadence.** At least 24 months to the next round (Carta, 616 days seed to A, Q2 2025, https://carta.com/data/series-a-fundraising-q2-2025; 2.1).
- **Retention.** Benchmark private companies against a median NRR just above 100% and GRR near 90% (KeyBanc/Sapphire 2025, https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey), not the 117% top-quartile figure (2.4).

## 9.4 Red flags

- No clean cap table. Unpapered instruments.
- Revenue not reconciled to cash.
- Founder will not provide references or raw data.
- Related-party revenue or expenses undisclosed.
- A history of budgets missed optimistically (Schrand and Zechman).
- A "CFO" who is really a controller; no director able to chair audit (O'Dowd and McLarty).
- Margin expansion in the plan with no named cost line (Thomas et al.).
- Exit case that needs a multiple above entry (5.14).
- Insiders leading a round priced below their own recent marks, with a short window for others (Footprint, 2.11).
- A strategic investor with a veto over financing (Zync, 2.11).
- Raised into a theme at its media peak (Ben-David et al.).
- No cohort data (2.10).

## 9.5 Failure modes

New in v2. v1 had none for this chapter.

| Failure mode | Example | CHECK |
|---|---|---|
| Insider-led recap dilutes minority holders | Footprint, Del. Ch. 2026: $450M of a $500M round from three insider funds at about half their own implied value; three weeks to decide (2.11) | Preference-stack and control map; price against insiders' marks; information and time rights for non-participants. |
| Strategic investor blocks financing | Zync v. Porsche, Del. Ch. 2026: designee voted down a $10M Series A; company shut down (2.11) | List every veto and holder. |
| Forecast optimism becomes misreporting | Schrand and Zechman 2012: about a quarter of AAER misstatements began as optimistic errors | Budget-versus-actual history. |
| Margin plan never arrives | Thomas, Ertan and Lewellen: no average expansion with growth | Flat-margin base case. |
| Growth bought with marketing | Blue Apron 2017; Wayfair 2018 (2.7) | CBCV. |
| Cash stranded at a failed bank | SVB, March 2023 (2.7) | Treasury map. |
| Fabricated customers | Frank / JPMorgan, 2021 (2.7) | Live-user sampling. |
| Founder control with no governance | Theranos (2.7) | Governance map; real CFO; audit-capable director. |

## 9.6 Hard questions

- Show the last three budgets against actuals.
- Which cost lines fall as a share of revenue in the plan, and what evidence supports each?
- At flat margins and a 20% revenue haircut, what exit multiple returns 2x?
- Who can block or lead the next round, and what happened in every prior bridge or down round?
- Who on the cap table is a strategic, and what rights do they hold?
- Is your CFO a CFO? Who on the board can chair audit?
- How many weeks of payroll survive if your main bank closes?
- How many customers did you acquire and keep, by period?

## 9.7 Return attribution for growth deals

See 5.14. With little leverage, debt paydown contributes almost nothing; the split is revenue growth, margin change and multiple change. Report how much of the return survives flat margins and exit at entry. Search-fund evidence shows about 80% of small-company value creation came from multiple expansion and margins fell (Wasserstein and Thomas, Yale Insights, Apr. 2026, https://insights.som.yale.edu/insights/do-search-fund-ceos-improve-performance): treat a growth case that looks the same as a warning, not a comfort.

# 10 Funds and Co-Investments

*LP diligence on GPs, operational due diligence, ILPA, SPVs, fee economics, return measurement.*

Sections 10.1 to 10.7 keep their v1 numbers so cross-references hold. Sections 10.8 to 10.17 are new in v2. The allocator-level material (portfolio construction, pacing, manager selection) is in Chapter 12; GP-led secondaries in Chapter 13; subscription lines and NAV loans in Chapter 14; evergreen and semi-liquid vehicles in Chapter 15. Sponsor background checks, KYC/AML and valuation fraud case files (Infinity Q, SQN) sit in Chapter 0; buyout deal mechanics in Chapter 5.

## 10.1 How it works

The LP commits to a fund. The GP calls capital, invests, and returns distributions through the LPA waterfall. A co-investment is a direct stake alongside the GP, usually with no fee or a low fee.

- **The LP cannot fire the manager. The contract is the only governance.** Fund investors generally cannot remove the management company except for egregious misconduct. LPACs have no day-to-day authority and cannot hire or fire, though they may approve conflicts and sometimes trigger dissolution or removal votes. LPs who exercise control risk losing limited liability. Exit rights substitute for control: the weaker the exit (a 10-year PE lockup), the more the LPA must carry (key-person dissolution, for-cause removal standard, no-fault divorce threshold, LPAC conflict approvals) (Morley, "The Separation of Funds and Managers," Yale Law Journal 123 (2014), https://www.yalelawjournal.org/article/the-separation-of-funds-and-managers-a-theory-of-investment-fund-structure-and-regulation). CHECK: read the removal standard (cause definition, vote threshold, who decides) and the key-person trigger. Treat a fund with neither key-person dissolution nor a workable removal right as having no governance.
- **Litigation is not a remedy.** Of 153 lawsuits over four decades against the top and bottom 50 PE firms, only 6 (4%) were filed by fund investors and 3 (2%) by institutions. LPAs carry broad GP indemnification, exculpation, mandatory arbitration and limited information rights, and LPs fear losing allocations. The rare exception: the Abu Dhabi Investment Council sued a US PE firm in Delaware Chancery (Dec. 2025) over a continuation-fund transaction (HLS Forum, "Opting Out of Court? Reputation and Informal Norms in Private Equity," 2026, https://corpgov.law.harvard.edu/2026/06/29/opting-out-of-court-reputation-and-informal-norms-in-private-equity/). The protection you get is what you negotiate before signing: information rights, LPAC composition, no-fault removal, consent rights on GP-leds (Chapter 13) and NAV loans (Chapter 14).
- **Most GP revenue is fixed.** In 238 funds raised 1992 to 2006, about 60% (2007 working paper) to about two-thirds (2010 RFS version) of expected GP revenue came from management and transaction fees, which do not depend on performance. Buyout funds earn relatively more from fixed fees than VC funds (Metrick and Yasuda, "The Economics of Private Equity Funds," Rodney White WP 07-17, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf; RFS 2010, https://econpapers.repec.org/RePEc:oup:rfinst:v:23:y:2010:i:6:p:2303-2341). The two versions disagree on the share; quote both. Full fee benchmark in 10.9.
- **Being an LP is expensive.** In present-value terms roughly half of an LP's total cost is illiquidity, a quarter management fees and a quarter carry; the break-even alpha a GP must generate is comparable to its total compensation (Sorensen, Wang and Yang, "Valuing Private Equity," HLS Forum, 2014, https://corpgov.law.harvard.edu/2014/01/12/valuing-private-equity/).
- **Whether PE is an alpha source is contested. Do not assume it.**
  - Against: measured from the investor's own portfolio (US public pensions, 1995 to 2018), the average plan's risk-adjusted PE outperformance is about zero; buyouts show positive risk-adjusted performance (partly value exposure), VC underperformed on average, real estate funds showed none; pensions' better fund picks reflected access, not selection skill (Korteweg, Panageas and Systla, HLS Forum, 2025, https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/). Buyout returns before fees can be largely replicated by about 2x-levered small, low EV/EBITDA public stocks; after roughly 6% a year in fees, PE investors underperformed the replicating portfolio (Stafford, RFS 2022, https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting).
  - For: endowments earned materially higher PE returns than other LPs (about 14 to 21 points a year higher in different versions), mainly by deciding better whether to re-up (Lerner, Schoar and Wongsunwai, "Smart Institutions, Foolish Choices?," JF 2007, https://www.nber.org/papers/w11136). GPs whose fund beats the industry tend to beat it in the next fund (Kaplan-Schoar, via Metrick and Yasuda survey, NBER w16652, https://www.nber.org/system/files/working_papers/w16652/w16652.pdf).
  - Cyclical: the estimated PE premium over traded factors was positive in the first half of the sample and turned negative later (Ang, Chen, Goetzmann and Phalippou, JF 2018, https://econpapers.repec.org/RePEc:bla:jfinan:v:73:y:2018:i:4:p:1751-1783) **WEAK** (abstract-level for the published figures). Do not underwrite a constant illiquidity premium.
- **Pension risk allocations to alternatives rose from about 14% (2001) to almost 40% (2021)** on beliefs about alpha that are hard to verify because "alternative asset classes are very hard to benchmark" (Siriwardane, HBS Working Knowledge, https://www.library.hbs.edu/working-knowledge/rethinking-risk-why-pension-funds-are-betting-on-alternative-assets). CHECK: before committing, write down the expected net alpha, the benchmark it is measured against (PME and a levered small-value index), and how prior predictions for this GP compared with outcomes.
- **Manager choice dominates in private markets.** Ten-year first-to-third-quartile spreads to June 2005: fixed income 0.5 points a year, buyouts 13.7, venture top-to-bottom quartile 43.2 (Swensen, Yale ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9). Full table and selection method in Chapter 12.

## 10.2 The ILPA DDQ 2.0 baseline

- **20 sections:** Firm, Fund, Succession and Key Persons, Investment Strategy, Co-Investments, GP-Led Secondaries, Credit Facilities, Investment Process, Team, Alignment of Interests, Market Environment, Fund Terms, Firm Governance / Risk / Compliance, Track Record, Accounting and Valuation, Reporting, Legal, Data Security and Technology, ESG, DEI (ILPA Due Diligence Questionnaire 2.0, 2021, ilpa.org).
- Appendix A lists 89 requested documents (mattercite.com, https://mattercite.com/ilpa-ddq). **WEAK**: confirm the count against the ILPA document itself.
- LPs spend the most time on Track Record, Fund Terms, and Governance / Risk / Compliance, where a first-time manager's story holds together or falls apart (angelinvestorsnetwork.com, https://angelinvestorsnetwork.com/capital-raising/ilpa-ddq-2-0-guide-vet-first-time-fund-manager). **WEAK** (practitioner).
- **The primary ILPA set to hold GPs to (cite these, not aggregators):**

| Document | Date | What it requires or recommends | Use in diligence |
|---|---|---|---|
| ILPA Principles 3.0 | 2019 | Subscription lines reasonable in size (as % of fund) and duration; LPs offered an opt-out at the outset (https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf) | Term-sheet baseline for 10.4 Fund terms |
| ILPA DDQ 2.0 | 2021 | 20 sections above | Send to every GP; diff answers against data room |
| Guidance on Disclosures Related to Subscription Lines of Credit | 2020 | Quarterly facility size and balance; IRR with and without the facility; uncalled-capital estimate; 15% to 25% of commitments and 180 days outstanding as PE reference points (https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf) | Chapter 14 |
| Continuation Funds: Considerations for LPs and GPs | May 2023 | True status quo option; LPAC conflict vote; at least 30 days to re-underwrite (https://ilpa.org/resource/continuation-funds-considerations-for-limited-partners-and-general-partners/) | Chapter 13 |
| NAV-Based Facilities Guidance | July 2024 | LPAC consent regardless of use of proceeds; NAV-funded distributions inflate IRR and DPI and may be recallable (https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf) | Chapter 14 |
| Updated Reporting Template and new Performance Template | Published 2025 | Reporting Template replaces the 2016 template for funds still in their investment period in Q1 2026 or launched on/after Jan. 1, 2026. Performance Template standardizes gross and net IRR and TVPI WITH and WITHOUT the fund-level subscription facility ("granular" or "gross-up" method); sub-line interest is a separate expense line (ILPA Combined Overview, https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf; Templates Hub, https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub; Katten, https://katten.com/insights/advisories/ilpa-publishes-updated-reporting-template-and-new-performance-template) | Ask every GP raising today for the Performance Template for each prior fund |

CHECK: ask every GP raising today for the ILPA Performance Template for each prior fund. Refusal is a signal.

**THE ONE CHECK (fund terms):** since June 2024 there is no federal rule requiring a quarterly fee statement, a fund audit beyond the Custody Rule's audit option, or a fairness opinion on a GP-led (10.15). Everything you need, you must get into the LPA or side letter before you sign.

## 10.3 Operational due diligence: the section that catches frauds

**Figure 15 (v1), in table form.** Operational due diligence compares the structure you are shown with the structure you need.

| The Madoff structure | The institutional structure |
|---|---|
| One firm acts as manager, broker-dealer, custodian and administrator | Manager, independent administrator, custodian, prime broker and auditor are separate firms |
| Two-partner auditor | Auditor sized for the mandate |
| No independent NAV | Administrator computes NAV from its own records |
| LP relies on the manager's word | You (the LP) call each service provider directly, unsolicited |

**Core v1 tests (kept):**
- Independent administrator and NAV verification. The red flag is self-administration, or an administrator using the manager's own records (dealroom.net, https://dealroom.net/blog/hedge-fund-due-diligence; now backed by the SEC and DOJ case files in 10.6).
- Auditor quality. The red flag is a firm too small for the mandate, a qualified opinion, late statements, or an unexplained auditor change.
- Cash controls and segregation of duties. The red flag is one person able to initiate and approve a wire.
- Service-provider verification. Call the administrator, auditor, and prime broker directly and unsolicited (ryanoconnellfinance.com, https://ryanoconnellfinance.com/hedge-fund-due-diligence/; dealroom.net). Primary backing: SEC Division of Examinations private-fund risk alerts and the case files in 10.6.

> **THE MADOFF LESSON.** Madoff served as manager, broker-dealer, custodian, and administrator at once, with a two-partner auditor and no independent NAV. Every structural red flag was present and visible. Intake was about $65B and investor losses about $18B; the pitch worked because it promised modest, stock-like returns with almost no downside (Antle, "Where Did Madoff's Money Go?," Yale Insights, https://insights.som.yale.edu/insights/where-did-madoffs-money-go). Madoff's own rule, quoted in the ODD literature: "You must do a third-party check. It's an absolute must... It's accounting 101" (Brown, Goetzmann, Liang and Schwarz, "Trust and Delegation," NBER w15529, https://www.nber.org/papers/w15529).

**ODD base rates (Goetzmann et al.).** Brown, Goetzmann, Liang and Schwarz studied 444 operational due-diligence reports from a major hedge-fund DD firm ("Trust and Delegation," NBER w15529, JFE 2012, https://www.nber.org/papers/w15529). The sample is hedge funds; apply to PE, credit and real estate managers by analogy. Use these as the comparison set for your ODD scorecard.

| Finding | Base rate |
|---|---|
| Funds with some past legal or regulatory problem | 41% (more than twice the rate in Form ADV filings) |
| Defendants in legal disputes | 32% |
| Regulatory problems | 15% |
| Misrepresented past legal or regulatory problems | 21% |
| Other statements wrong or unverifiable | 28% |
| At least one misrepresentation or inconsistency | 42% |
| Disclosed some problems, hid others ("strategic misstatement") | 6% |
| Disclosed nothing and had problems | 9% |
| Would have passed as clean on DDQ and voluntary disclosure; caught only by independent background check | 10% |
| Verbal figures in interviews (assets, performance) contradicted the manager's own documents | 20% |
| Manager's wire-signature process disagrees with the administrator's | 16% |
| Pricing process disagrees with the administrator's | 3.6% |
| Major data vendor switched in last 3 years | 11% |
| Fund or administrator refused some DD questions | 14% |
| Asset information unverifiable or conflicting with a third party | ~19% |
| Performance unverifiable or disagreeing | 14% |
| Typical third-party ODD report cost at the time | ~$12,500 |

(All rows: Trust and Delegation, NBER w15529; summarized in the Yale lane.)

- **Non-Big 4 auditor and internal pricing** were each significantly associated with misrepresentation (Trust and Delegation).
- **ODD is commissioned at the wrong moment, and the market ignores it.** DD reports are typically commissioned after strong performance and inflows. The operational-risk score built from them predicted later fund failure out of sample, yet operational risk did not reduce investor flows (Trust and Delegation). Run ODD to the same standard on a hot manager as on a cold one, and give the ODD team veto power.
- **Form ADV is predictive.** Past legal and regulatory problems in Form ADV were strongly related to conflicts of interest, ownership concentration and leverage. An "omega score" estimates operational risk from public data (performance, volatility, size, age, fees) when an ADV is not available (Brown, Goetzmann, Liang and Schwarz, "Mandatory Disclosure and Operational Risk," JF 2008, https://econpapers.repec.org/RePEc:bla:jfinan:v:63:y:2008:i:6:p:2785-2815; omega-score, FAJ 2009, https://econpapers.repec.org/RePEc:taf:ufajxx:v:65:y:2009:i:1:p:43-53) **WEAK** (abstract-level). CHECK: pull Form ADV Parts 1 and 2 from IAPD for every adviser and reconcile every disclosure item to the manager's DDQ answers.
- CHECK: write down every number given in management meetings and reconcile it to the data room. Treat a gap as a finding, not a slip (Trust and Delegation).
- CHECK: obtain the bank signatory list and wire-approval matrix from the bank or administrator directly. Do not take the manager's description (Trust and Delegation).
- CHECK: track "refused or deflected question" (count and topic) as a field in the A.2 diligence report.
- **Third-party pricing is not independence.** "Third-party pricing service" means nothing if the manager can choose models or alter inputs (Infinity Q; Chapter 0.6 and 10.6). CHECK: who has write access to pricing inputs; administrator's independent price for a sample of Level 3 positions; valuation-committee minutes for dissent; the named valuation firm's engagement letter, and a call to the firm (SQN; 10.6).
- **Ratio metrics can be manufactured.** The Sharpe ratio, Jensen's alpha, the information ratio, the Sortino ratio and M-squared can all be gamed by managers using derivatives or dynamic strategies; only a utility-based measure is manipulation-proof (Goetzmann, Ingersoll, Spiegel and Welch, RFS 2007, https://repec.som.yale.edu/icfpub/publications/2471.pdf). CHECK: never accept a Sharpe or Sortino figure as evidence of skill. Ask for the return distribution, option-like exposures and drawdowns, and compute a manipulation-proof measure (MPPM) from monthly returns.
- **Smoothness is the core Ponzi tell, at any return level.** Low volatility combined with steady gains should raise suspicion in anyone who believes higher expected return requires risk (Antle, Yale Insights). Widen the red flag from "guaranteed returns" to "returns smooth relative to the stated strategy."

**SEC examination deficiencies as ODD test steps.** The SEC Division of Examinations' private-fund risk alerts (June 2020; Jan. 2022) list recurring deficiencies (SEC, "Observations from Examinations of Investment Advisers Managing Private Funds," https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf; Holland & Knight on the Jan. 2022 alert, https://www.hklaw.com/en/insights/publications/2022/02/division-of-examinations-publishes-risk-alert-for-private-fund; HLS Forum, "SEC Identifies Private Fund Deficiencies," 2022, https://corpgov.law.harvard.edu/2022/02/17/sec-identifies-private-fund-deficiencies-signifying-increased-industry-scrutiny/). Test each against LPAC minutes, fee calculations and the side-letter set.

| # | Deficiency the SEC finds | Test step |
|---|---|---|
| 1 | Undisclosed conflicts in allocations and cross-trades | Obtain the allocation policy and the log of every cross-trade and co-invest allocation; match to LPAC approvals |
| 2 | LPAC consent skipped for conflicted transactions | Read LPAC minutes for 3 years; list every affiliated transaction from the financial statements and find its consent |
| 3 | Preferential liquidity or information terms in side letters | Obtain all side letters (or the MFN compendium); flag liquidity or information rights not offered to you |
| 4 | Portfolio-company monitoring, board, transaction or deal fees not offset | Schedule every portfolio-company fee for 3 years and recompute the offset (TZP, 10.6) |
| 5 | Valuations not following stated policy, inflating fees and carry | Compare marks to the written policy for a sample; recompute fees on the corrected NAV |
| 6 | Post-commitment-period fee base not stepped down after investments sold, written down or written off | Recompute the management-fee base quarter by quarter after the investment period |
| 7 | Fund terms extended without required approval, keeping fees running ("zombie funds") | Check every term extension against the LPA's approval requirement |
| 8 | Leverage and strategy outside fund documents | Reconcile holdings and fund-level debt to the LPA limits (style drift, 10.6) |
| 9 | Key-person events not followed or disclosed | List departures against the key-person clause; ask when LPs were told |
| 10 | Track records cherry-picked, shown gross, without leverage effects, over selective periods, or borrowed from people not primarily responsible | Rebuild the track record from fund cash flows (10.10); attribute each deal to the person who led it |
| 11 | Inadequate diligence on investments and on service providers (placement agents, alternative data vendors) | Ask for the manager's own vendor-diligence files |
| 12 | Hedge clauses purporting to waive fiduciary duty except for gross negligence or fraud | Legal review of the LPA and subscription documents |

## 10.4 Diligence checklist

**Kept from v1:**
- Track record: gross-to-net, PME, loss ratio, DPI and TVPI, attribution to the current team, realized versus unrealized marks.
- Fund terms versus ILPA Principles: fees, carry, waterfall (deal-by-deal versus whole-fund), clawback, GP commit, key-person and no-fault-divorce provisions.
- Alignment: GP commitment size, team compensation and retention.
- Governance: valuation policy, conflicts, LPAC, subscription-line usage and its effect on reported IRR.
- Operations: administrator, auditor, custody, cyber, business continuity.

**Added in v2, by workstream:**

*Track record*
- Every fund and vehicle ever managed, including closed, abandoned and side vehicles (survivorship, 10.10) (Swensen, ECON 252 lecture 9).
- ILPA Performance Template for each prior fund, gross and net, with and without the subscription facility (10.2).
- Deal-level attribution: who led each deal, and are they still there and still leading. VC persistence comes from deal access that reputation unlocks, and reputation often sits with partners, not the firm (Sorenson, Nanda and Samila, Yale Insights, https://insights.som.yale.edu/insights/for-top-venture-capital-firms-success-breeds-success).
- Decompose each realized deal into revenue/EBITDA growth versus leverage versus multiple change, and score the manager on the operating share (PRINCO lessons, BU Insights, https://insights.bu.edu/four-mantras-from-the-endowment-a-personal-journey/; 0.7 item 6).
- Show IRR with and without the largest one or two exits; for VC, with and without the top one or two outcomes (Yale News, https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion; Ouyang, Yu and Jagannathan, NBER w27690, https://www.nber.org/papers/w27690).
- Read the GP's portfolio commentary history, not just the marks; flag companies where early letters dwell on refinancing, covenants or capital structure (HLS Forum, "Understanding Communications by Private Fund Managers," 2026, https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/; numbers in 10.10).
- Decline managers whose recent funds land consistently in the third or fourth quartile (Erickson, KaW, Mar. 13, 2023, https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/).

*Fund size and scaling*
- Compare successor-fund size with the funds that earned the track record, and with team size and deals per partner. Persistence is weaker in buyout because successful buyout GPs scale fund size faster; "Size is the enemy of performance" (Metrick and Yasuda, NBER w16652; Swensen, ECON 252 lecture 9).
- Chart deals per year and AUM growth against team size. A sponsor doubling its pace without doubling its operating bench is a yellow flag; rapid growth in a group's deal volume is associated with lower employment growth at its targets (Davis, Haltiwanger, Handley, Lipsius, Lerner and Miranda, NBER w26371, https://www.nber.org/papers/w26371).
- Deployment pressure: very large deployment targets make selective underwriting hard. The largest perpetual private-credit fund must deploy about $43B a year, more than a quarter of annual US direct lending (Harker, KaW, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/). Ask the required annual deployment against the strategy's market size.

*Fund terms and fees (benchmarks in 10.9)*
- Full fee-tier schedule and commitment thresholds; invoke MFN; compare your net terms with the best tier (Begenau and Siriwardane, 10.9).
- Fee and expense allocation policy; 3-year schedule of all portfolio-company fees (monitoring, transaction, director, operating-partner) with offset calculations; broken-deal expense allocation across funds and co-investors; who pays operating partners (HLS Forum, SEC enforcement review, 2016, https://corpgov.law.harvard.edu/2016/12/19/the-year-in-review-sec-enforcement-actions-against-investment-advisers/).
- Monitoring agreements with acceleration clauses on exit: red flag (derived from Metrick and Yasuda; Blackstone case in 10.6).
- Management-fee step-down or basis switch after the investment period; hurdle and catch-up; carry basis (committed vs invested) (Metrick and Yasuda).
- Model GP revenue under base and downside. If fixed fees dominate in the downside, alignment is weaker than headline carry suggests (Metrick and Yasuda; KaW podcast "Secrets of the Private Equity Trade," https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/secrets-of-the-private-equity-trade/).

*Alignment and team (detail in 10.13)*
- Carry and GP-ownership split by person for the current and prior fund (Ivashina and Lerner, "Pay Now or Pay Later?," JFE 2019, https://nber.org/system/files/working_papers/w22660/w22660.pdf).
- Succession plan: who decides, who owns the LP relationship, what happens economically if a founder steps back (HLS Forum, "Succession Planning in Private Equity," 2026, https://corpgov.law.harvard.edu/2026/02/21/succession-planning-in-private-equity-a-strategic-imperative-for-gps-and-lps/).

*Governance and LP protections*
- Removal standard (cause definition, vote threshold), no-fault divorce threshold, key-person dissolution (Morley, YLJ 2014).
- LPAC composition and consent rights over GP-leds, NAV loans and affiliated transactions (HLS Forum, "Opting Out of Court," 2026).
- Any SEC deficiency letters or Wells notices in the last 5 years (HLS lane synthesis).
- Sub-line and NAV-facility terms and performance ex-facilities (Chapter 14).
- Co-invest allocation policy and the list of co-invests offered and to whom (10.12).

*Operations*
- The 10.3 base-rate scorecard, the 12 SEC test steps, and direct service-provider calls.
- For any fund-of-funds or OCIO: who can terminate a manager and how fast, and is the decision-maker paid on assets retained (PRINCO Organizational Model, https://princo.princeton.edu/about/organizational-model; Chapter 12).
- Insurer-affiliated managers: when the manager's permanent capital is an affiliated insurer, the manager is lending policyholders' money into its own platform's deals. Life-insurer private-placement lending reached about $849B (14% of balance sheets) in 2024, driven by PE-owned insurers, whose private placements in ABS and financial borrowers rose from 2% to 8% of assets, 2017-2024 (Meisenzahl, Overpeck and Polacek, Chicago Fed WP 2025-09, https://www.chicagofed.org/publications/working-papers/2025/2025-09). Affiliated "shadow" reinsurance grew from about $11B (2002) to $370B (2013); adjusting for it cut average risk-based capital by about 53 points (Koijen and Yogo, NBER w19568, https://www.nber.org/papers/w19568; industry critics, e.g. Harrington for ACLI, argue the effect is overstated). CHECK: statutory statements (not GAAP), Schedule S, consolidated RBC including affiliated captives, affiliated-transaction policy, independent valuation of affiliated private placements (Chapter 4).

*Fund-level LP failure-avoidance checklist (HLS lane synthesis of the cases in 10.6):* (a) fee/expense allocation policy and 3-year schedule of portfolio-company fees with offsets; (b) NAV-facility and sub-line terms, plus performance ex-facilities; (c) carry/ownership split by partner; (d) co-invest allocation policy and the list of co-invests offered and to whom; (e) any SEC deficiency letters or Wells notices in the last 5 years.

## 10.5 The numbers

**Kept from v1:**
- Scrutinize IRR with and without the subscription credit facility. A facility can inflate reported IRR materially. ILPA now standardizes both figures (10.2); facility reference points 15% to 25% of commitments and 180 days outstanding (ILPA 2020 guidance).
- Benchmark the track record against vintage-year peers and a PME.
- Do not accept gross IRR alone.

**Added in v2 (detail in 10.9 and 10.10):**

| Metric | Benchmark | Source |
|---|---|---|
| Expected PV of GP revenue, median buyout fund | $19.36 per $100 committed: $10.34 management fees, $5.35 carry, $1.44 entry transaction fees, $2.11 monitoring and exit fees | Metrick and Yasuda (238 funds, 1992-2006), https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf |
| Expected PV of GP revenue, median VC fund | $23.50 per $100: about $14.61 fees, $8.86 carry | Same |
| Fixed share of GP revenue | About 60% (2007 WP) vs about two-thirds (2010 RFS) | Same; both versions shown |
| Median lifetime management fees | Buyout 12% of committed (IQR 10% to 13.5%); VC 17.75% (IQR 14% to 21.25%) | Same |
| Fee-tier spread inside one fund | About 91 bps management fee and 5.8 points of carry between tiers on average (smaller in VC) | Begenau and Siriwardane, JF 2024 (about 2,400 funds, 1990-2019), https://corpgov.law.harvard.edu/2024/05/10/fee-variation-in-private-equity/ |
| Fees in a replication test | Roughly 6% a year; after fees PE underperformed a 2x-levered small-value replicating portfolio | Stafford, RFS 2022 |
| LP cost split (PV) | About 1/2 illiquidity, 1/4 management fees, 1/4 carry | Sorensen, Wang and Yang, HLS Forum 2014 |
| VC aggregate return | IRR about 22%, generalized PME 1.44 (17,242 US ventures first funded 1980-2006); dropping the best 5% of ventures makes the risk-adjusted return negative | Ouyang, Yu and Jagannathan, NBER w27690 |
| Hedge fund pre-fee alpha vs linear factors | 6% to 10% a year (1996-2012), not reliably distinguishable from index put-writing; fee equating put strategy to the index about 3.6% a year (WP version) | Jurek and Stafford, JF 2015, https://www.nber.org/papers/w19643 |
| Interim marks as predictor of final fund-company returns | Coefficient about 0.16 in years 1-2, 0.62 in years 3-4, 0.78 later (7,271 company-years, 536 US PE funds, 2015-2020) | HLS Forum 2026, StepStone data |
| Database bias (hedge funds) | Backfill 500+ bp a year; survivorship 379 bp (paper) vs 4.4% survivorship and 7.3% backfill (Swensen's citation) | Malkiel and Saha; Swensen; 10.10 |
| Outside-view return anchor | Princeton cut its long-term endowment return assumption from 10.2% to 8% (early 2026) | Chapter 12 **WEAK** (press-sourced) |

## 10.6 Failure modes

**Kept from v1:**
- Self-administration and no independent NAV (Madoff). CHECK: independent administrator, and call them.
- Subscription-line-inflated IRR. CHECK: recompute without the facility; ask for the ILPA Performance Template.
- Style drift: strategy not matching 13F filings or the stated mandate. CHECK: reconcile holdings to strategy (SEC exam deficiency 8, 10.3).

**Case files (v2).**

| Firm | Year | What happened | CHECK that would have caught it |
|---|---|---|---|
| Bernard L. Madoff Investment Securities | 2008 | Manager, broker-dealer, custodian and administrator in one firm; two-partner auditor; no independent NAV; about $65B intake, about $18B investor losses; smooth stock-like returns (Antle, Yale Insights) | Independent administrator and custodian, called unsolicited; smoothness test against the stated strategy |
| Infinity Q | Collapsed 2021; sentenced Apr. 2023 to 15 years | Founder/CIO Velissaris manipulated inputs to the supposedly independent Bloomberg BVAL models to mismark OTC derivatives, allegedly overvaluing fund assets by more than $1B and collecting nearly $27M in fees on inflated NAV; fabricated valuation-committee minutes and gave them to the SEC (DOJ SDNY, https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-investment-officer-infinity-q-sentenced-15-years-prison; SEC Lit. Rel. 25331, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25331) | Who has write access to pricing inputs; administrator's independent price for a sample of Level 3 positions; read valuation-committee minutes for dissent (cross-ref 0.6) |
| SQN Capital Management | SEC, Oct. 9, 2026 (settled) | The principal personally prepared the only valuations for four funds while telling investors an independent expert did; allegedly materially inflated them from at least 2019 through 2025 (SEC Lit. Rel. 26671, https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671) | Obtain the named valuation firm's engagement letter and call the firm |
| GPB Capital | Convicted Aug. 2024; sentenced May 2025 to 7 years; commuted late Nov. 2025 after 12 days served (conviction stands) | About $1.6B raised from individual investors; distributions represented as funded by portfolio operating cash flow were paid from new investor capital (NBC News, https://www.nbcnews.com/politics/white-house/trump-commutes-7-year-prison-sentence-former-private-equity-ceo-david-rcna246744; Bloomberg, https://www.bloomberg.com/news/articles/2025-12-01/trump-commutes-sentence-of-gpb-capital-founder-david-gentile) | Reconcile every distribution to the source account and to underlying portfolio-company cash flow; a fixed "distribution rate" on an illiquid PE fund is a red flag |
| Momentum Advisors | SEC, Mar. 7, 2025 (settled) | COO diverted about $223,000 from a private fund's portfolio companies via company debit cards and excess salary, concealed from the adviser, the bookkeeper and SEC staff; managing partner failed to supervise and caused the fund to pay a $346,904 debt of an entity the two controlled; the fund was never audited; penalties $515,000 total (SEC 2025-53, https://www.sec.gov/newsroom/press-releases/2025-53) | An unaudited fund is an automatic pass; also test portfolio-company card and payroll spend for insiders, since the fund audit alone will not catch portfolio-level leakage |
| TZP Management | SEC, Aug. 15, 2025 | Charged with overcharging management fees by failing to offset portfolio-company transaction fees (SEC order; release number to confirm on sec.gov) | Recompute fee offsets from portfolio-company payments |
| Blackstone (four affiliated PE advisers) | SEC, 2015-16 | Accelerated monitoring fees on portfolio exits without adequate disclosure; $12.5M penalty plus $37.5M disgorgement (HLS Forum, 2016, https://corpgov.law.harvard.edu/2016/12/19/the-year-in-review-sec-enforcement-actions-against-investment-advisers/) | Read every monitoring agreement for acceleration clauses; schedule fees paid on exit |
| Unnamed PE adviser (fee-offset allocation) | SEC, 2015-16 | Allocated fee offsets among funds in a way that favored itself; $2.3M fine plus $10.4M reimbursement (HLS Forum 2016; "Fund Advisers and Fee Disclosure in SEC Enforcement Action," https://corpgov.law.harvard.edu/2015/10/30/fund-advisers-and-fee-disclosure-in-sec-enforcement-action/) | Recompute offsets fund by fund, including co-invest vehicles |
| Unnamed PE adviser (expense allocation) | SEC, 2015-16 | Funds paid all insurance premiums and extra fees while the adviser negotiated a legal-fee discount only for itself; $3.5M fine plus about $8.3M reimbursements (HLS Forum 2016) | Obtain the expense allocation policy and vendor invoices for shared services |
| Unnamed PE adviser (operating-partner fees) | SEC, 2015-16 | Unauthorized "operating partner oversight fees"; fund money used for political, charitable and entertainment expenses; $2.3M disgorgement plus penalty (HLS Forum 2016) | Confirm who pays operating partners; sample fund expenses against the LPA's permitted-expense list |
| Archegos Capital (family office) | Collapsed Mar. 2021; Hwang sentenced Nov. 2024 to 18 years | Concentrated exposures built through total-return swaps across multiple prime brokers, none of whom saw the whole book; banks lost more than $10B (DOJ SDNY sentencing release, Nov. 20, 2024; URL to confirm) | For co-investments alongside family offices: aggregate exposure across ALL counterparties, not one prime broker's view |
| Heller / Paramount-Prestige ATM network | SEC, Sept. 3, 2025 | Over $770M from about 2,700 mostly retail investors for fixed monthly distributions supposedly from ATM fees; paid from new money and high-interest short-term loans; about $400M investor losses and $185M+ allegedly misappropriated (SEC 2025-111, https://www.sec.gov/newsroom/press-releases/2025-111-sec-charges-pennsylvania-resident-his-companies-770-million-ponzi-scheme) | Independent confirmation from the processor, not the sponsor, that the claimed operating assets exist and earn the claimed revenue |
| Weston Presidio / Doughty Hanson / Charterhouse | 2014 / 2015 / 2015 | Weston Presidio suspended fundraising after partners left; Doughty Hanson wound down, with an investor citing concentration of power and economics at the top; Charterhouse faced friction over profit split and succession (HBS Working Knowledge, "Is Greed Ruining Private Equity Firms?," https://www.library.hbs.edu/working-knowledge/is-greed-ruining-private-equity-firms) | Carry and ownership split by person; succession plan (10.13) |
| Connecticut state pension (allocator) | Decade to 2023 | Would have earned about $5B more over five years and about $27B more over ten at the 50-state median; a plain 60/40 beat it by over 1 point a year; 8 CIOs and 4 interim CIOs; high fees, sometimes where the state was a manager's sole or dominant client; fees reported on total rather than active assets (Sonnenfeld and Tian, Yale Insights, May 2023, https://insights.som.yale.edu/insights/why-connecticuts-investments-are-underperforming) | For any allocator, fund-of-funds or OCIO: CIO tenure; fees as % of actively managed assets; manager net performance vs a passive alternative; concentration where the LP is anchor or only client (Chapter 12) |
| Long-Term Capital Management | 1998 | Lost 92% of capital and reported none of it to the hedge-fund databases (Malkiel and Saha, Princeton CEPS WP 104, https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf) | Survivor-inclusive benchmarks; haircut any "industry average" (10.10) |
| Reserve Primary Fund | 2008 | A "safe" pooled vehicle gated for years (Chapter 15 case file) | Look through "cash" holdings; model the gate |

**Additional failure modes and their checks:**
- Fee base not stepped down after write-downs; zombie-fund extensions. CHECK: SEC test steps 6 and 7 (10.3).
- Carry paid on NAV-loan-funded distributions; IRR/DPI inflated near a fundraise. CHECK: synthetic DPI excluding NAV-funded distributions (Chapter 14).
- Track record borrowed from people who have left. CHECK: deal-level attribution (10.4).
- Senior departures after carry is concentrated in founders. CHECK: Ivashina-Lerner split (10.13).
- Co-invest adverse selection. CHECK: why is the GP syndicating, and is the main fund taking its full pro rata (10.12).
- Hot manager waved through ODD. CHECK: ODD to the same standard regardless of performance; ODD veto (Trust and Delegation).

> **THE ONE CHECK (funds).** Call the administrator, the auditor, the custodian and the named valuation firm yourself, unsolicited, and reconcile what each says to what the GP told you. It catches Madoff, Infinity Q, SQN and the 16% of managers whose wire-approval story differs from the administrator's.

## 10.7 Red flags

**Kept from v1:**
- No independent administrator or custodian.
- Auditor too small or recently changed.
- Refusal of direct service-provider contact or an on-site visit.
- Guaranteed or suspiciously smooth returns. v2 widening: returns that are smooth relative to the stated strategy, at any level (Antle, Yale Insights).

**Added in v2:**
- Unaudited fund (Momentum Advisors): automatic pass.
- Non-Big 4 or niche auditor combined with internal pricing; both associated with misrepresentation (Trust and Delegation).
- Manager's account of cash controls or wire authority differs from the administrator's (16% base rate).
- Verbal figures that contradict the manager's own documents (20% base rate).
- Refused or deflected DD questions (14% base rate).
- "Independent valuation" that the principal prepares, or a pricing service whose inputs the manager controls (SQN; Infinity Q).
- Fixed "distribution rate" on an illiquid fund (GPB).
- Successor fund much larger than the funds that produced the track record, without a matching increase in senior team (Metrick and Yasuda; Swensen).
- Track record shown as a compounded IRR, or IRR compared with a time-weighted index (Yale News 2018; 10.10).
- Sharpe or Sortino offered as proof of skill for a strategy that uses options or leverage (Goetzmann et al. RFS 2007).
- Peer benchmark that does not state whether it excludes backfill and includes dead funds (Malkiel and Saha).
- Refusal to provide the ILPA Performance Template or performance ex-subscription line (ILPA 2025).
- Monitoring agreements with acceleration on exit; portfolio-company fees not 100% offset without disclosure (Metrick and Yasuda; Blackstone 2015-16).
- Founders holding most carry while those who generated the track record hold little, or founders who will not be in seat for the fund's life (Ivashina and Lerner).
- No formal succession plan in a founder-led firm (HLS Forum 2026).
- Hedge clauses waiving fiduciary duty except for gross negligence or fraud (SEC exam findings).
- LPA with neither key-person dissolution nor a workable removal right (Morley).
- Deal pace or AUM doubling without the bench doubling (Davis et al.).
- Fee tiers you cannot see; MFN that excludes the best tier (Begenau and Siriwardane).

## 10.8 Data room index (LP diligence on a GP)

1. PPM, draft LPA, subscription documents, side-letter template and MFN compendium.
2. ILPA DDQ 2.0 responses, with Appendix A documents.
3. ILPA Performance Template for each prior fund (gross/net IRR and TVPI with and without the sub line) and quarterly ILPA Reporting Template history.
4. Fund-level cash flows for every prior fund and vehicle, including closed, abandoned and side vehicles, with dates (needed for PME, KS-PME and GPME).
5. Deal-level track record: entry/exit dates, invested, realized, unrealized, entry and exit multiples, EBITDA at entry and exit, leverage at entry, deal lead.
6. Audited financial statements of every fund for 3+ years; auditor engagement letters; management letters.
7. Valuation policy, valuation-committee minutes, third-party valuation engagement letters and reports; marks versus exit prices for the last 3 years of realizations.
8. Fee and expense allocation policy; schedule of all management fees, offsets, portfolio-company fees, broken-deal expenses and operating-partner costs for 3 years.
9. Fee-tier schedule and commitment thresholds.
10. Carry and GP-ownership allocation by person for the current and prior funds; vesting and clawback guarantees.
11. Organization chart, bios, departures in 5 years with reasons, succession plan.
12. Form ADV Parts 1 and 2; compliance manual; code of ethics; SEC exam correspondence, deficiency letters, Wells notices for 5 years.
13. LPAC minutes and consents for 3 years.
14. Co-invest allocation policy and the list of co-invests offered, to whom and on what terms.
15. Subscription-line and NAV-facility agreements, borrowing history and LPAC consents (Chapter 14).
16. GP-led and continuation-vehicle history (Chapter 13).
17. Service-provider list with contacts: administrator, custodian, prime broker(s), auditor, valuation agent, legal counsel; bank signatory list and wire-approval matrix (from the bank or administrator).
18. Quarterly letters and portfolio commentary since the predecessor fund's first close.
19. Cyber, business-continuity and IT policies; vendor-diligence files.
20. Litigation list for the firm and each principal.

## 10.9 Fee economics and terms benchmark

**Metrick and Yasuda benchmark (238 funds, 1992-2006).** Rodney White WP 07-17 (https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf); RFS 2010 (https://econpapers.repec.org/RePEc:oup:rfinst:v:23:y:2010:i:6:p:2303-2341). Dated sample: use for structure and relative size, confirm current terms against your own pipeline.

| Term | Buyout | VC |
|---|---|---|
| Expected PV of GP revenue per $100 committed (median) | $19.36 ($10.34 mgmt fees, $5.35 carry, $1.44 entry transaction fees, $2.11 monitoring and exit fees) | $23.50 (about $14.61 fees, $8.86 carry) |
| Median lifetime management fees, % of committed | 12% (IQR 10% to 13.5%) | 17.75% (IQR 14% to 21.25%) |
| Funds with a hurdle | 93.1% (8% modal, mostly 100% catch-up) | 47.6% |
| Hurdle band | 6% to 10%, 8% modal | |
| Fee basis switches to invested capital after the investment period | 84% | 43% |
| Carry basis on committed capital | 83% | 92% |
| LPAs sharing transaction fees with LPs | About 80% (a third return 100%, a third split 50/50) | |
| Monitoring fees | 1% to 5% of portfolio-company EBITDA a year, typically shared 80/20 in the LPs' favor | |
| Fixed share of GP revenue | About 60% (2007 WP) to about two-thirds (2010 RFS); higher in buyout | Lower than buyout |

- **Fee tiers within the same fund.** Across about 2,400 PE funds (1990-2019), most funds run a two-tier fee structure; within a fund, management fees differ by about 91 bps and carry by about 5.8 percentage points on average between tiers (much smaller in VC). Tier is predicted by LP size and sophistication, by the GP's law firm, and by unexplained negotiating skill and relationships; top-performing GPs use fewer tiers (Begenau and Siriwardane, "Fee Variation in Private Equity," JF 2024, HLS Forum summary, https://corpgov.law.harvard.edu/2024/05/10/fee-variation-in-private-equity/; NBER w29887, https://www.nber.org/papers/w29887). CHECK: ask for the full tier schedule and thresholds, invoke MFN, and compare your net terms to the best tier. A 90 bp a year gap compounds to a large net-return gap over a 10-year fund.
- **Real estate fund fees (dated, 2002):** 1% to 2% of committed capital plus a 20% promote; sponsor co-invest 2% to 25% (Linneman and Ross, KaW, July 31, 2002, https://knowledge.wharton.upenn.edu/article/towards-greater-transparency-in-real-estate-private-equity-funds/). Real estate sponsors draw the same SEC fee findings as PE sponsors (unauthorized fees, no step-down after write-downs, extensions without consent, related-party property management or construction fees without LPAC consent) (HLS lane; Chapter 1).
- **CLO managers:** management fees typically about 50 bp of collateral, falling since 2017; underwrite on after-fee PME by vintage (Cordell, Roberts and Schwert, https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf; Chapter 4).
- **Fund-of-funds layer:** fund-of-funds returned less than the hedge-fund universe after the second fee layer (Malkiel and Saha, CEPS WP 104). Price the second layer against what it adds in access.
- CHECK: model GP revenue in base and downside; compute the fixed share. If fees, not carry, pay the partners in the downside, alignment is weaker than the headline carry suggests.
- CHECK: deal-level fee audit. For every buyout, list every transaction, monitoring, director and exit fee charged to the company and apply the LPA offset.

## 10.10 Return measurement and benchmark hygiene

**IRR rules.**
- Never compound an IRR, and never compare an IRR to a time-weighted index. Yale reported a 20-year VC IRR of 165.9% to June 2018 and said it should not be compounded because it was dominated by internet-boom distributions; the 20-year time-weighted figure was 24.6%. Yale uses dollar-weighted IRR for illiquid classes because "the managers... determine when to buy and sell" (Yale News, Oct. 2018, https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion).
- IRR is sensitive to holding period and financing events. Report gross and net IRR with TVPI, DPI and a PME (Kaplan-Schoar PME; generalized PME, Korteweg-Nagel) (Wharton lane; Cordell, Roberts and Schwert 2020 methodology).
- Show IRR with and without the subscription line (ILPA 2025), with and without NAV-loan-funded distributions (Chapter 14), and with and without the largest one or two exits (Yale).
- **Investor (dollar-weighted) returns can be far below fund returns.** The ten best internet funds of 1997 to 2002 showed +1.5% a year time-weighted, but investors lost $9.9B of $13.7B invested (72%) because money came in near the top. Morningstar found dollar-weighted below time-weighted returns in all 17 equity categories, a 13.4-point a year gap for tech funds (Swensen, ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9). For evergreen and semi-liquid funds, request investor-level returns and flow history (Chapter 15).

**Benchmark choice.**
- Buyout: benchmark against a levered small-value public index, not just an S&P 500 PME. Treat low reported volatility and low correlation as an accounting artifact of appraisal-based, hold-to-maturity marks: the replicating portfolio's measured beta falls from about 2 to statistically zero under mark-at-cost accounting (Stafford, RFS 2022).
- Private funds generally: payoffs are partly spanned by public factors; across nearly 5,000 funds, Goetzmann, Gourier and Phalippou extract latent "private factors," several only weakly correlated with public markets. Benchmark against size, value and leverage-adjusted equity exposures before crediting alpha ("How Alternative Are Private Markets?," NBER) **WEAK** (abstract-level, preliminary draft). Note: the Yale lane cites this paper as NBER w24941, while the HBS lane cites w24941 as Lerner, Mao, Schoar and Zhang, "Investing Outside the Box." One citation is wrong; confirm the working-paper number before publication.
- Hedge, credit and any short-volatility strategy (credit, merger arb, levered carry, "market neutral"): benchmark against a levered S&P 500 index put-writing series, not a linear beta. The aggregate hedge-fund index's beta, drawdowns and volatility are matched by mechanical put writing; 6% to 10% annual pre-fee alpha against linear factor models (1996-2012) is not reliably distinguishable from put writing; the working-paper fee that equates the put strategy to the index was about 3.6% a year (Jurek and Stafford, "The Cost of Capital for Alternative Investments," JF 2015, NBER w19643, https://www.nber.org/papers/w19643). A strategy earning a steady spread with rare large losses is selling insurance; its calm-year "alpha" is the premium.
- VC: the aggregate is a right-tail business. IRR about 22% and GPME 1.44 for 17,242 US ventures (first funded 1980-2006, tracked to 2018 or exit), but dropping the best 5% makes the risk-adjusted return negative, and returns decline after 1999. Later-stage headline post-money valuations are biased upward (Gornall and Strebulaev, cited there) (Ouyang, Yu and Jagannathan, NBER w27690). CHECK: show VC track records with and without the top one or two outcomes; a "consistent singles" thesis contradicts the base rate; never mark off a headline post-money with preferences, ratchets or participation.
- Real estate funds: no risk-adjusted outperformance for US public pensions (1995-2018); require a levered public-REIT comparison (Korteweg et al., HLS Forum 2025; Chapter 1).

**Database bias haircuts (hedge-fund and manager-universe data).** Two sources, different numbers. Present both; do not average.

| Source | Survivorship | Backfill | Attrition |
|---|---|---|---|
| Malkiel and Saha, TASS 1994-2003 (Princeton CEPS WP 104, https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf; FAJ 2005, https://ideas.repec.org/a/taf/ufajxx/v61y2005i6p80-88.html) | Surviving funds 13.50% vs 9.71% for all funds: 379 bp; live funds out-earned dead funds by almost 750 bp a year (1996-2003) | Backfilled returns averaged over 500 bp a year above contemporaneously reported | Of 604 funds reporting in 1996, fewer than 25% (124) existed in 2004 |
| Swensen, citing Malkiel's estimates (ECON 252 lecture 9) | About 4.4% a year | About 7.3% a year | About 75% of 1996 funds gone by 2004 |
| Swensen, citing Ibbotson (about 3,500 funds) | 2.9% a year | 4.6% a year | |
| Posthuma and van der Sluis (cited in Malkiel and Saha) | End-of-life non-reporting bias over 600 bp a year | | |
| Russell manager universe (Swensen) | Fell from 307 to 177 reporters, 1996-2005; the year-2000 domestic equity universe return was reported as -3.1% at the time and +1.2% in the 2005 database | | |

CHECK: any peer benchmark or "industry average" in a manager deck must state whether it excludes backfill and includes dead funds; otherwise haircut it by several hundred bp before comparing. Benchmark against vintage-matched, survivor-inclusive data.

**Interim marks versus narrative.** In 7,271 company-years in 536 US PE funds (2015-2020, StepStone data), interim returns predict final returns only weakly in years 1-2 (coefficient about 0.16), rising to 0.62 in years 3-4 and 0.78 later. A one-standard-deviation more positive tone in early GP commentary predicts about 3 to 4 points higher annualized final return (sample mean about 7%); commentary on cash flow and business model predicts better outcomes, focus on capital structure predicts worse (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/). Re-up decisions made on a predecessor fund's year-2 marks are made on noise; this is also why endowment re-up skill matters (Lerner, Schoar and Wongsunwai).

**Outside view.** Write down expected net alpha and its benchmark before committing (Siriwardane). If the best-resourced LPs now assume about 8% total portfolio returns (Princeton, 2026; **WEAK**, press-sourced), a sponsor projecting 20%+ net IRRs for a generic buyout strategy needs specific evidence (Chapter 12).

## 10.11 Manager dispersion and persistence (summary; full treatment in Chapter 12)

- Dispersion: buyout first-to-third-quartile spread 13.7 points a year, VC top-to-bottom 43.2 (Swensen, to June 2005). In private markets a median manager forfeits most of the reason to be in the asset class.
- Persistence: present all positions.
  - PE persistence is real and stronger in VC (Kaplan-Schoar), but decays with fund growth; weaker in buyout because successful GPs scale faster (Metrick and Yasuda survey, NBER w16652).
  - Phalippou argues VC persistence is concentrated among funds backed by less sophisticated LPs (via Metrick and Yasuda survey).
  - Top-VC persistence comes from deal access that reputation unlocks, not from better picking or advising (Sorenson, Nanda and Samila, Yale Insights).
  - Hedge funds: close to a coin flip. About 50% of above-average funds repeat the next year (about 55% if funds that stopped reporting are excluded); a top-quartile fund had about a 50% chance of being above average the next year and about a third stayed top quartile (Malkiel and Saha).
  - LP-side skill: endowments outperformed other LPs mainly through re-up decisions (Lerner, Schoar and Wongsunwai) versus pensions' better picks reflecting access, not selection skill (Korteweg, Panageas and Systla).
- CHECK: do not accept "top quartile" as evidence of skill for hedge or liquid-alternatives managers; require attribution and a factor or put-writing benchmark. For PE, test whether the people, strategy and fund size that produced the record are the ones you are buying.

## 10.12 Co-investments

**How it works.** The LP invests directly in one deal alongside the GP's fund, usually with no or low fee and carry, through an SPV or direct holding. The LP takes single-asset concentration and must underwrite the company (Chapter 5) on a compressed timetable.

**Evidence.**
- **Co-invests underperform the fund deals they sit beside.** In 392 direct investments by seven large institutions (1991-2011), co-investments underperformed, consistent with adverse selection (GPs offer larger, weaker deals to co-investors); solo deals the LP sourced itself did better; the advantage of direct investing over funds was limited and concentrated in buyouts (Fang, Ivashina and Lerner, "The Disintermediation of Financial Markets," JFE 2015, https://www.nber.org/papers/w19299).
- **Alternative vehicles (co-invest, SMAs, sidecars) reached about 40% of PE commitments by 2017;** on average they match the PE market but underperform the sponsoring GP's own main fund; top LPs get the good vehicles. If you are not a top-decile LP, assume adverse selection in what you are offered (Lerner, Mao, Schoar and Zhang, "Investing Outside the Box," JFE 2022, https://www.nber.org/papers/w24941).
- **Sponsor dry powder is downside protection.** In 2008-09, PE-backed companies increased investment and raised more equity and debt versus peers, most strongly where the PE firm had more resources (Bernstein, Lerner and Mezzanotti, NBER w23626, https://www.nber.org/papers/w23626). CHECK: confirm the sponsor's uncalled capital and reserve policy in the fund that owns the company.
- **CEO change is the base case.** In 196 buyouts, 69% changed CEO at least once during the hold; over 60% of exit CEOs were appointed after year 2; holds averaged 5.5 years with no change and 8.5 with two (HLS Forum, "The CEO Decision," 2026, https://corpgov.law.harvard.edu/2026/09/23/the-ceo-decision-how-pe-investors-select-and-reassess-leaders-from-entry-to-exit/). Budget an extended hold in the co-invest downside.

**Checklist.**
- Why is the GP syndicating: size cap, concentration limit, or a deal the fund would not take in full? Is the main fund taking its full pro rata?
- Same terms, same security, same price as the fund? Any fee, carry or monitoring fee on the co-invest vehicle?
- Broken-deal and expense allocation between the fund and co-investors (SEC 2015-16 cases, 10.6).
- Information and exit rights: tag/drag, information parity with the fund, ability to sell.
- Full company diligence: QoE, legal, CEO assessment (Chapter 5). Do not rely on the GP's IC memo.
- For family-office or club co-invests: aggregate exposure across all counterparties (Archegos).
- Same-sponsor credit: is the lender affiliated with the equity sponsor, and how are amendments approved (Elias and de Fontenay, YLJ, https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark)?

**Red flags.** Offered late with a short fuse; main fund not taking full pro rata; deal larger than the fund's usual size; co-invest charged fees the fund does not pay; no information parity; sponsor deal pace doubling.

**Hard question.** "How do you decide whether to take a co-invest the GP offers you, given evidence that co-invests underperform the main fund?" (HBS lane interview guide).

## 10.13 GP succession, team stability and carry

- **Succession base rates.** About 6% of GP leaders transition over five years (versus more than 50% turnover for public-company CEOs); fewer than half of GPs have a formal transition plan; 96% of LPs say succession readiness is decisive for re-ups (HLS Forum, "Succession Planning in Private Equity," 2026, https://corpgov.law.harvard.edu/2026/02/21/succession-planning-in-private-equity-a-strategic-imperative-for-gps-and-lps/).
- **Carry follows founder status, not track record.** Across 717 PE partnerships, the mean founder gets 19.2% of carry vs 10.9% for non-founders; mean senior partner 15% of carry and 21% of firm ownership, junior partners 7% and 3%. Underprovision of carry and ownership inequality predicts senior departures, and senior departures hurt the next fundraise. Senior partners who stayed held 16% carry and 23% ownership versus 9% and 13% for those who left (Ivashina and Lerner, "Pay Now or Pay Later?," JFE 2019, https://nber.org/system/files/working_papers/w22660/w22660.pdf; HBS Working Knowledge, https://www.library.hbs.edu/working-knowledge/is-greed-ruining-private-equity-firms).
- **Questions.** Who actually makes investment decisions? Who owns the LP relationship? What happens economically if a founder steps back, and has carry already moved? Has the successor led at scale? Is governance strong enough to manage post-transition conflict? (HLS Forum 2026.)
- CHECK: carry and GP-ownership split by person for current and prior fund; flag funds where those who generated the track record hold little carry, or founders hold most carry but will not be in seat for the fund's life. Match the key-person clause to the people who actually decide.
- Case files: Weston Presidio (2014), Doughty Hanson (2015), Charterhouse (2015) in 10.6.

## 10.14 Third parties

- Independent ODD provider (a typical third-party report cost about $12,500 in the Trust and Delegation sample period; current pricing not sourced).
- Background-check firm (10% of managers caught only by the independent check).
- Fund administrator, custodian, prime broker(s), auditor: each called directly.
- Independent valuation agent for Level 3 marks; confirm engagement letter.
- Fund counsel (LP side) for LPA, side letter and MFN.
- Placement agent: diligence the agent itself (SEC exam deficiency 11).
- For GP-leds: fairness-opinion provider with no other GP mandate (Chapter 13). For NAV facilities: rating agency and independent valuation (Chapter 14).

## 10.15 Legal, structure and regulatory status (as of Nov. 2026)

- **The SEC's 2023 Private Fund Adviser rules were vacated.** On June 5, 2024 the Fifth Circuit (National Association of Private Fund Managers v. SEC, No. 23-60471) vacated all of the SEC's August 2023 rules: quarterly statements, private fund audits, restricted activities, adviser-led secondaries (fairness/valuation opinion), and preferential treatment. No federal rule now requires a quarterly fee/performance statement, a fund audit beyond the Custody Rule's audit option, or a fairness opinion on a GP-led secondary. Contract for them (MoFo, https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules; Paul Weiss, https://www.paulweiss.com/insights/client-memos/fifth-circuit-vacates-private-fund-adviser-rule).
- **Investment Adviser AML rule delayed to Jan. 1, 2028.** FinCEN finalized a two-year postponement; the agency said it intends to review and tailor the rule (FinCEN, https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028; Federal Register, Jan. 2, 2026, https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf; Proskauer, https://www.proskauer.com/blog/fincen-finalizes-twoyear-delay-of-the-investment-adviser-aml-rule-reaffirms-intent-to-further-review-and-tailor-the-rule-and-to-coordinate-with-other-rulemakings). Until then, a registered adviser or exempt reporting adviser has no federal obligation to run an AML program or file SARs; adviser AML/KYC is contractual and voluntary (Chapter 0.3). CHECK: ask every GP whether it voluntarily runs an AML program, who its administrator relies on for investor KYC, and whether the administrator files SARs (FinCEN, above).
- **No federal BOI registry.** FinCEN's Aug. 2026 final rule permanently exempts domestic reporting companies and U.S. persons from CTA beneficial-ownership reporting; collect and verify GP and co-investor ownership directly (Chapter 0.3; Mayer Brown, https://www.mayerbrown.com/de/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons).
- **What to put in the LPA or side letter, since no rule does it for you:**
  - Quarterly ILPA Reporting Template and annual Performance Template, including with/without sub line.
  - Annual audit by a named auditor of adequate size; delivery deadline.
  - Fee and expense definitions; 100% offset of portfolio-company fees; no acceleration of monitoring fees; step-down after the investment period and after write-downs.
  - LPAC consent for affiliated transactions, GP-leds (with true status quo option and fairness opinion), NAV facilities, and term extensions.
  - Sub-line size and duration caps with LP opt-out (Principles 3.0).
  - Key-person with suspension and dissolution; for-cause removal with a workable definition; no-fault divorce threshold.
  - MFN covering the best fee tier.
  - Information rights sufficient to monitor; no hedge clause narrowing fiduciary duty.
  - Clawback with personal or entity guarantees; whole-fund waterfall preferred to deal-by-deal.
- **Sponsor liability reaches funds.** False Claims Act (Riordan, Lewis & Haden named with portfolio pharmacy Diabetic Care Rx; settled 2019 for $21.36M), ERISA multiemployer withdrawal liability (Sun Capital, D. Mass. 2018), control-person liability, veil-piercing, FCPA (Och-Ziff 2016) (HLS Forum, "Secondary Liability Risks for Private Funds," 2019, https://corpgov.law.harvard.edu/2019/10/09/secondary-liability-risks-for-private-funds-recent-developments/). Relevant to LPs in healthcare and government-contract funds (Chapter 17).

## 10.16 Hard questions

1. Show me the ILPA Performance Template for every prior fund, with and without the sub line. What is DPI excluding NAV-loan-funded distributions?
2. List every fund and vehicle you have ever managed, including the ones you closed or abandoned.
3. Who led each realized deal, and are they here and leading in this fund?
4. What share of your realized value came from EBITDA growth versus leverage versus multiple expansion?
5. What is your fixed-fee share of GP revenue in the downside? (Wharton lane interview guide.)
6. Show the full fee-tier schedule. Which tier am I in, and why not the best one?
7. Show three years of portfolio-company fees and the offset calculation. Any monitoring agreement with acceleration?
8. Who has write access to the pricing inputs? Who signs the valuation report, and may I call them?
9. Give me the bank signatory list and wire matrix from the bank or administrator.
10. How is carry split by person, and how did it change from the last fund? Who leaves if the founder steps back?
11. How large is this fund against the funds that earned the track record, and how many senior people have you added?
12. Which of your statements did third-party records contradict in your last ODD review? (Yale lane interview guide.)
13. When did you last decline a hot manager or deal on operational grounds alone? (Yale lane; ask allocators.)
14. What does your benchmark exclude: backfill, dead funds, leverage?
15. Any SEC deficiency letters or Wells notices in five years? Show the response.
16. Which co-invests did you offer in the last fund, to whom, and did the fund take its full pro rata?

## 10.17 Interview guide additions (for B.2)

- "How do you decide whether to take a co-invest the GP offers you, given evidence that co-invests underperform the main fund?" (Fang, Ivashina and Lerner.)
- "What is your fixed-fee share of GP revenue in the downside?" (Metrick and Yasuda.)
- "Which of your managers' or borrowers' statements did third-party records contradict?" (Trust and Delegation.)
- "When did you last decline a hot manager or deal on operational grounds alone?" (Trust and Delegation.)
- "Who can terminate a manager in your program, and how fast?" (PRINCO.)

---

# 11 Further Categories and Niches

*Each uses Chapter 0 plus the nearest sector playbook.*

## 11.0 Category map

v1 table, retained, with a v2 column for additions and cross-references. Several rows now have their own section below or their own chapter elsewhere in v2.

| Category | What the diligence must cover (v1) | v2 additions and cross-references |
|---|---|---|
| Healthcare services | Licensing, reimbursement and payor mix, Stark and anti-kickback compliance, billing quality. QoE must test payor concentration and revenue-cycle quality. | Under PE ownership, nursing-home short-term mortality rose about 10% to 11%, frontline staffing fell about 3%, and costs shifted to fees, interest, and leases; government payors are about 75% of revenue. CHECK: staffing ratios, CMS Five-Star trend after acquisition, fees and leases paid to related parties or landlords, and whether a sale-leaseback leaves rent coverage (Gupta et al., NBER w28474; Knowledge at Wharton, Jul. 2024). See 11.8 and the new Healthcare Services and Physician-Practice Roll-Ups chapter. |
| Life sciences and biotech | IP and patent runway, clinical trial stage and data, FDA pathway, reimbursement. Expert scientific diligence. | Killer-acquisition exit risk, earnout structure, data-integrity audit. See 11.3. |
| Industrials and manufacturing | Capex, maintenance backlog, environmental (Phase I and II), customer concentration, supply chain, equipment condition. | Regulated manufacturing (pharma, food, devices): independent data-integrity audit of quality systems (HBS lane, Akorn; see 11.3). Labor: union contracts, open grievances, pension or withdrawal liability (Yale lane; cross-reference 5.3). |
| Financial services and specialty lenders | Loan tape audit, loss reserves, funding stability, licensing. | Bank-like liquidity tests. See 11.7. Collateral integrity (First Brands, Tricolor): cross-reference Chapters 3 and 4. |
| Sports, media, entertainment | Rights contracts, revenue durability, talent and key-person risk, residuals and royalties. | Primary sources to pull (11.11). |
| Shipping and logistics | Asset surveys, charter contracts, counterparty risk, flag and registry, cyclicality. | No new findings. |
| Agriculture | Land and water rights, commodity price exposure, crop and weather risk, offtake. | Water-right seniority and curtailment; Colorado River structural deficit. See 11.4. |
| Secondaries | NAV validation, underlying asset marks, GP consent, discount rationale. | Distinguish the GP's dollar-weighted IRR from a TWR; ask for NAV marks against public-factor benchmarks. Yale reportedly sold part of its PE portfolio on the secondary market in 2025, so expect sophisticated sellers (press-reported, Bloomberg, not Yale-sourced). Infrastructure LP stakes priced about 91% of NAV in H1 2026 (Jefferies, July 2026). See the new Secondaries and GP-Led Continuation Vehicles chapter. |
| Distressed and special situations | See Chapter 4.2. | No change. |
| Crypto and digital assets | See 11.1. | Rebuilt in v2. |
| Tokenized real-world assets | (new) | See 11.2. |
| Physical climate, water, insurability | (new, cross-asset) | See 11.5. |
| Policy, appropriation, government counterparties | (new, cross-asset) | See 11.6. |
| SPACs, de-SPACs, PIPEs | (new) | See 11.9. |
| Theme vehicles (AI, crypto, climate, space SPVs) | (new) | See 11.10. |
| Litigation finance; NAV lending; search funds; evergreen vehicles; PE-owned insurers | (new) | Cross-reference the new chapters and sections drafted by other lanes (Litigation Finance; NAV Lending and Fund Finance; Search Funds and ETA; Chapter 10 evergreen vehicles; Chapter 4 insurance-linked balance sheets). |
| Franchise, insurance and specialty finance, sports franchises, family-office directs, farmland, art, music royalties | (new) | Not yet researched; primary sources to pull in 11.11. |

---

## 11.1 Crypto and digital assets

### 11.1.1 What v1 said (retained)

- Custody and key management. Smart-contract audit.
- Token distribution and lockups.
- Wash-trading detection. Exchange and liquidity reality.
- Patterns to screen for, per the "Fraud 2026" file: fake market-making through 15 to 25 wallets, speculative "anchor swaps," self-dealt liquidity, bundled launches, and rug pulls. WEAK (internal file; not externally sourced).
- CHECK: on-chain verification of liquidity depth and holder distribution, independent custody, audited contracts.

### 11.1.2 Regulatory status (as of Nov. 2026)

- **No SEC case is not a clean bill of health.** The SEC dismissed its civil enforcement action against Coinbase on Feb. 27, 2025, explicitly "not a judgment on the merits," to pursue rulemaking via its Crypto Task Force. Absence of an SEC case is no longer evidence that a token or platform is compliant; diligence must rest on custody, audit and on-chain verification (SEC Press Release 2025-47, https://www.sec.gov/newsroom/press-releases/2025-47).
- **GENIUS Act (2025), payment stablecoins.** Payment stablecoins must be backed 1:1 by high-quality liquid assets (cash, demand deposits, short-dated Treasuries, repo, certain money-market funds), held for holders' benefit, audited, and not lent, pledged or rehypothecated (Circle Internet Group FY2025 annual report describing GENIUS Act requirements, https://www.sec.gov/Archives/edgar/data/1876042/000187604226000116/a2025annualreport0331.pdf; HLS Forum, "Financial Institutions M&A Key Trends and Outlook," 2026, https://corpgov.law.harvard.edu/2026/04/24/financial-institutions-ma-key-trends-and-outlook-2/). Secondary description via an issuer filing and a law-firm post; confirm against the statute and implementing rules.
- **Reserve-report criteria.** AICPA reserve-report criteria were issued March 2025 (noted as non-Wharton context in Wharton BDAP, "Stablecoin Toolkit," Parts I to II, 2026, https://bdap.wharton.upenn.edu/wp-content/uploads/2026/01/Stablecoin-Toolkit.pdf). WEAK until confirmed on aicpa-cima.com.
- **Sanctions.** OFAC's SDN list includes crypto addresses; screening must be address-level, not only name-level (Princeton lane; see 11.1.8).

### 11.1.3 Base rate: exchanges and custodians fail

The Princeton Bitcoin textbook classifies exchange risk into three types, all of which have occurred: a bank run (fractional reserves, simultaneous withdrawals), an operator fraud or Ponzi, and a hack (including insiders). A 2013 study (Moore and Christin) found 18 of 40 Bitcoin exchanges had closed through failure or inability to pay customers. Mt. Gox, once the largest exchange, became insolvent without being able to explain where the coins went (Narayanan, Bonneau, Felten, Miller and Goldfeder, "Bitcoin and Cryptocurrency Technologies," Princeton University Press, ch. 4.4, free draft at https://bitcoinbook.cs.princeton.edu).

Werbach's rule for any custodian or exchange: do not commit fraud, and do not use customer money for other ventures. After FTX he warned that opaque firms may have been carrying unrecognized holes from earlier failures (Celsius, Three Arrows, Terra) (Knowledge at Wharton podcast, "What the FTX Collapse Means for the Cryptocurrency Market," Nov. 22, 2022, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/what-the-ftx-collapse-means-for-the-cryptocurrency-market/). WEAK on the "holes" claim (podcast-sourced); the rule itself is the standard.

### 11.1.4 Proof of reserves AND proof of liabilities

**Proof of reserves is half a proof.** A proof of reserves (payment-to-self plus signing a third-party challenge string with the same key) proves only that whoever controls those coins cooperated, and only a lower bound on assets. Solvency needs a matching proof of liabilities: a Merkle sum tree with every customer balance as a leaf, a signed root, and each customer able to verify inclusion and that every node sums correctly with no negative balances. Reserves alone can be borrowed for the snapshot (Narayanan et al., ch. 4.4 "Proof of reserve" and "Proof of liabilities").

**CHECK:**

1. Require both reserves and liabilities proofs, dated the same block.
2. The challenge string comes from you or an independent party, not the exchange.
3. A sample of real customer accounts independently verifies inclusion.
4. Check that the reserve addresses were not funded shortly before the snapshot and drained after (on-chain flow review around the attestation date).
5. Liabilities include derivatives, loans and fiat, not just spot crypto.
6. An auditor with crypto-custody competence, and segregation of customer assets with an independent custodian (general lane, FTX; Werbach).
7. Reconcile customer assets to liabilities on the balance sheet: the balance sheet records customer assets and the matching liabilities (Yale Insights, Antle, https://insights.som.yale.edu/insights/did-crypto-cause-the-ftx-collapse).

FTX had no meaningful proof of liabilities; the bankruptcy estate later found customer and corporate funds were commingled (FTX debtors' first interim report, summarized by Axios, https://www.axios.com/2023/06/27/ftx-management-misuse-customer-funds).

GAP: proof-of-reserves standards for custodians and exchanges (who supplies the challenge, liabilities coverage, auditor scope) are not settled. Interview a crypto custody auditor (Princeton lane).

### 11.1.5 Key control and cold storage

Hot and cold wallets must use separate keys; cold keys should be split (threshold secret sharing or t-of-n multisignature) so no single person can move funds (Narayanan et al., ch. 4.2 to 4.3).

**CHECK:** obtain the key-ceremony documentation, the signer list and geographic separation, and test that withdrawals require the stated quorum. A single founder holding keys is the crypto version of the Chapter 0.4 segregation-of-duties failure.

> **CASE FILE: SOLE KEY HOLDER**
>
> **QuadrigaCX (2019).** After the CEO died, reportedly the sole key holder, the Ontario Securities Commission found the exchange had run as a Ponzi, with fictitious balances credited to aliases and at least C$169M of client losses (OSC staff report, "QuadrigaCX: A Review," June 2020, https://osc.ca/quadrigacxreport/index.html).
>
> **THE CHECK** Key-ceremony documentation, signer quorum tested, no single key holder; proof of liabilities to expose fictitious balances.

### 11.1.6 Stablecoins and tokenized cash

- **GENIUS Act reserve test.** CHECK: for any stablecoin exposure or issuer investment, obtain the reserve attestation, its date and auditor, the custodian list, and confirm no encumbrance; an unregulated or offshore coin that cannot show this is a different (and higher) risk class (HBS lane; Circle FY2025 annual report).
- **What a reserve report proves.** Diligence covers reserve composition, redemption mechanism, and regulatory status. Algorithmic, crypto-collateralized, and synthetic designs sit largely outside the segregated-reserve frameworks. A reserve report shows backing at a point in time; controls keep it between reports (Wharton BDAP, Stablecoin Toolkit, 2026).
- **Holding the peg under stress is not proof of safety.** Gorton likens stablecoins to free-banking-era private banknotes, which traded at discounts and suffered runs. Tether briefly broke its peg in 2022 and recovered. Reserve reports build reputation but do not remove run risk. CHECK: require reserve composition at the instrument level, its custodian, and redemption terms and timing for non-retail holders (Gary Gorton, "Stablecoins Survived 'Crypto Winter,' But That Doesn't Make Them Safe," Yale Insights, https://insights.som.yale.edu/insights/stablecoins-survived-crypto-winter-but-that-doesnt-make-them-safe).
- **Vulnerability framework.** Score each money-like product on five features: liquidity transformation; threshold effects (a peg or $1 NAV that invites runs once broken); use as a money-like asset; contagion channels; reactive investors. Apply it to any stablecoin, tokenized MMF or "yield-bearing dollar" held as collateral or treasury (Journal of Financial Crises, "A Framework for Understanding the Vulnerabilities of New Money-Like Products," JFC 8(3), https://elischolar.library.yale.edu/journal-of-financial-crises/vol8/iss3/1/).
- **What backs the peg.** For any stablecoin, identify what backs the peg (reserves vs a volatile sister token) and stress the redemption path (HBS lane, Terra).

| Stablecoin feature | Lower risk | Higher risk | Source |
|---|---|---|---|
| Backing | 1:1 HQLA, segregated, unencumbered (GENIUS Act) | Volatile sister token (Terra), crypto collateral, synthetic | Circle FY2025; HLS Forum (Terra); Wharton BDAP |
| Evidence | Dated attestation by a named auditor, custodian list, instrument-level composition | Undated or self-published reserve claim | HBS lane; Gorton |
| Redemption | Stated terms and timing for non-retail holders | Gated, discretionary, or only via secondary market | Gorton |
| Regulatory status | Regulated payment stablecoin | Unregulated or offshore | HBS lane |
| Run features (JFC) | Few of the five | Liquidity transformation plus threshold effect plus reactive holders | JFC 8(3) |

> **CASE FILE: ALGORITHMIC PEG AND SUBSIDIZED YIELD**
>
> **Terra / Luna (May 2022).** Anchor paid a 19.5% yield on UST deposits, funded by a subsidy that reached about $6M a day by April 2022. LUNA peaked at $119.18 on April 5. The run began May 7 when two large addresses pulled 375M UST from Anchor; LUNA supply went from about 1 billion to 6 trillion in three days as UST holders swapped out, a death spiral. Wealthier, sophisticated wallets exited first with small losses; retail ran late and lost more; Alameda Research made the most UST-LUNA swaps, linked to its privileged access via FTX. Pre-run on-chain signals were visible: falling LUNA value relative to UST, a sharp drop in Anchor entries and rise in exits in late April, and a growing subsidy (HLS Forum, "Anatomy of a Run: The Terra Luna Crash," 2023, https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/).
>
> **THE CHECK** (1) Decompose any yield into organic income vs subsidy/emissions and require the subsidy runway. (2) For any stablecoin, identify what backs the peg and stress the redemption path. (3) Monitor large-holder flows on-chain. (4) Ask who has privileged exit routes.

### 11.1.7 Token economics, wash trading and bubble dynamics

- **Token networks can break down by design.** Sockin and Xiong (Princeton) model a token as membership in a platform: because user participation and token price feed each other, the token market can collapse; speculator sentiment crowds out real users and is the source of fragility; expected miner/validator attacks worsen it. CHECK: separate holders and volume into actual platform users versus speculators (wallet-level activity: fees paid for use versus transfers between exchanges). A token whose volume is mostly exchange-to-exchange churn has no user floor (Sockin and Xiong, "A Model of Cryptocurrencies," Management Science 2023, NBER w26816, https://www.nber.org/papers/w26816).
- **Supply unlocks puncture bubbles.** Xiong's review of historical bubbles (tulips, South Sea, railways, 1920s, internet, Chinese warrants) finds four common features: they coincide with technological or financial innovation; they feature frenzied trading, often by new investors; they are vulnerable to increases in asset supply; and they can burst without warning. The internet bubble's collapse coincided with mass IPO lockup expirations in early 2000 (Ofek and Richardson). In the 2005 to 2008 Chinese warrant bubble, warrants with near-zero fundamental value turned over 328% a day on average. CHECK: for any token or newly listed asset, map the full unlock and emission schedule (team, investors, treasury, staking rewards) against current float and average daily volume; an unlock above several days of real volume within the hold period is a structural price risk. Turnover far above fundamentals is a bubble signature, not a liquidity strength (Xiong, "Bubbles, Crises, and Heterogeneous Beliefs," NBER w18905, https://www.nber.org/papers/w18905). Cross-reference the Chapter 0 credit-cycle and bubble overlay, if adopted.
- **Rational speculators ride bubbles rather than correct them.** Brunnermeier and Nagel showed hedge funds were heavily overweight tech stocks in 1998 to 2000, cut exposure before the peak, and the large fund that refused to ride (Tiger) did not survive. A sophisticated co-investor being in a hot asset is not evidence of value; ask what their exit plan and timing assumption are (Brunnermeier and Nagel, "Hedge Funds and the Technology Bubble," Journal of Finance 2004, https://www.princeton.edu/~markus/research/papers/hedgefunds_bubble.htm).
- **Fraud waves (Soltes).** ICOs, then NFTs, now pump-and-dump dynamics in tokens whose prices move on touting rather than utility; telling some investors that something is a pump-and-dump can attract them ("lottery-ticket" behavior). Red flags: no identifiable product or cash flow, returns marketed as high with "no additional risk," price moves unexplained by fundamentals, heavy social-media/crowd promotion (HBS Working Knowledge, Soltes, 2025, https://www.library.hbs.edu/working-knowledge/ai-schemes-could-make-bernie-madoffs-fraud-look-trivial-eugene-soltes).

### 11.1.8 Crypto company equity: governance first

- **FTX governance baseline.** FTX raised nearly $2B from VCs with no internal audit function and no experienced finance, accounting, HR or security leadership, while customer funds were diverted to an affiliated trading firm (Alameda) (HLS Forum, "Untamed Unicorns," 2026, https://corpgov.law.harvard.edu/2026/11/04/untamed-unicorns-why-startup-finance-is-broken-and-how-to-fix-it/). FTX raised $400M at a $32B valuation, up from $25B six months earlier, before it collapsed (Knowledge at Wharton, Nov. 2022; Erickson, Mar. 2023). There was no accounting department (the work was outsourced), the company could not produce a complete list of its own employees, and customer crypto deposits were not recorded as assets on the main entities' balance sheets; John Ray called it "a complete failure of corporate controls" (Yale Insights, Antle, Dec. 2022).
- **CHECK:** segregation of customer assets verified on-chain and by an independent auditor; related-party trading-firm exposure; who controls keys; existence of a CFO, controller and audit committee (HBS lane); an employee census that reconciles to payroll (Yale Insights, Antle). Controls and accounting infrastructure first, then token economics (Yale Insights, Antle).
- **Last-round valuation is not a mark** (FTX $32B; cross-reference 2.4).

> **CASE FILE: CUSTOMER ASSETS AT AN AFFILIATE**
>
> **FTX (2022).** Customer deposits were routed to and used by Alameda Research; Sam Bankman-Fried was sentenced to 25 years (March 2024) (DOJ SDNY, SBF sentencing release, March 28, 2024 [confirm URL]; FTX debtors' interim report via Axios, URL above).
>
> **THE CHECK** Proof of reserves alone is insufficient; require proof of LIABILITIES and segregation of customer assets with an independent custodian, and an auditor with crypto-custody competence. No accounting function is an automatic pass.

### 11.1.9 Source of wealth, tracing and sanctions (crypto-specific; cross-reference 0.3)

- **On-chain tracing is heuristic.** Blockchain analytics cluster addresses using heuristics (inputs spent together share an owner; fresh change addresses), then label clusters by transacting with known services. These heuristics produce false positives (researchers in the Princeton text had to retract a publicized link caused by an online wallet commingling coins), and "taint" scores assume the adversary uses the same mechanical method, so a low taint score is not proof of clean funds. Mixing services and CoinJoin are designed to defeat these heuristics; custodial wallets mix by default but keep internal records (Narayanan et al., ch. 6 "Bitcoin and Anonymity").
- **CHECK** for any investor or counterparty whose wealth or funds derive from crypto: (1) obtain wallet addresses and a signed message proving control; (2) commission a tracing report from an analytics vendor covering the full history to fiat on-ramps, with mixer, darknet, sanctioned-address (OFAC SDN lists crypto addresses) and high-risk-exchange exposure; (3) obtain exchange account statements and KYC records for the on-ramp; (4) treat any mixer or privacy-protocol exposure as an escalation, not an automatic pass or fail, and document the judgment (same).
- **State hackers.** North Korean state hackers (Lazarus Group) are a primary source of stolen crypto laundered through mixers and DeFi; a Princeton fellowship policy paper documents ransomware and exchange hacks as a sanctions-evasion revenue source. CHECK: OFAC screening for crypto counterparties must include address-level screening, not only name screening (June Park, Princeton Fung Global Fellow, "Cyber-hacking as a Means of Self-reliance," NCNK/Wilson Center, https://ncnk.org/resources/briefing-papers/all-briefing-papers/cyber-hacking-means-self-reliance).

### 11.1.10 Crypto lenders and levered vehicles

Market liquidity and funding liquidity reinforce each other: falling prices raise margins and haircuts (margin spiral) and inflict losses on levered holders (loss spiral), so liquidity can vanish suddenly and across assets at once. CHECK: for any crypto lender or levered crypto vehicle, obtain the haircut/margin schedule and model a simultaneous 20% to 30% collateral price fall plus a haircut increase; confirm what assets are sold first and whether a forced sale would breach covenants elsewhere (Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity," RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf). Celsius and Three Arrows are named as earlier failures (Werbach, KaW podcast, Nov. 2022); no case detail was sourced in this pass. GAP.

### 11.1.11 Failure cases

| Case | Year | What happened | CHECK that would have caught it | Source |
|---|---|---|---|---|
| Mt. Gox | 2014 (year from public record; not stated in the source) | Largest exchange became insolvent without being able to explain where the coins went | Proof of reserves AND liabilities; independent custody | Narayanan et al., ch. 4.4 |
| 18 of 40 Bitcoin exchanges | Study 2013 | Closed through failure or inability to pay customers | Treat exchange failure as a base rate, not a tail | Moore and Christin, via Narayanan et al. |
| QuadrigaCX | 2019 | Sole key holder died; OSC found a Ponzi with fictitious balances, at least C$169M client losses | Key quorum; proof of liabilities | OSC, June 2020 |
| Terra / Luna | 2022 | 19.5% subsidized yield; algorithmic peg; LUNA supply 1B to 6T in three days | Yield decomposition; what backs the peg; large-holder flows | HLS Forum 2023 |
| Tether peg break | 2022 | Briefly broke its peg and recovered | Instrument-level reserves; redemption terms | Gorton, Yale Insights |
| FTX | 2022 | Customer deposits used by Alameda; no accounting department; SBF sentenced to 25 years (2024) | Proof of liabilities; segregation; CFO, controller, audit committee | General lane; HBS lane; Yale Insights; Axios |
| Coinbase (SEC action dismissed) | 2025 | Dismissed "not a judgment on the merits" | Do not read an absent enforcement action as compliance | SEC 2025-47 |

### 11.1.12 Red flags

**RED FLAG** list:

- Proof of reserves with no proof of liabilities, or a challenge string supplied by the exchange (Narayanan et al.).
- Reserve addresses funded just before the attestation and drained after (Narayanan et al.).
- One person holds the keys (QuadrigaCX).
- No in-house controller or CFO; no internal audit; no employee census (FTX; Yale Insights; HLS Forum).
- An affiliated trading firm with privileged exit or credit lines (FTX; Terra).
- A yield with no organic source, or a subsidy with no runway (Terra).
- A stablecoin backed by a sister token, or a reserve report that is undated, unaudited, or not at instrument level (Terra; Gorton; HBS lane).
- Volume that is mostly exchange-to-exchange churn (Sockin and Xiong).
- An unlock or emission above several days of real volume inside the hold period (Xiong).
- Returns marketed as high with "no additional risk"; price moves unexplained by fundamentals; heavy social-media promotion (Soltes).
- "No SEC action" offered as evidence of compliance (SEC 2025-47).
- Source-of-wealth story with no wallet addresses, no signed message, or a mixer history waved away (Princeton lane).
- v1 patterns: fake market-making through 15 to 25 wallets, speculative "anchor swaps," self-dealt liquidity, bundled launches, rug pulls ("Fraud 2026" file, WEAK).

### 11.1.13 Hard questions

- Show proof of reserves and proof of liabilities at the same block height, with our challenge string. (Narayanan et al.)
- Who holds keys, what is the quorum, and where are the signers? Show the key-ceremony record. (Narayanan et al.)
- Where is the yield coming from, and how long can the subsidy run? (HLS Forum, Terra)
- What backs the peg, who audits it, as of what date, and how fast can a non-retail holder redeem? (Gorton; HBS lane)
- Who is your controller, who is on the audit committee, and who audits customer-asset segregation? (FTX)
- What share of volume is from real users rather than transfers between exchanges? (Sockin and Xiong)
- Show the full unlock and emission schedule against daily volume. (Xiong)
- For crypto-derived wealth: show the wallets, sign a message, and let us trace to fiat. (Princeton lane)

> **THE ONE CHECK**
>
> Prove solvency, not holdings: reserves AND liabilities at the same block, with a challenge you supplied, customer assets segregated at an independent custodian, and keys under a tested multi-person quorum. That would have caught FTX and QuadrigaCX.

---

## 11.2 Tokenized real-world assets (new)

**How it works.** A token is usually a contractual or beneficial claim on an off-chain asset (credit, real estate, Treasuries) held by an issuer, custodian, trust, or SPV, not direct title (Cong, Mayer and Rabetti, "Tokenizing Real-World Assets," WFFI (Wharton) Policy Series white paper, 2026, https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf).

**Market size (April 2026).** About $29B on public chains, excluding about $300B of stablecoins, plus $16.9B of private-credit tokens on Figure's Provenance chain, for about $46B in total. Up from about $2.9B in 2022 and about $12B at end-2024 (same).

**Core principle.** A tokenized claim's trading speed should match the speed at which the underlying asset can honor redemptions (same). A token that trades 24/7 on an asset that redeems quarterly is a liquidity mismatch (compare the JFC money-like-product framework in 11.1.6).

**Diligence checklist** (Cong, Mayer and Rabetti 2026):

- What legal right the token conveys, and whether it is enforceable.
- The custodian, and whether the asset is bankruptcy-remote from the sponsor.
- Redemption mechanics, timing, and gates.
- Oracle design, governance, and fallback rules for NAV and collateral prices.
- Independent audit of the reserves or underlying assets.
- Then underwrite the underlying asset with its own chapter (Chapter 1 for real estate, Chapter 3 or 4 for credit); tokenization changes the wrapper, not the credit.

**Red flags.** "Ownership" language for what is a contractual claim. No bankruptcy-remote holder. Secondary trading faster than redemption with no gate disclosure. A single oracle with no fallback. Reserves attested by the sponsor.

**Hard questions.** If the issuer fails, what do token holders own and in which court do they enforce it? Who holds the asset, and is it off the sponsor's balance sheet? How long does a redemption actually take, and when can it be gated? Who sets the NAV the token trades on?

---

## 11.3 Life sciences and biotech

**v1 row, retained.** IP and patent runway, clinical trial stage and data, FDA pathway, reimbursement. Expert scientific diligence.

**Strategic-exit thesis risk: killer acquisitions.** About 6% of pharma acquisitions (6.4% in the working paper) were "killer acquisitions," bought to shut down an overlapping drug project. They cluster just below Hart-Scott-Rodino notification thresholds; the authors estimate as many as 50 a year in pharma (Colleen Cunningham, Florian Ederer, Song Ma, "Killer Acquisitions," JPE 2021, SSRN 3241707, https://papers.ssrn.com/abstract=3241707; Yale Insights, https://insights.som.yale.edu/insights/when-corporate-acquisitions-affect-healthcare). Implications:

- An exit thesis that relies on a strategic acquirer with an overlapping program should expect growing FTC and DOJ scrutiny of sub-threshold deals.
- Earnouts and milestones tied to continued development are at risk when the buyer has an overlapping program and may shelve the asset. Require diligence covenants on development effort (Yale lane).

**Earnouts are the norm in life sciences.** Outside life sciences, earnouts appear in about one in five private deals (15% in 2019, peak 30% to 37% in 2023, about 22% in 2024). In life sciences, over 80% of private pharma deals use them, median about 61% of total consideration, often 3 to 5 years. Dispute risk rises with earnout share and length (HLS Forum, "The Art and Science of Earn-Outs in M&A," 2025, https://corpgov.law.harvard.edu/2025/07/11/the-art-and-science-of-earn-outs-in-ma/). Drafting checklist: objective milestone definitions with worked examples; explicit efforts standard or fixed spend commitment; buyer reporting and audit rights; acceleration triggers (including on shelving or sale of the program); expert-not-arbitrator scope; records of efforts (same).

**Data integrity in regulated manufacturing.**

> **CASE FILE: DATA INTEGRITY**
>
> **Fresenius / Akorn (2017 to 2018).** Fresenius's diligence flagged deficiencies in Akorn's testing and manufacturing but it signed anyway; post-signing whistleblower letters led to an investigation finding falsified data and FDA submissions with false data. Delaware Chancery (2018) let Fresenius walk under the MAE clause (first such ruling), but noted the agreement did not carve out diligence-disclosed matters. Akorn's CEO testified he never read the audit reports he received (Skadden, "Analyzing Akorn," https://www.skadden.com/insights/publications/2018/10/analyzing-akorn; Delaware Chancery opinion, https://law.justia.com/cases/delaware/court-of-chancery/2018/ca-2018-0300-jtl.html).
>
> **THE CHECK** In regulated manufacturing (pharma, food, medical devices), run an independent data-integrity audit of quality systems (raw lab data vs reported data, FDA 483s and warning letters, audit trails), and draft specific closing conditions or indemnities for every known regulatory issue rather than relying on a general MAE.

**Checklist additions.** Independent data-integrity audit (Akorn). Overlap map of likely acquirers' pipelines (killer acquisitions). Earnout and milestone terms against the checklist above. Patent runway and FDA pathway (v1).

**Red flags.** Exit thesis dependent on one overlapping strategic buyer. Milestones with no efforts covenant. FDA 483s or warning letters not reconciled to remediation. Management that has not read its own audit reports (Akorn).

**Hard questions.** Which likely acquirers have an overlapping program, and what happens to our milestones if they shelve this one? Show raw lab data against reported data for the pivotal studies. List every 483 and warning letter and its close-out.

---

## 11.4 Agriculture, farmland and water

**v1 row, retained.** Land and water rights, commodity price exposure, crop and weather risk, offtake.

**Water-right seniority and curtailment risk.** About 80% of Colorado River allocations go to agriculture; the Imperial Irrigation District holds the largest right. Water rights are often carried as permanent assets with no impairment for junior priority (Todd Cort, "The Colorado River Is Overdrawn," Yale Insights, May 2026, https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent).

**The structural deficit.** The 1922 Colorado River Compact allocates 16.5M acre-feet a year, but 2000 to 2023 flows averaged about 12.5M (a structural deficit of about 4M a year). Lakes Mead and Powell are at about one-third of their 2000 levels, and further flow declines of 20% to 30% are projected (same).

**CHECK:**

- Water source, seniority (senior versus junior rights), and curtailment priority for every acre and facility; impair junior rights in the valuation, whatever the balance sheet says.
- Stress water cost at post-2026 tiered pricing (same).
- Bindable crop and property insurance for the hold (11.5).
- Commodity price and offtake per v1.

**Primary data to pull (not yet retrieved).** USDA NASS Land Values and Cash Rents summary (annual, August); NCREIF Farmland Index (general lane, suggested primary sources). GAP: farmland cap rates, cash-rent yields and transaction benchmarks not sourced in this pass.

**Red flags.** Junior water rights carried at full value. A farmland or water-dependent thesis in the Colorado River basin with no curtailment case. Crop insurance assumed at historical premiums.

**Hard questions.** What priority date does each water right carry, and what happens to yield if junior rights are curtailed? What did water cost per acre-foot in each of the last five years, and what is the tiered price after 2026?

---

## 11.5 Physical climate, water and insurability risk (new, cross-asset)

Applies to long-lived real assets: real estate (Chapter 1), infrastructure and power (Chapter 6), data centers (6A), agriculture (11.4). Yale lane proposed this as its own section (Cort and Yale Insights climate pieces).

**Insurability is a diligence gate.** In parts of California wildfire coverage is unavailable, and banks will not lend against uninsurable property, leaving cash-only buyers and lower values. In property-tax states, falling values erode the municipal revenue base, a possible "nasty spiral" (Yale Insights, "Putting a Price on Climate Risk," https://insights.som.yale.edu/insights/putting-price-on-climate-risk).

**Premiums are repricing through reinsurance.** Using more than 74M premiums inferred from mortgage escrow data (2014 to 2024), Keys and Mulder find that average homeowners premiums rose about 33% from 2020 to 2023 ($1,902 to $2,530). Against 2018: Florida premiums up 90% by 2023, Texas up 50%. The pass-through from disaster risk into premiums doubled; reinsurance costs roughly doubled from 2017 to 2023 and drove most of the rise. Premium increases are capitalized into values: home price growth was more than $40,000 lower in the most exposed ZIP codes (an earlier version reported about 11% lower relative 2024 prices). The data is residential, but the reinsurance channel is the same one that prices commercial property coverage (Keys and Mulder, "Property Insurance and Disaster Risk: New Evidence from Mortgage Escrow Data," NBER w32579, rev. Oct. 2026, https://www.nber.org/papers/w32579; Knowledge at Wharton, "How Higher Property Insurance Premiums Mirror Climate Risk," Sep. 24, 2024, https://knowledge.wharton.upenn.edu/article/how-higher-property-insurance-premiums-mirror-climate-risk/).

**Water.** Colorado River structural deficit of about 4M acre-feet a year (Cort, 2026; 11.4). Data-center cooling in Phoenix and the Front Range depends on it (6A.3).

**Extreme weather and the grid.** Winter Storm Uri (2021): about $140B of estimated losses, about $90B of it property and casualty (Yale Insights, Hirs; 6.7).

**CHECK** (all from the sources above):

- Bindable insurance quotes (not indications) for the full hold; stress a 2x premium (Yale Insights).
- A three-year premium history, a current bound quote at closing, and the deductible and named-storm or wildfire terms; stress exit value for capitalization of higher premiums (Keys and Mulder).
- Flag any asset where coverage depends on a state insurer of last resort (Yale Insights).
- Water source and seniority; post-2026 tiered water pricing (Cort).
- For power and data centers: winterization and freeze-event fuel (Hirs).

**Red flags.** Insurance expense held flat in a coastal or wildfire market (Keys and Mulder). Coverage only from a state insurer of last resort. An indication presented as a bound quote. No water-source answer in an arid market.

**Hard questions.** What is the bound insurance quote today against the pro forma, and what did premiums do over the last three renewals? Is the asset insurable at a bindable price for the full hold, and what is the water source and its priority?

---

## 11.6 Policy, appropriation and government-counterparty risk (new, cross-asset)

Yale lane proposed this as its own section: government tenants' termination options, legislative sweeps of public funding, and market-design risk in deregulated power.

| Risk | Evidence | CHECK | Chapter |
|---|---|---|---|
| Government tenant termination for policy | DOGE listed 793 federal leases (about 9M sq ft) for cancellation in 2025; 384 were still listed by August 2025. GSA leases average 14 years against 5 to 10 for private tenants; early-termination options are typically exercisable after year 5 on 90 to 120 days' notice, historically almost never used. In D.C. buildings with listed leases, landlord NOI fell 5% and junk-rated CMBS fell about 4% more than comparable GSA-backed bonds. Barclays put CMBS tied to government-leased buildings at about $12B (LaPoint and Choi, via Yale Insights, https://insights.som.yale.edu/insights/doges-lease-cancellations-are-already-hitting-the-commercial-real-estate-market) | Read every government lease for ETOs and termination-for-convenience rights, model the exercise case, cap single-agency share of NOI | 1 |
| Legislative sweep of public funding | Connecticut Green Bank, 2018 (Yale SOM case) | Confirm whether funds can legally be swept; model their loss | 6.10 |
| Concession renegotiation | 54% of transport and 74% of water concessions renegotiated (World Bank; Gomez-Ibanez) | Tariff-adjustment track record; termination compensation | 6.11 |
| Tax-credit repeal | OBBBA 2025: about 29 GW less solar and 43 GW less wind through 2030 (REPEAT, approximate, not peer reviewed) | No-credit downside case; begin-construction and FEOC evidence | 6.10 |
| Market-design change in power | ERCOT did not pay for winterization (Uri, 2021); PJM capacity collar and 2026 large-load proposals (Kleinman, WEAK) | Model rule changes as a variable; collar-expiry case | 6, 6A |
| Ratepayer backlash | 20% residential bill increase in parts of New Jersey became a 2025 governor's-race issue (Princeton arXiv 2609.08166); colocation centers raised consumer costs (HBS Working Knowledge) | Large-load tariff, rate cases, moratorium risk | 6A.3 |
| Enforcement posture is not compliance | SEC dismissed Coinbase action, "not a judgment on the merits" (SEC 2025-47) | Diligence on custody, audit, on-chain verification | 11.1 |
| Partial rescheduling | Cannabis: DEA partial final rule (April 2026) moved only qualifying medical and FDA-approved products to Schedule III; adult-use remains Schedule I (Federal Register 2026-08176, via general lane) | See Chapter 8 | 8 |

**THE ONE CHECK (policy).** For every revenue line that depends on a government act (a lease, an appropriation, a credit, a tariff, a market rule), name the act, the date it could change, and the downside if it does. Then model it.

---

## 11.7 Financial services and specialty lenders

**v1 row, retained.** Loan tape audit, loss reserves, funding stability, licensing.

**Bank-like lenders: the uninsured-deposit and duration test.** For any bank, credit union, fintech lender or specialty finance company that funds with deposits or short-term money (Yale lane; JFC, "How US Bank Regulation Failed SVB and Its Supervisors," JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/12/; Andrew Metrick, "The Failure of Silicon Valley Bank and the Panic of 2023," JEP 2024):

- Uninsured share of funding.
- Unrealized losses on securities against equity.
- IRRBB (economic value of equity under rate shocks).
- An LCR-style 30-day outflow test.
- Collateral pre-positioned at the Fed. Signature Bank was "particularly unprepared": it lacked collateral pre-positioned at the Fed (Metrick, JEP 2024).

One JFC analysis argues that the Basel IRRBB standard would have flagged SVB's asset-liability strategy 10 quarters before failure, and the LCR would have forced tens of billions more liquidity at least 4 quarters before (JFC 7(2)).

> **CASE FILE: SILICON VALLEY BANK (2023)**
>
> Uninsured deposits about 94% (FDIC limit $250,000); mark-to-market losses on securities of about $17B at Dec. 31, 2022 exceeded $15B of book equity; a $42B one-day run (Metrick, JEP 2024, via Yale lane).
>
> **THE CHECK** Uninsured-funding share, unrealized loss to equity, IRRBB, and a 30-day outflow test, all from public data.

Cross-reference Chapter 0 (treasury and bank-counterparty diligence) and Chapters 3 and 4 (collateral integrity: First Brands, Tricolor).

---

## 11.8 Healthcare services (cross-reference)

See the new Healthcare Services and Physician-Practice Roll-Ups chapter (general lane). Retain the v1 row. Add the nursing-home evidence in 11.0 (Gupta et al., NBER w28474): short-term mortality up about 10% to 11% and frontline staffing down about 3% under PE ownership, with costs shifted to fees, interest and leases. CHECK: staffing ratios, CMS Five-Star trend after acquisition, related-party fees and leases, and rent coverage after any sale-leaseback.

---

## 11.9 SPACs, de-SPACs and PIPEs (new)

**Net cash per share is the number.** For SPACs that merged between January 2019 and June 2020, the cash actually delivered per $10 share averaged $4.10 (median $5.70) after redemptions, sponsor promote, warrants and fees ($7.50 before redemptions). Later deals were higher but far below $10 (Klausner, Ohlrogge and Ruan, "A Sober Look at SPACs," Yale Journal on Regulation 39 (2022), https://openyls.law.yale.edu/entities/publication/44dd0075-0956-44d1-bb2e-ea326755b4b5; Yale JREG bulletin, "Net Cash per Share: The Key to Disclosing SPAC Dilution," https://www.yalejreg.com/bulletin/net-cash-per-share-the-key-to-disclosing-spac-dilution/). A Harvard Forum critique disputes how much this predicts returns (Yale lane note).

**CHECK:** for any de-SPAC, PIPE or SPAC-adjacent deal, compute net cash per share (cash minus merger costs minus warrant value, over shares). Treat headline EV as unreliable. Cross-reference Chapter 5.

---

## 11.10 Theme vehicles (new)

**Thematic launches buy at the top.** Ben-David, Franzoni, Kim and Moussawi found specialized (thematic) ETFs lose about 30% in risk-adjusted terms over their first five years, not because of fees but because they are launched holding stocks that are already overvalued after a run of performance, media attention and sentiment. The same logic applies to private "theme" vehicles (AI, crypto, space, climate SPVs) raised after a hype cycle (Ben-David, Franzoni, Kim and Moussawi, "Competition for Attention in the ETF Space," RFS 2023, NBER w28369, https://nber.org/papers/w28369).

**CHECK:** compare entry valuation to the sector's own history and to the date the theme peaked in media and fund-launch counts; a wave of new vehicles in the same theme is a late-cycle signal (same). Apply Xiong's four-feature bubble test (11.1.7).

---

## 11.11 Niches not yet researched: primary sources to pull

Proposed by the general lane; not drafted. Each uses Chapter 0 plus the nearest playbook until drafted.

| Niche | Primary sources to pull | Nearest playbook |
|---|---|---|
| Insurance and specialty finance | NAIC statutory filings and RBC ratios; AM Best methodology; state insurance department exam reports | 4; 11.7 |
| Franchise businesses | FTC Franchise Rule (16 CFR Part 436) and the Franchise Disclosure Document (Item 19 financial performance, Item 20 outlet turnover, Item 21 audited franchisor financials); SBA Franchise Directory. Also: about 58% of major franchisors' 2016 agreements contained no-poach clauses, since forced out by state AGs and class actions; review FDD Item 17 and agreements for no-poach and wage-fixing provisions (Krueger and Ashenfelter, NBER w24831, https://www.nber.org/papers/w24831) | 5, 7 |
| Farmland | USDA NASS Land Values and Cash Rents summary (annual, August); NCREIF Farmland Index | 11.4 |
| Music royalties | U.S. Copyright Royalty Board Phonorecords IV mechanical-rate determination; MLC data; historical catalog multiples from public filings (listed royalty funds' NAV disclosures and write-downs) | 5, 11.0 media row |
| Sports franchises | League ownership and debt rules (league constitutions; leaguewide credit facilities); local media-rights contracts | 11.0 media row |
| Art and collectibles | Auction-house disclosure of guarantees and third-party irrevocable bids; title/provenance databases; UCC Article 9 for art lending | 0.5, 3 |
| Family-office direct deals | Aggregate exposure across ALL counterparties, not one prime broker's view (Archegos, 2021; general lane) | 10 |

(General lane, "Suggested primary sources for the chapters not yet drafted.")

---

> **THE ONE CHECK (Chapter 11)**
>
> In every niche, find the one asset that is not what it appears: keys controlled by one person, a reserve with no liability proof, a token that is a contract and not title, a water right that is junior, a policy that is not bindable, a government payment that can be swept. Verify that asset with an independent party before anything else.

# 12 LP Portfolio Construction and Manager Selection

*The allocator playbook: asset allocation, manager selection, pacing, re-up discipline, allocator governance. Chapter 10 covers diligence on a single GP; this chapter covers building and running the program.*

## 12.1 How it works

An allocator (endowment, foundation, pension, family office, fund-of-funds, OCIO) sets a policy portfolio, commits to managers across asset classes and vintages, and manages liquidity between capital calls, distributions and its own spending or benefit payments.

- **Asset allocation drives most return variation; manager selection drives the rest in illiquid assets.** Swensen cites Ibbotson's finding that asset allocation explains over 90% of the variability of institutional portfolio returns (Swensen, Yale ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9).
- **In private markets the manager is the decision.** Ten-year first-to-third-quartile manager spreads to June 2005 (Swensen's figures, same lecture):

| Asset class | Spread (points a year) |
|---|---|
| Fixed income | 0.5 |
| Large-cap equity | ~2 |
| Small-cap equity | 4.7 |
| Hedge funds | 7.1 |
| Real estate | 9.3 |
| Leveraged buyouts | 13.7 |
| Venture capital (top vs bottom quartile, not first vs third) | 43.2 |

  Choosing a median manager in private markets forfeits most of the reason to be in the asset class. Swensen: "there's absolutely no way" to index venture capital. The table is dated (to June 2005); refresh with vintage-matched, survivor-inclusive data before quoting.
- **The Yale model in Swensen's words.** Managers "maniacally focused on beating the markets," not on gathering fees; modest fund sizes and willingness to close to new money ("Size is the enemy of performance"); integrity and character weighed alongside numbers; openness to emerging managers. Swensen called the standard pension process, a 50-to-100-page questionnaire plus 5 to 10 years of audited history, "not the richest pond." The Yale Investments Office says many of its longest partnerships "began with talented but unproven managers" (Swensen, ECON 252 lecture 9; Yale Investments Office, https://investments.yale.edu/partners).
- **Spending rule drives pacing.** Yale spends about 5.25% a year using an 80% weight on prior-year spending, which smooths the claim on liquidity that commitments must respect (Yale, https://www.yale.edu/funding-yale-home/overview-yales-endowment).
- **The PRINCO mantras** (a former 15-year Princeton endowment staffer): (1) "Fewer, better, stronger": after the GFC Princeton cut the manager roster because more managers diluted attention without adding safety; (2) "Who matters more than when": commitment pacing follows manager quality, with a multi-year moving average only loosely tracking fundraising cycles; (3) prefer managers who create value through operations and company-building over leverage, multiple expansion or momentum; (4) look for managers who discuss portfolio problems and team issues openly and stay engaged in bad periods (BU Insights, "Four Mantras from the Endowment," https://insights.bu.edu/four-mantras-from-the-endowment-a-personal-journey/; PRINCO Investment Strategy, https://princo.princeton.edu/about/investment-strategy).
- **Governance is a return driver.** PRINCO staff are "fully empowered on all matters of execution," hiring and terminating managers and shifting assets without board sign-off, while the board sets policy; PRINCO cites this as an advantage over peers (PRINCO Organizational Model, https://princo.princeton.edu/about/organizational-model). Connecticut's pension cycled through 8 CIOs and 4 interim CIOs and lagged the 50-state median (12.7).
- **The elite-endowment edge is shrinking.** Princeton cut its long-term endowment return assumption from 10.2% to 8% (early 2026), its president citing excess capital chasing limited opportunities and the loss of the special access elite endowments once had; PE was about $14.7B, about 40% of the portfolio, at June 2025; alternatives about 78% of managed investments in 2024; the 20-year rolling return fell from over 14% (2005) to under 10% (2025) (iTiger/Deep News, https://www.itiger.com/news/1145037528; AI-CIO, https://www.ai-cio.com/?p=107176; Daily Princetonian, https://www.dailyprincetonian.com/article/2025/10/princeton-news-endowment-returns-market-private-equity-tax-research-funding-alternative-assets; PAW, https://paw.princeton.edu/inbox/princos-private-equity-investments) **WEAK** (press and aggregator summaries; confirm against PRINCO's annual report). Yale itself reportedly sold part of its PE portfolio on the secondary market in 2025 (Bloomberg, press-reported, not Yale-sourced) **WEAK**.

## 12.2 Data room index

*A. What to obtain from each manager under consideration:* the Chapter 10.8 list, plus:
1. Cash-flow history (dated calls and distributions) for every fund, for PME, KS-PME and GPME.
2. Every fund and vehicle ever managed, including closed and abandoned ones.
3. Deal-level attribution by partner; operating-versus-financial decomposition of each realized deal.
4. Quarterly letters since the predecessor fund's first close (narrative tone and topic, 12.4).
5. Fund-size history, team-size history and deals per partner.
6. Monthly returns for liquid strategies (for MPPM, drawdown and option-like exposure analysis).

*B. What to obtain when you are diligencing an allocator, fund-of-funds or OCIO:*
1. Investment policy statement, policy portfolio, spending rule, liquidity policy.
2. Commitment pacing model and its last five years of forecast versus actual calls and distributions.
3. Manager roster with commitment, NAV, fees paid (as % of actively managed assets, not total assets), and net performance against a passive alternative.
4. Delegation of authority: who hires and fires managers, how fast, and on what pay basis.
5. CIO and staff tenure history.
6. Concentration list: managers where the allocator is anchor, sole or dominant client.
7. Unfunded commitments by vintage and the liquidity sources that cover them (cash, distributions, credit lines, secondaries).
8. Re-up record: managers re-upped versus dropped, and subsequent performance of both.

## 12.3 Diligence checklist by workstream

*Policy and allocation*
- Write down expected net alpha per private sleeve, and the benchmark it is measured against (PME and a levered small-value index for buyout; put-writing for short-vol strategies; levered public REITs for real estate) before committing (Siriwardane, HBS WK, https://www.library.hbs.edu/working-knowledge/rethinking-risk-why-pension-funds-are-betting-on-alternative-assets; Stafford, RFS 2022; Jurek and Stafford, NBER w19643).
- Treat low reported volatility and low correlation of private assets as an artifact of appraisal-based, hold-to-maturity marks, not as diversification (Stafford, https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting). Size the allocation on economic, not reported, risk.
- Do not underwrite a constant illiquidity premium; the PE premium has been cyclical (Ang, Chen, Goetzmann and Phalippou, JF 2018) **WEAK** (abstract-level).
- Use an outside-view return assumption. If Princeton assumes about 8% (12.1, **WEAK**), a 20%+ net projection needs specific evidence.

*Manager sourcing and selection*
- Concentrate: "fewer, better, stronger." Flag over-diversified rosters that mask low conviction (PRINCO mantras).
- Score managers on operating value creation versus leverage, multiple expansion and momentum (PRINCO mantras; Chapter 10.4).
- Emerging managers: allowed and sometimes preferred (Yale), but replace the missing track record with heavier ODD, references and deal-level attribution from prior firms (Chapter 10.3).
- Partners, not brands: in VC, reputation and deal access sit with partners; attribute each deal to its lead and test whether that partner is still there (Sorenson, Nanda and Samila, Yale Insights, https://insights.som.yale.edu/insights/for-top-venture-capital-firms-success-breeds-success).
- Decline managers whose recent funds land consistently in the third or fourth quartile; expect fund-size discipline after a bubble (Erickson, KaW, Mar. 13, 2023, https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/).
- Prefer managers who discuss problems openly (PRINCO). Read the commentary history; early focus on refinancing, covenants and capital structure predicts worse outcomes (HLS Forum 2026, https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/).

*Track-record forensics (rules in Chapter 10.10)*
- Rebuild IRR, TVPI, DPI and PME from cash flows; never compound an IRR or compare it to a TWR (Yale News 2018).
- Remove the top one or two outcomes (VC: dropping the best 5% of ventures turns the aggregate risk-adjusted return negative; Ouyang, Yu and Jagannathan, NBER w27690, https://www.nber.org/papers/w27690).
- Haircut database benchmarks for backfill and survivorship (Malkiel and Saha; Swensen; Chapter 10.10 table).
- For liquid strategies: MPPM, not Sharpe or Sortino (Goetzmann, Ingersoll, Spiegel and Welch, https://repec.som.yale.edu/icfpub/publications/2471.pdf); put-writing benchmark for short-vol exposure (Jurek and Stafford).
- Persistence test: does successor-fund size, team and strategy match the funds that earned the record (Metrick and Yasuda survey, NBER w16652)?

*Re-up discipline*
- Endowments' PE edge came mainly from better re-up decisions, and bank-selected funds lagged sharply (Lerner, Schoar and Wongsunwai, JF 2007, https://www.nber.org/papers/w11136). Write a re-up memo as if it were a new commitment.
- At re-up, the predecessor fund is usually 2 to 4 years old, where interim marks predict little (coefficient about 0.16 in years 1-2; 0.62 in years 3-4) (HLS Forum 2026). Weight team, process, commentary and realized deals from older funds over current marks.

*Pacing and liquidity*
- Pace by manager quality first, calendar second ("who matters more than when," PRINCO).
- Model calls and distributions under a stress in which distributions stop while calls continue; liquidity can vanish across assets at once (Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity," RFS 2009, https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf).
- Treat NAV-loan-funded distributions as potentially recallable and exclude them from distribution forecasts (ILPA NAV guidance 2024; Chapter 14).
- Price the exit: LP portfolios traded at about 87% of NAV in H1 2026 (buyout 91%, venture 79%, real estate 68%), tail-end funds at 25%+ discounts (Jefferies, July 2026, https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf). A secondary sale is the liquidity source of last resort and it is not free (Chapter 13).
- Spending or benefit-payment smoothing (Yale's 80% weight on prior-year spending) reduces forced selling; document the allocator's equivalent.
- Pacing-model mechanics (call and distribution curves, commitment-to-NAV targets): **GAP**. None of the five research lanes sourced a primary pacing model or industry call/distribution curves. Resolve by interview (B.1).

*Co-investment and alternative vehicles*
- Assume adverse selection unless you are a top-decile LP (Lerner, Mao, Schoar and Zhang, JFE 2022; Fang, Ivashina and Lerner, JFE 2015; Chapter 10.12).

*Allocator governance (when diligencing an allocator, fund-of-funds or OCIO)*
- CIO and staff tenure; delegation (who can fire a manager, how fast); decision-maker paid on assets retained? (PRINCO; Connecticut.)
- Fees reported as % of actively managed assets, not total assets including index funds (Sonnenfeld and Tian, Yale Insights, https://insights.som.yale.edu/insights/why-connecticuts-investments-are-underperforming).
- Manager-level net performance versus a passive alternative (60/40 or policy benchmark).
- Concentration where the allocator is a manager's anchor or only client.

*Hedge funds and liquid alternatives*
- Persistence is close to a coin flip: about 50% of above-average funds repeat; about a third of top-quartile funds stay top quartile (Malkiel and Saha, https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf). Require attribution and a factor or put-writing benchmark; do not buy "top quartile."
- Fund-of-funds returned less than the hedge-fund universe after the second fee layer (Malkiel and Saha).
- ODD scorecard and base rates: Chapter 10.3 (Trust and Delegation sample is hedge funds).

*Thematic vehicles*
- Thematic launches buy at the top: specialized ETFs lose about 30% in risk-adjusted terms over their first five years because they launch holding already-overvalued stocks after a run of performance and media attention; the same logic applies to private theme vehicles (AI, crypto, space, climate SPVs) (Ben-David, Franzoni, Kim and Moussawi, RFS 2023, https://nber.org/papers/w28369). CHECK: compare entry valuation with the sector's history and the date the theme peaked in media and fund-launch counts.
- A complex, illiquid product marketed to unsophisticated investors usually means the cycle is near its peak (Harker, KaW, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).

## 12.4 The numbers

| Metric | Value | Source |
|---|---|---|
| Asset allocation share of return variability | Over 90% | Ibbotson via Swensen, ECON 252 lecture 9 |
| Manager spread, buyout / VC | 13.7 pts (Q1-Q3) / 43.2 pts (top-bottom), 10 years to June 2005 | Swensen |
| Endowment PE outperformance vs other LPs | About 14 to 21 pts a year (different versions) | Lerner, Schoar and Wongsunwai, JF 2007 |
| Average pension risk-adjusted PE outperformance | About zero (1995-2018); buyout positive, VC negative, real estate none | Korteweg, Panageas and Systla, HLS Forum 2025, https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/ |
| Pension risk allocation to alternatives | About 14% (2001) to almost 40% (2021) | Siriwardane, HBS WK |
| Fees in buyout replication | About 6% a year | Stafford, RFS 2022 |
| LP cost split | 1/2 illiquidity, 1/4 fees, 1/4 carry | Sorensen, Wang and Yang, HLS Forum 2014, https://corpgov.law.harvard.edu/2014/01/12/valuing-private-equity/ |
| Alternative vehicles share of PE commitments | About 40% by 2017 | Lerner, Mao, Schoar and Zhang, JFE 2022 |
| Yale 20-year VC IRR vs TWR (to June 2018) | 165.9% vs 24.6% | Yale News, Oct. 2018, https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion |
| Internet funds 1997-2002 | +1.5% a year TWR; investors lost $9.9B of $13.7B (72%) | Swensen |
| Dollar- vs time-weighted gap | Below in all 17 Morningstar equity categories; 13.4 pts a year for tech | Swensen |
| Yale spending rule | About 5.25% a year, 80% weight on prior-year spending | Yale |
| Princeton return assumption | 10.2% to 8% (early 2026) | Press summaries **WEAK** |
| Hedge-fund persistence | About 50% repeat above average; about 1/3 of top quartile stay | Malkiel and Saha |
| Hedge-fund database bias | See Chapter 10.10 (two sets of estimates) | Malkiel and Saha; Swensen |
| VC aggregate | IRR about 22%, GPME 1.44; negative risk-adjusted ex top 5% | Ouyang, Yu and Jagannathan |
| LP secondary pricing, H1 2026 | About 87% of NAV overall; buyout 91%, venture 79%, real estate 68%, tail-end 25%+ discount | Jefferies, July 2026 |
| Thematic launch underperformance | About 30% risk-adjusted over first five years | Ben-David et al., RFS 2023 |

## 12.5 Third parties

- Investment consultant or OCIO (diligence them as an allocator, 12.3).
- Benchmark data providers: require vintage-matched, survivor-inclusive, backfill-free data and a statement of what is excluded.
- ODD and background-check providers (Chapter 10.3, 10.14).
- Secondary adviser for portfolio sales (Chapter 13).
- Fund counsel for LPAs, side letters and MFN.

## 12.6 Legal and structure

- Fund governance is contractual: LPs cannot fire the manager; negotiate key-person, removal, no-fault divorce, LPAC rights and consent over GP-leds and NAV loans (Morley, YLJ 2014; HLS Forum "Opting Out of Court," 2026; Chapter 10.1).
- Fee terms: MFN to the best tier (Begenau and Siriwardane; Chapter 10.9).
- The SEC Private Fund Adviser rules were vacated June 5, 2024; reporting, audit and fairness-opinion protections are contractual only (Chapter 10.15).
- Allocator delegation documents: investment policy statement, delegation of authority, conflicts policy for staff and consultants.
- Retail and 401(k) channels: a 2025 executive order directed the SEC and DOL to open 401(k) plans (about $10T) to private assets (HLS Forum, https://corpgov.law.harvard.edu/2026/02/28/private-equity-for-all-the-paradoxical-push-to-democratize-private-markets/). Expect competing capital and new semi-liquid structures (Chapter 15).

## 12.7 Failure modes and the check that catches each

| Firm or case | Year | What happened | CHECK |
|---|---|---|---|
| Connecticut state pension (about $40B) | Decade to 2023 | Would have earned about $5B more over five years and about $27B more over ten at the 50-state median; a plain 60/40 beat it by more than 1 point a year; 8 CIOs and 4 interim CIOs; high fees, sometimes to managers where it was sole or dominant client; fees reported on total rather than active assets (Sonnenfeld and Tian, Yale Insights, May 2023) | CIO tenure; fees as % of actively managed assets; manager net performance vs passive; concentration as anchor or only client |
| Bank-selected PE funds | 1990s sample | Funds selected by banks as LPs lagged sharply; endowments outperformed through re-up decisions (Lerner, Schoar and Wongsunwai, JF 2007) | Re-up memo written as a new commitment; incentives of the selector |
| Internet funds 1997-2002 | 1997-2002 | Ten best funds showed +1.5% a year time-weighted but investors lost $9.9B of $13.7B (72%) by buying near the top (Swensen) | Dollar-weighted investor returns and flow history; thematic-launch test |
| Long-Term Capital Management | 1998 | Lost 92% of capital and reported none of it to databases (Malkiel and Saha) | Survivor-inclusive benchmarks |
| Hedge-fund databases (1996 cohort) | 1996-2004 | Fewer than 25% (124 of 604) of 1996 reporters still existed in 2004 (Malkiel and Saha); Swensen cites about 75% gone | Haircut benchmarks; ask for dead funds |
| Russell manager universe | 1996-2005 | Reporters fell from 307 to 177; the year-2000 return was restated from -3.1% to +1.2% as losers dropped out (Swensen) | Benchmark against data frozen at the time |
| Yale VC IRR misuse (illustration) | 2018 | A 165.9% 20-year IRR that must not be compounded; TWR 24.6% (Yale News) | Never compound IRR; compare via PME |
| Over-diversified rosters | Post-GFC | Princeton cut its roster because more managers diluted attention without adding safety (PRINCO mantras) | Count managers per staff member; conviction test |
| Thematic vehicles | 2020s | Theme vehicles launched after hype underperform (Ben-David et al.) | Entry valuation vs history; launch-count peak |

> **THE ONE CHECK (allocators).** For every manager, compare the fund size, team and strategy you are buying with the fund size, team and strategy that produced the track record, and rebuild the record from cash flows against a survivor-inclusive, factor-appropriate benchmark. Most of the persistence and dispersion evidence turns on this.

## 12.8 Red flags

- Track record shown as compounded IRR or against a TWR index.
- Benchmark that does not disclose backfill and survivorship treatment.
- Re-up justified by the predecessor fund's year-1 or year-2 marks.
- Roster growing faster than staff; many small commitments (low conviction).
- Returns explained by leverage, multiple expansion or momentum rather than operations (PRINCO).
- Manager reluctant to discuss problems or team issues (PRINCO).
- Allocator reporting fees on total assets; CIO turnover; staff paid on assets retained (Connecticut; PRINCO).
- Allocator is a manager's anchor or only client.
- 20%+ net IRR projections against an 8% elite-endowment outside view.
- Thematic product launched after a media peak; complex illiquid product sold to unsophisticated buyers (Harker).

## 12.9 Hard questions

1. What net alpha do you expect from this sleeve, against what benchmark, and how did your last five predictions compare with outcomes?
2. For this manager, what changed between the funds that earned the record and this fund: size, team, strategy?
3. What does the record look like without the top two deals?
4. Which managers did you drop at re-up in the last five years, and how did their next funds do?
5. Who can fire a manager here, and how fast? How is that person paid?
6. What are fees as a share of actively managed assets?
7. If distributions stop for two years and calls continue, how do you fund them, and what would you sell at 87% of NAV (or lower)?
8. Where are you the anchor or only LP, and why?

---

# 13 Secondaries and GP-Led Continuation Vehicles

*LP-led portfolio sales, single- and multi-asset continuation vehicles, structured liquidity. The GP sits on both sides of a GP-led, which is the whole diligence problem.*

## 13.1 How it works

- **LP-led:** an LP sells fund interests, priced as a % of the latest reported NAV. The buyer inherits unfunded commitments and the GP's marks; GP consent and transfer provisions apply (v1 Chapter 11 row: NAV validation, underlying asset marks, GP consent, discount rationale).
- **GP-led:** the sponsor moves one asset (single-asset CV, SACV) or several (multi-asset CV, MACV) from an old fund into a new vehicle it also manages; existing LPs choose to sell (cash at the set price) or roll. A lead secondary buyer prices the deal and funds the cash-out; the GP usually crystallizes carry in the selling fund and commits to the CV (general lane draft; Jefferies, July 2026, https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf).
- **Structured liquidity solutions** (preferred equity and similar) are about 9% of volume (Jefferies, July 2026); see also NAV loans (Chapter 14).
- **Market (H1 2026):** record first-half global volume $118B (2025 full-year record $240B); GP-led $62B (53%), LP-led $56B (47%); single-asset CVs 68% of CVs, multi-asset 32%; buyout about 66% of GP-led volume; dedicated secondary capital $290B (from $327B at end-2025) (Jefferies, July 2026). Update semi-annually.
- **Sellers are sophisticated.** Yale reportedly sold part of its PE portfolio on the secondary market in 2025 (Bloomberg, press-reported) **WEAK**. Expect the seller to know more than you about the tail.
- **Litigation is now possible.** The Abu Dhabi Investment Council sued a US PE firm in Delaware Chancery (Dec. 2025) over a continuation-fund transaction, a rare LP suit in a market where only 4% of suits against top and bottom PE firms come from fund investors (HLS Forum, "Opting Out of Court?," 2026, https://corpgov.law.harvard.edu/2026/06/29/opting-out-of-court-reputation-and-informal-norms-in-private-equity/).

## 13.2 Data room index

*GP-led (for an existing LP deciding to sell or roll, or a buyer):*
1. Transaction rationale memo to the LPAC.
2. Alternatives considered (sale process, IPO, hold) with any third-party bids received.
3. Price-setting evidence: lead-buyer bid, auction book and buyer list, fairness or valuation opinion, opinion provider's engagement letter and other mandates from the GP.
4. Asset-level model and 100-day plan for the CV; full company diligence materials (QoE, legal, debt documents) as given to the lead buyer.
5. Old-fund LPA and side letters; proposed CV LPA (fees, carry, hurdle, term, extensions, GP commitment).
6. GP's crystallized carry at the transaction price, and how much is reinvested.
7. Election materials and timetable; default election.
8. Conflicts disclosure; LPAC minutes and vote.
9. Secondary adviser engagement letter and fee basis.
10. The GP's portfolio commentary history on the asset(s).

*LP-led (buyer):*
1. Fund LPAs, side letters, transfer and GP-consent provisions.
2. Quarterly reports and capital-account statements; unfunded commitments by fund.
3. Fund cash flows; latest audited financials; valuation policy.
4. Asset-level marks for the top holdings and recent exit-to-mark history.
5. Fund-level leverage: sub lines and NAV facilities (Chapter 14), including recallable distributions.

## 13.3 Diligence checklist by workstream

*Process*
- Was there a genuine market test? Who set the price, and was the GP's own valuation the anchor? How many bidders were contacted and how many bid?
- Was the transaction presented to the LPAC with rationale and alternatives, and did the LPAC vote to waive the conflicts? GPs should bring ALL conflicts to the LPAC even if pre-cleared in the LPA (ILPA, May 2023).
- Is a fairness opinion provided by a firm with no other mandate from the GP? Since June 2024 it is contractual only (13.6).

*Alignment*
- GP commitment to the CV as % of total, and how much is new money versus rolled carry. Market: about 10% of total commitments in North American deals versus about 5% in Europe, where carry in the selling fund is often not crystallized at closing (Jefferies, July 2026).
- Is the selling fund's carry crystallized at a price the GP itself set?

*Terms*
- CV management-fee base (invested versus committed), carry tiers, hurdle reset, term and extensions.
- Does a TRUE status quo option exist: no change in management fee, no change in carry, full roll of carry, side letters carried over (ILPA, May 2023)?

*Asset*
- The CV is a concentrated single-company position (SACVs are 68% of CVs). Underwrite it as a direct deal (Chapter 5) with full QoE, not on the GP's NAV.
- Why did the asset not clear a sale process?
- Read the GP's commentary history on the asset: early focus on refinancing, covenants or capital structure predicts worse outcomes (HLS Forum, 2026, https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/).
- Return attribution: how much of the CV case requires multiple expansion versus EBITDA growth? Buyers increasingly underwrite to static or contracting exit multiples (Jefferies, July 2026).

*LP mechanics*
- Election period, default election (sell or roll if no response), information parity between rolling LPs and the lead buyer. ILPA's materials cite at least 30 days as a reasonable review window.

*LP-led pricing*
- NAV validation: recency of the reference NAV; private marks lag public markets by at least four quarters (IMF GFSR Apr. 2024, Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md). Roll the NAV forward for public-market moves and known events.
- Distinguish the GP's dollar-weighted IRR from a TWR; compare NAV marks against public-factor benchmarks (Yale lane; Chapter 10.10).
- Exclude NAV-loan-funded distributions from DPI and check whether they are recallable (ILPA NAV guidance 2024).
- Unfunded commitments: who funds them, and are they priced in?

## 13.4 The numbers

| Metric | Value (H1 2026 unless noted) | Source |
|---|---|---|
| Global secondary volume | $118B H1 2026 (record first half); $240B full-year 2025 (record) | Jefferies, July 2026 |
| GP-led / LP-led | $62B (53%) / $56B (47%) | Same |
| Single-asset / multi-asset CVs | 68% / 32% of CVs | Same |
| Buyout share of GP-led | About 66% | Same |
| Structured liquidity solutions | About 9% of volume | Same |
| Dedicated secondary capital | $290B (from $327B end-2025) | Same |
| LP portfolio pricing, all strategies | About 87% of NAV | Same |
| By strategy | Buyout 91%; venture 79%; infrastructure 91%; credit 89% (from 91%); real estate 68% | Same |
| Tail-end funds | 25%+ discounts; some geographies 35%+ | Same |
| Software exposure | Portfolios with limited software exposure priced better | Same |
| GP commitment to CVs | About 10% (North America) vs about 5% (Europe) | Same |
| LP review window | At least 30 days (ILPA materials) | ILPA, May 2023 |

**Underwriting rules.**
- Price versus NAV and versus the most recent arm's-length mark. A SACV at or near 100% of NAV when the GP's LP portfolios trade at 87% to 91% needs a reason.
- GP commitment under about 5% of the CV with mostly rolled carry is weak alignment; about 10% with new cash is market in North America.
- Recompute the GP's carry at the transaction price and at a 15% to 20% lower price; see who bears the gap.

## 13.5 Third parties

- Secondary adviser (engaged by the GP; check fee basis, and whether paid only on closing).
- Fairness or valuation opinion provider with no other mandate from the GP.
- Lead secondary buyer (its diligence package is the information-parity benchmark).
- LP's own counsel for LPA comparison; QoE provider for the underlying asset(s).

## 13.6 Legal and structure

- **The ILPA standard (May 2023).** Continuation-fund transactions should maximize value for existing investors, and rolling LPs should be no worse off than if no transaction had occurred; a TRUE status quo option should always be offered (no change in management fee or carry, full roll of carry, side letters carried over); the GP should present the rationale to the LPAC and show it explored alternatives; the LPAC should vote to waive conflicts, and GPs should bring ALL conflicts to the LPAC even if pre-cleared; LPs need enough time to re-underwrite (ILPA, https://ilpa.org/resource/continuation-funds-considerations-for-limited-partners-and-general-partners/; ILPA release, https://ilpa.org/wp-content/uploads/2023/05/ILPA-Releases-Continuation-Fund-Guidance.pdf; Torys, https://www.torys.com/our-latest-thinking/publications/2023/05/ilpa-releases-continuation-fund-guidance-for-limited-partners-and-general-partners).
- **No federal fairness-opinion requirement.** The SEC's adviser-led secondaries rule (mandatory fairness or valuation opinion plus disclosure of material business relationships with the opinion provider) was vacated with the rest of the Private Fund Adviser rules on June 5, 2024 (Fifth Circuit, No. 23-60471; MoFo, https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules). Require one, from a provider with no other mandate from the GP, as a condition of rolling, and write it into the LPA for future funds.
- **LPA protections to negotiate up front** (since litigation rarely works): LPAC consent rights over GP-leds; status quo option; minimum election period; information parity with the lead buyer; fairness opinion (HLS Forum, "Opting Out of Court?," 2026).

## 13.7 Failure modes and the check that catches each

| Failure | What happens | CHECK |
|---|---|---|
| Price set by the GP's own mark with a thin market test | Selling LPs get too little, or rolling LPs and the buyer overpay | Obtain the bid book and the adviser's buyer list; call a bidder who declined |
| No real status quo | Rollers forced onto new fees and carry | Compare old LPA and CV LPA side by side |
| Carry crystallized on an inflated mark that the CV buyer funds | GP is paid on a price it set | Recompute carry at the transaction price and at a 15% to 20% lower price |
| CV used to hold an asset that could not be sold | Concentrated bad asset with a fresh fee clock | Full direct-deal diligence on the company and its debt; ask why it did not clear a sale |
| Information asymmetry | Lead buyer receives diligence LPs never see | Demand the same data-room access as the lead |
| Stale NAV in LP-led pricing | Buyer pays for marks that lag public markets by four quarters or more (IMF) | Roll NAV forward; exit-to-mark history |
| NAV-loan-funded distributions in the history | DPI overstated; distributions recallable | Synthetic DPI; read the recall clause (Chapter 14) |
| LP challenge after closing | ADIC v. US PE firm (Del. Ch., Dec. 2025) | Process record: LPAC vote, alternatives, fairness opinion, election period |

Named public case files with confirmed outcomes are thin in the research set; ADIC (filed Dec. 2025) is the only named GP-led dispute and its outcome was not sourced. **GAP.**

> **THE ONE CHECK (GP-leds).** Get the bid book. If you cannot see how many buyers were asked, how many bid, and at what prices, you are accepting a price the GP set for an asset it is buying from itself.

## 13.8 Red flags

- Election period under 20 business days (ILPA's materials cite at least 30 days as reasonable).
- Default election is "roll on new terms."
- No fairness opinion, or an opinion provider with other GP mandates.
- Adviser paid only on closing, by the GP.
- GP commitment entirely rolled carry.
- LPAC asked to approve after pricing is fixed.
- SACV priced at or near 100% of NAV while the GP's LP interests trade at 87% to 91%.
- Asset previously marketed and withdrawn.
- GP commentary on the asset dominated by refinancing and covenant language.

## 13.9 Hard questions

1. What were the other bids, and who declined?
2. Why now, and why not a sale or IPO?
3. What is the status quo option, exactly, term by term?
4. How much new cash is the GP investing, and how much is rolled carry?
5. What carry does the GP crystallize at this price, and at 15% to 20% below it?
6. Who provides the fairness opinion, and what else do they do for you?
7. Will I get the lead buyer's full data room?
8. What exit multiple does the CV case assume against entry?

---

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

# 15 Evergreen and Semi-Liquid Private Market Vehicles

*Non-traded and perpetual BDCs, interval funds, tender-offer funds, NAV REITs, evergreen PE and the 401(k)/retail channel. Illiquid assets inside a vehicle that promises periodic liquidity. The 2026 private-credit redemption stress is the case study.*

## 15.1 How it works

- The vehicle raises continuously, invests in illiquid loans, equity or property, strikes a periodic NAV (usually monthly or quarterly, on model or appraisal marks), and offers to repurchase a limited share, typically 5% of shares per quarter. When requests exceed the cap, it prorates, queues or gates (Fang, Goldstein and Zeng, via KaW, Oct. 26, 2026, https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/).
- BDCs must distribute 90% of income, so net investment income does not accumulate as a liquidity buffer (same).
- **Who holds US private credit (Fed, Q3 2025):** private debt funds 54.7%, perpetual (non-traded) BDCs 18.7%, public BDCs 12.4%, middle-market CLOs 5.9%, private BDCs 5.4%, interval funds 3.0% (Federal Reserve FEDS Note, Aug. 11, 2026, https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html). A perpetual BDC with redemption queues behaves differently in a workout than a closed-end fund; ask which vehicle holds your loan.
- **Growth:** semi-liquid private credit net assets grew from $10B (2019) to $300B (end-2025) (KaW, Oct. 2026).
- **Private credit size depends on the definition and date. Present all; do not average:** about $3.5T global private credit market (KaW, Oct. 2026); about $2.1T in assets and dry powder globally, 2023 (IMF GFSR Apr. 2024, Ch. 2, https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md); about $1.8T to $2T (Goldstein, KaW, May 5, 2026, https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit); about $1.4T of private-credit debt outstanding to US nonfinancial private corporations by Q1 2026 (Fed FEDS Note, Aug. 2026).
- **Retail push.** A 2025 executive order directed the SEC and DOL to open 401(k) plans (about $10T) to private assets, likely via target-date funds; managers push retail capital because of higher rates, an exit backlog and institutional allocation limits. HLS Forum authors argue retail access erodes the illiquidity and contracting advantages that made PE work, keeps higher fees, and creates liquidity mismatch (HLS Forum, "Private Equity for All," 2026, https://corpgov.law.harvard.edu/2026/02/28/private-equity-for-all-the-paradoxical-push-to-democratize-private-markets/).
- **Cycle signal.** A complex, illiquid product marketed to unsophisticated investors usually means the cycle is near its peak; very large deployment targets make selective underwriting hard. The largest perpetual private-credit fund must deploy about $43B a year, more than a quarter of annual US direct lending (Harker, KaW, Apr. 22, 2026, https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/).

**The 2026 semi-liquid private-credit stress (case study).**

| Date | Event | Source |
|---|---|---|
| Early 2026 | Blue Owl ended quarterly redemptions from the $1.6B OBDC II | KaW, Oct. 2026; Harker, KaW, Apr. 2026 |
| Early 2026 | Blackstone met record redemptions of about 8% of its flagship credit fund | Same |
| 2026 | AI disruption of SaaS led to sharp revisions in software borrowers' default probabilities (a "software crisis"); about one-fifth of loans in semi-liquid private credit funds are to software firms | KaW, Oct. 2026 |
| Q2 2026 | $7.1B of repurchases against $3.8B of inflows: the sector's first aggregate net outflow; $10.7B of requests unmet (gated) | KaW, Oct. 2026 |
| Q2 2026 | Blue Owl Capital Corp II received redemption requests for about 22% of shares; Blue Owl Credit Income Corp about 40%; Blackstone, BlackRock and Apollo vehicles also saw requests above the cap | KaW, Oct. 2026 |
| Through Q3 2026 | Proskauer Private Credit Default Index: 1.76% Q2 2025, 1.84% Q3 2025, 2.46% Q4 2025, 2.73% Q1 2026, 2.41% Q3 2026 (covenant and payment defaults) | Proskauer, https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-241-for-q3-2026 (and prior quarters) |

Mechanism (Fang, Goldstein and Zeng): stale marks plus a 5% gate plus thin cash produced gating, rising fund leverage and deferred payments.

## 15.2 Data room index

1. Prospectus/PPM, charter, repurchase or tender-offer policy, board resolutions on each repurchase decision.
2. Redemption history by quarter: requests, cap, paid, prorated, queued, carried forward; "repurchases payable" balance.
3. Flow history (subscriptions and redemptions) and investor-level (dollar-weighted) returns versus fund TWR.
4. Valuation policy; independent valuation agent's engagement letter and reports; NAV strike process and frequency; mark-to-market lag analysis.
5. Schedule of investments with marks; for BDCs, the same loans' marks in other BDCs' schedules of investments.
6. Liquidity sources: cash, NII run rate, contractual maturities by quarter, undrawn credit facilities, sub lines or NAV facilities and their covenants.
7. Leverage history and limits (asset coverage for BDCs).
8. PIK income as % of total investment income; amend-and-extend and maturity-extension log by loan.
9. Sector exposure (software share), borrower concentration, sponsor-affiliated borrowers.
10. Fee schedule: base, incentive on income and gains, distribution and servicing fees, fund-of-fund layers.
11. Sponsor support history (insider purchases, fee waivers, support agreements).
12. Distribution policy and the source of each distribution (income, gains, return of capital, borrowing).

## 15.3 Diligence checklist by workstream

*Liquidity coverage (the core test)*

Compute a **liquidity coverage ratio** each quarter: (cash + NII retained + contractual maturities + committed undrawn facilities usable for repurchases) / maximum repurchase obligation at the cap. Then stress it for two to four consecutive quarters at the cap.

| Input | Typical level (semi-liquid private credit) | Source |
|---|---|---|
| Redemption cap | 5% of shares per quarter | Fang, Goldstein and Zeng (KaW, Oct. 2026) |
| Cash | About 5.5% of total net assets (average) | Same |
| Net investment income | About 2.5% a quarter, mostly paid out (90% distribution requirement) | Same |
| Loan maturities | Under 0.5% a quarter | Same |
| Leverage response | Net debt issuance rises 0.38 pp of TNA per 1-point increase in net outflows | Same |
| Secondary market for the loans | About 80% unrated; fewer than 20% held by 10+ fund families | Same |

Illustrative arithmetic (derived from the table, not a sourced figure): cash of about 5.5% covers roughly one quarter of full 5% repurchases; after that, retained NII (small, since about 90% is distributed) plus maturities of under 0.5% cover a fraction of a 5% quarterly cap, so the gap is filled by borrowing, asset sales at fire-sale discounts, or the gate. Recurring 5% redemptions exhaust the buffer quickly (Fang, Goldstein and Zeng).

- Check gating history and whether unmet requests carry forward.
- "Repurchases payable": deferred redemption payments that work like trade credit owed to exiting investors. Count them as debt.
- Sponsor support (insiders buying in) is discretionary and may not scale (Fang, Goldstein and Zeng).
- Assume the gate will be used. Suspensions of fund withdrawals work like bank holidays: they pause the run, carry stigma, and managers delay using them until late (YPFS, "Survey of Bank Holidays and Fund Suspensions," JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/1/). Read the gate, suspension and in-kind provisions.

*Valuation*
- Stale NAV: if marks lag, redeeming investors exit above economic value at remaining holders' expense, creating a first-mover run incentive (Fang, Goldstein and Zeng).
- BDC loan marks lag B-rated leveraged loans; price and NAV take at least four quarters to converge after a shock; the IMF recommends mandatory independent external valuations and more frequent reviews (IMF GFSR Apr. 2024, Ch. 2).
- Compare the manager's mark on each loan with the same loan's mark in other BDCs' schedules of investments; BDC filings are one of the few public windows (loans held by private-credit BDCs rose from 1,395 to 20,182, 2010-2022) (Elias and de Fontenay, "The Credit Markets Go Dark," YLJ 134, https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark).
- Appraisal-based marks smooth volatility; low reported volatility is an artifact (Stafford, RFS 2022; Chapter 10.10). Smoothness relative to the strategy is also a Ponzi tell (Antle, Yale Insights; Chapter 10.3).
- Who values? Independent valuation agent, or the manager? (HLS Forum 2026; SQN case file, Chapter 10.6.)

*Credit quality and hidden losses*
- PIK interest's share of BDC interest income has doubled since 2019 (IMF GFSR Apr. 2024). Track PIK toggles, amend-and-extend and maturity extensions by loan; private lenders can forbear indefinitely, creating "zombie" borrowers (Elias and de Fontenay).
- Software exposure: stress ARR for AI substitution (seat compression, price pressure) and test the debt on downside ARR, not ARR multiples (KaW, Oct. 2026).
- Default definitions differ (Proskauer counts covenant defaults; Cliffwater counts realized losses; rating agencies payment defaults). Ask which definition any quoted rate uses (IMF; general lane; Chapter 3.4).
- Labels like "alternative assets," "direct lending" or "multi-strategy income" can hide private-loan exposure; look through to holdings (Goldstein, KaW, May 2026).

*Leverage*
- Leverage-redemption feedback loop: net debt rises with outflows (0.38 pp per point). Map every facility, its covenants and margin-call triggers (Harker; Fang, Goldstein and Zeng).
- Are sub lines or NAV facilities used to meet redemptions? (HLS Forum 2026; Chapter 14.)
- Model a simultaneous collateral fall and haircut increase (Brunnermeier and Pedersen; Gorton and Metrick; Chapter 14.3).

*Fees and incentives*
- All-in fee load including fund-of-fund layers, against a levered small-value index (HLS Forum 2026; Stafford).
- Does manager pay depend on inflows (asset-based fees on a growing NAV)? (HLS Forum 2026.)
- Deployment pressure (Harker's $43B-a-year example).

*Investor outcomes*
- Request investor-level (dollar-weighted) returns and flow history, not just fund TWR; investors in hot vehicles often buy near the top (Swensen: internet funds +1.5% a year TWR but investors lost 72% of $13.7B; Morningstar dollar-weighted below time-weighted in all 17 equity categories, 13.4 points a year for tech) (Swensen, ECON 252 lecture 9, https://oyc.yale.edu/economics/econ-252-08/lecture-9).
- Does new money fund old redemptions or distributions? Ponzi-like dynamics under stress (HLS Forum 2026; GPB, Chapter 10.6).
- Source of each distribution: income, gains, return of capital, or borrowing.

*Cash holdings*
- "Cash equivalents" are not cash: look through money-market and "cash management" holdings and model a 6-to-24-month gate on any pooled cash vehicle (Reserve Primary Fund, 15.7).

## 15.4 The numbers

| Metric | Value | Source |
|---|---|---|
| Semi-liquid private credit net assets | $10B (2019) → $300B (end-2025) | KaW, Oct. 2026 |
| Q2 2026 flows | $7.1B repurchases vs $3.8B inflows; $10.7B unmet | KaW, Oct. 2026 |
| Redemption requests, Q2 2026 | Blue Owl Capital Corp II about 22% of shares; Blue Owl Credit Income Corp about 40% | KaW, Oct. 2026 |
| OBDC II | $1.6B; quarterly redemptions ended early 2026 | KaW, Oct. 2026; Harker, Apr. 2026 |
| Blackstone flagship credit fund | Record redemptions of about 8% met | Same |
| Redemption cap | Typically 5% a quarter | Fang, Goldstein and Zeng |
| Cash / NII / maturities | About 5.5% of TNA / about 2.5% a quarter / under 0.5% a quarter | Same |
| Unrated loans | About 80% | Same |
| Software share of loans | About one-fifth | KaW, Oct. 2026 |
| Holder mix of US private credit | Perpetual BDCs 18.7%; public BDCs 12.4%; private BDCs 5.4%; interval funds 3.0% | Fed FEDS Note, Aug. 2026 |
| Mark-to-market lag | At least four quarters | IMF GFSR Apr. 2024 |
| PIK share of BDC interest income | Doubled since 2019 | IMF GFSR Apr. 2024 |
| Largest perpetual fund's deployment need | About $43B a year, over a quarter of US direct lending | Harker, KaW, Apr. 2026 |
| Private credit defaults (Proskauer) | 2.73% Q1 2026; 2.41% Q3 2026 | Proskauer |
| Direct-lending realized losses | About 1.0% a year long run (1.03% through 2023); 0.70% in 2025 | Cliffwater, https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf (2025 figure from a staging host, **WEAK** until confirmed on cliffwater.com) |
| 401(k) assets targeted by 2025 executive order | About $10T | HLS Forum 2026 |

## 15.5 Third parties

- Independent valuation agent (IMF recommends mandatory independent external valuations).
- Fund administrator and transfer agent (redemption queue records).
- Auditor (Big 4 or equivalent; Chapter 10.3).
- Credit facility lenders (covenants that can force sales).
- Independent directors of the BDC or interval fund board (who decides each repurchase).

## 15.6 Legal and structure

- **Repurchase terms are discretionary in most non-traded BDCs and tender-offer funds;** interval funds make periodic repurchase offers under their fundamental policy. Read who decides each repurchase, whether unmet requests carry forward, and the suspension and in-kind provisions (Fang, Goldstein and Zeng; YPFS survey). The legal basis of each structure (Investment Company Act rules for interval funds and BDCs) was not sourced in the research set: **GAP**; confirm with fund counsel.
- **BDC distribution requirement:** 90% of income (KaW, Oct. 2026).
- **Regulatory status, Nov. 2026:** SEC Private Fund Adviser rules vacated June 5, 2024 (Chapter 10.15); 2025 executive order on 401(k) access (HLS Forum 2026); IA AML rule delayed to Jan. 1, 2028 (Chapter 10.15). DOL and SEC implementing guidance after the executive order was not sourced: **GAP**.
- **Tokenized wrappers:** a tokenized claim's trading speed should match the speed at which the underlying asset can honor redemptions (Wharton lane; Chapter 11).

## 15.7 Failure modes and the check that catches each

| Firm or case | Year | What happened | CHECK |
|---|---|---|---|
| Blue Owl (OBDC II) | Early 2026 | $1.6B fund ended quarterly redemptions (KaW, Oct. 2026; Harker, Apr. 2026) | Liquidity coverage ratio across consecutive quarters at the cap; redemption queue history |
| Blue Owl Capital Corp II / Blue Owl Credit Income Corp | Q2 2026 | Redemption requests of about 22% and about 40% of shares against a 5% cap (KaW, Oct. 2026) | Investor concentration and channel (wealth platforms move together); flow history |
| Semi-liquid private credit sector | Q2 2026 | First aggregate net outflow ($7.1B out vs $3.8B in); $10.7B gated; rising fund leverage; deferred payments (Fang, Goldstein and Zeng) | LCR, mark-lag test, queue history, leverage-redemption loop |
| Reserve Primary Fund | 2008 | $62.5B fund held $785M of Lehman paper; more than $40B of redemption requests in two days; broke the buck Sept. 16, 2008 and suspended redemptions; investors got about 50 cents within six weeks, 99 cents only after two years; final distribution (99.1 cents) in 2014 (YPFS, JFC 7(2), https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/9/) | Look through "cash"; model a 6-to-24-month gate |
| GPB Capital | Convicted 2024 | Fixed distributions on illiquid assets paid from new investor capital (Chapter 10.6) | Source of every distribution |
| Heller / Paramount-Prestige ATM network | SEC, Sept. 2025 | Fixed monthly distributions to about 2,700 mostly retail investors paid from new money and short-term loans (Chapter 10.6) | Processor confirmation of asset revenue |

> **THE ONE CHECK (semi-liquid).** Compute the liquidity coverage ratio for four consecutive quarters of maximum redemptions, using marks rolled forward for public-market moves. If coverage depends on new inflows or new borrowing, the vehicle is only as liquid as its next sales quarter.

## 15.8 Red flags

- Redemptions above liquidity coverage (Wharton lane red-team item).
- Rising "repurchases payable" or a growing queue.
- Leverage rising as flows turn negative.
- Smooth NAV while comparable public credit or equity fell.
- Marks above the same loan's marks in other BDCs.
- Rising PIK share; frequent amend-and-extend.
- Fixed distribution rate exceeding NII; distributions funded by borrowing or new money.
- Large software or single-sector concentration.
- Manager pay driven by inflows; deployment target large against the market.
- Gate or suspension provisions that are vague about who decides.
- Fund-level sub line or NAV facility used to meet redemptions.

## 15.9 Hard questions

1. Show the redemption history: requests, paid, prorated, queued, every quarter since launch.
2. What is your liquidity coverage at the cap for four straight quarters, without new inflows?
3. Who values the book, and how do your marks compare with other BDCs' marks on the same loans?
4. What share of income is PIK, and how many loans were amended or extended in the last year?
5. What share of the book is software, and what is the downside-ARR test?
6. Where did each of the last eight distributions come from?
7. What facilities can you draw to meet redemptions, and what covenants could force sales?
8. What are investors' dollar-weighted returns, not the fund's TWR?
9. Who decides whether to gate, and what did they decide last time?

---

# 16 Search Funds and Entrepreneurship Through Acquisition

*Traditional (funded) search funds, self-funded search, and the ETA buyer as CEO. The investor underwrites a first-time CEO and a small owner-run company at once. Lower-middle-market deal mechanics are in Chapter 5.*

## 16.1 How it works

- A searcher raises a small search fund (salary and deal costs) from investors who get a right to invest in the eventual acquisition, buys one small private company, and runs it as CEO for 5 to 10 years. Investors provide search capital, then acquisition equity (often with a step-up on search capital); the searcher earns equity in tranches (acquisition, time, performance) (general lane draft; IESE, ST-689-E, https://www.iese.edu/media/research/pdfs/ST-0689-E).
- **Return engine: mostly multiple expansion, not operating improvement.** In search-fund acquisitions later sold, aggregate enterprise value rose from about $1B to $4B; about 80% came from EBITDA multiple expansion (6.3x at entry to 15.6x at exit) and only about 20% from EBITDA growth; margins fell from 25% to 19%; holds were about five years. Returns are back-end-loaded and depend on exit conditions (Wasserstein and Thomas, "Do Search Fund CEOs Improve Performance?," Yale Insights, Apr. 2026, https://insights.som.yale.edu/insights/do-search-fund-ceos-improve-performance).
- **Owner-operator private equity has not reliably beaten public equity.** Moskowitz and Vissing-Jorgensen found entrepreneurial (owner-held) private equity returns no higher than public equity despite extreme concentration (about three-quarters of such holdings in a single firm) (AER 2002, NBER w8876, https://www.nber.org/papers/w8876). A Bank of Canada follow-up disputes how robust this is beyond the 1990s (Kartashova, Bank of Canada WP 2011-6). Present both; do not assume an illiquidity premium appears on its own in lower-middle-market deals.
- Reading: Ruback and Yudkoff, *HBR Guide to Buying a Small Business* (2017), from the HBS Entrepreneurship Through Acquisition course (HBS lane).

## 16.2 Data room index

1. Searcher's PPM and search-fund LPA; investor list and step-up terms.
2. Searcher equity grant and vesting schedule (acquisition, time, performance tranches).
3. Target CIM; 3 to 5 years of tax returns (small targets often have only tax-basis books); monthly bank statements; customer list with revenue by customer.
4. QoE report and its engagement letter (required: owner-run businesses carry personal expenses in the P&L; a QoE carries no assurance, so read the scope, Chapter 0.5).
5. SBA 7(a) or senior loan terms; seller note and its subordination and standstill.
6. Seller transition and employment agreement; earn-out terms.
7. Key-employee list, compensation and retention arrangements.
8. Board composition post-close and the CEO-replacement right.
9. For franchise targets: franchise agreement and FDD (Item 17), with any no-poach or non-solicit clauses.
10. 100-day plan.

## 16.3 Diligence checklist by workstream

*Searcher*
- References from prior managers and from investors in the search fund; background check (Chapter 0.2).
- Has the searcher ever run a P&L? Most have not.
- LOI discipline: successful searchers signed an average of 4.6 LOIs (first by month six); unsuccessful ones 8.2 (IESE 2026).

*Target: quality of earnings*
- QoE with proof of cash against TAX RETURNS and bank statements. Owner add-backs are the main source of overstatement.
- Replace the seller's labor at market salary in the QoE; capex study for deferred maintenance.
- Adverse discoveries in diligence were the top reason deals died: across 716 LOIs, 59% cited adverse diligence findings, 41% valuation disagreements, 32% seller retraction, 31% lack of investor support (IESE 2026). Budget for diligence that kills deals.

*Target: commercial*
- Customer concentration, and whether relationships are personal to the seller. Call customers before close.
- Key employees and retention.
- Capital intensity: failures cluster in capital-intensive targets whose growth fell short (KaW podcast, Aug. 22, 2007, https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/looking-for-a-company-to-run-search-funds-could-be-the-answer/) **WEAK** (dated 2007, podcast).

*Structure*
- Total leverage including the seller note; seller-note subordination and standstill; personal guarantee requirements on SBA loans; equity cushion.
- Fixed-charge coverage in a 20% revenue-decline case.
- Return with exit multiple equal to entry multiple (Wasserstein and Thomas): what survives without the 6.3x-to-15.6x re-rating?

*Governance*
- An experienced board (typically lead investors) with the right to replace the CEO.
- Leadership base rates from buyouts: 69% of deals change CEO during the hold (HLS Forum, "The CEO Decision," 2026, https://corpgov.law.harvard.edu/2026/09/23/the-ceo-decision-how-pe-investors-select-and-reassess-leaders-from-entry-to-exit/). Plan the succession path for a first-time CEO.

*Legal and HR*
- No-poach and wage-fixing clauses in franchise, multi-unit or staffing targets: about 58% of major franchisors' 2016 franchise agreements contained no-poach clauses; AG actions and class actions followed (Krueger and Ashenfelter, NBER w24831, https://www.nber.org/papers/w24831). Confirm removal and any open exposure; confirm non-compete enforceability by state.

## 16.4 The numbers

Two eras of data disagree. Present both; the 2026 studies govern.

| Metric | Stanford GSB / IESE 2026 | Wharton KaW 2007 (**WEAK**, dated practitioner figures) |
|---|---|---|
| Investor IRR | US/Canada aggregate pre-tax IRR 33.9%, ROI 4.75x (data through Dec. 31, 2025) | About 37% historical average (Stanford study as cited in 2007) |
| Share that acquire | About 58% of concluded US/Canada searches acquired; international 73% (79% in the 2024 study) | About 25% never close an acquisition (i.e., about 75% acquire) |
| Deal size | International median: $12M price, $8M revenue | Historical EV $4M to $11M |
| Search capital | Median $450K (solo), $649K (partnered) | About $30K to $50K per unit; about 90% of search investors take up the acquisition round |
| Seller transition | Not reported | Seller typically stays 6 to 12 months |

Sources: Stanford GSB 2026 Search Fund Study (https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations), as cited by IESE, International Search Funds 2026: Selected Observations, ST-689-E (https://www.iese.edu/media/research/pdfs/ST-0689-E); KaW podcast, Aug. 22, 2007.

**More from the 2026 studies (IESE, ST-689-E):**

| Metric | Value |
|---|---|
| US/Canada known search funds since 1984 / acquisitions | 862 / 382 |
| International (ex-US/Canada) funds / acquisitions | 492 / 216 |
| International aggregate ROI / IRR | 2.8x / 30% (up from 2.0x / 18%) |
| International median acquisition outcome | 1.1x investors' capital; top fund 23.8x |
| International concluded funds that lost money | About 21% (of which roughly a third total loss) |
| Median international acquisition | $12M price; $8M revenue; 26% EBITDA margin; 5.7x EBITDA; 1.4x revenue; 11% trailing revenue growth; 50 employees |
| Median searcher salary | $100K, i.e. 45% to 60% of search capital |
| LOIs to close | Successful 4.6 (first by month six); unsuccessful 8.2 |
| Why deals died (716 LOIs) | Adverse diligence 59%; valuation 41%; seller retraction 32%; investor support 31% |
| Exit attribution (Yale) | About 80% multiple expansion (6.3x → 15.6x), about 20% EBITDA growth; margins 25% → 19%; about 5-year holds (Wasserstein and Thomas, 2026) |

Dispersion is the point: the aggregate is driven by a few outliers (international median 1.1x vs top 23.8x). Size a search-fund program as a portfolio, not a single bet.

LMM process timing: 60 to 90 days from LOI to close (ctacquisitions.com, v1 Chapter 5) **WEAK**.

## 16.5 Third parties

- QoE provider (proof of cash to tax returns and bank statements).
- Lender (SBA 7(a) or senior) and lender's counsel.
- Background-check firm for the searcher and the seller.
- Experienced board members and, where used, CEO coach.
- Employment counsel for non-compete, no-poach and transition agreements.

## 16.6 Legal and structure

- Search-fund LPA: investor right (not obligation) to invest in the acquisition; step-up on search capital.
- Searcher equity: tranches for acquisition, time and performance; full vesting at close is a red flag.
- Seller note: subordination and standstill to the senior lender; tie part of it, or an earn-out, to customer retention.
- SBA loans: personal guarantees (general lane draft; terms not primary-sourced: **WEAK**, confirm current SBA SOP).
- Board: lead investors with CEO-replacement rights.
- No-poach clauses: unwind before close (Krueger and Ashenfelter).

## 16.7 Failure modes and the check that catches each

| Failure | What happens | CHECK |
|---|---|---|
| Owner add-backs that are real operating costs (seller's unpaid labor, deferred capex) | EBITDA overstated at entry | Replace the seller's labor at market salary; capex study |
| Relationship revenue that leaves with the seller | Revenue falls after transition | Customer calls before close; transition agreement with earn-out or seller note tied to retention |
| First-time CEO overwhelmed | Execution stalls; CEO change mid-hold | Board with operating experience; 100-day plan; CEO coaching; succession plan |
| Over-leverage on a small, cyclical business | Covenant breach in a mild downturn | Fixed-charge coverage in a 20% revenue-decline case |
| Return depends on multiple expansion | Exit at entry multiple leaves little return; margins fell in the Yale sample | Show return with exit multiple = entry multiple |
| Capital-intensive target with growth shortfall | Cash consumed by capex (**WEAK**, 2007 source) | Capex study; maintenance vs growth capex split |
| No-poach or wage-fixing clause in a franchise target | AG action or class action | FDD Item 17 and agreement review |

Named public search-fund failure case files were not sourced in the research set: **GAP**.

> **THE ONE CHECK (search funds).** Rebuild EBITDA from tax returns and bank deposits with the seller's labor replaced at market salary, then price the deal at an exit multiple equal to entry. If the deal works only with a re-rating, it is a bet on the exit market, not on the CEO.

## 16.8 Red flags

- Purchase multiple well above the about 5.7x international median without recurring revenue to justify it (IESE 2026).
- Seller unwilling to stay for transition.
- No QoE ("too small").
- Searcher's equity vests fully at close.
- Search capital spent mostly on salary with fewer than three LOIs by month 12.
- Customer relationships personal to the seller; no customer calls allowed before close.
- Model needs multiple expansion to return capital.

## 16.9 Hard questions

1. What would you pay if the seller left on day one?
2. What does EBITDA look like with a market-rate replacement for the seller?
3. Who on the board has run this kind of business?
4. Which three customers would you call first, and have you?
5. What is the return at exit multiple equal to entry multiple?
6. What is fixed-charge coverage if revenue falls 20%?
7. How many LOIs have you signed, and why did the others die?

---

# 17 Healthcare Services and Physician Practice Roll-Ups

*Physician practice management (PPM) platforms, MSO structures, nursing homes and post-acute care, hospital sale-leasebacks. Revenue is set by payors, so diligence centers on reimbursement durability, billing compliance, referral law, and state ownership rules. Extends the v1 Chapter 11 healthcare row (licensing, reimbursement and payor mix, Stark and anti-kickback compliance, billing quality; QoE must test payor concentration and revenue-cycle quality).*

## 17.1 How it works

- **Roll-up model.** A sponsor buys a "platform" practice (dermatology, anesthesia, GI, dental, behavioral, home health, etc.) and adds on smaller practices at lower multiples (multiple arbitrage), centralizing billing and administration in a management services organization (MSO), because many states bar non-physicians from owning medical practices (corporate practice of medicine, CPOM). The physician-owned practice ("friendly physician" or professional entity) contracts with the sponsor-owned MSO (general lane draft).
- **Payors set price.** Revenue comes from Medicare, Medicaid and commercial payors; government payors are about 75% of nursing-home revenue (Gupta, Howell, Yannelis and Gupta, NBER w28474, https://www.nber.org/papers/w28474; KaW, July 22, 2024, https://knowledge.wharton.upenn.edu/article/how-to-align-private-equity-motives-with-nursing-home-outcomes/).
- **The evidence on PE ownership of care providers is adverse in nursing homes.** Across 1,674 acquisitions in 128 deals among about 12,400 for-profit homes, PE ownership raised short-term patient mortality by about 10% to 11% (about 1.7 percentage points); frontline nursing-assistant hours per patient-day fell about 3%; costs shifted toward non-patient items (monitoring fees, interest, lease payments) (Gupta et al., NBER w28474; KaW, July 2024). Expect regulatory and reputational exposure to track staffing and quality.
- **Control brings liability.** The False Claims Act can reach a sponsor involved in the conduct: DOJ named PE sponsor Riordan, Lewis & Haden alongside its portfolio pharmacy Diabetic Care Rx for financing a kickback scheme (HLS Forum, "Secondary Liability Risks for Private Funds," 2019, https://corpgov.law.harvard.edu/2019/10/09/secondary-liability-risks-for-private-funds-recent-developments/). Date conflict: the HBS lane (HLS Forum 2019) says settled 2019 for $21.36M; the general lane draft referred to it as a 2021 matter and flagged it [VERIFY]. The HLS Forum post is dated Oct. 2019, which supports 2019; confirm on justice.gov.

## 17.2 Data room index

1. Payor mix by revenue and by visit; top payor contracts with rates and renewal dates.
2. CPT-level volume and reimbursement trend.
3. Revenue-cycle KPIs by month: days in A/R, initial denial rate, net collection rate, A/R over 90 days.
4. Remittance files (835) and bank deposits for revenue rebuild.
5. Billing and coding audit results; compliance program; hotline log; prior self-disclosures and overpayment refunds.
6. OIG exclusion and SAM checks for every provider.
7. Provider employment agreements, compensation formulas, noncompetes; production by provider.
8. MSO agreement and fee formula; friendly-physician ownership and succession agreements.
9. Licenses, DEA registrations, accreditation.
10. Malpractice history and tail coverage.
11. Add-on purchase agreements with fair-market-value (FMV) opinions; medical directorship and other referral-source arrangements with FMV and commercial-reasonableness support.
12. State CPOM analysis and state transaction-notice filings.
13. Real estate: leases, sale-leaseback agreements, landlord identity and relationships.
14. For nursing homes and post-acute: staffing ratios, CMS Five-Star history, survey deficiencies, related-party fees, leases and interest.

## 17.3 Diligence checklist by workstream

*Revenue and reimbursement*
- Rebuild net revenue from remittances (835 files) and bank deposits, not gross charges; test contractual allowance estimates against cash.
- Payor concentration: largest commercial payor as % of revenue; renewal dates.
- Medicare physician fee schedule changes (annual CMS rule).
- In-network status by payor and share of revenue from out-of-network billing. Out-of-network economics changed with the No Surprises Act arbitration process from 2022 (general lane draft; not primary-sourced) **WEAK**.

*Coding and billing*
- Independent coding audit on a statistically valid sample per provider; outlier billing versus peers.
- Escrow or special indemnity for pre-close billing.

*Fraud-and-abuse compliance*
- The Anti-Kickback Statute (42 U.S.C. 1320a-7b(b)) and Stark (42 U.S.C. 1395nn) govern referral relationships, MSO fee structures (percentage-of-revenue fees are a known risk area) and add-on purchase prices (paying above FMV for a referral source) (general lane draft).
- FMV and commercial-reasonableness support for every compensation arrangement with referral sources; OIG/SAM exclusion screening; prior overpayments refunded within 60 days.
- DOJ's Evaluation of Corporate Compliance Programs asks whether the acquirer performed comprehensive pre-acquisition compliance diligence, integrates the target into its controls promptly, and audits acquired entities post-close (HLS Forum, 2020, https://corpgov.law.harvard.edu/2020/06/29/justice-department-updates-its-guidance-on-corporate-compliance-programs/). Document compliance diligence scope and gaps in the IC memo; put a 100-day compliance integration plan in the value-creation plan.
- Diligence billing and referral practices before close in any government-reimbursed target; confirm D&O coverage at fund and company level (HLS Forum 2019).

*Providers*
- Post-close compensation versus pre-close; noncompetes (void in some states, 17.6); number of providers producing the top 50% of revenue.
- Rollover equity and vesting tied to tenure.

*Structure*
- CPOM-compliant ownership; the friendly physician's agreements; what happens if he or she leaves.
- MSO fee formula: flat or cost-plus versus percentage of collections.

*Integration (the thesis)*
- The platform-versus-add-on multiple spread is the thesis; test whether add-ons have actually been integrated (one billing system, one payor contract).

*Antitrust*
- Local market share by specialty; state notice requirements. Serial add-ons below HSR thresholds are not safe from challenge (FTC v. U.S. Anesthesia Partners and Welsh Carson, 17.7). In pharma, about 6% of acquisitions (6.4% in the working paper) were "killer acquisitions" clustered just below HSR thresholds, up to about 50 a year, and FTC/DOJ scrutiny of sub-threshold deals is growing (Cunningham, Ederer and Ma, JPE 2021, SSRN 3241707; Yale Insights, https://insights.som.yale.edu/insights/when-corporate-acquisitions-affect-healthcare).

*Real estate*
- Sale-leasebacks used to fund dividends weaken hospitals and practices. Model rent coverage after any sale-leaseback, with escalators, and trace where the proceeds went (Steward, 17.7).
- Related-party landlords: the friendly physician or sponsor affiliate as landlord.

*Quality (nursing homes and post-acute)*
- Staffing ratios and nursing-assistant hours per patient-day; CMS Five-Star trend after acquisition; fees, leases and interest paid to related parties or landlords (Gupta et al.).

## 17.4 The numbers

| Metric | Value | Source |
|---|---|---|
| Government payor share, nursing homes | About 75% of revenue | Gupta et al., NBER w28474 |
| PE nursing-home mortality effect | About +10% to +11% short-term mortality (about 1.7 pp) | Same |
| Frontline staffing effect | Nursing-assistant hours per patient-day about -3% | Same |
| Sample | 1,674 acquisitions in 128 deals among about 12,400 for-profit homes | Same |
| Killer acquisitions (pharma) | About 6% (6.4% WP); up to about 50 a year; cluster below HSR | Cunningham, Ederer and Ma, JPE 2021 |
| Riordan, Lewis & Haden / Diabetic Care Rx FCA settlement | $21.36M (2019 per HLS Forum) | HLS Forum 2019 |
| Steward Massachusetts sale-leaseback | $1.25B to MPT (2016); Chapter 11 May 2024 | Brookings via Wharton lane |
| Revenue-cycle benchmarks | Days in A/R, denial rates against HFMA MAP Keys peer data | Practitioner standard **WEAK** (confirm) |
| Provider productivity | wRVUs per FTE against MGMA benchmarks | Practitioner **WEAK** |

Specific numeric thresholds for days in A/R, denial rates and wRVUs were not sourced: **GAP**. Resolve with HFMA and MGMA primary data or operator interviews.

## 17.5 Third parties

- Healthcare regulatory counsel (AKS, Stark, CPOM, state notice laws).
- Independent coding auditor.
- FMV and commercial-reasonableness appraiser for physician compensation and add-on prices.
- Revenue-cycle QoE provider (remittance-to-cash rebuild).
- Antitrust counsel for serial add-ons.
- Real estate appraiser and lease reviewer for sale-leasebacks.
- Malpractice and tail-coverage broker.

## 17.6 Legal and structure

- **Corporate practice of medicine (CPOM).** Oregon SB 951 (2025 Reg. Sess., enacted as Ch. 295, emergency clause): an MSO, and its shareholders, directors, officers and employees, may not own or control shares in, serve as director or officer of, be employed by, or manage a professional medical entity with which the MSO has a management services contract; voids most noncompetition, nondisclosure and nondisparagement agreements between such entities and medical professionals; voids agreements violating the control prohibitions (Oregon Legislature, https://olis.oregonlegislature.gov/liz/2025R1/Measures/Overview/SB951). This is the template for the strictest CPOM regime.
- **State PE-healthcare notice and oversight laws.** Several other states (e.g. California, Massachusetts) enacted PE-healthcare notice or oversight laws in 2024-25 (general lane draft) **WEAK** [VERIFY current statutes per deal].
- **Federal fraud and abuse.** Anti-Kickback Statute (42 U.S.C. 1320a-7b(b)); Stark (42 U.S.C. 1395nn); False Claims Act liability can reach the sponsor when the sponsor is involved in the conduct (general lane; HLS Forum 2019).
- **Other sponsor liabilities:** ERISA multiemployer pension withdrawal liability (Sun Capital funds held to be a trade or business under common control with a bankrupt portfolio company, D. Mass. 2018, because of active management, GP control of hiring and pay, and board control); control-person liability; veil-piercing. Keep fund ownership structured to avoid 80% common control where withdrawal liability exists; observe corporate formalities (HLS Forum 2019).
- **Antitrust:** HSR thresholds are not a safe harbor for serial add-ons (17.7).
- **Deal protections:** escrow or special indemnity for pre-close billing; R&W exclusions for known billing issues (Chapter 5).

## 17.7 Failure modes and the check that catches each

| Firm or case | Year | What happened | CHECK |
|---|---|---|---|
| Steward Health Care / Cerberus | 2016 sale-leaseback; Chapter 11 May 2024 | Sale-leaseback of hospital real estate to MPT ($1.25B for Massachusetts) funded dividends and left escalating rents (Brookings, https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/, via Wharton lane) | Model rent coverage after any sale-leaseback; trace where the proceeds went |
| Riordan, Lewis & Haden / Diabetic Care Rx | Settled 2019 (HLS Forum) | DOJ named the PE sponsor alongside its portfolio pharmacy for financing a kickback scheme; $21.36M (HLS Forum 2019) | Pre-close billing and referral diligence; sponsor involvement in marketing practices |
| U.S. Anesthesia Partners / Welsh Carson | FTC suit 2023 | Serial roll-up of Texas anesthesia practices followed by price increases; Welsh Carson later entered an FTC consent order requiring prior notice of certain acquisitions (general lane draft) **WEAK** [VERIFY dates and order terms on ftc.gov] | Local market share by specialty; price increases after add-ons; state notice requirements |
| PE-owned nursing homes (aggregate) | Study period in NBER w28474 | Mortality up about 10% to 11%; staffing down about 3%; costs shifted to fees, interest, leases (Gupta et al.) | Staffing ratios; Five-Star trend; related-party fees and leases; rent coverage |

**Generic failure modes:**

| Failure | CHECK |
|---|---|
| Upcoding or medically unnecessary services inflating EBITDA | Independent coding audit and peer-benchmark outlier analysis before close; escrow or special indemnity |
| Kickback-tainted referral relationships (above-FMV medical directorships, MSO percentage fees) | FMV opinions; healthcare regulatory counsel review |
| Payor rate cuts or out-of-network revenue collapse | In-network status by payor; out-of-network share of revenue |
| Physicians leaving after earn-outs | Rollover equity and vesting tied to tenure; production concentration |
| Antitrust or state-law block of add-ons | Local share by specialty; state notice requirements |
| Add-ons never integrated | One billing system and one payor contract test |
| CPOM structure unwinds (friendly physician leaves; Oregon-style law) | Friendly-physician succession agreements; state-by-state CPOM analysis |

> **THE ONE CHECK (healthcare roll-ups).** Rebuild revenue from remittances and bank deposits and run an independent coding audit per provider before close. Payor-set revenue that cannot be traced to cash, or that depends on outlier coding or above-FMV referral arrangements, is the liability, not the asset.

## 17.8 Red flags

- EBITDA growth driven by price in concentrated local markets.
- MSO fee as a % of collections.
- No billing audit in three years.
- Large out-of-network revenue.
- Providers with prior exclusions.
- Friendly physician who also owns the MSO's landlord.
- Sale-leaseback proceeds used for dividends; escalating rents.
- Staffing ratios falling after acquisition; Five-Star rating declining.
- Fees, interest and rent paid to sponsor affiliates or related landlords.
- Add-ons on separate billing systems years after acquisition.

## 17.9 Hard questions

1. What share of revenue comes from the top payor, and when does that contract renew?
2. What did the last external coding audit find?
3. Show FMV support for every arrangement with a referral source.
4. Which add-ons are still on separate billing systems?
5. Which state laws require notice or approval for this deal, and does any state's CPOM law reach the MSO structure?
6. Who is the friendly physician, and what happens if he or she leaves?
7. After the sale-leaseback, what is rent coverage, and where did the proceeds go?
8. What happened to staffing ratios and quality ratings at prior acquisitions?

---

# 18 Litigation Finance

*Outline-level chapter. The research set supports the structure and the regulatory baseline, not market numbers or case files; what is missing is listed in 18.10. Extends the v1 Chapter 4.2 row (case merits by independent legal opinion, duration, capital adequacy to see cases through, portfolio diversification, non-recourse to claimant) and 4.4 (independent legal opinion).*

## 18.1 How it works

- A funder advances non-recourse capital to a claimant or law firm (single case or portfolio) in exchange for a share of recoveries, typically a multiple of capital or a percentage of proceeds, whichever is greater. Returns depend on win rate, collection and DURATION (general lane draft).
- Commercial deals run into the millions; consumer advances are usually under $10,000 (GAO-23-105210, Dec. 2022, https://www.gao.gov/products/gao-23-105210).
- No federal statute specifically regulates litigation funding; there is no nationwide requirement to disclose funding agreements to courts or opposing parties; some courts require it case by case; some states cap fees or rates in consumer funding; GAO found public data on volumes and returns too limited to size the market (GAO-23-105210).
- Investor positions: (a) LP in a litigation-finance fund; (b) direct single-case or portfolio funding; (c) lender to a funder or law firm. Each uses Chapter 10 (fund diligence) or Chapter 4 (credit) plus this chapter.

## 18.2 Data room index

1. Funding agreement(s): return waterfall (multiple vs percentage), priority against counsel fees, termination and withdrawal rights.
2. Independent merits opinion by counsel not involved in the case.
3. Damages model and the defendant's collectability analysis (assets, insurance, jurisdiction, sovereign status).
4. Case timeline and procedural history; expected and stressed duration, including appeals.
5. Budget to trial and appeal; who funds overruns.
6. Engagement letter between claimant and counsel (contingency terms, conflicts).
7. For a funder or fund: portfolio list with cost, marks, status and expected resolution; valuation policy and the auditor's approach to Level 3 case assets; commitments versus uncalled capital; cross-collateralization terms.
8. Any court disclosure orders that apply.

## 18.3 Diligence checklist by workstream

- **Merits:** independent merits opinion by counsel not involved in the case (v1 4.2; general lane).
- **Damages and collection:** damages model; collectability of the defendant (judgment-proof or sovereign defendants carry enforcement risk).
- **Duration:** model the duration distribution; appeals add years. Model IRR at 1.5x the expected duration (general lane draft heuristic, not sourced to data) **WEAK**.
- **Control and ethics:** the funder must not control litigation strategy where state ethics rules forbid it; check who controls settlement decisions.
- **Portfolio:** diversification and cross-collateralization across cases.
- **Funder capacity:** the funder's own capital adequacy and commitments versus uncalled capital. Can it fund through trial? (v1 4.2.)
- **Valuation:** fair-value marks of case assets are Level 3; read the policy and the auditor's approach. Apply Chapter 10.3 ODD (who has write access to marks; independent valuation; Infinity Q and SQN lessons).
- **Disclosure exposure:** court-level disclosure is spreading (e.g. standing orders in the U.S. District Court for the District of Delaware since 2022) (general lane draft) **WEAK** [VERIFY current federal rulemaking status].

## 18.4 The numbers

- Market size, win rates, loss rates, duration distributions and realized returns: not sourced. GAO found public data too limited to size the market (GAO-23-105210). **GAP**.
- Report returns as both MOIC and IRR, with duration; MOIC alone hides duration risk (general lane draft).
- Consumer advances usually under $10,000; commercial deals in the millions (GAO-23-105210).

## 18.5 Third parties

- Independent merits counsel (v1 4.4).
- Damages expert.
- Collection and enforcement counsel (especially cross-border or sovereign).
- Valuation agent for Level 3 case marks; auditor.
- ODD provider for funder or fund (Chapter 10.3).

## 18.6 Legal and structure

- Non-recourse to the claimant (v1 4.2; GAO).
- No federal statute; no nationwide disclosure requirement; state consumer-funding caps in some states; case-by-case court disclosure (GAO-23-105210).
- Champerty, usury and state ethics rules on funder control: state-by-state analysis required; primary sources not retrieved in the research set **GAP**.
- Funding-agreement priority against counsel's contingency fee and any insurer.

## 18.7 Failure modes and the check that catches each

| Failure | What happens | CHECK |
|---|---|---|
| Win but cannot collect | Judgment against a judgment-proof or sovereign defendant | Collectability analysis; enforcement counsel |
| Duration blowout | IRR collapses while MOIC looks fine | Duration distribution with appeals; IRR at stressed duration |
| Marks move with headlines | Level 3 marks above cost on unresolved cases | Valuation policy; marks vs cost without a judgment; auditor approach |
| Funder liquidity squeeze | Cases left unfunded mid-stream | Funder commitments vs uncalled capital; budget to trial |
| Funder controls settlement | Ethics and enforceability problems; conflict with claimant | Read control provisions against state rules |
| Single-case concentration | One loss wipes out the fund | Portfolio diversification; cross-collateralization terms |

No named litigation-finance failure case file was sourced: **GAP**.

> **THE ONE CHECK (litigation finance).** Underwrite collection and duration, not just merits. Ask what the IRR is if the case takes twice as long and the defendant pays late, and who funds the case until then.

## 18.8 Red flags

- Marks above cost on cases without a judgment.
- Returns quoted in MOIC only.
- Single-case concentration.
- A funder that also controls settlement decisions.
- Merits opinion from the counsel running the case.
- Funder whose commitments exceed its uncalled capital.

## 18.9 Hard questions

1. Who wrote the merits opinion, and do they have any role in the case?
2. If you win, how and from what assets do you collect?
3. What is the IRR at 1.5x and 2x the expected duration?
4. Who decides whether to settle?
5. How are unresolved cases marked, and who signs the valuation?
6. Can the funder fund every case through trial and appeal from committed capital?

## 18.10 What is missing (research gaps)

- Market size and growth from a primary source (GAO says public data are too limited).
- Realized returns, win/loss rates and duration distributions by case type (commercial, patent, international arbitration, mass tort, consumer).
- Named failure case files (funder insolvencies, collection failures, disputes over funder control).
- Current federal and state disclosure rules beyond GAO (Dec. 2022) and the Delaware standing orders ([VERIFY]).
- State champerty, usury and ethics rules on funder control.
- Fair-value accounting practice for case assets and auditor approaches.
- Insurance products (e.g. judgment-preservation or after-the-event cover) and their effect on underwriting.
- Secondary market for case interests and its pricing.

Resolve by interviewing 3 to 5 funders, litigation counsel and fund LPs (B.1).

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

# Appendix B Open Gaps and Interview Guide

What the research could not settle, what v2 settled, and how to close the rest.

## B.1 Open gaps

Resolve remaining gaps by interviewing 3 to 5 lenders or investors per deal type.

### v1 gaps: status in v2

| v1 gap | v2 status | Resolved by | What remains |
|---|---|---|---|
| Real estate LTC and DSCR cutoffs, and promote terms, by deal size (WEAK) | PARTLY RESOLVED | Federal programs as ceilings: HUD Mortgagee Letter 2025-03 (Jan. 8, 2025) raised 221(d)(4) market-rate new construction to 87% LTC at 1.15x min DSCR (from 85% and 1.176x); affordable 90% at 1.11x (https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf). Fannie Mae Form 4660 tiers; Key Principal guaranty required below 1.35x on fixed-rate loans; underwrite at the higher of note rate or Fannie floor (https://mfguide.fanniemae.com/fnmf-pdf/download/9906). Wharton: exit-cap benchmark (Linneman framework) and the in-place-lease DSCR rule (Levitin and Wachter). | Private-lender LTC norms by deal size; promote structures by deal size (HBS: Lietz frameworks unpublished; Wharton: no current source). Still a gap |
| Energy availability-guarantee benchmarks from a primary OEM LTSA | RESOLVED | Entergy 2020 CCGT toll term sheet: 98% monthly availability in summer and winter months, 96% otherwise, 2% capacity-payment discount per 1% shortfall (https://rfp.entergy.com/ENTRFP/SEND/2020ETICCGTRFP/Documents/04282020/Appendix%20B-2%20-%20Term%20Sheet%20-%20Toll.pdf); DOE wind O&M checklist: typical 95% guarantee (2023). | A primary OEM LTSA itself was not obtained; the utility toll term sheet is the offtaker-side evidence |
| Moody's and Fitch DSCR scorecard thresholds against primary criteria | LARGELY RESOLVED | S&P General PF Methodology (Dec. 14, 2022) Table 8 (min DSCR by OPBA) and Table 9 (downside resiliency); Fitch indicative 'BBB' renewable table (2012); Morningstar DBRS (Feb. 2025) merchant guidance. | Moody's Power Generation Projects methodology (Jan. 2022) grid is behind registration. Gearing (60% to 80%) stays WEAK and is reframed as an output of DSCR sculpting |
| Credit and specialty advance-rate and loss-rate norms by sub-strategy | PARTLY RESOLVED | Direct lending realized loss about 1.0% a year (Cliffwater); OCC ABL Handbook advance rates (receivables 70% to 85%; inventory up to about 65% of cost or about 80% of NOLV; concentration caps 10% to 20%; over-advances 10% to 15%); NAV loans initial LTV 10% to 30%, max about 40%; factoring 70% to 90% of eligible AR; recovery anchors loans 84%, secured bonds 60%, unsecured 38% (Schwert); CLO AAA break-even about 60% defaults at 40% recovery (Roberts and Schwert); stressed haircuts 0 to about 50% (Gorton and Metrick) and margins about 10% to above 40% (Geanakoplos) as the stress side. Tricolor shows advance rate is meaningless without collateral dedupe. | Consumer installment and equipment residual norms; factoring cost (WEAK); venture debt terms (WEAK; Stifel deck remains best); unitranche pricing (practitioner) |
| How venture investors weight the Rule of 40 against NRR by stage | BOTH POSITIONS | General lane: RESOLVED by ICONIQ State of Software 2025: Rule of 40 gets real weight only at about $25M ARR or more; below that, underwrite growth plus NRR/GRR and burn; a point of growth has nearly twice the valuation impact of a point of FCF margin (https://www.iconiq.com/growth/reports/2025-state-of-software). Investor-published data: WEAK until corroborated. Private SaaS median NRR is just above 100%, not 117% (KeyBanc/Sapphire 2025). | Yale lane: NOT resolved by academic sources; Yale evidence (deal access drives VC outcomes; no average margin expansion) argues for weighting growth durability (NRR) over projected margins. Confirm by investor interviews |

### Gaps the v2 research raised

Data and sourcing:

- Middle-market entry multiples (6x to 10x, soferadvisors) and direct-lender share (about 70%, Bain via ctacquisitions): no primary retrieved; keep WEAK until GF Data or PitchBook-LCD is pulled. Lower anchor: median search-fund acquisition 5.7x EBITDA at about $12M EV (IESE 2026, general lane).
- Covenant-lite share in private credit (48%, botminds): needs the Proskauer primary.
- Burn multiple and magic number: practitioner originators only (Craft Ventures; David Skok).
- An EBITDA add-back study; subscription-line IRR inflation magnitude (partly addressed by the ILPA 2025 Performance Template); continuation-vehicle pricing (Wharton lane).
- Process timing (weeks 9 to 16; 60 to 90 days sign-to-close): vendor-only (0.1).
- Fu and Taylor hours-of-diligence distribution: abstract only read.
- Gyourko NBER w14708 full text (CRE price-decline figures) not retrieved.
- Search-fund figures from 2007 (about 37% IRR; 25% never close): update against the current Stanford GSB study.

Regulatory and legal:

- IRS guidance on 280E after the April 2026 partial rescheduling: none located.
- Liability management exercises (priming, uptiers, drop-downs): flagged by WFFI 2026 (roundtable listing only, WEAK); needs law-firm and court primaries.
- Flexible or conditional-firm large-load tariffs are being written utility by utility. Interview utilities and data-center lenders on how non-firm service is treated in lease and debt documents (Princeton lane).
- Proof-of-reserves standards for crypto custodians and exchanges (who supplies the challenge, liabilities coverage, auditor scope). Interview a crypto custody auditor (Princeton lane).
- Consolidated RBC for insurer-affiliated private-credit platforms. Interview an insurance regulator or rating analyst (Princeton lane).
- Data-center interconnection: 3 to 7 years typical (Camus/encoord/Princeton ZERO Lab, Dec. 2025) against v1's 8 to 12 years in primary hubs (gi-advisors, WEAK). BOTH POSITIONS; verify per utility.

Items marked [VERIFY] by the research lanes (WEAK until confirmed on the primary site):

| Item | Where used |
|---|---|
| OFAC 50 Percent Rule and Compliance Framework document links | 0.3, 0.18 |
| SEC staff no-action letter, Mar. 12, 2025 (506(c) minimum investment) | 0.3, 0.18 |
| TZP Management SEC order release number (Aug. 15, 2025) | 0.15 |
| DOJ SDNY Archegos sentencing URL (Nov. 20, 2024) | 0.4 |
| DOJ SDNY SBF sentencing URL (Mar. 28, 2024) | 0.4 |
| Cliffwater 2025 results release (staging host) | 0.10 |
| ABA 2025 Deal Points survival and deductible splits (secondary summaries) | 0.16 |
| SR 13-3 "4.0x total / 3.0x senior" wording | 0.18 |
| Nareit REIT-implied vs NCREIF ODCE cap rates, Q2 2026 | 0.6 |
| Tricolor "$2.2B pledged against $1.4B" (single report) | 0.4 |
| Harvard Extension School attribution of MGMT E-2790 | 0.9 |

Abstract-level or podcast-sourced items (WEAK): Brown et al. omega score (JF 2008, FAJ 2009); Ang, Chen, Goetzmann and Phalippou published figures; Goetzmann, Gourier and Phalippou (preliminary); Fader and McCarthy CBCV cases (podcast); Werbach on FTX (podcast); Kleinman Center episodes (podcast); Princeton endowment return assumption (press reports).

Chapters proposed but not yet drafted (general lane): insurance and specialty finance; sports franchises; franchise businesses; family-office direct deals; farmland; art and collectibles; music royalties. Litigation finance is drafted in outline only. Suggested primaries: NAIC statutory filings and RBC, AM Best methodology; FTC Franchise Rule (16 CFR Part 436) and FDD Items 19 to 21; USDA NASS Land Values and NCREIF Farmland Index; Copyright Royalty Board Phonorecords IV and MLC data; league constitutions and leaguewide credit facilities; auction-house guarantee disclosures and UCC Article 9 for art lending.

Lane-specific gaps: no CPG- or cannabis-specific material in free HBS, HLS Forum or HKS sources (HBS lane); Wharton faculty not mined in depth (Yamazaki, Amit, Opp, van Binsbergen, Holthausen beyond his textbook, Guay beyond Theranos, Daniel Taylor's 10b5-1 "three red flags").

## B.2 Core interview guide

Universal (v1):

1. What are the first three things you look at, and what makes you stop reading?
2. What do you ask for that sponsors rarely have ready?
3. What does a deck get wrong most often here?
4. Which numbers do you rebuild yourself, and which do you take from the sponsor?
5. Tell me about a deal that looked clean and went bad. What did you miss?
6. What third-party reports do you require?
7. What terms are non-negotiable?
8. What would make you trust diligence done by someone else?

Process and decision hygiene (v2):

9. How many hours did you spend with management in person before you committed? (Fu and Taylor.)
10. Tell me about a decision process you changed after a loss. (Schwarzman.)
11. When did you last decline a hot manager or deal on operational grounds alone? (Brown et al.)
12. How do you size the haircut you apply to management's forecast, and how has it compared with outcomes? (Gompers et al. 2016: 20% median.)
13. Who sets your walk-away price, and is that person on the deal team? (Feldman.)

Verification and misconduct (v2):

14. Which of your managers' or borrowers' statements did third-party records contradict? (Brown et al.)
15. When did you last call a target's whistleblower hotline, and what happened? (Soltes.)
16. Show me the amendment history. (Wharton lane; Elias and de Fontenay.)
17. How do you dedupe collateral against other lenders' borrowing bases? (First Brands; Tricolor.)

Leadership (v2):

18. What share of your last ten deals changed CEO, and when did you first know? (HLS CEO study.)

Funds and credit (v2):

19. How do you decide whether to take a co-invest the GP offers you, given evidence that co-invests underperform the main fund? (Fang, Ivashina and Lerner.)
20. Who chose lender counsel on your last three LBO loans, and what did your own counsel change? (Sponsor-designated counsel.)
21. What is your fixed-fee share of GP revenue in the downside? (Metrick and Yasuda.)
22. Which default definition do you report, and what is your realized loss rate? (IMF 2024; Cliffwater; Proskauer.)

Specialist interviews to close B.1 gaps (v2):

23. Utilities and data-center lenders: how is non-firm or flexible interconnection treated in the lease and the debt documents, and how many curtailment hours does the lender underwrite? (Princeton lane.)
24. Crypto custody auditors: who supplies the proof-of-reserves challenge, what liabilities are covered, and what is the audit scope? (Princeton lane.)
25. Insurance regulators or rating analysts: how do you consolidate RBC across affiliated captives and private placements? (Princeton lane.)
26. Real estate lenders: what LTC and DSCR do you actually lend at, by deal size, and what promote structures do you see? (v1 gap.)
27. Venture investors: at what ARR does the Rule of 40 start to matter more than NRR in your pricing? (v1 gap.)

## B.3 Note on process

This is Version 2.0 (November 2026). It rebuilds Version 1.0 from five parallel research lanes, each instructed to work only from free primary or institutional sources and to tag every finding as NEW, STRENGTHENS, CONTRADICTS or RESOLVES a v1 weakness or gap:

1. Harvard lane: HBS faculty research (NBER and SSRN versions), HBS Working Knowledge, the Harvard Law School Forum on Corporate Governance, and Harvard Kennedy School. Strongest on PE and VC practitioner surveys, covenants, fund economics, M&A fraud litigation, compliance and misconduct.
2. Wharton lane: Knowledge at Wharton, Wharton faculty research, the Zell/Lurie Real Estate Center, the Rodney L. White Center, the Wharton financial-institutions policy series (WFFI), the Kleinman Center for Energy Policy, and the Wharton Blockchain and Digital Asset Project. Strongest on real estate pricing and distress, covenants and CLOs, semi-liquid private credit, customer-based valuation, and behavioral process failure. This lane exhausted its search budget; its open items are in B.1.
3. Yale lane: Yale SOM, Yale Law School, Yale economics and Cowles, the Yale Investments Office, the Yale Program on Financial Stability and its Journal of Financial Crises, Yale ICF working papers, Yale Insights, and Open Yale Courses. Strongest on ODD base rates, crises, counterparty and liquidity risk, track-record forensics and allocator practice.
4. Princeton lane: Bendheim Center for Finance, economics, ORFE, the Griswold Center (CEPS), Julis-Rabinowitz Center, Andlinger Center (Net-Zero America, ZERO Lab, REPEAT), SPIA, CITP and PRINCO. Strongest on credit cycles and bubbles, decision bias, hedge-fund data biases, energy and data-center power, and crypto custody.
5. Primary and institutional lane (non-Ivy): regulators and agencies (SEC, DOJ, FinCEN, OFAC, Federal Reserve, OCC, FDIC, HUD, DEA, LBNL, DOE, GAO, IMF), rating agencies (S&P, Fitch, Morningstar DBRS, Moody's), industry bodies (ILPA, NVCA, ABA, ACFE, AICPA), and institutional data (Proskauer, Cliffwater, SRS Acquiom, Aon, AIG). Replaced most v1 vendor sources and supplied the November 2026 regulatory status.

Version 1.0 was built from primary and institutional sources (OCC, FDIC, Federal Reserve, SEC enforcement filings, ILPA, NVCA, EIA, Lazard, World Bank, S&P, Credit Agricole CIB, the law firms Mintz, Wilson Sonsini, Sidley, Pillsbury, and Cole Schotz, and practitioner QoE and ODD guidance), plus a dedicated energy project-finance research pass. All v1 content is retained unless a v2 finding corrected it; corrections are marked CONTRADICTS or noted inline, and where sources disagree both positions are shown.

Merge rules used for v2: findings from different lanes were deduplicated, keeping the best-sourced version and citing every lane that agreed; numbers keep their citation and year; anything tagged [VERIFY], confirmed only at abstract level, or sourced to a podcast is marked WEAK.

Items marked WEAK rest on vendor, aggregator, or practitioner-only sourcing, or are unverified. Confirm them against a primary source or a live practitioner interview before they anchor a posted deal.

The structure is modular, so each chapter can be expanded into its own standalone volume as deal flow in that category grows. Version 2.0 adds universal sections 0.10 to 0.20. The lanes also proposed new sector chapters (secondaries and GP-led continuation vehicles; NAV lending and fund finance; search funds and ETA; data centers and digital infrastructure; healthcare services roll-ups; litigation finance in outline; semi-liquid and evergreen vehicles; LP portfolio construction and manager selection; tokenized real-world assets; SPACs and de-SPACs), which are handled in their own chapters, not in Chapter 0.

# Appendix C Sources

Every URL cited in this volume, in order of first citation.

1. <https://knowledge.wharton.upenn.edu/opinion/these-investments-promise-high-yield-with-bond-like-safety-but-what-looks-too-good-to-be-true-often-is/>
2. <https://www.justice.gov/usao-sdny/pr/ceo-cfo-coo-charged-connection-billion-dollar-collapse-tricolor-auto>
3. <https://www.acfe.com/en-us/-/media/files/acfe/pdfs/rttn/2026/2026-report-to-the-nations.pdf>
4. <https://knowledge.wharton.upenn.edu/article/why-many-ma-deals-fail-and-how-to-beat-the-odds/>
5. <https://oyc.yale.edu/economics/econ-252-08/lecture-20>
6. <https://www.nber.org/papers/w21133>
7. <https://www.nber.org/papers/w22587>
8. <https://leeds-faculty.colorado.edu/bhagat/vc-decisions.pdf>
9. <https://corpgov.law.harvard.edu/2019/08/20/how-do-venture-capitalists-make-decisions/>
10. <https://www.nber.org/papers/w33987>
11. <https://www.nber.org/papers/w15529>
12. <https://econpapers.repec.org/RePEc:bla:jfinan:v:63:y:2008:i:6:p:2785-2815>
13. <https://econpapers.repec.org/RePEc:taf:ufajxx:v:65:y:2009:i:1:p:43-53>
14. <https://repository.upenn.edu/accounting_papers/119>
15. <https://www.nber.org/papers/w16215>
16. <https://insights.som.yale.edu/insights/remote-work-is-linked-to-decline-in-financial-misconduct>
17. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26456>
18. <https://insights.som.yale.edu/insights/even-small-businesses-need-corporate-governance>
19. <https://knowledge.wharton.upenn.edu/article/lessons-from-theranos/>
20. <https://corpgov.law.harvard.edu/2022/01/30/theranos-the-limits-of-the-fake-it-till-you-make-it-strategy/>
21. <https://corpgov.law.harvard.edu/2010/04/16/performance-persistence-in-entrepreneurship-and-venture-capital/>
22. <https://www.nber.org/papers/w26371>
23. <https://papers.ssrn.com/abstract=3347159>
24. <https://www.library.hbs.edu/working-knowledge/ai-schemes-could-make-bernie-madoffs-fraud-look-trivial-eugene-soltes>
25. <https://www.mayerbrown.com/de/insights/publications/2026/08/the-final-chapter-fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons>
26. <https://public-inspection.federalregister.gov/2026-16576.pdf>
27. <https://kpmg.com/us/en/articles/2026/cta-beneficial-ownership-info-boi-reporting-fincen-final-rule.html>
28. <https://corpgov.law.harvard.edu/2026/08/27/fincen-permanently-eliminates-boi-reporting-requirements-for-us-companies-and-us-persons/>
29. <https://ofac.treasury.gov/>
30. <https://ncnk.org/resources/briefing-papers/all-briefing-papers/cyber-hacking-means-self-reliance>
31. <https://bitcoinbook.cs.princeton.edu>
32. <https://www.fincen.gov/news/news-releases/fincen-issues-final-rule-postpone-effective-date-investment-adviser-rule-2028>
33. <https://www.govinfo.gov/content/pkg/FR-2026-01-02/pdf/2025-24184.pdf>
34. <https://www.proskauer.com/blog/fincen-finalizes-twoyear-delay-of-the-investment-adviser-aml-rule-reaffirms-intent-to-further-review-and-tailor-the-rule-and-to-coordinate-with-other-rulemakings>
35. <https://insights.som.yale.edu/insights/where-did-madoffs-money-go>
36. <https://www.sec.gov/newsroom/press-releases/2024-107>
37. <https://insights.som.yale.edu/insights/did-crypto-cause-the-ftx-collapse>
38. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/what-the-ftx-collapse-means-for-the-cryptocurrency-market/>
39. <https://osc.ca/quadrigacxreport/index.html>
40. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/4/>
41. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/5/>
42. <https://oyc.yale.edu/economics/econ-252-08/lecture-8>
43. <https://www.library.hbs.edu/working-knowledge/bernie-madoff-explains-himself>
44. <https://insights.som.yale.edu/insights/customer-data-can-reveal-revenue-fraud-at-supplier-firms>
45. <https://www.nber.org/papers/w20947>
46. <https://spia.princeton.edu/news/how-income-fraud-made-housing-bubble-worse>
47. <https://www.nber.org/papers/w25084>
48. <https://corpgov.law.harvard.edu/2026/11/04/untamed-unicorns-why-startup-finance-is-broken-and-how-to-fix-it/>
49. <https://justice.gov/usao-sdny/pr/first-brands-executives-charged-multibillion-dollar-fraud>
50. <https://irs.gov/compliance/criminal-investigation/first-brands-executives-charged-with-multibillion-dollar-fraud>
51. <https://www.sec.gov/newsroom/press-releases/2026-77-sec-charges-former-executives-fraud-connection-19-billion-collapse-subprime-auto-lender-tricolor>
52. <https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-october/seeing-red-flags-in-tricolor-collateral-interests>
53. <https://www.nbcnews.com/politics/white-house/trump-commutes-7-year-prison-sentence-former-private-equity-ceo-david-rcna246744>
54. <https://www.sec.gov/newsroom/press-releases/2025-111-sec-charges-pennsylvania-resident-his-companies-770-million-ponzi-scheme>
55. <https://www.journalofaccountancy.com/issues/2020/sep/ssae-no-19-flexibility-for-agreed-upon-procedures.html>
56. <https://pcaobus.org/oversight/standards/attestation-standards/details/AT601>
57. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/6/>
58. <https://www.sec.gov/newsroom/press-releases/2025-98-sec-charges-georgia-based-first-liberty-building-loan-its-owner-operating-140-million-ponzi-scheme>
59. <https://www.sec.gov/newsroom/press-releases/2025-76-sec-charges-former-real-estate-investment-ceo-operating-multimillion-dollar-ponzi-scheme>
60. <https://www.itiger.com/news/1145037528>
61. <https://www.ai-cio.com/?p=107176>
62. <https://www.dailyprincetonian.com/article/2025/10/princeton-news-endowment-returns-market-private-equity-tax-research-funding-alternative-assets>
63. <https://insights.som.yale.edu/insights/contrary-to-conventional-wisdom-margins-don-t-rise-as-company-grows>
64. <https://knowledge.wharton.upenn.edu/article/kicking-tires-ubers-17-billion-valuation-worth-much/>
65. <https://insights.som.yale.edu/insights/is-anthropic-worth-125-trillion>
66. <https://insights.som.yale.edu/insights/how-does-private-equity-create-value>
67. <https://insights.som.yale.edu/insights/do-search-fund-ceos-improve-performance>
68. <https://knowledge.wharton.upenn.edu/article/mas-overlooked-pitfall-the-false-negative/>
69. <https://knowledge.wharton.upenn.edu/article/game-changing-method-valuing-companies/>
70. <https://realestate.wharton.upenn.edu/working-papers/how-should-commercial-real-estate-be-priced/>
71. <https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/441.pdf>
72. <https://oyc.yale.edu/economics/econ-252-08/lecture-12>
73. <https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2019/04/03-18.schwert.pdf>
74. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss2/1/>
75. <https://www.imf.org/-/media/files/publications/gfsr/2024/april/english/ch2.pdf.md>
76. <https://yalelawjournal.org/index.php/article/the-credit-markets-go-dark>
77. <https://knowledge.wharton.upenn.edu/article/whats-wrong-with-the-private-equity-market-and-how-to-fix-it/>
78. <https://www.nber.org/papers/w27690>
79. <https://ar5iv.labs.arxiv.org/html/1205.2299>
80. <https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-investment-officer-infinity-q-sentenced-15-years-prison>
81. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-25331>
82. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26671>
83. <https://www.library.hbs.edu/working-knowledge/why-companies-failand-how-their-founders-can-bounce-back>
84. <https://www.nber.org/papers/w27316>
85. <https://aiinstitute.hbs.edu/forget-the-algorithms-follow-the-electricity/>
86. <https://knowledge.wharton.upenn.edu/article/lender-roundtable-outlook-on-debt-markets/>
87. <https://insights.bu.edu/four-mantras-from-the-endowment-a-personal-journey/>
88. <https://corpgov.law.harvard.edu/2020/06/29/justice-department-updates-its-guidance-on-corporate-compliance-programs/>
89. <https://corpgov.law.harvard.edu/2016/09/21/what-do-private-equity-firms-say-they-do/>
90. <https://www.nber.org/papers/w23626>
91. <https://www.nber.org/papers/w8876>
92. <https://bcf.princeton.edu/academic-programs/master-in-finance/requirements-core-courses/tracks-and-electives>
93. <https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2014/04/0717.pdf>
94. <https://www.nber.org/system/files/working_papers/w16652/w16652.pdf>
95. <https://www.library.hbs.edu/working-knowledge/how-to-write-a-great-business-plan>
96. <https://www.nber.org/papers/w27492>
97. <https://oyc.yale.edu/economics/econ-252-08/lecture-9>
98. <https://www.nber.org/papers/w22660>
99. <https://www.nber.org/papers/w19299>
100. <https://www.nber.org/papers/w24941>
101. <https://www.nber.org/papers/w11136>
102. <https://www.nber.org/papers/w29887>
103. <https://repec.som.yale.edu/icfpub/publications/2471.pdf>
104. <https://gceps.princeton.edu/wp-content/uploads/2017/01/104malkiel.pdf>
105. <https://www.nber.org/papers/w19643>
106. <https://knowledge.wharton.upenn.edu/article/why-semi-liquid-private-credit-funds-are-in-fragile-territory/>
107. <https://www.yalelawjournal.org/article/the-separation-of-funds-and-managers-a-theory-of-investment-fund-structure-and-regulation>
108. <https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf>
109. <https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm>
110. <https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/CovenantInvestmentJF2008.pdf>
111. <https://finance.wharton.upenn.edu/~mrrobert/resources/Publications/RenegotiationJFE2009.pdf>
112. <https://www.nber.org/papers/w20484>
113. <https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2020/12/10-20.Schwert02.pdf>
114. <https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html>
115. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol4/iss1/10/>
116. <https://economics.yale.edu/sites/default/files/2024-02/metrick-2024-the-failure-of-silicon-valley-bank-and-the-panic-of-2023.pdf>
117. <https://repec.som.yale.edu/icfpub/publications/2358.pdf>
118. <https://cowles.yale.edu/sites/default/files/2022-08/d1715.pdf>
119. <https://www.nber.org/papers/w18905>
120. <https://www.princeton.edu/~markus/research/papers/Mkt_Fun_Liquidity.pdf>
121. <https://www.nber.org/papers/w21581>
122. <https://www.nber.org/papers/w24823>
123. <https://www.federalreserve.gov/supervisionreg/srletters/SR2305.htm>
124. <https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/519.pdf>
125. <https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/747.pdf>
126. <https://www.nber.org/papers/w14708>
127. <https://realestate.wharton.upenn.edu/working-papers/robbing-the-bank-non-recourse-lending-and-asset-prices/>
128. <https://www.nber.org/papers/w32579>
129. <https://wffi.wharton.upenn.edu/wp-content/uploads/2025/10/HSVRegional-Banks-and-CRE-Risks.pdf>
130. <https://real-estate.wharton.upenn.edu/programs/mba/course-descriptions/>
131. <https://sec.gov/files/Private%20Fund%20Risk%20Alert.pdf>
132. <https://fs.blog/before-you-make-that-big-decision>
133. <https://www.nber.org/papers/w22026>
134. <https://netzeroamerica.princeton.edu>
135. <https://repeatproject.org>
136. <https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf>
137. <https://maalot.co.il/Publications/MT20221215151143.PDF>
138. <https://bdap.wharton.upenn.edu/wp-content/uploads/2026/01/Stablecoin-Toolkit.pdf>
139. <https://wffi.wharton.upenn.edu/wp-content/uploads/2026/05/WIFPR-Tokenizing-Real-World-Assets-Cong-Mayer-and-Rabetti.pdf>
140. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol8/iss3/1/>
141. <https://www.nber.org/papers/w19568>
142. <https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf>
143. <https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub>
144. <https://nvca.org/model-legal-documents/>
145. <https://corpgov.law.harvard.edu/tag/due-diligence/>
146. <https://corpgov.law.harvard.edu/tag/private-equity/>
147. <https://www.library.hbs.edu/working-knowledge>
148. <https://wffi.wharton.upenn.edu/policy-series-topics/>
149. <https://insights.som.yale.edu>
150. <https://www.nber.org/digest/jan16/household-debt-and-business-cycles-worldwide>
151. <https://corpgov.law.harvard.edu/2009/06/08/did-securitization-lead-to-lax-screening/>
152. <https://nber.org/papers/w28369>
153. <https://www.princeton.edu/~markus/research/papers/hedgefunds_bubble.htm>
154. <https://corpgov.law.harvard.edu/2011/11/28/investment-cycles-and-startup-innovation/>
155. <https://corpgov.law.harvard.edu/2026/02/28/private-equity-for-all-the-paradoxical-push-to-democratize-private-markets/>
156. <https://library.hbs.edu/working-knowledge/how-private-debt-became-2-trillion-industry>
157. <https://knowledge.wharton.upenn.edu/article/five-things-to-know-about-private-credit>
158. <https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-184-for-q3-2025>
159. <https://cliffwater.com/files/cdli/docs/Cliffwater_Report_on_US_DirectLending.pdf>
160. <https://nber.org/papers/w25775>
161. <https://econpapers.repec.org/RePEc:bla:jfinan:v:73:y:2018:i:4:p:1751-1783>
162. <https://insights.som.yale.edu/insights/is-commercial-real-estate-in-for-downturnor-crisis>
163. <https://insights.som.yale.edu/insights/whats-next-for-the-startups-that-banked-with-svb>
164. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/12/>
165. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/24/>
166. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/9/>
167. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/1/>
168. <https://insights.som.yale.edu/insights/stablecoins-survived-crypto-winter-but-that-doesnt-make-them-safe>
169. <https://www.sec.gov/Archives/edgar/data/1876042/000187604226000116/a2025annualreport0331.pdf>
170. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss1/18/>
171. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/7/>
172. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/8/>
173. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss1/3/>
174. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol3/iss1/6/>
175. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss3/2/>
176. <https://www.acli.com/-/media/acli/public/files/pdfs-public-site/public-public-policy/captives/captive_reinsurance_in_life_ins_harrington_2014.pdf>
177. <https://www.chicagofed.org/publications/working-papers/2025/2025-09>
178. <https://www.nber.org/digest/jun16/gamblers-fallacy>
179. <https://insights.som.yale.edu/insights/passionate-startup-pitch-is-powerful-but-can-be-misleading>
180. <https://insights.som.yale.edu/insights/how-corporate-jargon-obscures-the-truth-and-fuels-disaster>
181. <https://elischolar.library.yale.edu/ypfs-jpm-chase-london-whale/>
182. <https://elischolar.library.yale.edu/journal-of-financial-crises/vol1/iss1/3/>
183. <https://princo.princeton.edu/about/organizational-model>
184. <https://insights.som.yale.edu/insights/why-connecticuts-investments-are-underperforming>
185. <https://faculty.washington.edu/pathaksd/BBUS549/Required%20Readings/Before%20You%20Make%20that%20Big%20Decision.pdf>
186. <https://hbswk.hbs.edu/item/replicating-private-equity-with-value-investing-homemade-leverage-and-hold-to-maturity-accounting>
187. <https://news.yale.edu/2018/10/01/investment-return-123-brings-yale-endowment-value-294-billion>
188. <https://ilpa.org/wp-content/uploads/2025/09/Combined-Overview-ILPA-Templates.pdf>
189. <https://katten.com/insights/advisories/ilpa-publishes-updated-reporting-template-and-new-performance-template>
190. <https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf>
191. <https://corpgov.law.harvard.edu/2024/07/15/private-equity-and-net-asset-value-loans-ticking-time-bomb-or-ticking-all-the-right-boxes/>
192. <https://www.nber.org/papers/w24941.pdf>
193. <https://corpgov.law.harvard.edu/2025/02/03/private-equity-for-pension-plans-evaluating-private-equity-performance-from-an-investors-perspective/>
194. <https://corpgov.law.harvard.edu/2014/01/12/valuing-private-equity/>
195. <https://www.library.hbs.edu/working-knowledge/rethinking-risk-why-pension-funds-are-betting-on-alternative-assets>
196. <https://insights.som.yale.edu/insights/for-top-venture-capital-firms-success-breeds-success>
197. <https://nber.org/system/files/working_papers/w22660/w22660.pdf>
198. <https://princo.princeton.edu/about/investment-strategy>
199. <https://investments.yale.edu/partners>
200. <https://corpgov.law.harvard.edu/2026/10/14/understanding-communications-by-private-fund-managers/>
201. <https://corpgov.law.harvard.edu/2022/02/17/sec-identifies-private-fund-deficiencies-signifying-increased-industry-scrutiny/>
202. <https://corpgov.law.harvard.edu/2026/09/23/the-ceo-decision-how-pe-investors-select-and-reassess-leaders-from-entry-to-exit/>
203. <https://corpgov.law.harvard.edu/2014/01/30/the-impact-of-venture-capital-monitoring/>
204. <https://corpgov.law.harvard.edu/2026/02/21/succession-planning-in-private-equity-a-strategic-imperative-for-gps-and-lps/>
205. <https://www.stern.nyu.edu/sites/default/files/assets/documents/Eugene%20Soltes%20-%20The%20Difficulty%20of%20Being%20Good%20The%20Efficacy%20of%20Integrity%20Hotlines.pdf>
206. <https://corpgov.law.harvard.edu/2018/08/14/fcpa-successor-liability/>
207. <https://corpgov.law.harvard.edu/2019/10/09/secondary-liability-risks-for-private-funds-recent-developments/>
208. <https://www.skadden.com/insights/publications/2018/10/analyzing-akorn>
209. <https://law.justia.com/cases/delaware/court-of-chancery/2018/ca-2018-0300-jtl.html>
210. <https://www.nber.org/papers/w24831>
211. <https://papers.ssrn.com/abstract=3241707>
212. <https://www.hklaw.com/en/insights/publications/2022/02/division-of-examinations-publishes-risk-alert-for-private-fund>
213. <https://www.sec.gov/newsroom/press-releases/2025-53>
214. <https://corpgov.law.harvard.edu/2026/07/30/are-hints-disclosures-delaware-supreme-court-revives-ma-fraud-claim-despite-buyers-red-flags/>
215. <https://corpgov.law.harvard.edu/2025/08/26/chancery-decision-doubles-down-on-due-diligence/>
216. <https://corpgov.law.harvard.edu/2026/02/10/drafting-guidance-from-delaware-supreme-court-on-earnouts-efforts-obligations-and-fraud/>
217. <https://corpgov.law.harvard.edu/2017/07/19/the-looming-specter-post-closing-fraud-claims-in-private-company-ma-litigation/>
218. <https://corpgov.law.harvard.edu/2019/07/01/deal-insurance-representation-warranty-insurance-in-ma-contracting/>
219. <https://businesslawtoday.org/?p=33407>
220. <https://www.klgates.com/2025-ABA-Private-Target-Mergers-Acquisitions-Deal-Points-Study-12-19-2025>
221. <https://www.goulstonstorrs.com/insights/article/2025-aba-private-target-m-and-a-deal-points-study-what-s-market>
222. <https://media.taftlaw.com/wp-content/uploads/2025/04/15175412/2025-SRS-Acquiom-MA-Deal-Terms-Study-2-page-quick-reference.pdf>
223. <https://www.aon.com/en/insights/reports/transaction-solutions-global-claims-study>
224. <https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2023-r-and-w.pdf.coredownload.pdf>
225. <https://corpgov.law.harvard.edu/2025/07/11/the-art-and-science-of-earn-outs-in-ma/>
226. <https://corpgov.law.harvard.edu/2026/06/29/opting-out-of-court-reputation-and-informal-norms-in-private-equity/>
227. <https://corpgov.law.harvard.edu/2026/07/20/chancery-finds-potential-liability-for-blocking-company-financings-despite-contractual-veto-rights/>
228. <https://corpgov.law.harvard.edu/2026/06/17/chancery-finds-funds-liable-for-aiding-directors-fiduciary-breaches/>
229. <https://corpgov.law.harvard.edu/2026/04/16/sponsor-designated-lenders-counsel/>
230. <https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules>
231. <https://www.paulweiss.com/insights/client-memos/fifth-circuit-vacates-private-fund-adviser-rule>
232. <https://www.sec.gov/newsroom/press-releases/2025-47>
233. <https://govinfo.gov/content/pkg/FR-2026-04-28/html/2026-08176.htm>
234. <https://www.justice.gov/opa/pr/justice-department-places-fda-approved-marijuana-products-and-products-containing-marijuana>
235. <https://zenodo.org/records/15801701>
236. <https://huduser.gov/portal/hud/mortgagee_letters/25-3_Hsngml.pdf>
237. <https://insights.som.yale.edu/insights/putting-price-on-climate-risk>
238. <https://insights.som.yale.edu/insights/the-colorado-river-is-overdrawn-and-corporate-reckoning-is-imminent>
239. <https://insights.som.yale.edu/insights/why-the-texas-power-market-failed>
240. <https://insights.som.yale.edu/insights/doges-lease-cancellations-are-already-hitting-the-commercial-real-estate-market>
241. <https://cases.som.yale.edu/connecticut-green-bank-2018>
242. <https://www.hks.harvard.edu/publications/regulating-infrastructure-monopoly-contracts-and-discretion>
243. <https://documents1.worldbank.org/curated/en/678041468765605224/pdf/288160PAPER0Granting010renegotiating.pdf>
244. <https://library.hbs.edu/working-knowledge/blaming-data-centers-for-higher-electric-bills-its-not-that-simple>
245. <https://arxiv.org/abs/2609.08166>
246. <https://www.nixonpeabody.com/insights/alerts/2025/01/14/hud-adopts-relaxed-loan-sizing-standards-for-fha-insured-loans>
247. <https://www.hud.gov/sites/documents/10-11hsgn.pdf>
248. <https://mfguide.fanniemae.com/fnmf-pdf/download/9906>
249. <https://fdic.gov/news/financial-institution-letters/2023/fil23034.html>
250. <https://www.govinfo.gov/content/pkg/FR-2023-07-06/html/2023-14247.htm>
251. <https://occ.gov/publications-and-resources/publications/comptrollers-handbook/files/commercial-real-estate-lending/pub-ch-commercial-real-estate-previous.pdf>
252. <https://knowledge.wharton.upenn.edu/podcast/ripple-effect/next-crisis-empty-office-buildings-joe-gyourko/>
253. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/whats-going-to-happen-to-all-those-empty-office-buildings/>
254. <https://cases.som.yale.edu/canary-wharf>
255. <https://www.nber.org/papers/w16685>
256. <https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/407.pdf>
257. <https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/730.pdf>
258. <https://knowledge.wharton.upenn.edu/article/towards-greater-transparency-in-real-estate-private-equity-funds/>
259. <https://www.sec.gov/newsroom/press-releases/2024-97>
260. <https://www.bisnow.com/national/news/commercial-real-estate/real-estate-firms-executives-hit-with-sec-charges-over-372m-ponzi-scheme-132575>
261. <https://www.sec.gov/newsroom/press-releases/2024-2>
262. <https://realestate.wharton.upenn.edu/working-papers/real-estate-crashes-and-bank-lending/>
263. <https://realestate.wharton.upenn.edu/working-papers/the-crash-and-rebound-of-canary-wharf/>
264. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/on-shaky-ground-commercial-real-estate-faces-financial-tremors/>
265. <https://www.brookings.edu/articles/lessons-from-the-collapse-of-steward-health-care/>
266. <https://www.nber.org/papers/w28474>
267. <https://knowledge.wharton.upenn.edu/article/fallout-from-the-banking-crisis-whats-ahead>
268. <https://knowledge.wharton.upenn.edu/article/how-higher-property-insurance-premiums-mirror-climate-risk/>
269. <https://nber.org/papers/w27690>
270. <https://carta.com/data/state-of-private-markets-q2-2025/>
271. <https://carta.com/data/series-a-fundraising-q2-2025>
272. <https://carta.com/data/state-of-private-markets-q3-2025-full-report/>
273. <https://www.justice.gov/usao-sdny/pr/startup-ceo-charlie-javice-sentenced-85-months-prison-175-million-fraud>
274. <https://www.iconiq.com/growth/reports/2025-state-of-software>
275. <https://www.iconiq.com/growth/insights/growth-and-efficiency>
276. <https://networkcraft.net/2026-saas-metrics-benchmarks/>
277. <https://cxcash.com/metrics/saas>
278. <https://designrevision.com/blog/saas-growth-benchmarks>
279. <https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey>
280. <https://www.bvp.com/atlas/scaling-to-100-million>
281. <https://kylepoyar.substack.com/p/2025-saas-benchmarks-report>
282. <https://vcbeast.com/nvca-model-legal-documents-startup-forms>
283. <https://www.1752.vc/learn/venture-capital-deal-documents-explained>
284. <https://insights.som.yale.edu/insights/companies-invest-in-startups-to-repair-weaknesses>
285. <https://insights.som.yale.edu/insights/when-corporate-acquisitions-affect-healthcare>
286. <https://knowledge.wharton.upenn.edu/article/continuing-defaults-by-private-equity-portfolio-companies-transform-the-middle-market/>
287. <https://www.sidley.com/en/insights/newsupdates/2026/03/financial-covenants-in-private-credit-transactions>
288. <https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-246-for-q4-2025>
289. <https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-273-for-q1-2026>
290. <https://www.proskauer.com/report/proskauers-private-credit-default-index-reveals-rate-of-241-for-q3-2026>
291. <https://cliffwaterdev-staging.azurewebsites.net/files/docs/CliffwaterPressRelease_CDLI_2025_Results.pdf>
292. <https://founderpath.com/blog/venture-debt>
293. <https://ctacquisitions.com/what-is-venture-debt-financing/>
294. <https://www.stifel.com/Newsletters/AdGraphics/FlipBooks/_GRP/Macolino-WMG/Past-Events/VentureDebtWebinarSlides.pdf>
295. <https://en.wikipedia.org/wiki/Venture_debt>
296. <https://beancount.io/blog/2026/05/14/venture-debt-recurring-revenue-loans-series-a-b-startups-runway-extension-warrant-coverage-mrr-financing-non-dilutive-growth-capital-guide>
297. <https://kadenwoodgroup.com/perspectives/revenue-based-financing-vs-venture-debt>
298. <https://ideas.repec.org/a/oup/rfinst/v25y2012i6p1713-1761.html>
299. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-demise-of-toys-r-us/>
300. <https://www.gao.gov/products/gao-23-105210>
301. <https://ranfunding.com/asset-based-lending/>
302. <https://knowledge.wharton.upenn.edu/article/clos-will-not-cause-next-financial-crisis/>
303. <https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26612>
304. <https://www.goreuben.com/templates/ic-memo-buyout>
305. <https://www.v7labs.com/blog/quality-of-earnings-analysis>
306. <https://modusalliance.com/insights/buy-side-vs-sell-side-qoe/>
307. <https://f2.ai/blog/how-ai-is-rewriting-the-diligence-to-close-playbook-for-pe-deal-teams>
308. <https://knowledge.wharton.upenn.edu/article/how-to-align-private-equity-motives-with-nursing-home-outcomes/>
309. <https://soferadvisors.com/insights/blog/what-is-a-leveraged-buyout-lbo-structure-explained/>
310. <https://www.iese.edu/media/research/pdfs/ST-0689-E>
311. <https://ctacquisitions.com/lbo-meaning/>
312. <https://ctacquisitions.com/lower-middle-market-private-equity-2026/>
313. <https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations>
314. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/looking-for-a-company-to-run-search-funds-could-be-the-answer/>
315. <https://corpgov.law.harvard.edu/2016/12/19/the-year-in-review-sec-enforcement-actions-against-investment-advisers/>
316. <https://privateequitybro.com/top-lower-middle-market-investment-banks-to-watch-in-2026/>
317. <https://www.srsacquiom.com/our-insights/reps-warranties-findings/>
318. <https://www.aig.com/content/dam/aig/america-canada/us/documents/business/management-liability/aig-manda-2021-r-and-w.pdf>
319. <https://openyls.law.yale.edu/entities/publication/44dd0075-0956-44d1-bb2e-ea326755b4b5>
320. <https://www.yalejreg.com/bulletin/net-cash-per-share-the-key-to-disclosing-spac-dilution/>
321. <https://netzeroamerica.princeton.edu/img/Princeton%20NZA%20FINAL%20REPORT%20SUMMARY%20(29Oct2021>
322. <https://www.energy.gov/sites/default/files/2023-07/om-agreement-checklist-on-site-wind-energy.docx>
323. <https://www.ourenergypolicy.org/wp-content/uploads/2017/08/Definitions-of-availability-terms-for-the-wind-industry-white-paper-09-08-2017.pdf>
324. <https://ibinterviewquestions.com/blog/project-finance-explained>
325. <https://rfp.entergy.com/ENTRFP/SEND/2020ETICCGTRFP/Documents/04282020/Appendix%20B-2%20-%20Term%20Sheet%20-%20Toll.pdf>
326. <https://kleinmanenergy.upenn.edu/commentary/podcast/the-future-of-electricity-demand-in-the-ai-era/>
327. <https://www.wsgr.com/PDFSearch/ctp_guide.pdf>
328. <https://kleinmanenergy.upenn.edu/commentary/podcast/will-interconnection-reform-unlock-the-grid/>
329. <https://kleinmanenergy.upenn.edu/commentary/blog/the-landscape-of-renewable-energy-in-the-united-states-in-an-era-of-subsidy-scrutiny/>
330. <https://www.cdfa.net/cdfa/cdfaweb.nsf/ord/iefc12-joassin.html/$file/Joassin.%20Fitch%20CJ%20-%20CDFA%20Intro%20Course%207-31-12.pdf>
331. <https://plausity.com/en/news/ai-data-center-power-due-diligence-grid-cooling-energy-risk>
332. <https://gi-advisors.com/data-center-project-finance-development-commercial-structuring-power-constraints-and-bankability/>
333. <https://www.rtoinsider.com/wp-content/uploads/2025/12/Whitepaper-dec-2025.pdf>
334. <https://www.utilitydive.com/news/repeat-project-carbon-emissions-transmission-report/687446/>
335. <https://netzeroamerica.princeton.edu/img/NZA%20Annex%20F%20-%20HV%20Transmission.pdf>
336. <https://insights.som.yale.edu/insights/who-will-finance-the-ai-revolution>
337. <https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power>
338. <https://kleinmanenergy.upenn.edu/commentary/podcast/how-pjm-is-grappling-with-data-center-power-demand/>
339. <https://savrn.com/blog/ai-data-center-supply-chain>
340. <https://kleinmanenergy.upenn.edu/commentary/blog/re-2025-navigating-the-u-s-power-systems-current-challenges/>
341. <https://maalot.co.il/Publications/MT20171116151537.pdf>
342. <https://dbrs.morningstar.com/research/447217>
343. <https://ratings.moodys.com/api/rmc-documents/361401>
344. <https://www.yahoo.com/video/longview-power-llc-moodys-upgrades-191706199.html>
345. <https://www.ca-cib.com/sites/default/files/2020-10/Project%20Bond%20Focus%20-%20Wind%202020%20VF.pdf>
346. <https://publicenterprise.org/wp-content/uploads/Project-Finance-September-2024.pdf>
347. <https://uspeglobal.com/articles/what-is-an-independent-power-producer-ipp-business-models/>
348. <https://jakenenergy.com/knowledge/merchant-power-plant-financing.html>
349. <https://www.eia.gov/outlooks/aeo/pdf/electricity_generation.pdf>
350. <https://prismecs.com/blog/technical-comparison-between-the-gas-turbine-and-combustion-engine>
351. <https://www.lazard.com/media/2ozoovyg/lazards-lcoeplus-april-2023.pdf>
352. <https://ar5iv.arxiv.org/html/1205.2302>
353. <https://www.jefferies.com/wp-content/uploads/sites/4/2026/07/Jefferies-Global-Secondary-Market-Review-July-2026.pdf>
354. <https://www.utilitydive.com/news/panda-temple-bankruptcy-could-chill-new-gas-plant-buildout-in-ercot-market/442582/>
355. <https://www.coleschotz.com/new-delaware-chapter-11-filing-homer-city-generation-l-p/>
356. <https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers>
357. <https://www.canarymedia.com/articles/data-centers/pjm-needs-flexible-data-centers>
358. <https://www.energyconnects.com/news/gas-lng/2025/december/flexible-power-accelerates-data-center-projects-princeton-says>
359. <https://auxocapitaladvisors.com/cpg-m-and-a-advisory/>
360. <https://www.logicagencyinc.com/guides/cpg-channel-economics>
361. <https://www.trustcultivar.com/resources/cpg-financial-kpis-emerging-brands>
362. <https://alloy.ai/cpg-analytics>
363. <https://greengrowthcpas.com/irc-280e-cannabis-tax-guide/>
364. <https://www.peasebell.com/insights/cannabis-280e-deductions-2026/>
365. <https://cannabizguide.com/guides/280e-tax-basics>
366. <https://knowledge.wharton.upenn.edu/podcast/this-week-in-business/cannabusiness-marijuana-regulations-banking-concerns/>
367. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/policy-paradox-legalized-marijuana/>
368. <https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/>
369. <https://www.morganlewis.com/pubs/2026/09/high-time-for-a-change-post-dea-hearing-broader-marijuana-rescheduling-questions-remain>
370. <https://w4.stern.nyu.edu/sternfin/mkacperc/public_html/sin.pdf>
371. <https://www.stern.nyu.edu/experience-stern/news/uat_024862>
372. <https://econpapers.repec.org/RePEc:oup:rfinst:v:23:y:2010:i:6:p:2303-2341>
373. <https://mattercite.com/ilpa-ddq>
374. <https://angelinvestorsnetwork.com/capital-raising/ilpa-ddq-2-0-guide-vet-first-time-fund-manager>
375. <https://ilpa.org/resource/continuation-funds-considerations-for-limited-partners-and-general-partners/>
376. <https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf>
377. <https://dealroom.net/blog/hedge-fund-due-diligence>
378. <https://ryanoconnellfinance.com/hedge-fund-due-diligence/>
379. <https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/secrets-of-the-private-equity-trade/>
380. <https://corpgov.law.harvard.edu/2024/05/10/fee-variation-in-private-equity/>
381. <https://www.bloomberg.com/news/articles/2025-12-01/trump-commutes-sentence-of-gpb-capital-founder-david-gentile>
382. <https://corpgov.law.harvard.edu/2015/10/30/fund-advisers-and-fee-disclosure-in-sec-enforcement-action/>
383. <https://www.library.hbs.edu/working-knowledge/is-greed-ruining-private-equity-firms>
384. <https://ideas.repec.org/a/taf/ufajxx/v61y2005i6p80-88.html>
385. <https://corpgov.law.harvard.edu/2026/04/24/financial-institutions-ma-key-trends-and-outlook-2/>
386. <https://www.axios.com/2023/06/27/ftx-management-misuse-customer-funds>
387. <https://corpgov.law.harvard.edu/2023/05/22/anatomy-of-a-run-the-terra-luna-crash/>
388. <https://www.nber.org/papers/w26816>
389. <https://www.yale.edu/funding-yale-home/overview-yales-endowment>
390. <https://paw.princeton.edu/inbox/princos-private-equity-investments>
391. <https://ilpa.org/wp-content/uploads/2023/05/ILPA-Releases-Continuation-Fund-Guidance.pdf>
392. <https://www.torys.com/our-latest-thinking/publications/2023/05/ilpa-releases-continuation-fund-guidance-for-limited-partners-and-general-partners>
393. <https://www.sidley.com/en/insights/newsupdates/2025/08/net-asset-value-based-fund-financings-credit-rating-criteria-and-key-structuring-considerations>
394. <https://sg.finance.yahoo.com/news/rating-firms-cautious-ratifying-private-101145008.html>
395. <https://www.kbra.com/publications/qHMNTvyP>
396. <https://olis.oregonlegislature.gov/liz/2025R1/Measures/Overview/SB951>
