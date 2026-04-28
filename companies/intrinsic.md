# Intrinsic
**Vertical:** Picks-and-shovels | **URL:** https://www.intrinsic.ai | **HQ:** Mountain View, CA | **Founded:** 2021 (spun out of Alphabet X) | **Stage/Funding:** Alphabet "Other Bet" (wholly-owned); folded into Google as a distinct business unit in February 2026; no independent funding disclosed. Est. $27.2M revenue as of Sept 2025 (Latka).

## Product
Intrinsic sells Flowstate, a web-based developer environment for building production-grade industrial automation. Flowstate bundles AI-assisted perception (pose estimation via the Intrinsic Vision Model), motion planning with auto-generated collision-free trajectories, and sensor-based real-time control (force, torque, distance). The platform targets roboticists and developers who lack deep domain expertise, abstracting away low-level robot programming. Flowstate runs on Alphabet/Google Cloud infrastructure and integrates with NVIDIA Isaac and Omniverse for simulation. Pricing is not publicly disclosed; the product is in beta.

## ICP
Large industrial manufacturers and tier-1 electronics contract manufacturers, primarily in the US. The Foxconn joint venture (announced Nov 2025) anchors the ICP in high-volume, precision assembly environments — Foxconn's Houston facility producing NVIDIA server racks is the named deployment. Deal cycles appear long (Foxconn discussions ran ~1–2 years before formalizing). No meaningful SMB or mid-market presence is visible.

## Traction
Est. $27.2M revenue with ~247 employees as of September 2025 (Latka, unverified). One named major deployment: Foxconn US factories. No published customer count. Laid off 20% of staff in January 2023 before recovering headcount through 2024–2025.

## Tech moat
Access to Google DeepMind models and Google Cloud infrastructure post-merger. Acquired Vicarious (robotics ML, ~$250M previously raised by Vicarious) in 2022 and Open Robotics assets (ROS 2 stewards), giving Intrinsic a foundation in open robotics standards. Intrinsic Vision Model for industrial perception is a proprietary asset. The overall moat is moderate: deep-pocketed parent provides durable compute and model access, but the software layer itself (motion planning, perception APIs) faces credible open-source competition from ROS 2 and commercial rivals.

## Distribution model
Direct enterprise sales with long co-development cycles (evidenced by the Foxconn JV structure). No channel or marketplace model currently visible. Post-merger into Google, distribution may shift toward Google Cloud Marketplace and Google's existing enterprise sales force. Not RaaS.

## Critical weakness
Alphabet's repeated internal restructurings (20% RIF in 2023, full absorption into Google in 2026) signal organizational instability and shifting strategic priority. Being inside Google means product roadmap is now subordinate to Google's broader AI/cloud strategy rather than customer pull. This creates a window where enterprise customers evaluating multi-year robotics software commitments may hesitate to bet on a platform whose independence and roadmap continuity are uncertain.

## Adjacent gap
Intrinsic's entire motion — JV with Foxconn, Google Cloud dependency, long enterprise sales cycles — is calibrated for Fortune 500 manufacturers with 1,000+ robot deployments. **Small and mid-size contract manufacturers (50–500 employees, 5–50 robots) in Europe and the UK are entirely unaddressed.** These shops need the same perception-and-motion abstraction but cannot absorb 12-month co-development deals or Google Cloud lock-in. A startup offering a lighter-weight, hardware-agnostic Flowstate equivalent with a self-serve SaaS motion (monthly subscription, on-prem or edge deployment, no JV required) and a channel through robot OEM distributors (Universal Robots resellers, KUKA integrators) could own this segment before Intrinsic's Google-scale sales machine ever reaches it.

## Sources
- https://techcrunch.com/2026/02/25/alphabet-owned-robotics-software-company-intrinsic-joins-google/
- https://www.cnbc.com/2026/02/25/alphabet-robotics-software-intrinsic-google-ai.html
- https://fortune.com/2025/11/20/alphabet-intrinsic-foxconn-intelligent-robots-ai-joint-venture/
- https://getlatka.com/companies/intrinsic.ai
- https://www.intrinsic.ai
