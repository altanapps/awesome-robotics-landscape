# EU Regulatory Deep-Dive: "Vanta for Robots" (Wedge 2)

_Research date: 2026-04-28. Scope: EU AI Act + Machinery Regulation 2023/1230, UK post-Brexit, notified body landscape, Vanta precedent, and market implications._

---

## A. Machinery Regulation (EU) 2023/1230 — applies 20 January 2027

**What changed from the old Machinery Directive (2006/42/EC)?**

The Directive was a minimum-harmonisation instrument; the new Regulation is directly applicable across all EU member states with no national transposition — meaning there is no variation in how it is enforced. Structurally, Annex I of the old Directive (essential health and safety requirements, EHSRs) has moved to Annex III. The old Annex IV (high-risk machinery requiring notified body involvement) has become Annex I, now split into Part A and Part B.

Source: [TÜV Rheinland overview](https://www.tuv.com/world/en/new-machinery-regulation-eu-2023-1230.html), [CertifyComply](https://certifycomply.com/blog/machine-regulation-2023-1230-how-it-affects-machine-manufacturers-and-importers/), [Pilz](https://www.pilz.com/en-US/support/law-standards-norms/manufacturer-machine-operators/machinery-regulation)

**How are autonomous / AI-driven / self-evolving machines classified?**

Annex I Part A explicitly includes "safety components and embedded safety systems with self-evolving capabilities, utilizing machine learning to ensure safety functions." This is the critical new category. Autonomous mobile robots (AMRs), cobots with sensor-driven autonomy, and any machine whose safety functions are governed by a learning algorithm fall here. Part A machines cannot self-declare — they require independent notified body assessment regardless of whether harmonised standards for the AI module exist.

Additional requirements specific to this category (Annex III, EHSRs):
- Sensor-fed or autonomous machines must document the general characteristics, capabilities, and limitations of the system.
- Data acquisition, development, testing, and validation processes must be documented when safety-related actions are controlled by sensor data.
- Machines with self-learning behaviour must document decision-making processes.
- AMRs must include monitoring functions providing real-time information to a human supervisor and must support safe fallback/override modes.

Source: [TechWorks AI](https://www.techworksai.org/how-ai-impacts-the-2027-eu-machinery-regulation/), [EU-OSHA](https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery)

**Conformity assessment routes:**

- **Part A (Annex I) — self-evolving AI, safety components with ML:** Mandatory third-party assessment by a notified body. No self-declaration permitted.
- **Part B (Annex I) — other high-risk machinery:** Either notified body involvement OR full quality assurance system (similar to ISO 9001 pathway), depending on subcategory.
- **All other machinery:** EU Declaration of Conformity (self-declaration) + CE marking, as under the old Directive.

The new regulation therefore moves the most commercially interesting machines — autonomous mobile robots, AI-controlled presses, collaborative robots with self-evolving safety functions — out of the self-declaration bucket and into mandatory third-party certification.

---

## B. EU AI Act overlap with Machinery Regulation

**How the two regimes interact:**

The AI Act does not replace the Machinery Regulation for robotic products. Instead, it layers on top. Under Article 6(1) of the AI Act, an AI system is high-risk if it is intended to be used as a safety component of a product covered by EU harmonisation legislation listed in Annex II — and if that product requires third-party conformity assessment under that sectoral legislation. The Machinery Regulation is explicitly listed in Annex II of the AI Act.

Result: an autonomous machine covered by the Machinery Regulation (self-evolving, Annex I Part A) that also contains a high-risk AI system is subject to **both** frameworks simultaneously. The practical effect is that the conformity assessment under the Machinery Regulation can subsume the AI Act assessment — but only if the notified body is designated under both regimes.

Source: [Bird & Bird analysis](https://www.twobirds.com/en/insights/2026/smart-robots,-dual-regulations-navigating-the-ai-act-and-machinery-compliance), [EU AI Act Article 6](https://artificialintelligenceact.eu/annex/3/)

**AI Act high-risk timeline:**

- **2 August 2026:** Annex III high-risk AI systems placed on market after this date must comply with all Chapter III obligations (risk management, data governance, technical documentation, transparency, human oversight, accuracy, robustness, cybersecurity).
- **2 August 2027:** High-risk AI systems that are embedded in regulated products listed in Annex II (including machinery) get a 36-month transition — i.e., obligations apply from 2 August 2027. This is the operative deadline for most robotics OEMs.

Source: [AI2 Work](https://ai2.work/economics/eu-ai-act-high-risk-rules-hit-august-2026-your-compliance-countdown/), [HI AI Design](https://www.hiai-design.com/blog-eu-ai-act-robotics-2026)

**What Annex IV of the AI Act requires (technical documentation):**

Annex IV is a long-form technical documentation obligation. Required content includes:
- A general description of the AI system and its intended purpose
- Design decisions, including trade-offs made
- Description of relevant data, data acquisition, labelling, and pre-processing methods
- Description of the training, validation, and testing methods, including metrics used
- Results of testing and evaluation, including known limitations
- Risk management system documentation (ongoing, not point-in-time)
- Any changes made throughout the lifecycle

This maps directly onto what a compliance workflow SaaS would generate and maintain. The documentation must be updated whenever the system is substantially modified.

**Double-classification problem:**

An autonomous industrial robot with an AI-based safety function sold in the EU must simultaneously satisfy:
1. Machinery Regulation Annex III EHSRs + notified body assessment (Annex I Part A)
2. AI Act Annex IV technical documentation + conformity assessment (Article 43) — which for Annex II products is folded into the Machinery Regulation assessment if the notified body is dual-designated

The administrative burden is compounding. If the OEM's chosen notified body is not yet AI-Act designated (which is most of them, as of mid-2026), they face separate assessment tracks.

---

## C. Notified body landscape

**Major notified bodies active across machinery and AI:**

- **TÜV SÜD** — notified under Machinery Directive and MDR; pursuing AI Act designation; has published [7 tips guidance](https://www.tuvsud.com/en/newsroom/press-releases/2025/october/7-tips-for-manufacturers-and-operators) for Machinery Regulation 2023/1230 transition
- **DEKRA** — large German conformity body, notified across multiple product directives including machinery
- **TÜV Rheinland** — active on new Machinery Regulation guidance; see [dedicated page](https://www.tuv.com/world/en/new-machinery-regulation-eu-2023-1230.html)
- **BSI Group (UK)** — notified for MDR and IVD; actively pursuing AI Act notified body designation; published [EU AI Act readiness assessment tools](https://www.gov.uk/ai-assurance-techniques/british-standards-institution-eu-ai-act-readiness-assessment-and-algorithmic-readiness-assessment-and-algorithmic-auditing) with UK government backing
- **SGS, Intertek, UL Solutions** — broader product safety bodies extending into AI

**Capacity and bottleneck:**

As of April 2026, the AI Act notified body designation process (which commenced August 2025) is still running with very few bodies fully designated for AI-specific conformity assessment. Team-NB (European Association of Medical Devices Notified Bodies) has formally warned that a shortage of qualified AI auditors could "massively hinder" the AI Act's implementation. End-to-end certification timelines are estimated at 9–24 months depending on documentation readiness and notified body queue. Costs for comparable assessments (using MDR as a proxy) run €50K–€300K+.

Source: [RAPS Euro Roundup](https://www.raps.org/news-and-articles/news-articles/2025/10/euro-roundup-notified-bodies-highlight-issue-that), [MedEnvoy](https://medenvoyglobal.com/blog/the-eu-ai-act-and-notified-bodies/), [eyreACT](https://eyreact.com/notified-bodies-ai-act/)

**Are notified bodies building tooling?**

No evidence of notified bodies building proprietary compliance workflow software for OEMs. Their business model is assessment services, not SaaS. BSI has published readiness assessment toolkits — but these are guidance documents, not software. This is the gap.

---

## D. UK post-Brexit

**UK regulatory regime:**

The UK did not adopt the EU AI Act or the new Machinery Regulation (EU) 2023/1230. Post-Brexit, the UK runs its own product safety regime:

- **UKCA marking** replaces CE marking for the UK market (mandatory for machinery placed on the UK market after 1 January 2023, if new and for industrial/commercial use). However, the UK government is consulting on whether to recognise the new EU Machinery Regulation requirements or introduce equivalent measures — indicating likely divergence in the 2027+ timeframe.
- **UK AI regulation:** The UK's approach remains sector-based and principle-driven, following a pro-innovation whitepaper from February 2024. A dedicated AI bill is expected no earlier than the second half of 2026, and likely addresses only the most powerful AI models and copyright — not robotics directly.
- UK OEMs selling into the EU must still meet CE marking requirements under the EU Machinery Regulation from January 2027. UKCA is irrelevant for EU market access.

Source: [HSE post-Brexit guidance](https://www.hse.gov.uk/work-equipment-machinery/brexit.htm), [Osborne Clarke](https://www.osborneclarke.com/insights/regulatory-outlook-january-2026-artificial-intelligence), [easyclearance.pl](https://easyclearance.pl/en/articles/eksport-maszyn-przemyslowych-uk.html)

**BSI as EU channel:**

BSI Group is UK-headquartered and is actively positioning as an AI Act notified body. It is accredited for MDR/IVDR in the EU and is pursuing AI Act designation. Because it has existing EU-operating arms (BSI has offices and accreditations in Germany and Netherlands), it can serve as a notified body for EU conformity purposes — it is not limited to UKCA. BSI has co-developed EU AI Act readiness tools with OECD.AI, giving it credibility with both regulators and early-adopter OEMs. This makes BSI the highest-value potential channel partner for a compliance SaaS: they have the OEM relationships, the assessment mandate, and no native workflow software.

**MHRA and surgical robots:**

MHRA published a revised regulatory roadmap for medical devices with draft regulations mid-2025 and statutory instrument introduction to Parliament late 2025, coming into force 2026. Guidance on AI development and deployment for Software as a Medical Device is anticipated in 2025–2026. MHRA is targeting a framework for AI regulation by mid-2026. Surgical robots are classified as Class IIb/III medical devices; autonomous surgical systems add AI-Act-equivalent scrutiny. This is an adjacent vertical — not the first beachhead, but worth watching for Version 2 of the product.

---

## E. Adjacent precedent — Vanta and the SOC 2 analogy

**Vanta's trajectory:**

Vanta launched in 2018 focusing exclusively on SOC 2 automation for engineering-led startups. It reached approximately $80M ARR by June 2023, crossed $100M ARR in late 2023, and is at $220M ARR as of July 2025 with ~12,000 customers. Average revenue per customer grew from ~$14K (early 2024) to ~$18K (mid-2025) as it moved upmarket. Its core GTM was through YC companies and auditor partnerships — it embedded audit firms directly into the platform so the auditor could review evidence without leaving Vanta. Three-quarters of YC companies use it.

Source: [Sacra](https://sacra.com/c/vanta/), [Sacra $220M profile](https://sacra.com/research/vanta-at-220m-year/)

**Pricing:**

Vanta subscriptions start around $7,500–$15,000/year (small companies, single framework) rising to $25,000–$100,000+ for enterprise. The audit itself is separate (€10,000–€50,000/year, paid to the auditor). Each additional framework adds ~$1,500/year. This is the pricing architecture to copy: platform subscription + auditor marketplace, not all-in-one.

**Drata and Secureframe (ISO 27001 equivalents):**

Both platforms sit at $7,500–$25,000/year entry. Neither has meaningful EU data residency (Secureframe is UK/AWS London; Drata is US-primary). Neither has robotics or machinery compliance coverage. ISO 27001 automation for EU enterprises is the closest existing analogue — complex, multi-standard, evidence-heavy documentation requirements, recurring audit cycle. The structural parallel to AI Act + Machinery Regulation technical documentation is strong.

**Lessons for robotics compliance tooling:**

1. **The auditor/notified body is the distribution channel, not the competitor.** Vanta grew by making auditors' lives easier, not threatening them. Partner with notified bodies (BSI, TÜV SÜD) the same way.
2. **Recurring documentation beats point-in-time assessment.** Vanta's value is continuous evidence collection; this maps directly onto the AI Act's requirement for ongoing risk management documentation (not just a snapshot).
3. **Start narrow.** Vanta was SOC 2 only for the first two years. The analogue here is: pick one machinery subcategory (e.g., AMRs or collaborative robots) and one regulation (start with AI Act Annex IV, not the full Machinery Regulation).
4. **The audit cost justifies the software cost.** If a notified body assessment costs €50K–€300K and takes 9–24 months, €15K/year for software that shortens prep time by 6 months is an easy sell.

---

## F. Market implications and kill criterion

**Addressable market in 2027–2028:**

The EU AI Act Compliance Solutions market is valued at ~$609M in 2026, growing at 37.3% CAGR to ~$10.5B by 2035 — but this covers all industries, not just robotics. The robotics-specific slice is smaller. There are approximately 2,000–4,000 companies in the EU placing machinery with self-evolving AI on the market (OEMs, system integrators, component suppliers) who will need Annex IV AI Act documentation plus Machinery Regulation Annex I Part A conformity packages by 2027. At €15K–€25K per customer per year, that is a €30M–€100M TAM for a focused robotics compliance SaaS — realistic in 2027–2028 as the deadlines crystallise. The adjacent markets (medical devices, automotive ADAS, construction machinery) expand it materially.

Source: [Dimension Market Research](https://dimensionmarketresearch.com/report/eu-ai-act-compliance-solutions-market/)

**First 10 customers (named OEMs and SIs):**

The most reachable early customers are mid-market EU-based OEMs and system integrators who do not have large internal regulatory affairs teams and who are actively selling into German/French/Benelux manufacturing customers. In rough priority order:

1. **KUKA (Germany)** — market leader in AI-enabled industrial robots, explicitly building certification tooling for partners; compliance pressure is real
2. **ABB Robotics (Switzerland/EU)** — major automotive and logistics robot supplier; well-documented AI integration
3. **Franka Robotics (Germany)** — mid-market cobot OEM, leaner regulatory team, likely earlier adopter
4. **Universal Robots / Teradyne (Denmark)** — market-leading cobot, high sales volume into EU integrators
5. **Omron Robotics (EU operations)** — AMR focus, strong EU presence
6. **Mobile Industrial Robots / MiR (Denmark, Teradyne)** — AMR leader, direct AI Act exposure
7. **Synaos, Magazino, Magazino-type warehouse robot startups** — small teams, no internal compliance bandwidth
8. **System integrators: STILL (Germany), Swisslog (Switzerland)** — install autonomous machinery into production lines, need compliance assistance for CE/UKCA simultaneously
9. **Safety component suppliers: SICK AG, Pilz GmbH** — make the safety sensors and controllers that are Annex I Part A items; documentation burden is identical
10. **BSI Group** — not an OEM, but as an early notified body + channel partner, a BSI-co-branded compliance product is the fastest route to the OEM customer list

Channel: the fastest route is through the notified bodies themselves (BSI, TÜV SÜD, TÜV Rheinland) who are currently drowning in demand, under-tooled, and actively looking for documentation acceleration. A white-label or API integration that helps their OEM clients generate Annex IV technical documentation packages would let the notified body absorb more clients without proportional headcount growth — a direct revenue alignment, not a threat.

**Kill criterion:**

Kill this idea if, within 90 days of outreach to 3 notified bodies (BSI, TÜV SÜD, TÜV Rheinland), none expresses willingness to either (a) co-sell, (b) refer clients, or (c) trial the documentation tool on a live assessment. Notified bodies are the make-or-break distribution choke point. If they are building this internally, or if a competitor (Palantir, ServiceNow, or a well-funded EU GRC startup) has already signed partnerships, the channel advantage disappears. A secondary kill signal is if the EU Commission's Digital Omnibus revision (currently in discussion) extends AI Act deadlines beyond 2028 — it would delay urgency without eliminating it.

---

_Sources used in this research:_
- [EU-OSHA — Regulation 2023/1230](https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery)
- [CertifyComply — Machinery Regulation key changes](https://certifycomply.com/blog/machine-regulation-2023-1230-how-it-affects-machine-manufacturers-and-importers/)
- [TÜV Rheinland — New Machinery Regulation](https://www.tuv.com/world/en/new-machinery-regulation-eu-2023-1230.html)
- [Pilz — Machinery Regulation 2027 changes](https://www.pilz.com/en-US/support/law-standards-norms/manufacturer-machine-operators/machinery-regulation)
- [TechWorks AI — AI and 2027 Machinery Regulation](https://www.techworksai.org/how-ai-impacts-the-2027-eu-machinery-regulation/)
- [Bird & Bird — Dual regulations: AI Act + Machinery](https://www.twobirds.com/en/insights/2026/smart-robots,-dual-regulations-navigating-the-ai-act-and-machinery-compliance)
- [EU AI Act — Annex III](https://artificialintelligenceact.eu/annex/3/)
- [EU AI Act — Article 43 (conformity assessment)](https://artificialintelligenceact.eu/article/43/)
- [HI AI Design — August 2026 robotics deadline](https://www.hiai-design.com/blog-eu-ai-act-robotics-2026)
- [AI2 Work — High-risk rules August 2026](https://ai2.work/economics/eu-ai-act-high-risk-rules-hit-august-2026-your-compliance-countdown/)
- [eyreACT — Notified bodies and AI Act](https://eyreact.com/notified-bodies-ai-act/)
- [RAPS — Notified bodies capacity warning](https://www.raps.org/news-and-articles/news-articles/2025/10/euro-roundup-notified-bodies-highlight-issue-that)
- [BSI / GOV.UK — EU AI Act readiness assessment](https://www.gov.uk/ai-assurance-techniques/british-standards-institution-eu-ai-act-readiness-assessment-and-algorithmic-auditing)
- [HSE — Machinery and Brexit](https://www.hse.gov.uk/work-equipment-machinery/brexit.htm)
- [Osborne Clarke — UK AI regulatory outlook Jan 2026](https://www.osborneclarke.com/insights/regulatory-outlook-january-2026-artificial-intelligence)
- [Sacra — Vanta revenue and growth](https://sacra.com/c/vanta/)
- [Sacra — Vanta at $220M ARR](https://sacra.com/research/vanta-at-220m-year/)
- [Dimension Market Research — EU AI Act compliance solutions market](https://dimensionmarketresearch.com/report/eu-ai-act-compliance-solutions-market/)
- [Intertek — Machinery Regulation overview](https://www.intertek.com/industrial-equipment/machinery-regulation/)
