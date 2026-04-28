# RealMan Robotics
**Vertical:** Picks-and-shovels | **URL:** https://www.realman-robotics.com | **HQ:** Beijing, China (factory in Jiangsu; office in Shenzhen) | **Founded:** 2010 (R&D start); incorporated ~2018 | **Stage/Funding:** Series B; investors include Yunqi Partners, ECOVACS, Yuan Angel, Yuanke Venture Capital, Changjiang Venture Capital

## Product
RealMan sells ultra-lightweight 7-DOF robotic arms (RM, RML, ECO, GEN series; 2–5 kg payload, 600–900 mm reach) plus integrated joint actuators (WHJ series: up to 360 Nm torque, 88 mm diameter, 18-bit dual encoders, harmonic reducer). They also sell compound/dual-arm platforms, a wheel-foldable humanoid (RealBOT), and — as of 2025 — a teleop-plus-data pipeline: their Beijing Humanoid Robot Data Training Center offers 108 embodied robot bodies across 10 real-world scenes, producing imitation-learning datasets (RealSource, open-sourced) and a Global Labor Network (GLN) teleoperation platform. All four core components (controller, driver, servo motor, harmonic reducer) are developed in-house. Annual production capacity exceeds 100,000 joint modules.

## ICP
Research labs, universities (30+ partnerships cited), and enterprise automation buyers in industrial, 3C manufacturing, food service, healthcare, and commercial services. Core geography is China; active trade-show presence in the US (CES 2025, CES 2026, Automate 2025) and Europe (Automatica 2025) signals international sales push. Deal size not disclosed; >4,000 enterprise customers claimed with 20,000+ arms deployed.

## Traction
20,000+ robotic arms deployed and >4,000 enterprise customers (company-stated, CES 2026 press release, January 2026). 100,000+ joint modules annual production capacity. No revenue figures publicly disclosed. Series B stage implies post-product-market-fit but pre-profitability; exact raise size not public.

## Tech moat
In-house vertical integration across the full actuator stack (controller, driver, motor, harmonic reducer) plus 124+ patents is the primary moat — it compresses cost and lets them iterate faster than assemblers. The open-sourced RealSource dataset and GLN teleop platform are a secondary bet: network-effect moat if enough third-party labs train on their hardware. MTBF of 50,000 hours is a credible reliability claim. Moat is moderate; Chinese peers (Unitree, JAKA) compete on similar vertical-integration logic.

## Distribution model
Direct sales to enterprise and research customers, supplemented by trade-show lead generation (CES, Automate, Automatica). Developer ecosystem via open-source dataset (RealSource on GitHub) to seed research adoption. No formal channel or reseller network publicly documented. International motion appears direct/self-managed for now.

## Critical weakness
Geographic concentration and export risk: the bulk of revenue is China-domestic at a time when US/EU export controls on Chinese robotics hardware are tightening. Their teleop GLN platform — which routes real-time control data cross-border (Beijing to Las Vegas demo at CES 2026) — is directly exposed to data-sovereignty and national-security scrutiny in Western markets. If export restrictions tighten further, their international expansion stalls and Western OEM partnerships become untenable.

## Adjacent gap
The GLN teleoperation + data-collection infrastructure is genuinely novel but is being built for and by a Chinese entity, which forecloses serious adoption by US/EU defense-adjacent manufacturers, regulated healthcare buyers, and any customer with data-residency requirements. A credible wedge: a Western-domiciled picks-and-shovels company offering sovereign teleop-and-training infrastructure — on-prem or cloud with US/EU data residency — targeting North American and European robot-deploying manufacturers who need imitation-learning datasets but cannot use Chinese-controlled platforms. The ICP is contract manufacturers, automotive Tier-1s, and medtech OEMs building embodied AI workflows; the wedge is compliance-friendly data collection and teleoperation tooling that RealMan structurally cannot sell into those accounts.

## Sources
- https://www.realman-robotics.com
- https://www.roboticstomorrow.com/news/2026/01/07/realman-robotics-showcases-embodied-intelligence-infrastructure-at-ces-2026/25980/
- https://www.cbinsights.com/company/realman-robot
- https://www.therobotreport.com/realman-robotics-open-sources-realsource-robot-dataset/
- https://www.roboticstomorrow.com/news/2025/01/08/realman-robotics-showcases-game-changing-ultra-lightweight-humanoid-robotics-solutions-at-ces-2025/23824
- https://develop.realman-robotics.com/en/joints/summarize/
