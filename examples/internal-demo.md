# Example: Engineer → Mixed Product Team (Problem-Solution-Proof)

**Scenario:** A backend engineer presents a new internal search feature to their product,
design, and engineering team in a sprint demo. The audience is mixed: designers care
about UX, PM cares about metrics, engineers care about reliability. 15 minutes, 6 slides.

---

## Pipeline output

### Step 1 — analyze-audience

```json
{
  "profile_type": "internal-demo",
  "attention_span_slides": 6,
  "vocabulary": "mixed",
  "primary_goals": [
    "understand what was built and why",
    "flag UX concerns before launch",
    "decide if this ships in the current sprint"
  ],
  "what_they_care_about": [
    "PM: does it move the retention metric?",
    "Design: does the interaction feel right?",
    "Eng: is it stable, what are the failure modes?"
  ],
  "what_loses_them": [
    "deep architecture walk-through (PM + Design)",
    "pixel-level UX feedback loop (Eng)",
    "cost/latency numbers without user impact context (PM)"
  ],
  "recommended_framework": "Problem-Solution-Proof",
  "tone": "conversational",
  "hook_type": "contrast"
}
```

**Why Problem-Solution-Proof:** This is an internal team that knows the context, but
has different lenses (PM = outcome, Design = experience, Eng = reliability). PSP works
because it grounds everyone in the same shared pain before showing the solution — so
the PM, designer, and engineer all arrive at the demo with the same question in mind.

---

### Step 2 — build-narrative

**Framework:** Problem-Solution-Proof
**Slide count:** 6

| Slide | Slot | Primary audience |
|-------|------|-----------------|
| 1 | Problem — quantified | PM + everyone |
| 2 | The friction point | Design |
| 3 | Solution — what we built | Everyone |
| 4 | Proof — it works | PM + Eng |
| 5 | Tradeoffs + known limits | Eng |
| 6 | Ship decision | PM |

---

### Step 3 — compose-slides

---

#### Slide 1 — Problem
**Title:** 34% of users who use search leave without finding what they came for.
**Format:** big-number + contrast
**Content:**
- Today: search returns results by keyword match only — no intent understanding
- 34% search abandonment rate (industry benchmark: 18%)
- Users who abandon search churn at 2.3x the rate of users who find what they need
**Visual:** Funnel chart: search session → result interaction → retention. Abandonment highlighted.
**Speaker note:** "I want to start with a number that surprised me when I first pulled it. 34% of the people who use our search leave without clicking a single result. That's not a feature gap — that's a retention risk. And it's twice the industry average. That's the problem this sprint was about."

---

#### Slide 2 — The friction point
**Title:** Users search in plain language — we match them against exact product names they don't know.
**Format:** contrast
**Content:**
- User types: "something for back pain when sitting at a desk"
- Old result: no match (product is named "ErgoLumbar Pro 3000")
- Gap: users don't know our taxonomy, and we never taught them
**Visual:** Side-by-side: user query vs. current search result (empty state screenshot)
**Speaker note:** "Here's the specific failure mode. Our users speak in problems. Our search speaks in product names. Those two languages don't overlap. This slide is for the design team — this is the gap we needed to close at the UX layer, not just the backend."

---

#### Slide 3 — Solution
**Title:** We added intent matching — search now understands what the user means, not just what they typed.
**Format:** steps
**Content:**
1. User query is interpreted for intent ("back pain + sitting" → ergonomic support category)
2. Results ranked by relevance to intent, not keyword density
3. Fallback to keyword if intent score is below threshold — no empty states
**Visual:** Before/after: same query, new results with intent-matched products highlighted
**Speaker note:** "What we built: a layer that interprets the query before hitting the index. It's not magic — it's a classifier trained on 60K real user queries from our own data. The key design decision was the fallback: if intent confidence is low, we show keyword results anyway. Zero empty states was a hard requirement from the start."

---

#### Slide 4 — Proof (metrics)
**Title:** In staging, search abandonment dropped from 34% to 19% — below the industry benchmark.
**Format:** contrast
**Content:**
- Abandonment rate: 34% → 19% (staging, 14-day shadow test, 8K sessions)
- Click-through on first result: 28% → 41%
- Zero regression on keyword-only queries (p99 latency unchanged)
**Visual:** Before/after bar chart for the three metrics
**Speaker note:** "We ran a 14-day shadow test — real queries, new ranking applied in staging, results compared. Abandonment dropped 15 points. First-result click-through up 13 points. And critically: no regression on the cases that already worked. The keyword path is untouched. The new path only activates when it's confident."

---

#### Slide 5 — Tradeoffs + known limits
**Title:** Three edge cases to watch in production — none are blockers, all are monitored.
**Format:** bullets
**Content:**
- Low-confidence queries (< 12% of volume): falls back to keyword, no user impact
- Cold-start for new products: takes ~48h of query data before intent model covers them
- Languages: English only — intent model not trained on Spanish/PT queries yet
**Visual:** No visual needed
**Speaker note:** "This is the slide for the engineers. Three honest limitations. First: rare queries fall back to keyword — that's intentional and the behavior is the same as today. Second: new products take 48 hours to get coverage — that's acceptable and the team knows to wait before announcing new SKUs. Third: non-English is not covered. That's a follow-up item, not a ship blocker."

---

#### Slide 6 — Ship decision
**Title:** Ready to ship in this sprint — one approval needed on the monitoring dashboard before we flip the flag.
**Format:** bullets
**Content:**
- All acceptance criteria met (see PR #4421)
- Monitoring dashboard built — abandonment rate, intent confidence, fallback rate
- Waiting on PM sign-off on the dashboard layout before enabling in production
**Visual:** Screenshot of monitoring dashboard (real)
**Speaker note:** "We're ready. The ask is simple: PM signs off on the monitoring layout — that's a 5-minute review — and we flip the feature flag today. I'll be watching the dashboard for the first 24 hours. Any anomaly and I roll back immediately."

---

### Step 4 — humanize-content

**HUMANIZER NOTES:**
| Replaced | With |
|----------|------|
| semantic search / embeddings | intent matching |
| vector similarity score | how confident the system is |
| classifier inference | interpreting the query |
| p99 latency | slowest 1% of requests — unchanged |
| feature flag | on/off switch |

Hook applied: **contrast** — Slide 2 opens with the exact before/after mismatch (user language vs. product language). This is the "wow" moment for the design team.

Mixed vocabulary: technical precision preserved for Eng slides (4, 5), business outcomes framing for PM slides (1, 6), experience framing for Design slides (2, 3). ✅

---

### Step 5 — critique-deck

| Dimension | Score | Verdict |
|-----------|-------|---------|
| Clarity | 9/10 | Each slide addresses one primary audience without losing the others |
| Narrative Flow | 9/10 | PSP arc holds — problem is felt before solution is shown |
| Audience Fit | 8/10 | Mixed audience handled well; slide 5 is dense for PM |
| "So What" | 9/10 | Every slide has a clear takeaway per audience segment |
| Call-to-Action | 9/10 | Specific ask (PM sign-off, then feature flag) with a clear owner |
| Emotional Resonance | 8/10 | Slide 2 (the contrast) is the emotional anchor for design + PM |

**Overall: 8.7/10 — Ship it.**

**Minor issue:** Slide 5 (tradeoffs) reads technical for PM. Consider adding a one-line summary at the top: "None of these affect users today — here's what to watch." This lets PM skim and trust the detail is there if needed.
