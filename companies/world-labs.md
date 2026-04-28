# World Labs
**Vertical:** Foundation models for robotics | **URL:** https://www.worldlabs.ai | **HQ:** San Francisco, CA | **Founded:** January 2024 | **Stage/Funding:** Series B equivalent — $1.23B raised to date ($230M Series A, Sep 2024; $1B round, Feb 2026); investors include NVIDIA, AMD, Autodesk ($200M), Fidelity, Emerson Collective; estimated valuation ~$5B.

## Product
World Labs builds spatial intelligence models that generate persistent, navigable 3D environments from text, images, video, or rough 3D layouts. Their flagship product, Marble, produces photorealistic worlds exportable to Unreal, Unity, Blender, and Houdini. A programmatic World API (launched January 2026) exposes Marble's capabilities to developers, with pre-built integrations for NVIDIA Isaac Sim, MuJoCo, and RoboSuite — enabling synthetic training data generation for robotics simulation. A companion open-source library, Spark, handles real-time browser streaming of 3D Gaussian Splatting scenes via Three.js.

## ICP
Primary near-term buyers are VFX studios, game developers, and AR/VR content teams needing high-fidelity 3D scenes with production-grade output formats. Secondary target is robotics and industrial simulation teams (manufacturing, automotive, architecture) sourcing synthetic training environments. No disclosed deal sizes; Marble is currently free-to-use in beta. The Autodesk partnership signals an enterprise ACV likely in the six-to-seven-figure range for future licensing.

## Traction
Pre-revenue as of December 2025 (Contrary Research). Approximately 3,000 active beta users in Discord. Autodesk investment (announced 2026) includes a product integration commitment. EON Reality partnership (December 2024) is the only named commercial relationship. No ARR or deployment counts publicly available. (Sources: Contrary Research, Dec 2025; World Labs blog, Feb 2026.)

## Tech moat
Core differentiation is scene-level 3D coherence at interactive framerates — their RTFM (Real-Time Frame Model) runs persistent world generation on a single H100. Founding team IP is genuine: Ben Mildenhall co-created NeRF; Christoph Lassner built the Pulsar renderer; Fei-Fei Li's ImageNet legacy accelerates research recruiting. 3D training data scarcity is both a moat and a ceiling — they have more proprietary data than most startups but less than NVIDIA or Google.

## Distribution model
Browser-based self-serve beta (freemium) for creative users; API platform for developer/robotics teams. Strategic OEM-style integrations with Autodesk and NVIDIA for enterprise reach. Google Cloud is primary compute partner. Sales motion is not yet clearly enterprise-direct — the Autodesk deal likely drives near-term pipeline.

## Critical weakness
No proven revenue model after $1.23B raised. Creative industry adoption is structurally slow (artist resistance, union dynamics) and robotics/industrial sales cycles run 5–7 years. Larger compute-rich players — NVIDIA, Google DeepMind — can replicate the architecture with superior data access and distribution leverage. Reliance on Autodesk as the primary enterprise distribution channel concentrates commercial risk.

## Adjacent gap
The World API integrates with robotics simulators but targets well-funded robotics labs and large OEMs that can afford enterprise deals and have the ML teams to use raw API output. The unserved wedge is **mid-market robotics integrators and automation SMEs** — companies deploying 10–200 robot units in warehousing, agriculture, or light manufacturing — that need affordable, pre-configured synthetic training datasets for specific task domains (e.g., bin-picking, crop harvesting) but cannot afford custom simulation pipelines or a full ML stack. A startup could productize vertical-specific synthetic data packages on top of World Labs' or a competing world model, with a no-code configuration layer and per-task pricing, targeting the 500–5,000 robot-unit tier that NVIDIA Isaac and World Labs' current API motion leave unaddressed.

## Sources
- https://www.worldlabs.ai
- https://www.worldlabs.ai/blog/funding-2026
- https://research.contrary.com/company/world-labs
- https://fourweekmba.com/world-labs-1-25b-business-model-how-fei-fei-li-is-building-ai-that-understands-3d-space-like-humans-do/
- https://www.constructiondive.com/news/autodesk-invests-world-labs-artificial-intelligence/813121/
