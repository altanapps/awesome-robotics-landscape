# Robotics Ecosystem — Video Sources

*Scouted: 2026-04-28. Scope: YouTube channels, podcasts on YT, conference talks. 8-10 sources, 2025-2026 bias. Audience: software-first founders.*

---

## 1. The Robot Brains Podcast (Pieter Abbeel, host)

**Channel:** [The Robot Brains Podcast](https://www.youtube.com/c/TheRobotBrainsPodcast)

**Specific video:** [Season 1 Ep. 8 — Peter Chen on Building Brains for Robots in the Real World](https://www.youtube.com/watch?v=UfNftHnYAYk)

**Why it matters for a software-first founder:** Abbeel's framing throughout the show is that the intelligence layer — not the mechanical one — is the bottleneck; episodes consistently surface what training data regimes and sim-to-real gaps actually block deployment, which is exactly the gap a software wedge should target.

---

## 2. Physical Intelligence (pi.ai) — Sequoia Capital Talk

**Channel:** [Sequoia Capital on YouTube](https://www.youtube.com/watch?v=OJCT-HGxPjk) (uploaded January 2026)

**Specific video:** [Training General Robots for Any Task: Karol Hausman and Tobi Springenberg](https://www.youtube.com/watch?v=OJCT-HGxPjk)

**Why it matters:** Hausman's core claim is that robotics has been held back by an intelligence bottleneck, not a hardware one — a direct validation that the value layer is software and models, not actuators. He positions pi.ai as the "model provider" to hardware OEMs, exactly the platform wedge a software founder should study.

---

## 3. Figure AI / Brett Adcock — Shawn Ryan Show

**Channel:** [Shawn Ryan Show](https://www.youtube.com/@ShawnRyanShow)

**Specific video:** [Brett Adcock — Shawn Ryan's First Interview with a Robot | SRS #292](https://www.youtube.com/watch?v=99pOdGEGu6s) (March 2026)

**Why it matters:** Adcock describes Figure's BMW manufacturing line deployment (January 2025) as the unlock moment — not capability, but repeatability at scale. His emphasis is on software reliability and data flywheels from real deployments, not robot specs. The deployment → data → improvement loop is the moat he keeps returning to.

---

## 4. 1X Technologies / Bernt Bornich — World Model Talk

**Channel:** Multiple (Humanoids Daily / Bloomberg clips)

**Specific video:** [He's Building Robots That Will Live In Your Home | Bernt Bornich, Founder of 1X Technologies](https://www.youtube.com/watch?v=61hUFIMV-uY) (2025)

**Why it matters:** Bornich explicitly argues that 1X's world model — software that predicts consequences of robot actions before executing — is their differentiator, and that hardware is commoditizing. For a software founder, this is the signal that world-model infrastructure for robot fleets is an open problem worth attacking.

---

## 5. Chelsea Finn — AI Startup School Talk

**Channel:** [Y Combinator / AI Startup School](https://www.youtube.com/@ycombinator)

**Specific video:** [Chelsea Finn: Building Robots That Can Do Anything](https://www.youtube.com/watch?v=a8-QsBHoH94) (June 2025, San Francisco)

**Why it matters:** Finn's central argument is that broad, heterogeneous data — not more compute — is what enables generalization in robot policies; this directly implies that whoever aggregates and curates cross-robot, cross-environment training data owns the model quality ceiling. A data infrastructure play is live.

---

## 6. NVIDIA GTC 2025 — Jensen Huang Robotics Keynote

**Channel:** [NVIDIA](https://www.youtube.com/@nvidia)

**Specific video:** [GTC 2025 Keynote — Jensen Huang (Isaac GR00T N1 segment)](https://blogs.nvidia.com/blog/nvidia-keynote-at-gtc-2025-ai-news-live-updates/) — full keynote available on NVIDIA's YouTube channel

**Why it matters:** NVIDIA's announcement of Isaac GR00T N1 — an open, customizable foundation model for humanoid manipulation — signals that the model layer is being commoditized top-down by infrastructure players. A software founder's wedge must sit above the model layer (tooling, evaluation, fleet management, data pipelines) not inside it.

---

## 7. a16z Podcast — Big Ideas 2026: Physical AI and the Industrial Stack

**Channel:** [a16z](https://www.youtube.com/@a16z) / [Spotify](https://open.spotify.com/episode/0fi9o6w2n8xTH6tY8509ax) / [a16z.com](https://a16z.com/podcast/big-ideas-2026-physical-ai-and-the-industrial-stack/)

**Specific episode:** Big Ideas 2026: Physical AI and the Industrial Stack (December 2025, 22 min)

**Why it matters:** a16z partner Will Bitsky's line — "data, not compute, determines who wins" — is the sharpest investor framing of 2025-2026 for anyone building in physical AI. The episode also surfaces factory-first deployment principles and the concept of "physical observability" (real-time sensor data from industrial robots) as an unserved layer.

---

## 8. Conference on Robot Learning (CoRL) — YouTube Channel

**Channel:** [Conference on Robot Learning](https://www.youtube.com/c/ConferenceonRobotLearning)

**Specific video:** [CoRL 2024 Day 2 sessions including deployment and foundation model panels](https://www.youtube.com/watch?v=5VXUoytToAM) — CoRL 2025 (Seoul, September-October) content expected on the same channel

**Why it matters:** CoRL is the highest signal-density conference for robot learning research; the 2025 Seoul edition explicitly featured NVIDIA's Scott Reed on deploying learning-based systems in real environments, and multiple sessions on policy evaluation outside lab conditions — the exact gap a software evaluation/observability product could fill.

---

## 9. Lex Fridman Podcast — Sergey Levine (End-to-End Learning in Robotics)

**Channel:** [Lex Fridman](https://www.youtube.com/@lexfridman)

**Specific video:** [End-To-End Learning in Robotics | Sergey Levine and Lex Fridman](https://www.youtube.com/watch?v=W2fcJVtLspM)

**Why it matters:** Levine's argument for end-to-end learned policies over modular pipelines has aged extremely well — it anticipated the current shift to large action models and diffusion policies. The conceptual framing remains useful for understanding why legacy robot software stacks (hand-coded motion planners, perception modules) are being displaced and what the replacement architecture looks like.

---

## 10. BG2 Pod — Brad Gerstner and Bill Gurley (NVIDIA / Physical AI context)

**Channel:** [Bg2Pod](https://www.youtube.com/@Bg2Pod)

**Specific episode:** [A Fireside Chat with BG2: Brad Gerstner and Bill Gurley | 2025 Upfront Summit](https://www.youtube.com/watch?v=2wHzNOqRbDQ)

**Why it matters:** Gerstner and Gurley provide the investor-capital-allocation lens: their consistent framing in 2025-2026 is that physical AI is the next $10T market after software AI, and that the "picks and shovels" layer (data, simulation, evaluation tooling) will capture a disproportionate share of value because every hardware player needs it. This is the fund-raising narrative a software-only robotics founder should be fluent in.

---

## Synthesis: 5 Themes for Software-First Founders

**1. Data is the moat, not the model.**
This is the most-repeated claim across Finn (AI Startup School), Hausman (Sequoia), and a16z (Physical AI episode). Every credible voice in 2025-2026 agrees: whoever aggregates diverse, real-world robot trajectory data at scale sets the model quality ceiling. The commercial implication for a software founder is direct — a data collection, curation, or marketplace product has genuine defensibility that another fine-tuning wrapper does not.

**2. Deployment unlocks data, data unlocks deployment — the flywheel is everything.**
Adcock's BMW line story and Bornich's home-robot narrative share the same structure: the first real deployment is not the product, it is the data collection event. Software that helps operators instrument, log, and label robot behavior in production is a prerequisite for every hardware company to improve. This is an unsexy, high-value wedge — closer to Datadog for robots than to a new foundation model.

**3. Evaluation and observability are unsolved outside labs.**
CoRL 2025 and the NVIDIA GTC sessions both surfaced the same gap: policy evaluation in clean lab environments does not predict real-world performance. There is no standard benchmark for "does this robot policy hold up in a dirty warehouse with inconsistent lighting and novel objects." A software-only evaluation harness — think evals-as-a-service for robot fleets — is a plausible, fundable product that requires no hardware.

**4. The model layer is being commoditized from the top down.**
NVIDIA shipping GR00T N1 as an open foundation model is the signal. Within 18 months, every hardware OEM will have access to a capable base model for free or near-free. This means a software founder should not be building a foundation model — the value is in the layers above (fleet management, task specification, policy monitoring) and below (data pipelines, sim-to-real tooling). The window to compete at the model layer is closing fast.

**5. The GTM path runs through one vertical, not horizontally.**
Hausman's pi.ai went deep on dexterous manipulation before generalizing. Adcock went deep on automotive manufacturing. No credible voice in these sources advocates horizontal robotics software from day one. The implication for small teams is clear: pick one vertical (logistics, food service, warehousing), prove the software wedge there, then expand. The investor narrative (BG2, a16z) supports this — "factory-first principles" over platform abstraction.
