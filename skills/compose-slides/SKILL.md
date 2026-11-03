# Skill: compose-slides

## Purpose
Convert a narrative outline into full slide content — action titles, bullets, data callouts, and speaker notes. No design decisions yet; just the words that go on each slide, structured for clarity.

## Trigger
Use after `build-narrative` produces a narrative outline, or when the user says "write the slides" / "fill in the content" / "compose the deck".

## Inputs
- `narrative_outline` — the story arc from `build-narrative` (slide purposes + action titles + content direction)
- `audience_profile` — JSON from `analyze-audience`

## Steps

### 1. For each slide in the outline, produce:

**A. Action title** (required)
- Must be a complete sentence with a verb and a consequence
- Must contain the main insight of the slide — not a topic label
- ✅ "We lose $40K/month when the checkout flow is slow"
- ❌ "Checkout Performance"
- Max 12 words

**B. Body content** (choose one format based on content direction)

| Content type | Format | Max |
|---|---|---|
| Arguments / reasons | Bullet list | 3 bullets, 10 words each |
| Data comparison | 2-column contrast | 2 rows max |
| Single key metric | Big number callout | 1 number + 1 context line |
| Process / sequence | Numbered steps | 3 steps max |
| Story / scenario | 2-sentence narrative | 30 words max |

**C. Visual direction** (1 line)
Describe the visual that would reinforce the message without explaining it verbally. Options: chart type, photo direction, icon, diagram, contrast table. Mark as `[no visual needed]` if the text stands alone.

**D. Speaker note** (required)
- What to SAY, not what to READ from the slide
- Includes: opening line for that slide, key transition from previous, one thing to watch for in the audience, closing line before moving on
- Written in first person, natural speech, contractions OK
- Max 60 words

### 2. Apply the one-idea rule
After composing, check every slide:
- Does it communicate exactly one idea?
- If you can write two distinct action titles for a slide → split it
- If two slides make the same point → merge them

### 3. Check the ask slide last
The final slide must:
- Name the decision required (not "feedback" or "thoughts")
- Include a timeframe ("by end of week", "before sprint planning")
- Name the outcome if approved ("we can start phase 1 in 2 weeks")
- Be completable in under 30 seconds of reading

## Output format

```markdown
## Slide Deck: [Title]
**Audience:** [profile_type]
**Framework:** [SCQA | AIDA | Pyramid | Problem-Solution-Proof]
**Total slides:** [N]

---

### Slide [N] — [Framework slot]
**Title:** [Action title — complete sentence]
**Format:** [bullets | contrast | big-number | steps | story]
**Content:**
- [bullet 1]
- [bullet 2]
- [bullet 3]
**Visual:** [one-line visual direction, or "no visual needed"]
**Speaker note:** [natural speech, max 60 words]

---
```

## Rules
- Never exceed 40 words of body copy per slide (title excluded). More than 40 = failed slide.
- No "Introduction", "Agenda", or "Thank You" slides for executive audiences.
- Every data point needs a unit ("40%" not "forty percent", "$2M" not "two million dollars").
- If `audience_profile.vocabulary == "business_outcomes"`: every tech term must be translated before use.
- Bullets start with a number, a verb, or a key noun — never with "The" or "Our".
- Speaker notes must include a transition line connecting this slide to the next ("The reason this matters is...", "Which brings us to...", "So what do we do about it?").

## Anti-patterns to catch
- **Bullet soup**: 4+ bullets per slide → cut to 3 max
- **Topic title**: title is a noun phrase, not a sentence → rewrite as insight
- **Feature without value**: "supports 10K requests/sec" → "handles 3x our peak traffic without slowing down"
- **Data without "so what"**: chart or number with no takeaway sentence → add the conclusion explicitly
- **Weak ask**: "let us know your thoughts" → replace with a specific decision + deadline

## Example

**Input (narrative outline slot):**
```
Slide 2 — Complication
Purpose: create tension — something is at risk
Content direction: quantify the current pain with a business impact number
```

**Output:**
```markdown
### Slide 2 — Complication
**Title:** One slow page costs us 12% of monthly revenue — and it's getting worse.
**Format:** big-number + contrast
**Content:**
- Today: checkout abandonment rate 34% (industry avg: 22%)
- Root cause: 4.2-second load time on mobile
- Trend: up 18% since last quarter's traffic spike
**Visual:** Before/after bar chart — abandonment rate vs. load time, last 6 months
**Speaker note:** "Here's the number I want you to hold onto: 34%. More than 1 in 3 people who start a checkout don't finish it. That's not a UX problem — that's a revenue leak. And it's been getting worse, not better. Which means if we don't act before Q1, we're not just slow — we're losing ground."
```
