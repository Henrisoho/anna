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
