# Example: Running the build-presentation Workflow

## What this demonstrates
Phase 3 of the learning project: launching the full pipeline as a **Kiro Crew Workflow**
instead of running skills manually one by one.

## How to launch

### From the Kiro Crew dashboard (natural language)
Ask Kiro:
```
Use the presentation framework to build a pitch for [your idea] targeting [your audience]
```

### Via workflow_run (programmatic)
```
workflow_run(intent="Build a 5-slide pitch for my VP of Engineering asking for 2 additional backend engineers to meet the Q1 roadmap")
```

Kiro Crew will:
1. Parse the intent and extract `idea` + `audience_description`
2. Launch `.kiro/workflows/build-presentation.yml`
3. Return a `run_id` immediately (non-blocking)
4. Run phases sequentially; Phase 6 (revise) only runs if critique score < 8
5. Deliver the deck + speaker notes as Artifacts + an interactive widget

## How to restart a failed phase

If Phase 4 (humanize) fails, restart only from there:
```
workflow_rerun_subtree(run_id="<your-run-id>", phase="humanize")
```
Phases 1–3 replay from cache — no tokens spent, no re-running the audience profile.

## Input examples

| Intent | Audience | Framework chosen |
|--------|----------|-----------------|
| "Need budget to hire 2 engineers" | VP of Engineering | SCQA |
| "Pitch our app to investors" | Non-tech VC | AIDA |
| "Explain the API redesign" | Product + Design team | Problem-Solution-Proof |
| "Justify the infrastructure migration" | CTO (technical) | Minto Pyramid |

## Output artifacts produced

| Artifact | Content |
|----------|---------|
| `presentation_artifact` | Full slide deck in chosen format (markdown / html-reveal) |
| `speaker_notes_artifact` | What to say per slide — natural speech, with transitions |
| Dashboard widget | Interactive tabs: Deck · Critique scores · Speaker notes |

## Kiro Crew concept: Workflows vs. Skills

| | Skill | Workflow |
|---|---|---|
| **What it is** | A `.md` file with a protocol for one task | A `.yml` pipeline that chains multiple phases |
| **How to use** | Ask Kiro to "use the X skill" | `workflow_run(intent="...")` |
| **Restartable?** | No — runs in the current turn | Yes — `workflow_rerun_subtree` from any phase |
| **Parallel?** | No | Yes — phases can run in parallel (future) |
| **Trackable?** | Turn-by-turn only | Workflows tab in the dashboard |
| **Best for** | Single specialized tasks | Multi-step pipelines with branching + iteration |
