# Workflow: build-presentation

This is the Kiro Crew workflow definition for the full presentation pipeline.
In Phase 4 this will become a `.kiro/workflows/build-presentation.yml` file
that can be launched with `workflow_run(intent="build a presentation about X for Y audience")`.

## Intent examples
- "Build a 5-slide pitch for my VP of Engineering asking for 2 more hires"
- "Create a one-pager investor pitch for our app"
- "Make slides explaining our database migration to the product team"

## Phases

### Phase 1: audience-profile
```
agent: Kiro (using analyze-audience skill)
input:
  - idea: <user's raw idea>
  - audience_description: <user's description of who they're presenting to>
output: audience_profile.json
stop_condition: profile has profile_type, recommended_framework, attention_span_slides
```

### Phase 2: narrative-outline
```
agent: Kiro (using build-narrative skill)
input:
  - audience_profile.json (from Phase 1)
  - idea: <original>
output: narrative_outline.md
stop_condition: outline has N slides ≤ attention_span_slides, each with action title and purpose
restart_from: here if user requests structural change after Phase 3+
```

### Phase 3: compose-slides
```
agent: Kiro (using compose-slides skill — Phase 2 deliverable)
input:
  - narrative_outline.md (from Phase 2)
output: slides_draft.md
stop_condition: every slide has title + max 3 bullets + speaker note
```

### Phase 4: humanize
```
agent: Kiro (using humanize-content skill)
input:
  - slides_draft.md (from Phase 3)
  - audience_profile.json (from Phase 1)
output: slides_humanized.md
stop_condition: no jargon violations for audience type, reading level OK
```

### Phase 5: critique (parallel with Phase 4 output)
```
agent: Kiro (using critique-deck skill)
input:
  - slides_humanized.md (from Phase 4)
  - narrative_outline.md (from Phase 2)
  - audience_profile.json (from Phase 1)
output: critique_report.md
stop_condition: report has overall score and fix list
```

### Phase 6: revise (conditional)
```
condition: overall_score < 8
agent: Kiro (using humanize-content + targeted fixes)
input:
  - critique_report.md (from Phase 5)
  - slides_humanized.md (from Phase 4)
output: slides_final.md
max_iterations: 2
```

### Phase 7: deliver
```
output:
  - slides_final.md → Kiro Artifact (versioned, downloadable)
  - critique_report.md → displayed inline
  - speaker_notes.md → separate artifact
format_options: [markdown, html-reveal, speaker-notes-only]
```

## Kiro Crew concepts used
| Phase | Concept |
|-------|---------|
| 1-5 | Skills (specialized agent behaviors) |
| 5 | Parallel subagent (critic runs independently) |
| 6 | Conditional iteration (loop until quality threshold) |
| 7 | Artifacts (versioned output storage) |
| All | Workflows (restartable, phase-addressable pipeline) |
