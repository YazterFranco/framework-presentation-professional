# Skill: build-narrative

## Purpose
Turn a raw idea + an audience profile into a slide-by-slide story arc. No content yet — just the skeleton that ensures logical flow and emotional resonance.

## Trigger
Use after `analyze-audience` produces an audience profile, or when the user says "build the outline" / "structure the deck".

## Inputs
- `idea` — the user's raw description of what they want to communicate
- `audience_profile` — JSON from `analyze-audience`

## Steps

### 1. Select the framework
Use `audience_profile.recommended_framework`. If the user overrides, respect it.

### 2. Map the idea to framework slots

**SCQA mapping:**
```
Situation:    The shared context everyone in the room already knows
Complication: What changed / what's at risk / what's broken
Question:     The logical question the complication raises (can be implied)
Answer:       Your recommendation / decision / solution
Evidence:     3 supporting points (data, examples, analogies)
Ask:          What you need from the audience (decision, approval, resources)
```

**AIDA mapping:**
```
Attention:  1 powerful hook — a number, a story, a contrast, a consequence
Interest:   The problem they recognize and feel
Desire:     Your solution + why it's better
Action:     The specific next step you're asking for
```

**Problem-Solution-Proof mapping:**
```
Problem:    The pain, quantified
Solution:   What you built / propose
Proof:      Evidence it works (metrics, demo, case study, testimonial)
```

### 3. Write the outline
For each slide:
- **Slide N — [Framework Slot]**: one-sentence purpose ("This slide exists to make the audience feel X / understand Y / decide Z")
- **Action title**: title written as an insight, not a topic ("We're losing $2M/year to churn" not "Churn Analysis")
- **Content direction**: what type of content goes here (data point, story, diagram, quote, chart)

### 4. Check flow
- Does slide 1 create enough tension that they NEED to see slide 2?
- Does every slide answer "so what?"
- Is the ask at the end clear and specific?
- Is the slide count ≤ `attention_span_slides`?

## Output format

```markdown
## Narrative: [Title]
**Audience:** [profile_type]
**Framework:** [chosen framework]
**Slide count:** [N]

---

### Slide 1 — [Slot: Situation/Attention/Problem]
**Purpose:** [why this slide exists]
**Action title:** "[example title]"
**Content:** [description of what goes here]

### Slide 2 — [Slot: ...]
...

### Final slide — Ask
**Purpose:** make the audience take ONE specific action
**Action title:** "[example]"
**Content:** [the ask, made concrete and easy to say yes to]
```

## Rules
- Action titles must be complete sentences with a verb and a consequence.
- No "Introduction" or "Agenda" slides for exec audiences (wastes their first 90 seconds).
- Evidence slides should present one point each — never a "3 reasons why" dump.
- The Ask slide is mandatory for any deck where a decision is expected.
