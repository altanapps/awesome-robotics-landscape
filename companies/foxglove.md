# Foxglove
**Vertical:** Picks-and-shovels | **URL:** https://foxglove.dev | **HQ:** San Francisco, CA | **Founded:** 2021 | **Stage/Funding:** Series B — $58.7M total ($40M Series B, Nov 2025, led by Bessemer Venture Partners; prior rounds from Eclipse and Amplify Partners)

## Product
Foxglove sells a multimodal data platform for robotics and autonomy teams. The core SKU is a cloud-hosted (or self-hosted) observability suite covering data recording and ingestion, time-series and sensor visualization (20+ panel types: point clouds, images, maps, logs), fleet log search, and dataset curation for model training. A companion open-source file format, MCAP, handles serialization-agnostic data storage. The platform is accessed via a web UI, CLI, or API; an Agent SDK handles on-robot logging and live streaming. Pricing is freemium: free tier (3 users, 10 GB), Pro at $20/month base plus per-seat/per-device overages, and custom Enterprise contracts.

## ICP
Robotics and autonomy engineering teams — primarily at Series A–D companies and large OEMs in automotive, defense and aerospace, logistics, manufacturing, agriculture, and consumer robotics. Named logos include NVIDIA, Amazon, Anduril, Wayve, Dexterity, Shield AI, and ANYbotics. Deal size ranges from self-serve Pro (sub-$500/month) to enterprise contracts (custom, likely $50K–$500K+ ARR for large fleets). Geography is US-heavy with growing international enterprise accounts.

## Traction
"Tens of thousands of developers" and "hundreds of customers" per company statements at Series B close (Nov 2025). No public revenue figure. Investor base and Series B size ($40M) suggest the company is post-product-market-fit with meaningful ARR but pre-profitability. Source: BusinessWire / The Robot Report, Nov 2025.

## Tech moat
MCAP format has meaningful ecosystem lock-in — it is open source but Foxglove controls the tooling and is the primary beneficiary of adoption. ROS/ROS2 integration is deep. The broader moat is thin: the visualization layer is replicable, cloud storage is commodity, and competitors (Rerun, ReductStore) are actively building equivalent feature sets. Network effects are weak; switching cost comes mainly from MCAP adoption and workflow integration, not data gravity.

## Distribution model
Open-source-to-paid. The MCAP format and Foxglove Studio (desktop/web viewer) act as free top-of-funnel; sales motion converts active teams to Pro or Enterprise. Forward-deployed engineers are included in Enterprise tier, suggesting a land-and-expand model with high-touch for large accounts.

## Critical weakness
The open-source studio can be self-hosted entirely, reducing paid conversion pressure. Competitors like Rerun are building faster, more developer-native alternatives with strong open-source communities. Foxglove's cloud offering competes directly with hyperscaler robotics data pipelines (AWS RoboMaker, NVIDIA Isaac) that larger customers may prefer for compliance or cost reasons. The free-to-paid conversion funnel is structurally leaky.

## Adjacent gap
Foxglove is optimized for English-language, US/EU-based, venture-backed robotics teams with ROS-fluent engineers. It does not meaningfully serve (1) Asian OEM manufacturers (Chinese, Korean, Japanese) building proprietary robot stacks outside the ROS ecosystem, where data formats differ and cloud data sovereignty requirements block US-hosted SaaS; or (2) small industrial/field robotics operators (construction, agriculture, utilities) who need lightweight on-premise observability without a DevOps team to run it. A wedge: a self-contained, edge-deployable observability appliance — hardware + software — targeting sub-50-person industrial robotics teams in regulated or air-gapped environments (utilities, mining, defense subcontractors) who cannot use cloud SaaS and lack the engineering bandwidth to self-host Foxglove.

## Sources
- https://www.businesswire.com/news/home/20251112126106/en/Foxglove-Raises-$40-Million-Series-B-to-Power-the-Future-of-Physical-AI
- https://www.therobotreport.com/foxglove-raises-40m-scale-data-platform-roboticists/
- https://venturebeat.com/business/foxglove-raises-40-million-series-b-to-power-the-future-of-physical-AI
- https://foxglove.dev/pricing
- https://foxglove.dev
- https://discourse.openrobotics.org/t/foxglove-2-0-integrated-ui-new-pricing-and-open-source-changes/36583
- https://www.reduct.store/blog/comparison-rviz-foxglove-rerun
