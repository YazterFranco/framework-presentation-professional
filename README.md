# 🎯 Framework: Professional & Humanized Presentations

> A multi-agent Kiro Crew framework that turns raw ideas into audience-aware, high-impact presentations — from a 3-slide pitch to a full deck.

## The Core Problem

Technical people (engineers, data scientists, product folks) have great ideas but struggle to translate them to non-technical audiences. They over-explain mechanics, under-deliver on relevance, and lose people in the first 30 seconds.

This framework fixes that. You describe your idea + your audience; the agents do the rest.

---

## Agent Architecture

```
Input: {idea, context, audience_type, output_format}
        │
        ▼
┌─────────────────────┐
│  audience-profiler  │  → Who are they? What do they care about? What kills their attention?
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ narrative-architect │  → Picks the right framework (SCQA, Pyramid, AIDA…) + builds the story arc
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  slide-composer     │  → Generates slide content: titles, body, data callouts, visuals direction
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   humanizer         │  → Rewrites language for the specific audience — removes jargon, adds hooks
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   critic            │  → Punches holes in the deck: clarity, flow, missing "so what", weak endings
└──────────┬──────────┘
           │
           ▼
Output: Polished slide content + speaker notes + delivery tips
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

- `tech-to-exec` — Engineer explaining to VP/C-suite
- `tech-to-investor` — Founder pitching to non-tech VC
- `tech-to-tech` — Deep-dive for peers (less humanization, more precision)
- `internal-demo` — Feature demo to mixed product team
- `workshop` — Educational presentation to a learning group

---

## Quick Start

```bash
# Install
pip install -r requirements.txt   # (coming in Phase 2)

# Run via Kiro Crew
# → Ask Kiro: "Use the presentation framework to build a pitch for [your idea] targeting [your audience]"
```

---

## Phases

- [x] **Phase 0** — Repo scaffold + docs + agent specs
- [ ] **Phase 1** — Skills: audience-profiler + narrative-architect (prompt-based, no deps)
- [ ] **Phase 2** — Skills: slide-composer + humanizer
- [ ] **Phase 3** — Critic agent + iteration loop
- [ ] **Phase 4** — Kiro Crew workflow (end-to-end pipeline)
- [ ] **Phase 5** — Template library + examples
- [ ] **Phase 6** — Output formats: Markdown, HTML reveal.js, PPTX

---

## Learning Kiro Crew with this project

Each phase is designed to introduce a new Kiro Crew concept:

| Phase | Kiro Crew concept you'll practice |
|-------|-----------------------------------|
| 1 | Skills (prompt files that give Kiro specialized behavior) |
| 2 | Chained skills (output of one feeds the next) |
| 3 | Subagents (critic runs independently, parallel review) |
| 4 | Workflows (multi-phase, restartable pipelines) |
| 5 | Artifacts (saving + versioning generated outputs) |
| 6 | Crons (scheduled deck refreshes, reminders) |

---

## Contributing

Built with [Kiro Crew](https://kiro.dev). See `docs/architecture.md` for deep dive.
