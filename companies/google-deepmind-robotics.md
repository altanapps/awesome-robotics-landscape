# Google DeepMind Robotics
**Vertical:** Foundation models for robotics | **URL:** https://deepmind.google/models/gemini-robotics/ | **HQ:** London, UK / Mountain View, CA | **Founded:** DeepMind est. 2010, Gemini Robotics launched March 2025 | **Stage/Funding:** Internal Google DeepMind division (Alphabet-backed; no separate raise)

## Product
Gemini Robotics is a suite of foundation models that give physical robots the ability to perceive, reason, and act. The core offering is two complementary models: **Gemini Robotics 1.5**, a vision-language-action (VLA) model that converts visual inputs and natural-language instructions into motor commands, and **Gemini Robotics-ER 1.6**, an embodied-reasoning model that plans multi-step tasks, calls external tools (e.g. Google Search), and generates human-readable reasoning chains before acting. A third variant, **Gemini Robotics On-Device**, runs locally on robotic hardware and supports developer fine-tuning. Access is via the Gemini API / Google AI Studio (ER model) or a gated trusted-tester program (VLA model); an SDK with waitlist signup is available.

## ICP
Primary users are robotics OEMs and physical-AI startups that need a capable general-purpose brain without training from scratch. Named hardware partners include Apptronik (Apollo humanoid, logistics), Agility Robotics, Boston Dynamics (Atlas), Agile Robots (2026 partnership), and Enchanted Tools. Research institutions with existing robotic platforms (ALOHA 2, Franka) are also in the tester program. The 60+ trusted-tester cohort is the current go-to-market surface.

## Traction
60+ trusted testers as of early 2026 (Google DeepMind, 2026). Gemini Robotics-ER available publicly via Google AI Studio as of early 2026. VLA model remains gated. Agile Robots partnership announced March 2026 (CNBC, 2026). No revenue or deployment unit figures disclosed.

## Tech moat
Strong: Gemini 2.0 multimodal backbone with massive pretraining scale that no pure-play robotics startup can replicate. Cross-embodiment transfer (single model runs on ALOHA 2, Apollo, Franka without re-specialization) is a meaningful technical differentiator. Weak: no proprietary robot hardware, no exclusive data flywheel from deployed units at scale, and the on-device model competes directly with open-weight alternatives.

## Distribution model
Gated API / waitlist for the VLA model; open API (Google AI Studio) for the ER model. Sales motion is a partner-first OEM channel — Google supplies the model layer, hardware partners supply embodiment and go-to-market. No direct end-customer sales reported.

## Critical weakness
The model is hardware-agnostic by design, which limits data flywheel formation: Google does not own the robots, so real-world deployment data accrues to the hardware partners, not DeepMind. Partners may eventually train proprietary models on that data and reduce dependency on Gemini Robotics. Additionally, Google's history of deprecating developer platforms introduces adoption risk for OEM customers committing to a multi-year hardware program.

## Adjacent gap
Hardware partners in the current program are all well-capitalized US/EU firms targeting logistics, manufacturing, or research. **SMB and mid-market industrial operators** — factories, warehouses, and last-mile facilities that cannot afford a Boston Dynamics or Apptronik integration — have no accessible path to Gemini Robotics today. A startup that wraps Gemini Robotics-ER (publicly available API) in a vertical-specific deployment layer — handling robot procurement, integration, and fine-tuning for a single industry such as food manufacturing or pharmaceutical kitting — could own that underserved segment before Google builds a channel for it.

## Sources
- https://deepmind.google/models/gemini-robotics/
- https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/
- https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/
- https://www.cnbc.com/2026/03/24/google-agile-robots-ai-robotics.html
- https://www.technologyreview.com/2025/03/12/1113178/gemini-robotics-uses-googles-top-language-model-to-make-robots-more-useful/
- https://arxiv.org/abs/2503.20020
