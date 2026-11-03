# Architecture: Presentation Framework

## Design Principles

1. **Audience-first** — every decision (framework, language, depth) derives from the audience profile, not the speaker's comfort.
2. **Framework-aware** — the system picks the communication structure proven for that audience type; you don't have to know it.
3. **Iterative** — the critic agent forces at least one revision pass before output is delivered.
4. **Modular** — each agent is a standalone Kiro Crew skill. You can use them individually or chain them.

---

## Agent Responsibilities

### `audience-profiler`
**Input:** raw description of who will be in the room  
**Output:** structured profile
```json
{
  "type": "tech-to-exec",
  "attention_span_slides": 5,
  "vocabulary": "business_outcomes",
  "what_they_care_about": ["ROI", "risk", "timeline"],
  "what_loses_them": ["acronyms", "architecture diagrams", "long intros"],
  "recommended_framework": "SCQA"
}
```

### `narrative-architect`
**Input:** idea + audience profile  
**Output:** story arc (slide-by-slide outline)
- Selects framework (SCQA / Pyramid / AIDA / Problem-Solution-Proof)
- Maps idea to framework slots
- Produces a numbered outline with one-line purpose per slide

### `slide-composer`
**Input:** story arc  
**Output:** per-slide content
- Slide title (action title, not topic title — "Revenue is at risk" not "Revenue")
- 3 bullets max (rule of three)
- One key data point or visual callout
- Speaker note: what to say, not what to read

### `humanizer`
**Input:** slide content + audience profile  
**Output:** rewritten content
- Replaces jargon with business language
- Adds analogies or stories where density is high
- Checks reading level targeting (target: 8th grade for exec audiences)
- Adds hooks: question, number, contrast, or consequence

### `critic`
**Input:** full deck draft  
**Output:** critique report
Checks for:
- Missing "so what" on each slide
- Weak or missing call-to-action
- Slide count vs. attention span
- Consistency of voice
- Logic gaps in the narrative

---

## Narrative Frameworks

### SCQA (Situation → Complication → Question → Answer)
Best for executives and investors. Borrowed from McKinsey/Barbara Minto.

```
Slide 1: Situation   — "We're in X context." (shared ground)
Slide 2: Complication — "But Y happened / is changing / is at risk."
Slide 3: Question    — "So what should we do?" (implied, often skipped in exec decks)
Slide 4: Answer      — "Here's our recommendation."
Slide 5: Evidence    — "Here's why it works."
Slide 6: Ask         — "Here's what we need from you."
```

### Minto Pyramid
Best for analytical/consulting decks.
- Lead with the conclusion
- Support with 3 grouped arguments (MECE: mutually exclusive, collectively exhaustive)
- Each argument backed by evidence

### AIDA
Best for pitches and demos.
- **Attention:** hook with a number, story, or contrast
- **Interest:** explain the problem they recognize
- **Desire:** show the solution and its value
- **Action:** clear, specific ask

### Problem → Solution → Proof
Best for internal demos and feature launches.
- Problem: "Here's the pain, with data"
- Solution: "Here's what we built"
- Proof: "Here's evidence it works"

---

## Data Flow (Kiro Crew Workflow)

```
workflow: build-presentation
  phase 1: profile-audience
    agent: audience-profiler
    input: {idea, audience_description}
    output: audience_profile.json

  phase 2: build-narrative
    agent: narrative-architect
    input: audience_profile.json + original_idea
    output: narrative_outline.md

  phase 3: compose-slides
    agent: slide-composer
    input: narrative_outline.md
    output: slides_draft.md

  phase 4: humanize
    agent: humanizer
    input: slides_draft.md + audience_profile.json
    output: slides_humanized.md

  phase 5: critique (parallel)
    agent: critic
    input: slides_humanized.md + narrative_outline.md
    output: critique_report.md

  phase 6: revise
    agent: slide-composer + humanizer (iteration)
    input: critique_report.md + slides_humanized.md
    condition: repeat until critic score >= 8/10 or max 2 iterations
    output: slides_final.md

  phase 7: package
    output formats: markdown | html-reveal | speaker-notes
```

---

## Output Formats (Phase 6)

| Format | Use case |
|--------|----------|
| `markdown` | Copy into any tool (Notion, Google Slides, etc.) |
| `html-reveal` | Self-contained HTML presentation (Reveal.js) |
| `speaker-notes` | Separate doc with what to say per slide |
| `pptx` (future) | Direct PowerPoint export via python-pptx |
