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
