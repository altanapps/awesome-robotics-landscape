# VC Portfolio Scan: Robotics-Software Competitive Landscape
**Scan date:** 2026-04-28
**Scope:** 8–15 web queries, YC W25/S25/W26, a16z, Lux Capital, Bessemer, BCV, NFX, AngelList/TechCrunch Jan 2025–Apr 2026

---

## Companies Found

### Wedge 1 — Robot Fleet Underwriting / Parametric Insurance / Autonomous-System Liability

**Koop Technologies**
- URL: [koop.ai](https://www.koop.ai)
- Stage: Seed — $2.5M (Ubiquity Ventures, Bee Partners, Sure Ventures, WestWave Capital)
- Wedge overlap: Wedge 1 (direct)
- Product: Insurtech platform for autonomous vehicle and robotics operators; collects operational data from fleets to power underwriting, cost-of-risk modeling, and claims for off-road robotics, warehouse AMRs, and AV developers. Has live Robotics E&O and General Liability products via Lloyd's of London syndicates.
- Why they matter: Only funded pure-play robotics insurance underwriting startup found. Small raise but live products and real carrier relationships. Founders are ex-AV data / insurance stack. Threat level: **medium-low now, medium-high if they raise a Series A and verticalize into fleet operators**. The $2.5M raise is tiny for insurance capital requirements — execution risk is high, but they own the category name.

---

### Wedge 2 — EU AI Act + Machinery Regulation Compliance Workflow ("Vanta for Robots")

**Saphira AI**
- URL: [saphira.ai](https://www.saphira.ai)
- Stage: YC S24 — pre-seed / YC-backed (amount undisclosed)
- Wedge overlap: Wedge 2 (direct)
- Product: Hardware safety certification workflow automation for ISO 10218 (industrial robots), ISO 26262 (automotive), UL, CE, TÜV. Automates hazard identification, control measure assignment, safety function aggregation, and generates compliance reports. Positioned as "Vanta for hardware."
- Why they matter: Exact positioning match to Wedge 2. Founded by ex-Tesla, Twitter, Amazon, and Hyperloop engineers who built compliance tools internally. Already has a reference customer (RobCo, ISO 10218-1). YC S24 cohort gives them brand and network in the right circles. Biggest gap: today it appears focused on pre-deployment certification rather than ongoing regulatory change tracking (EU AI Act obligations phase in 2025–2027), which is a potential differentiator window. Threat level: **high** — they have the head start and the exact framing.

**Vanta (existing player)**
- URL: [vanta.com/products/eu-ai-act](https://www.vanta.com/products/eu-ai-act)
- Stage: Late-stage / Series C+; ~$2.5B valuation
- Wedge overlap: Wedge 2 (adjacent — generic AI Act compliance, not robotics-specific)
- Product: Adds EU AI Act controls, policies, and evidence automation on top of its existing SOC 2/ISO 27001 platform. High-risk AI classification, continuous monitoring, auditor-ready documentation.
- Why they matter: Vanta is the obvious gorilla trying to land-and-expand. But their product is a horizontal layer across all AI systems — it does not understand Machinery Regulation Annex I categories, ISO robot-safety standards, or CE marking. A robotics-specific wedge can beat them on depth. Threat level: **medium** — they will commoditize the generic AI Act checklist but won't go deep on machinery/physical safety standards without an acquisition.

---

### Wedge 3 — Multi-Vendor Robot Fleet Observability ("Datadog for Robots")

**Foxglove**
- URL: [foxglove.dev](https://foxglove.dev)
- Stage: Series B — $40M led by Bessemer Venture Partners (Nov 2025); total raised $58M+
- Wedge overlap: Wedge 3 (direct — the strongest incumbent)
- Product: Data and visualization platform for robotics teams: sensor data collection, replay, annotation, and analysis. Customers include Amazon, Anduril, NVIDIA, Wayve, Chef Robotics, Shield AI. Founded by ex-Cruise engineers Adrian Macneil and Roman Shtylman.
- Why they matter: Best-funded pure-play in fleet data/observability. "AWS or Datadog for robotics" is their explicit positioning. $40M Series B signals Bessemer believes this is a durable infra layer. They are post-product-market-fit with enterprise logos. Threat level: **very high** for any data observability or fleet telemetry play targeting the same physical-AI stack.

**InOrbit.AI**
- URL: [inorbit.ai](https://www.inorbit.ai)
- Stage: Series A — $10M (Sep 2025, co-led by L'Attitude Ventures and Globant Ventures); total $12.8M
- Wedge overlap: Wedge 3 (direct — robot orchestration and fleet ops)
- Product: Robot orchestration platform for enterprise multi-vendor fleets; command center, real-time telemetry, AI-assisted remote operations. Recently open-sourced fleet management layer as OpenRobOps (early 2026).
- Why they matter: Smaller than Foxglove but with a different angle — orchestration and remote ops rather than data/replay. The open-source move (OpenRobOps) is a land-and-expand moat play similar to HashiCorp or Grafana. Threat level: **medium** — less capital than Foxglove but deliberately commoditizing the ops layer to drive SaaS upsell.

**Formant**
- URL: [formant.io](https://formant.io)
- Stage: Series B — $21M (Oct 2023, BMW i Ventures, Intel Capital, SignalFire); total $45M
- Wedge overlap: Wedge 3 (direct — cloud robotics platform)
- Product: Cloud platform for robot fleet monitoring, remote operation, analytics, and workflow automation across multi-vendor deployments.
- Why they matter: Older entrant (2018), well-capitalized, automotive and industrial customer base. No major public round since Oct 2023 — possible they are digesting or at an inflection. Threat level: **medium** — a real player but not pulling away from the pack.

**Ember (YC W25)**
- URL: not publicly indexed at search time
- Stage: YC W25 — pre-seed
- Wedge overlap: Wedge 3 (adjacent — hardware and system observability for robots and IoT)
- Product: Observability tooling for robots and IoT, catching hardware failures early and reducing downtime. Founded by ex-Tesla Autopilot engineers.
- Why they matter: Early stage but pedigree matters — ex-Autopilot means they understand real-time embedded failure modes. Threat level: **low now, watch closely** — if they raise a Series A quickly this becomes a direct competitor.

---

### Wedge 4 — RaaS Billing / Usage Metering / Revenue Recognition for Physical Events

No directly funded, purpose-built startup found in this wedge via the queried sources. Adjacent players:

**Hardfin**
- URL: [hardfin.com](https://hardfin.com)
- Stage: Unknown / early
- Wedge overlap: Wedge 4 (adjacent — RaaS accounting and embedded-lease recognition)
- Product: RaaS-specific billing and accounting software addressing ASC 842 embedded lease classification, residual asset tracking, and variable payment accounting for robotics operators.
- Why they matter: The only company surfacing in search results specifically addressing RaaS revenue recognition complexity. No funding data found — may be pre-seed or consulting-driven. Threat level: **low** — but validates the pain point is real enough for someone to write product content around it.

Assessment: This wedge has the thinnest startup competition of all six. The pain is documented (insightsoftware, Ratio.tech, Hardfin all write about the problem) but no well-funded startup has planted a flag.

---

### Wedge 5 — Robot Policy Evaluation SaaS / VLA Model Benchmarks

**Physical Intelligence (pi.ai)**
- URL: [physicalintelligence.company](https://physicalintelligence.company)
- Stage: Series B — $600M (CapitalG / Alphabet lead, Lux Capital, Bond, Redpoint, Sequoia)
- Wedge overlap: Wedge 5 (adjacent — they build VLA models, not the evaluation tooling above them)
- Product: Foundation models (pi0 family) for robot manipulation; not a benchmark SaaS but the dominant model-layer company whose customers would need third-party policy evaluation.
- Why they matter: Their existence creates the market for Wedge 5 tooling — as pi0 and OpenVLA get deployed in production, operators need independent evaluation SaaS. Pi.ai's $1B+ in total raises shows VLA is a real infrastructure layer. Threat level: **indirect** — they could build eval tooling in-house and kill the wedge, but at $600M raised they are focused on the model, not the tooling ecosystem.

No dedicated VLA benchmark / policy evaluation SaaS startup found with meaningful funding. LIBERO, CALVIN, and SIMPLER are academic benchmark suites, not commercial products. This wedge appears pre-competitive at the startup layer.

---

### Wedge 6 — Robot Data Curation / Sovereignty / Search-over-Fleet-Video

**NomadicML (now Nomadic)**
- URL: [nomadicml.com](https://www.nomadicml.com) / [nomadicai.com](https://www.nomadicai.com)
- Stage: Seed — $8.4M (Mar 2026, TQ Ventures lead, Pear VC, Jeff Dean); post-money valuation ~$50M
- Wedge overlap: Wedge 6 (direct — the category-defining incumbent)
- Product: Semantic video search and dataset curation over fleet video archives for AV and robotics teams. Vision-language models turn raw footage into searchable, structured datasets and edge-case libraries. Customers: Zoox, Mitsubishi Electric Automotive America, Zendar.
- Why they matter: Named in the brief for good reason — they are the category reference. Jeff Dean on the cap table is a serious signal on the technical credibility side. $8.4M seed at $50M post-money is aggressive, suggests investor conviction. Zoox as a customer means they have cleared enterprise AV data security requirements. Threat level: **very high** — they own the wedge framing and have AV-grade customers. A differentiation on robot-specific data sovereignty or EU residency requirements is the only clear path around them.

**Encord**
- URL: [encord.com](https://encord.com)
- Stage: Series B — $60M (2025)
- Wedge overlap: Wedge 6 (adjacent — physical AI data curation and annotation at scale)
- Product: Unified platform for ingesting, curating, and annotating multimodal physical AI datasets including synchronized video and 3D sensor data. Robotics customers include Woven by Toyota, Zipline, Skydio. Revenue from physical AI customers 10x'd in 2025.
- Why they matter: Better-capitalized than Nomadic, with a broader annotation + curation stack. The 10x physical AI revenue growth says they are not a data-labeling legacy tool — they are actively pivoting into the robotics training-data stack. Threat level: **high** for any data-curation or search-over-fleet play. They have capital, customers, and momentum.

**Voxel51**
- URL: [voxel51.com](https://voxel51.com)
- Stage: Series B — $30M
- Wedge overlap: Wedge 6 (adjacent — visual AI data curation, FiftyOne open-source tool)
- Product: Open-source (FiftyOne) + enterprise visual AI dataset curation and model evaluation platform. Used by automotive, robotics, industrial automation, healthcare. NVIDIA Physical AI Data Factory blueprint partner.
- Why they matter: FiftyOne has massive developer adoption as open-source. NVIDIA partnership positions them as infrastructure for the Physical AI data factory pattern. Threat level: **medium** — strong developer moat but less robotics-sovereign than Nomadic's fleet-specific positioning.

---

## Synthesis

**Most crowded wedge: Wedge 3 (fleet observability / "Datadog for robots")**
Four funded companies — Foxglove ($58M total, Bessemer-backed), InOrbit ($12.8M, open-sourcing), Formant ($45M), and Ember (YC W25 seed) — are all competing on multi-vendor fleet monitoring and telemetry. Foxglove has pulled ahead with the $40M Series B and enterprise logos. The wedge is not won, but it is the most capitalized and most crowded of the six. New entry is a bad bet without a specific vertical or data-type angle Foxglove ignores.

**Second most crowded: Wedge 6 (data curation / fleet video search)**
Nomadic ($8.4M seed, $50M post-money, Zoox customer) owns the brand but Encord ($60M Series B, 10x physical AI revenue growth) is the bigger threat. Voxel51 ($30M) adds NVIDIA-backed infrastructure depth. Three real competitors with growing capital. A new entrant needs a sovereignty or compliance angle (EU data residency, on-prem fleet data) that none of them are leading with yet.

**Medium crowded: Wedge 2 (compliance workflow)**
Saphira AI (YC S24) is the purpose-built robotics compliance startup and has the right framing and early customer. Vanta is circling from the generic AI Act direction but lacks machinery-regulation depth. The wedge is not won — Saphira is still pre-Series A and has not addressed the EU AI Act / Machinery Regulation Annex XI intersection explicitly. There is a 12–18 month window before either Saphira raises enough to dominate or Vanta acquires depth.

**Least crowded: Wedge 4 (RaaS billing / metering / revenue recognition)**
No funded startup with a clean wedge here. Hardfin is writing about the problem but has no known raise. This is a red flag to investigate: either the pain is not acute enough to support a standalone company (CFOs at RaaS operators may just bolt on Stripe Billing + NetSuite workarounds) or the market is genuinely pre-competitive and represents an opening. The $16B → $157B RaaS market projection suggests the accounting complexity will compound — the question is whether it becomes a feature of a broader robotics ERP or a standalone wedge.

**Credible startup that may have already won: Foxglove (Wedge 3).** With $58M raised, Bessemer conviction, and Amazon/Anduril/NVIDIA as customers, Foxglove is pulling away from the pack in fleet data observability. Unless you bring a manufacturing-specific or EU-sovereign angle, competing head-on with Foxglove in 2026 is unlikely to produce a fundable narrative.

**Wedge with largest gap and most interesting red flag: Wedge 5 (VLA model benchmarks / policy evaluation SaaS).** Physical Intelligence has raised $1B+ and is shipping production VLA models into enterprise deployments, yet no one has built the evaluation and benchmark-tracking layer above it. This could mean (a) the market is genuinely early and the tooling moment hasn't arrived, or (b) model vendors will internalize evaluation and kill the independent SaaS. Worth a quick founder conversation with a Physical Intelligence customer to validate whether this pain is real before treating the absence of competition as an invitation.
