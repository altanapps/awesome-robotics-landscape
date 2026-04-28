# Robotics Landscape

Research bundle compiled April 2026. 82 company dossiers across 12 verticals, gap analysis, data-collection deep-dive, ecosystem chatter, and five validation research files. Aimed at a software-first solo founder evaluating wedges in robotics.

## Quick start

```bash
# Install the secret-scanning pre-commit hook (one-time)
cp hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

# Rebuild the interactive index page locally
ANTHROPIC_API_KEY=sk-ant-... python3 build.py

# Open in browser (or run a local server for CORS-friendly API calls)
open index.html
# OR
python3 -m http.server 8765
# then http://localhost:8765/index.html
```

`index.html` is gitignored because the build embeds your `ANTHROPIC_API_KEY` for the in-page chat panel. Rebuild after cloning.

The pre-commit hook blocks any commit containing a real Anthropic or OpenAI API key.

## What's here

### Synthesis
- `gap-analysis.md` — top 5 software-only wedges, ranked. Parts 5-7 cover ecosystem validation, validation research findings, and external second-opinion reconciliation. **Read this first.**
- `data-collection-deep-dive.md` — focused analysis on Wedge A (data infrastructure). Verdict: build on the curation/sovereignty layer, not collection.
- `external-second-opinion.md` — independent analysis from a different model on the same source bundle.
- `index.md` — raw scout-pass index of all 79 original companies with funding/one-liners.

### Ecosystem chatter
- `ecosystem-substacks.md` — 8 robotics newsletters with editorial angle and anchor pieces.
- `ecosystem-youtube.md` — 10 robotics YouTube channels and conference talks.

### Validation research
- `research-vc-portfolio-scan.md` — competitor map across the top wedges.
- `research-job-posting-signals.md` — labour-market signal of where robotics is being deployed.
- `research-insurance-prior-art.md` — Coalition / At-Bay / Skywatch / Koop case studies for Wedge 1.
- `research-failure-postmortems.md` — Berkshire Grey / Vicarious / Canvas / Nuro / iRobot lessons.
- `research-eu-regulatory.md` — EU AI Act + Machinery Regulation 2027 deep-dive for Wedge 2.

### Company dossiers
`companies/` — 82 individual dossiers, one markdown file per company. Each has Product, ICP, Traction, Tech moat, Distribution model, Critical weakness, and (most important) Adjacent gap.

## Top 5 wedges (current ranking after triangulation)

1. **RaaS billing infrastructure** — zero funded competitors, $8.2B market 2026, validated by labour-market signal (Serve Robotics improvising it via one role).
2. **"Vanta for robots"** — EU AI Act + Machinery Regulation Aug 2027 deadline, BSI as named UK channel partner.
3. **Robot fleet underwriting** — Lloyd's MGA shape, Koop Technologies is direct US prior art (UK-challenger framing still credible).
4. **Multi-vendor fleet observability (mid-market only)** — green-field for the operator-side mixed-fleet wedge that Foxglove ignores.
5. **Robotics policy evaluation SaaS** — independent benchmarks for VLA models, sim-only.

See `gap-analysis.md` Part 6 + 7 for the reasoning behind the ranking.

## Build script

`build.py` reads every markdown file in this directory + `companies/`, embeds them as a JS object, and produces a single-page `index.html` with a sidebar nav, marked-rendered content pane, and a chat panel that calls Anthropic or OpenAI directly from the browser.

The chat panel saves question history to localStorage and supports a "Copy as prompt" fallback for environments where browser-to-API CORS is blocked.

## Sources & freshness

All data was compiled in April 2026 using web research. Funding figures, deployment numbers, and competitive density are best-effort estimates from public sources (TechCrunch, company sites, IFR reports, VC portfolio pages). Verify before relying on any specific figure for a real decision.
