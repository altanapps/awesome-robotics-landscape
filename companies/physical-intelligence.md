# Physical Intelligence (π)
**Vertical:** Foundation models for robotics | **URL:** https://www.pi.website | **HQ:** San Francisco, CA | **Founded:** 2023 | **Stage/Funding:** Series B — $1.1B total raised (~$5.6B valuation, Nov 2025); investors include CapitalG, Sequoia, Lux Capital, Redpoint, NVIDIA Ventures, Jeff Bezos, Khosla Ventures

## Product
Physical Intelligence sells foundation models for robot control — general-purpose vision-language-action (VLA) models that can be fine-tuned to operate across robot embodiments and manipulation tasks. Their flagship model line (π0, π0.5, π0 FAST, π0.7) is trained on 10,000+ hours of real-world robot data spanning seven embodiments and 68 tasks. The commercial offering is a B2B subscription (~$300/month/connected robot) with optional on-premises licensing for latency-sensitive deployments. π0 weights are also open-sourced to drive ecosystem adoption.

## ICP
Robotics OEMs and manufacturers integrating AI-driven manipulation into their hardware stacks; industrial automation integrators deploying multi-robot fleets; research institutions fine-tuning on specific tasks. Primary geography is the US, with partnerships being built with humanoid platform makers (e.g., Agility, Apptronik). Deal size scales with fleet size under a per-robot subscription model.

## Traction
No public revenue figures disclosed. Total funding of $1.1B at ~$5.6B valuation (Nov 2025) implies strong investor conviction but pre-commercial scale. π0 open-source release on GitHub has meaningful developer adoption. Demonstrations span unstructured household environments (laundry, kitchen cleaning, bed-making) but these remain research results, not confirmed production deployments. Named enterprise customers not publicly disclosed as of April 2026.

## Tech moat
Proprietary training data (10,000+ hours across seven embodiments) accumulated through teleoperation pipelines is the primary moat — hard to replicate quickly. The flow-matching action architecture (π0 FAST) offers a 5x training speed advantage over diffusion-based competitors. Open-sourcing π0 creates an ecosystem flywheel: community fine-tunes feed back data and credibility. Research team pedigree (ex-Google, Berkeley, CMU) adds talent density. Moat is real but contested — BigTech (Google DeepMind RT-2 lineage) and well-funded peers (Figure, 1X) are on parallel tracks.

## Distribution model
Primarily direct B2B to robotics manufacturers and integrators, supplemented by an open-source developer channel (π0 weights on GitHub) that widens top-of-funnel. OEM licensing to humanoid platform makers is an emerging motion. No marketplace or RaaS layer currently visible.

## Critical weakness
Hardware-agnostic positioning requires constant re-adaptation engineering as new robot embodiments ship — a treadmill that raises costs without compounding advantage. More acutely: vertical-integration competitors (Tesla Optimus, Figure AI) bundle proprietary hardware + software, making the standalone model layer potentially commoditizable. If BigTech (Google, Meta) releases capable open-weight VLA models at zero marginal cost, Physical Intelligence's pricing power collapses before it achieves fleet-scale revenue.

## Adjacent gap
Physical Intelligence is focused on unstructured manipulation in Western markets with high-cost robot platforms. The credible wedge: **low-cost fixed-arm industrial SME deployments in Southeast Asia and Southern Europe** — factories too small for $100K+ humanoid integrations, needing a narrow manipulation model (pick-and-place, QC inspection) fine-tuned on minimal data and priced at a fraction of PI's per-robot subscription. PI's open-source π0 makes this technically accessible; the gap is a go-to-market and vertical focus that PI has explicitly not pursued.

## Sources
- https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/
- https://www.therobotreport.com/physical-intelligence-open-sources-pi0-robotics-foundation-model/
- https://techcrunch.com/2026/04/16/physical-intelligence-a-hot-robotics-startup-says-its-new-robot-brain-can-figure-out-tasks-it-was-never-taught/
- https://www.humanoidsdaily.com/news/physical-intelligence-unveils-0-7-the-rise-of-compositional-generalization-in-robotics
- https://sacra.com/c/physical-intelligence/
- https://eutechfuture.com/artificial-intelligence/physical-intelligence-building-foundation-models-for-robots-to-interact-with-the-real-world/
- https://github.com/Physical-Intelligence/openpi
- https://www.pi.website/
