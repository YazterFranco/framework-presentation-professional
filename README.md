# 🎯 Framework: Professional & Humanized Presentations

> A multi-agent Kiro Crew framework that turns raw ideas into audience-aware, high-impact presentations — from a 3-slide pitch to a full deck exported as HTML or PowerPoint.

[![Phases](https://img.shields.io/badge/phases-0–6%20complete-brightgreen)](#phases)
[![Skills](https://img.shields.io/badge/skills-7-blue)](#skills)
[![Output](https://img.shields.io/badge/output-markdown%20%7C%20html%20%7C%20pptx-orange)](#output-formats)

---

## The Core Problem

Technical people have great ideas but struggle to translate them to non-technical audiences. They over-explain mechanics, under-deliver on relevance, and lose people in the first 30 seconds.

This framework fixes that. You describe your idea + your audience — the pipeline does the rest.

---

## Agent Pipeline

```
Input: {idea, audience_description, output_format}
        │
        ▼
┌─────────────────────┐
│  analyze-audience   │  → Who are they? What kills their attention? Which framework fits?
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  build-narrative    │  → Picks SCQA / AIDA / Pyramid / PSP + builds the story arc
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  compose-slides     │  → Generates slide content: action titles, bullets, speaker notes
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  humanize-content   │  → Removes jargon, applies hook, adjusts reading level
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  critique-deck      │  → Scores 6 dimensions (1–10), produces fix list
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  render output      │  → Markdown | HTML Reveal.js | .pptx
└─────────────────────┘
```

---

## Narrative Frameworks Built-in

| Framework | Best for |
|-----------|----------|
| **SCQA** (Situation→Complication→Question→Answer) | Executive, board, investor audiences |
| **Minto Pyramid** | Consulting-style decks, analysis presentations |
| **AIDA** (Attention→Interest→Desire→Action) | Sales, demos, pitches |
| **Problem/Solution/Proof** | Internal demos, feature launches |
| **One-pager** | 1-slide pitches, busy stakeholders |

---

## Audience Profiles

| Profile | Description | Framework |
|---------|-------------|-----------|
| `tech-to-exec` | Engineer → VP/C-suite | SCQA |
| `tech-to-investor` | Founder → non-tech VC | AIDA |
| `tech-to-tech` | Deep-dive for peers | Pyramid |
| `internal-demo` | Feature demo to mixed team | Problem-Solution-Proof |
| `workshop` | Educational presentation | Pyramid or PSP |

---

## Output Formats

| Format | Command | Use case |
|--------|---------|----------|
| `markdown` | Default | Paste into Notion, Google Slides, Confluence |
| `html-reveal` | `render-html-reveal` skill | Browser presentation, no internet needed |
| `pptx` | `python3 scripts/generate_pptx.py` | PowerPoint, Google Slides, Keynote |
| `speaker-notes` | Embedded in all formats | Presenter View (PPTX) or S key (HTML) |

---

## Quick Start

```bash
# Install PPTX dependency
pip install python-pptx==1.0.2

# Run via Kiro Crew (recommended)
# → Ask Kiro: "Use the presentation framework to build a pitch for [idea] targeting [audience]"

# Generate PPTX directly from a composed deck
python3 scripts/generate_pptx.py \
  --input  output/slides_final.md \
  --title  "Your Presentation Title" \
  --tone   formal \
  --output output/your-presentation.pptx
```

---

## Skills

| Skill | Phase | What it does |
|-------|-------|-------------|
| `analyze-audience` | 1 | Profiles the audience → structured JSON |
| `build-narrative` | 1 | Maps idea to framework → slide-by-slide outline |
| `compose-slides` | 2 | Outline → full slide content with speaker notes |
| `humanize-content` | 2 | Jargon sweep + hook application + reading level |
| `critique-deck` | 2 | Scoring across 6 dimensions + actionable fix list |
| `render-html-reveal` | 5 | Markdown → self-contained HTML presentation |
| `render-pptx` | 6 | Markdown → .pptx via python-pptx |

---

## Workflow (Kiro Crew)

The full pipeline is defined as a Kiro Crew Workflow at `.kiro/workflows/build-presentation.yml`.

Launch it from the dashboard:
```
workflow_run(intent="Build a 5-slide pitch for my VP asking for budget approval")
```

Restart a failed phase without re-running earlier ones:
```
workflow_rerun_subtree(run_id="<id>", phase="humanize")
```

---

## Examples

| File | Scenario | Framework | Score |
|------|----------|-----------|-------|
| `examples/tech-to-exec-hiring.md` | Tech lead → VP: 2 new hires | SCQA | 8.8/10 |
| `examples/tech-to-investor.md` | Founder → VC: LegalLens pitch | AIDA | 8.8/10 |
| `examples/internal-demo.md` | Engineer → Product team: search feature | PSP | 8.7/10 |
| `examples/kiro-crew-mixed-audience/` | Kiro Crew explicado a audiencia mixta (tech + no-tech) | AIDA | 8.7/10 |
| `examples/workflow-run-example.md` | How to launch the workflow | — | — |

---

## Templates

| Template | Audience | Slides |
|----------|----------|--------|
| `templates/tech-to-exec/template.md` | VP / C-suite | 5–7 |
| `templates/tech-to-investor/template.md` | VC / Angel | 5 |
| `templates/one-pager/template.md` | Anyone, 2 min | 1 |

---

## Phases

- [x] **Phase 0** — Repo scaffold + docs + agent specs
- [x] **Phase 1** — Skills: `analyze-audience` + `build-narrative`
- [x] **Phase 2** — Skills: `compose-slides` + `humanize-content` + `critique-deck`
- [x] **Phase 3** — Kiro Crew workflow (`.kiro/workflows/build-presentation.yml`)
- [x] **Phase 4** — Template library + examples (tech-to-exec, tech-to-investor, internal-demo)
- [x] **Phase 5** — HTML Reveal.js output (`render-html-reveal` skill)
- [x] **Phase 6** — PPTX export (`render-pptx` skill + `scripts/generate_pptx.py`)

---

## Learning Kiro Crew with this project

Each phase introduces one Kiro Crew concept through a concrete task:

| Phase | Kiro Crew concept | What you practiced |
|-------|-------------------|--------------------|
| 1–2 | **Skills** | `.md` files that give Kiro specialized behavior, activated by name |
| 3 | **Workflows** | Restartable multi-phase pipelines via `workflow_run()` |
| 4–5 | **Artifacts** | Versioned output stored in the dashboard library |
| 6 | **Crons** | Scheduling recurring deck generation (see `render-pptx` skill doc) |
| Next | **Subagents** | Run `critique-deck` in parallel with `humanize-content` via `spawn_run` |

---

## Contributing

Built with [Kiro Crew](https://kiro.dev). See `docs/architecture.md` for the full agent spec and data flow.
