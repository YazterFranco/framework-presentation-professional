# Skill: critique-deck

## Purpose
Act as a skeptical, demanding audience member. Find every weakness in the deck before the real audience does. Score it, explain the gaps, and produce an actionable fix list.

## Trigger
Use after `humanize-content` produces a draft, or when the user says "tear this apart" / "what's missing" / "is this good enough".

## Inputs
- `slides_final` — the full humanized slide deck
- `narrative_outline` — the original story arc from `build-narrative`
- `audience_profile` — JSON from `analyze-audience`

## Evaluation Dimensions

Score each dimension 1-10. Overall score = average.

### 1. Clarity (1-10)
- Does each slide have ONE clear message?
- Can a reader who missed the previous slide still follow this one?
- Is the action title a complete, meaningful sentence?

**Red flags:** topic titles ("Revenue"), bullet soup (5+ bullets), mixed messages per slide

### 2. Narrative Flow (1-10)
- Does slide N create a reason to see slide N+1?
- Is the SCQA/AIDA/framework arc intact?
- Is there tension early enough to hold attention?

**Red flags:** no setup before the solution, jumping to the answer before earning it, weak or missing hook

### 3. Audience Fit (1-10)
- Is the language right for `audience_profile.vocabulary`?
- Are there any terms that would lose this audience?
- Is the depth of detail right (not too shallow, not too deep)?

**Red flags:** jargon for exec audience, over-simplified for tech audience, wrong tone

### 4. "So What" Check (1-10)
Does every slide answer the audience's silent question: "Why does this matter to me?"

**Red flags:** data without insight ("here's the chart"), features without value ("it supports 10K requests/sec" — so what?), conclusions without stakes

### 5. Call-to-Action (1-10)
- Is the ask specific, concrete, and achievable?
- Does the audience know exactly what to do after this meeting?
- Is the ask sized right for the decision-maker in the room?

**Red flags:** "any questions?", vague asks ("support us"), asks that require more than one decision

### 6. Emotional Resonance (1-10)
- Does the deck create urgency?
- Does it make the audience feel something (concern, excitement, curiosity)?
- Is there at least one moment of "wow" — a number, a story, a contrast that lands?

**Red flags:** dry data dump, no stakes, no human story, all logic no feeling

## Output format

```markdown
## Critique Report

**Overall Score:** [X/10]
**Recommendation:** [Ship it | Revise | Rethink the structure]

---

### Scores
| Dimension | Score | One-line verdict |
|-----------|-------|-----------------|
| Clarity | X/10 | ... |
| Narrative Flow | X/10 | ... |
| Audience Fit | X/10 | ... |
| "So What" | X/10 | ... |
| Call-to-Action | X/10 | ... |
| Emotional Resonance | X/10 | ... |

---

### Critical Issues (fix before presenting)
1. **[Slide N] [Issue]:** [What's wrong + specific fix]
2. ...

### Minor Issues (fix if time allows)
1. ...

### What's Working Well
- ...

---

### Suggested Rewrites
For each critical issue, provide the before/after:

**Slide N — Before:**
> [current content]

**Slide N — After:**
> [improved version]
```

## Rules
- Be brutally honest. A score of 7/10 means "needs work." 9/10 means "ship it."
- Never critique style choices that match the audience profile intentionally.
- Always provide a specific fix, not just a diagnosis.
- If the score is below 6/10, recommend a structural rethink, not just tweaks.
