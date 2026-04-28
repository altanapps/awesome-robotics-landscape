# Scale AI (Robotics)
**Vertical:** Picks-and-shovels | **URL:** https://scale.com | **HQ:** San Francisco, CA | **Founded:** 2016 | **Stage/Funding:** Private; $29B+ valuation (June 2025); $14.3B strategic investment from Meta (49% non-voting stake)

## Product
Scale's robotics-specific offering centers on its **Physical AI Data Engine** — a platform for collecting, annotating, and curating multimodal training data for embodied AI systems. The flagship partnership product is the **UR AI Trainer**, co-developed with Universal Robots and launched at GTC 2026. It uses a leader-follower teleoperation setup on UR cobots to capture synchronized motion, force-feedback, and visual data directly on production hardware. The data pipeline runs on-device, targeting the gap between lab demonstrations and factory-floor deployment. Scale also operates a separate human-demonstration recording program (launched September 2025) that hires contractors globally to record POV task demonstrations for robotics AI startups.

## ICP
Primary customers are robotics AI developers and foundation-model labs needing large-scale, high-quality manipulation data — companies such as Toyota Research Institute, Kodiak Robotics, Embark, and Skydio. The UR AI Trainer channel reaches the ~100,000+ existing UR cobot deployments, targeting OEMs and enterprise manufacturers adding AI layers to existing cobots. Deals are enterprise/government in character; no public per-unit pricing, but Scale's broader contracts run in the millions of dollars.

## Traction
Scale's total revenue reached ~$2B in 2025 (up from $870M in 2024). Robotics-specific revenue is not broken out publicly. Named robotics customers include Toyota Research Institute, Kodiak Robotics, Embark, and Skydio (sources: Sacra, Bloomberg 2025). The UR AI Trainer was announced March 2026 with a planned industrial dataset release later in 2026.

## Tech moat
Proprietary data curation tooling (RLHF pipelines adapted for physical AI), integration depth with UR's hardware fleet (force + vision multimodal capture), and a growing proprietary dataset of factory-floor demonstrations collected in partnership with UR. Network effects are nascent: more UR customers using the trainer means a richer shared dataset. Brand and existing government/enterprise relationships lower sales friction for enterprise robotics deals.

## Distribution model
Primarily direct enterprise sales for bespoke data programs. The UR AI Trainer introduces an **OEM/embedded** channel: Scale software ships inside UR's product, reaching UR's installed base without a separate sales motion. Scale also runs a marketplace-style contractor network for demonstration collection, functioning as a managed-services layer.

## Critical weakness
Scale's robotics data pipeline is optimized for industrial cobots (UR's 6-DOF arm form factor) and structured manipulation tasks. Force-feedback + visual multimodal capture requires proprietary hardware integration, making the pipeline brittle outside the UR ecosystem. Small robotics startups — especially those outside the US and EU, or using non-UR hardware (Doosan, JAKA, Chinese OEMs) — have limited access. The contractor demonstration network also depends on remote, unverified environments, limiting data quality for safety-critical or fine-motor use cases.

## Adjacent gap
**Most important field.** Scale's UR partnership locks in one cobot OEM and one data modality (manipulation/imitation learning). The unserved wedge is **non-UR cobot manufacturers in Asia-Pacific** (JAKA, Doosan, Techman, Aubo) whose developer ecosystems need the same lab-to-factory data infrastructure but have no Scale integration, no local competitor at scale, and growing demand from Chinese/Korean/Taiwanese manufacturers adding AI layers post-2025 export restrictions. A credible startup could attack this by embedding a hardware-agnostic Physical AI data stack with local-language support and on-premise deployment (critical for Asian enterprise buyers) into those OEM channels — the same OEM-embedded motion Scale uses with UR, replicated for the non-Western cobot installed base.

## Sources
- https://scale.com/blog/scale-ai-universal-robots-physical-ai
- https://www.universal-robots.com/news-and-media/news-center/universal-robots-scale-ai-launch-imitation-learning-system-accelerate-ai-training-lab-to-factory/
- https://www.prnewswire.com/apac/news-releases/universal-robots-and-scale-ai-launch-imitation-learning-system-to-accelerate-ai-model-training-bridging-the-lab-to-factory-gap-302717348.html
- https://thenextweb.com/news/universal-robots-and-scale-ai-launch-the-ur-ai-trainer
- https://www.bloomberg.com/news/articles/2025-04-02/scale-ai-expects-to-more-than-double-sales-to-2-billion-in-2025
- https://sacra.com/c/scale-ai/
- https://roboticsandautomationnews.com/2026/03/17/universal-robots-and-scale-ai-launch-imitation-learning-system-for-training-industrial-robots/99752/
