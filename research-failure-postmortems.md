# Robotics Company Failure Post-Mortems
**Written:** 2026-04-28
**Scope:** 6 cases + cross-cutting synthesis for software-first teams
**Sources:** SEC filings, TechCrunch, MDDIOnline, Bloomberg, CNBC

---

## 1. Berkshire Grey — The SPAC Valuation Trap

### What they did
Berkshire Grey built AI-powered warehouse automation: pick-and-place robots for retail fulfilment, sort systems for e-commerce. Founded 2013, went public via SPAC in mid-2021 at a $2.2B valuation. SoftBank was already a major investor pre-SPAC. By March 2023, SoftBank acquired all remaining shares at $1.40/share — a valuation of roughly $375M, a 90%+ drop from the SPAC peak — and took the company private. ([Robotics 24/7](https://www.robotics247.com/article/berkshire_grey_merging_with_softbank_group_will_go_private))

### Failure mode: capital structure + public-market mismatch
Not a technology failure. The underlying order backlog hit $265M and kept growing through the take-private. The company could not convert backlog to revenue fast enough: hardware integration timelines ran 12–18 months per deployment, so bookings lagged revenue lagged cash by up to two years. BGRY burned $25–30M adjusted EBITDA per quarter. For a public company in 2022's rate environment, that burn rate required a narrative of near-term profitability that the deployment cadence could never support. Revenue grew 29% in 2022 to $65.9M against a $153M net loss. Nasdaq threatened delisting. ([Global Venturing](https://globalventuring.com/corporate/deal-round-up/big-deal-berkshire-grey-softbank/), [Seeking Alpha](https://seekingalpha.com/article/4559948-berkshire-grey-growth-stock-but-risky))

### Decisions that look wrong in hindsight
1. **Going public via SPAC at peak hardware-robotics euphoria.** The $2.2B valuation priced in a scaling curve the company's deployment physics could not match. Public markets have no patience for 18-month hardware integration cycles.
2. **Enterprise-only GTM.** Every contract required multi-quarter procurement, custom integration, and an internal robotics team at the customer. No mid-market wedge, no product-led growth, no replicable unit.
3. **Treating backlog as a public-market story.** Backlog at $265M with $65M revenue means the market was right to discount it — none of that backlog was bankable.

### Lesson for a software-first team
If your revenue is gated by a physical installation or hardware delivery cycle, you cannot be in a public-market valuation mode. Software wedges that attach to already-installed hardware (observability, billing, compliance) decouple revenue from hardware timelines. The SPAC window for robotics is closed. Build for private cashflow discipline.

---

## 2. Vicarious Surgical — The Infinite Runway Illusion

### What they did
Vicarious Surgical built a miniaturised laparoscopic surgical robot using VR telepresence, targeting general and bariatric surgery. Khosla Ventures, Innovation Endeavors, and other A-list investors put in ~$220M. The company went public via SPAC in 2021 at a $1.1B valuation. As of April 2026, the company has never sold a commercial unit, is fighting NYSE delisting, and has enough cash to survive into 2026 only after deep cost cuts. ([MDDIOnline](https://www.mddionline.com/robotics/vicarious-remains-in-a-precarious-situation))

### Failure mode: regulatory timeline × capital structure
Surgical robotics has a mandatory multi-year regulatory gauntlet. Vicarious initially targeted 510(k) clearance, then switched to de novo — adding 12–18 months. Chip shortages delayed hardware. Each development delay consumed capital without any commercial offset. The company layered a SPAC capital structure (public shareholders, quarterly reporting, no tolerance for open-ended timelines) on top of a product that structurally cannot generate revenue until FDA clearance. As of early 2026, human trials have not yet begun and FDA submission is pushed to mid-2026 at the earliest. ([FierceBiotech](https://www.fiercebiotech.com/medtech/vicarious-lays-swath-rd-workers-delays-timeline-surgical-robot-development), [MDDIOnline](https://www.mddionline.com/robotics/vicarious-struggles-for-victory-in-a-post-spac-pre-commercial-phase))

### Decisions that look wrong in hindsight
1. **Going public before first commercial unit.** $220M in private capital should have been enough to reach clearance; instead it funded nine years of R&D against a $0 revenue line, with no commercial proof to buffer timeline slippage.
2. **Switching regulatory pathway mid-flight.** De novo is the right call technically but resetting the clock with public shareholders is near-impossible to survive.
3. **No revenue bridge.** Intuitive built training revenue, service contracts, and instrument consumables before its robot was dominant. Vicarious had nothing: no services, no data licensing, no interim revenue.

### Lesson for a software-first team
Any market that requires regulatory clearance before first dollar of revenue is a near-death gauntlet for a startup. The gap analysis's own note — "Distalmotion took 13 years and $400M to reach 3,000 procedures" — is not a competitive moat; it is a warning about the category's capital physics. Software wedges in this space (compliance tooling, evaluation SaaS, observability) all generate revenue before any regulatory event.

---

## 3. Canvas — RaaS Without a Balance Sheet

### What they did
Canvas (founded 2017, Boston Dynamics/SRI/MIT alumni) built a collaborative drywall finishing robot: the 1200CX, which compressed a four-to-five day finishing job into two days. Raised ~$40M total (Menlo Ventures, Brick & Mortar). Business model: operator as subcontractor initially, then annual robot leases (a RaaS model). In January 2026, JLG (Oshkosh subsidiary) acquired the core technology — not the company — in what the industry called an asset sale, not an exit. ([The Robot Report](https://www.therobotreport.com/oshkosh-acquires-core-technology-developed-by-canvas/), [ENR](https://www.enr.com/articles/62349-jlg-buys-san-francisco-drywall-robotics-automation-company-canvas))

### Failure mode: RaaS without financing infrastructure
Canvas's RaaS model required Canvas to own or finance the hardware, deploy it, maintain it, and wait for lease payments across a 12-month contract. Construction sites have irregular utilisation — robots sit idle between pours, between phases, between projects. The company was funding $100K+ per-robot hardware costs on a $40M total raise while the revenue from each unit dripped in over 12 months. The gap analysis noted this explicitly: "Canvas was killed precisely because they ran RaaS without the financing infrastructure." They had no residual-value underwriting, no third-party lender, no ABS structure. When deployment slowed — construction starts fell in 2023–2024 on rate hikes — the balance sheet cracked before revenue caught up. ([Robot Report Canvas Series B](https://www.therobotreport.com/canvas-24m-series-b-drywalling-robot/))

### Decisions that look wrong in hindsight
1. **Self-financing the hardware fleet.** RaaS is an embedded lending product. Every unit delivered is a loan to the customer. Canvas did not structure or fund it as one.
2. **Starting as a subcontractor.** This positioned Canvas as competition to its eventual customers (drywall contractors) rather than a vendor. The pivot to lease model happened late.
3. **Single-product, single-vertical concentration.** No adjacency to fall back on if construction volume dropped. It dropped.

### Lesson for a software-first team
RaaS is a fintech product wearing a hardware costume. A startup that ships RaaS without solving the financing layer first is handing hardware to customers on an unsecured vendor-financed basis. The RaaS billing wedge (Wedge 4 in the gap analysis) and the financing/leasing platform wedge (Wedge K) exist precisely because Canvas showed the cost of skipping that infrastructure. The lesson is that the software layer enabling RaaS economics — metering, billing, residual-value underwriting — is worth building before or instead of being the RaaS operator.

---

## 4. Nuro — The Operator Trap

### What they did
Nuro built purpose-built, goods-only autonomous delivery vehicles (R1, R2, R3) — no human occupants, hence NHTSA exemption pathway. Raised $1.5B+ (SoftBank, Google Ventures, Tiger Global). Deployed commercially with Kroger, Domino's, 7-Eleven. In May 2023, laid off 30% of staff (~340 people) and paused commercial expansion. In September 2024, announced a full pivot: ceased operating its own fleet, shifted to licensing "Nuro Driver" (Level 4 AV software) to automakers and mobility companies. In April–August 2025, raised $203M at a $6B valuation from Uber and NVIDIA to back the licensing model. ([TechCrunch pivot](https://techcrunch.com/2024/09/11/nuro-pivots-to-license-self-driving-tech-to-carmakers-mobility-companies/), [TechCrunch raise](https://techcrunch.com/2025/04/09/nuros-106m-raise-backs-its-shift-from-delivery-robots-to-licensing-autonomy-tech/))

### Failure mode: operator economics in a capital-intensive physical business
Nuro announced plans for a $40M custom test track and a 125,000 sq ft factory to build "tens of thousands of robots." That is an automotive manufacturer's cost structure applied to a startup with delivery-route revenue. Each R2/R3 unit cost hundreds of thousands of dollars to build and deploy; delivery fees per trip could not service the capex. Kroger and Domino's partnerships were marketing-scale pilots, not fleet-scale commercial contracts. The unit economics of operating a proprietary fleet against delivery-app economics never worked. The pivot to licensing is structurally correct — but required burning through most of the $1.5B to get there.

### Decisions that look wrong in hindsight
1. **Building a vertically integrated hardware-software-operations stack.** Nuro tried to be Tesla, Uber, and a delivery company simultaneously. Each layer added capital requirements without proportional revenue.
2. **Competing on delivery economics rather than autonomy tech.** Nuro's moat was always the L4 software stack, not the ability to deliver burritos 10% cheaper than DoorDash. The pivot validated this too late.
3. **Announcing factory-scale capex before unit economics were proven.** The $40M track and factory announcement signalled commitment to the operator model at exactly the moment the numbers were telling them to exit it.

### Lesson for a software-first team
The operator model in physical robotics is a capital trap. Every startup that positions itself as "the operator" (Nuro, Coco, Serve, Canvas) eventually either licenses the tech, sells to a strategic, or dies. Software wedges that sit above the operator layer — the billing platform, the observability stack, the insurance layer — capture value without needing to own the fleet.

---

## 5. iRobot/Picea — The Single-Product Consumer Trap

### What they did
iRobot invented the consumer robot vacuum category with the Roomba (2002), eventually reaching ~$1.4B in annual revenue. Amazon announced a $1.7B acquisition in 2022. European regulators blocked the deal in January 2024, citing Amazon's ability to disadvantage competing vacuums on its marketplace. Post-block: iRobot laid off 350 staff (~one-third), burned through cash fighting Chinese competition, saw US market share fall below 10% as Roborock, Ecovacs, Dreame, and Xiaomi took >50% combined share. Trump-era tariffs (up to 46% on Vietnam manufacturing) hit iRobot's cost structure while its Chinese rivals manufactured domestically. Filed Chapter 11 in December 2025; Picea Robotics (its Chinese contract manufacturer and largest lender) converted $254M in claims to equity. Delisted and taken private January 2026. ([TechCrunch](https://techcrunch.com/2025/12/14/how-irobot-lost-its-way-home/), [Manufacturing Dive](https://www.manufacturingdive.com/news/roomba-braava-maker-irobot-chapter-11-bankruptcy-acquisition-picea-china/807997/))

### Failure mode: hardware commoditisation + single-product dependency + strategic buyer dependency
iRobot's Roomba premium eroded as Chinese manufacturers shipped equivalent hardware at half the price. iRobot held brand equity but no structural software moat: no subscription, no data revenue, no platform lock-in. The Amazon deal was not a growth strategy — it was an exit from a deteriorating competitive position. When the deal died, iRobot had no fallback. The tariff regime that was supposed to protect US manufacturers instead punished iRobot's Vietnam manufacturing more than it hurt Chinese domestic production.

### Decisions that look wrong in hindsight
1. **Never building a durable software revenue layer.** 20+ years of Roomba deployments generated floor-plan data, usage patterns, and home-mapping data that could have become a recurring subscription or a platform. None of it was monetised.
2. **Allowing the supply chain to be controlled by a Chinese manufacturer (Picea) that became the largest lender.** When you let your contract manufacturer extend you credit, they own the company by the time the balance sheet cracks.
3. **Treating the Amazon acquisition as a product roadmap.** iRobot deferred innovation against the assumption the deal would close. It didn't, and they had two years of lost ground to make up with a shrinking cash balance.

### Lesson for a software-first team
Hardware categories commoditise. Even a category inventor with 20 years of head start can be zeroed out by manufacturing economics. Software attached to a hardware category — fleet management, data monetisation, compliance — retains margin even as hardware ASPs collapse. Any software wedge built on top of these robots (observability, privacy/sovereignty layer, insurance) benefits from the installed-base iRobot created, while being immune to the commoditisation that killed iRobot.

---

## 6. Trov — The B2C Insurance Unit Economics Wall

### What they did
Trov (founded 2012) built on-demand, per-item insurance via a mobile app. Cover a single item for a single day, toggled on/off from your phone. Backed by Munich Re, Suncorp, AXA, Sompo. Launched in Australia (2016), UK (2017), US (2018). Suspended the UK consumer app in 2019. Pivoted to B2B white-label platform in 2020. Acquired by Travelers Insurance in 2022, ceased operating independently. ([Wikipedia](https://en.wikipedia.org/wiki/Trov))

### Failure mode: CAC > CLV at every consumer price point
The unit economics of on-demand single-item cover are structurally broken for a direct-to-consumer startup. The cost to acquire a customer who wants to insure their iPhone for one afternoon exceeds the expected margin from that policy by an order of magnitude. Additionally, the product suffered from adverse selection — power users who activated cover only when they perceived risk drove loss ratios above projections. Most millennials were already covered by contents or renters' policies, removing the primary use case. Trov's own framing confirmed the issue: "high customer acquisition cost, the challenges of being a new entrant in a trust industry, and upside-down unit economics." ([Insurance Edge](https://insurance-edge.net/2019/06/25/gadget-specialist-trov-suspends-uk-on-demand-app-re-thinks-re-groups/))

### Decisions that look wrong in hindsight
1. **B2C direct as the first channel.** Insurance is a trust product. A startup selling micro-duration cover without an existing trust relationship faces CAC that no LTV can justify.
2. **Launching in three geographies simultaneously.** UK, AU, and US have different regulatory frameworks, carrier relationships, and consumer insurance literacy. Multi-market consumer launch before product-market fit is resource destruction.
3. **Not embedding into an existing purchase flow from day one.** Waymo, Free2Move, and car-sharing partnerships (which Trov eventually pursued) were the right channel — they embed the insurance into a moment of purchase. Consumer app was always second-best.

### Lesson for Wedge 1 — robot fleet underwriting
The robot fleet insurance wedge must not be B2C. Trov's failure is a precise template for what happens when you try to acquire insurance customers directly in a trust-deficit category. The correct model is embedded: sell the underwriting platform to an existing broker (Marsh, Aon, Lockton) or embed it into a RaaS contract as a vendor-side bundle. The MGA-first path the gap analysis recommends only works if distribution is through trusted intermediaries, not direct-to-fleet-operator cold outbound.

---

## 7. Argo AI — The "Near Enough" Technology Trap

### What they did
Argo AI (founded 2016) built Level 4 autonomous driving software for Ford and Volkswagen, with $3.6B invested between the two OEMs. Deployed test fleets in nine cities. Shut down in October 2022. Ford recorded a $2.7B non-cash impairment. ~2,000 employees absorbed by Ford, Volkswagen, and other AV companies. ([TechCrunch](https://techcrunch.com/2022/10/26/ford-vw-backed-argo-ai-is-shutting-down/), [CNBC](https://www.cnbc.com/2023/03/22/how-ford-and-vws-multibillion-dollar-self-driving-car-project-failed.html))

### Failure mode: technology horizon mismatch + single-customer concentration
Argo's technology was genuinely impressive — L4 in geofenced cities. The failure was not technical, it was commercial: profitable, full-scale autonomous vehicles were "a long way off," per Ford's CFO. Ford and VW needed near-term ADAS products (L2/L3) to compete with Tesla, not a 5+ year bet on L4 robotaxis that required "billions more." When both OEM sponsors simultaneously decided the timeline was too long and pivoted to L2/L3, Argo had no other customers, no independent revenue, and no consumer-addressable product. $3.6B in capital with zero commercial contracts at closure.

### Decisions that look wrong in hindsight
1. **Two-customer concentration.** Ford and VW were not customers — they were co-owners and sponsors. There was no independent commercial revenue to fall back on when sponsor priorities shifted.
2. **Optimising for L4 at the expense of near-term L2/L3 monetisation.** Mobileye, which did the opposite, went public at $17B in 2022 — the same year Argo shut down.
3. **No software licensing model alongside hardware deployment.** If Argo's software had been licensable to other OEMs or integrators, the company could have survived Ford and VW's exit.

### Lesson for a software-first team
Software companies must have multiple customers. A "two-sponsor" dependency is a liquidation waiting for a sponsor re-prioritisation event. Any robotics software product that relies on a single OEM's continued enthusiasm — proprietary observability built only for one hardware vendor, eval SaaS gated to one OEM's models — replicates Argo's structural fragility. Multi-vendor from day one is a survival requirement, not an aspiration.

---

## Cross-Cutting Synthesis

Seven cases. Four recurring patterns that kill robotics startups. Each pattern maps directly onto the top-5 software wedges.

### Pattern 1: Hardware physics defeat software-company economics
Berkshire Grey, Canvas, and Nuro all collapsed under the weight of hardware deployment timelines. Revenue recognition required a physical installation. Capital burned while backlog accumulated. This is the foundational argument for software-only wedges: they decouple revenue from hardware timelines entirely. A compliance SaaS (Wedge 2) signs a contract and starts billing within days of closing. A fleet observability product (Wedge 3) bills on API calls. Neither waits 18 months for a warehouse to be retrofitted.

**Wedge most at risk:** Wedge K (financing/leasing platform). If the team becomes the lender — originating loans against hardware — they are Canvas. The safe version is origination-and-servicing software that passes paper to a third-party balance sheet, not a startup that owns the receivables.

### Pattern 2: RaaS without financial infrastructure is vendor-financing without a bank
Canvas is the clearest case but the pattern recurs in Nuro (fleet operator without fleet economics) and iRobot (supply chain financed by the contract manufacturer). Running RaaS means owning hardware on a startup balance sheet while revenue accretes over months. Without residual-value underwriting, third-party lending rails, or securitisation, the startup is an undercapitalised hardware leasing company.

**Wedge most at risk:** Wedge O (RaaS billing). This wedge is safe as long as it is purely metering, reconciliation, and revenue-recognition software — the product generates no receivables. The risk emerges if the team is tempted to add embedded lending (a natural extension) before the balance-sheet infrastructure is in place. Build the meter first. Leave the loan book for Series B.

### Pattern 3: Regulatory and timeline dependency without a revenue bridge
Vicarious Surgical is the cleanest case. Nine years, $220M, zero revenue, because the product cannot be sold until regulatory clearance. iRobot's failure is a milder version: 20 years of hardware revenue with no software revenue bridge, so when hardware commoditised there was nothing to fall back on.

**Wedge most at risk:** Wedge 2 (Vanta for robots — EU AI Act compliance). The risk here is not that the team cannot get revenue. It is the inverse: customers only need the compliance workflow once the regulation is in force, and EU AI Act enforcement is on a 2025–2027 phased timeline. If the Machinery Regulation slips (Brussels has form), the TAM opens later. Mitigant: the gap analysis already identifies notified-body partnerships as the distribution channel — they pull the product into deals regardless of enforcement timing, because OEMs need to prepare before the deadline.

### Pattern 4: Capital structure mismatch — public (or SPAC) timelines on hardware-physics companies
Berkshire Grey, Vicarious Surgical, and iRobot all faced public-market pressure on timelines that hardware physics cannot compress. SPAC structures forced quarterly progress narratives on businesses whose deployment cycles run in years. This is not a problem for a software-first team building in 2026 — the SPAC window for robotics is closed and none of the top-5 wedges are public-market candidates in year one. The lesson is more subtle: any investor narrative that prices in "we will be profitable in Q6" on a hardware-deployment-gated revenue model will destroy the company when Q6 arrives with a shorter backlog.

**Wedge most at risk:** Wedge 1 (robot fleet underwriting). Insurance MGA economics require reinsurer backing within 18 months or the economics collapse — as the gap analysis itself notes. If reinsurer commitment slips, the timeline pressure on the MGA mimics the SPAC trap: obligations to current coverage commitments with no capacity to underwrite new ones. The pure data/risk-scoring SaaS path (sell scoring to existing insurers before standing up the MGA) explicitly hedges this risk and should be the first 12 months of the product regardless.

### Summary table

| Failure pattern | Primary case | Wedge most at risk | Risk mitigation |
|---|---|---|---|
| Hardware physics defeat software economics | Berkshire Grey, Canvas | Wedge K (financing rails) | Stay origination-software only; no owned receivables |
| RaaS without financial infra | Canvas, Nuro | Wedge O (RaaS billing) | Build the meter; defer embedded lending to Series B |
| Regulatory timeline with no revenue bridge | Vicarious Surgical | Wedge 2 (Vanta for robots) | Notified-body channel creates demand ahead of enforcement |
| SPAC/public capital structure on hardware timelines | Berkshire Grey, Vicarious | Wedge 1 (insurance MGA) | Start as risk-scoring SaaS; earn reinsurer trust before MGA |
| B2C direct in trust-deficit category | Trov | Wedge 1 (insurance) | Broker-embedded or SI-embedded only; no cold direct-to-fleet |
| Two-sponsor concentration | Argo AI | Wedge 5 (eval SaaS) | Multi-OEM from day one; open leaderboard as forcing function |
| Single-product hardware commoditisation | iRobot | All hardware-adjacent | Attach to installed base; never own the hardware |

The thread across the keep list from the gap analysis is the mirror image of these failure modes: software that attaches to already-installed hardware, sold through trusted intermediaries (SIs, brokers, notified bodies), with multi-vendor contracts from day one, and revenue that accretes from first week of deployment rather than after 18 months of integration. Every top-5 wedge passes that test. The traps above are the specific ways each one could fail if the team drifts toward the hardware-operator model they are designed to avoid.

---

*Sources consulted: [Robotics 24/7 BG take-private](https://www.robotics247.com/article/berkshire_grey_merging_with_softbank_group_will_go_private) — [Global Venturing BG losses](https://globalventuring.com/corporate/deal-round-up/big-deal-berkshire-grey-softbank/) — [MDDIOnline Vicarious cash](https://www.mddionline.com/robotics/vicarious-remains-in-a-precarious-situation) — [FierceBiotech Vicarious delays](https://www.fiercebiotech.com/medtech/vicarious-lays-swath-rd-workers-delays-timeline-surgical-robot-development) — [Robot Report Canvas JLG](https://www.therobotreport.com/oshkosh-acquires-core-technology-developed-by-canvas/) — [TechCrunch Nuro pivot](https://techcrunch.com/2024/09/11/nuro-pivots-to-license-self-driving-tech-to-carmakers-mobility-companies/) — [TechCrunch Nuro raise](https://techcrunch.com/2025/04/09/nuros-106m-raise-backs-its-shift-from-delivery-robots-to-licensing-autonomy-tech/) — [TechCrunch iRobot](https://techcrunch.com/2025/12/14/how-irobot-lost-its-way-home/) — [Manufacturing Dive iRobot](https://www.manufacturingdive.com/news/roomba-braava-maker-irobot-chapter-11-bankruptcy-acquisition-picea-china/807997/) — [Insurance Edge Trov](https://insurance-edge.net/2019/06/25/gadget-specialist-trov-suspends-uk-on-demand-app-re-thinks-re-groups/) — [TechCrunch Argo shutdown](https://techcrunch.com/2022/10/26/ford-vw-backed-argo-ai-is-shutting-down/) — [CNBC Argo analysis](https://www.cnbc.com/2023/03/22/how-ford-and-vws-multibillion-dollar-self-driving-car-project-failed.html)*
