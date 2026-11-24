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
- Insurer-affiliated managers: when the manager's permanent capital is an affiliated insurer, obtain statutory statements, Schedule S and an affiliated-transaction policy (Chapter 4; Koijen and Yogo, NBER w19568, https://www.nber.org/papers/w19568).

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
