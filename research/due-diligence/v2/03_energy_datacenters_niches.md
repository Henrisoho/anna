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

