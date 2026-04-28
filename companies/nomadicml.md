# NomadicML
**Vertical:** Physical AI / Autonomous Data Infrastructure | **URL:** https://www.nomadicai.com (formerly nomadicml.com) | **HQ:** San Francisco, CA | **Founded:** ~2023 | **Stage/Funding:** Seed — $8.4M (March 2026), post-money valuation $50M; led by TQ Ventures, with Pear VC and angels including Jeff Dean (Google), OpenAI and DeepMind executives

## Product
NomadicML (rebranding to Nomadic AI) sells a semantic video understanding platform for autonomous vehicle and robotics teams. It ingests raw camera footage from fleets or robots, runs vision-language models over it, and outputs structured, searchable datasets — surfacing edge cases, auto-labeling events, and curating training data for downstream model iteration. The core interface is described as an "agentic reasoning system": engineers describe what they need to find and the platform orchestrates multiple large models to locate and contextualize it across terabytes of footage.

## ICP
Autonomous vehicle companies, robotics OEMs, and autonomous-fleet operators that generate large volumes of sensor video and need to convert it into labeled training data. Known early customers include Mitsubishi Electric (industrial robotics), Natix Network (edge camera networks), and Zendar (radar-based AV sensing). Geography appears US-first; deal structure not publicly disclosed.

## Traction
Three named enterprise customers publicly referenced at seed stage (March 2026). Won first prize at Nvidia GTC pitch contest (March 2026). Team of ~12 engineers. No ARR or deployment scale figures published.

## Tech moat
Combination of physics-aware analysis tools (lane-change detection, gripper-positioning extraction from video) and multi-model orchestration built specifically for autonomous-systems data volumes. Early member of the Autoware Foundation, giving pipeline influence over open-source AV tooling. Moat is thin at this stage — vision-language model capability is rapidly commoditizing and incumbent data-labeling players (Scale AI) could extend into semantic search.

## Distribution model
Direct enterprise sales to AV and robotics engineering teams. No channel or OEM partnership disclosed. Integration with Autoware ecosystem may serve as a developer-led bottom-up wedge inside AV teams.

## Critical weakness
The platform sits between foundation model providers (who are rapidly building native video-understanding APIs) and end-customers, with no proprietary training data of its own. If OpenAI, Google, or AWS embed semantic video search into their existing MLOps offerings, the standalone value proposition collapses. Dependency on customer willingness to share raw footage also creates a data-custody friction at enterprise procurement.

## Adjacent gap
NomadicML targets well-funded AV and large-robotics teams with existing ML infrastructure. The underserved wedge is **smaller robotics-as-a-service operators** (last-mile delivery, warehouse automation SMBs) that generate substantial video but lack ML teams to operationalize it — a segment in Europe and Southeast Asia where no dominant physical-AI data platform has established a beachhead. A lighter, lower-cost, near-turnkey version of the same semantic curation layer, sold on a per-robot per-month basis rather than enterprise contract, could capture this cohort before Nomadic or Scale AI reaches them.

## Sources
- https://techcrunch.com/2026/03/31/nomadic-raises-8-4-million-to-wrangle-the-data-pouring-off-avs/
- https://www.cxodigitalpulse.com/nomadicml-raises-8-4m-seed-round-to-transform-autonomous-data-analysis/
- https://siliconangle.com/2026/03/31/nomadic-making-video-data-searchable-ai-model-training-raising-8-4m-funding/
- https://autoware.org/nomadicml/
- https://docs.nomadicml.com/getting-started/introduction
- https://www.nomadicai.com/
