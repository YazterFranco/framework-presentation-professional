# Skill: analyze-audience

## Purpose
Profile an audience so every subsequent decision (framework, language, depth, slide count) is grounded in who will actually be in the room.

## Trigger
Use this skill when the user provides a raw description of their audience (e.g., "my CEO and CFO", "a VC who doesn't know our tech", "my team of senior engineers").

## Steps

### 1. Extract signals
From the user's description, identify:
- **Role/seniority** — executive, manager, IC, investor, external customer?
- **Domain familiarity** — know the technical domain? The business domain? Neither?
- **Motivation** — what problem are THEY trying to solve by being in this meeting?
- **Decision power** — will they approve, fund, act, or just listen?
- **Time pressure** — how many slides/minutes before they check their phone?

### 2. Map to profile type
| Signals | Profile |
|---------|---------|
| C-suite / VP, non-technical | `tech-to-exec` |
| Investor, non-technical | `tech-to-investor` |
| Engineers, same domain | `tech-to-tech` |
| Mixed team (product, design, eng) | `internal-demo` |
| Learning audience (conference, class) | `workshop` |

### 3. Output the profile
Produce a structured JSON block:

```json
{
  "profile_type": "<type>",
  "attention_span_slides": <number 3-15>,
  "vocabulary": "<business_outcomes|technical|mixed>",
  "primary_goals": ["<what they want from this meeting>"],
  "what_they_care_about": ["<business concerns, not tech>"],
  "what_loses_them": ["<anti-patterns for this audience>"],
  "recommended_framework": "<SCQA|Pyramid|AIDA|Problem-Solution-Proof>",
  "tone": "<formal|conversational|data-driven>",
  "hook_type": "<number|story|contrast|question|consequence>"
}
```

### 4. Explain the choices (brief)
In 3-4 sentences, explain WHY you chose that framework for that audience. This teaches the user the reasoning.

## Rules
- Never pick a framework that matches the speaker's comfort — always pick for the audience.
- If attention span ≤ 5 slides, force the one-pager template.
- `tech-to-exec`: always recommend SCQA, never more than 7 slides.
- `tech-to-investor`: AIDA or SCQA, end with a clear "ask" slide.
- `tech-to-tech`: Pyramid OK, no artificial simplification.

## Example
**Input:** "I need to explain to our VP of Sales why we need 3 more engineers. She doesn't care about the tech stack."

**Output:**
```json
{
  "profile_type": "tech-to-exec",
  "attention_span_slides": 5,
  "vocabulary": "business_outcomes",
  "primary_goals": ["understand the business case", "make a budget decision"],
  "what_they_care_about": ["revenue impact", "timeline", "cost vs. benefit"],
  "what_loses_them": ["system architecture", "technical debt details", "language choices"],
  "recommended_framework": "SCQA",
  "tone": "formal",
  "hook_type": "consequence"
}
```
Framework chosen because SCQA leads with the business reality (Situation), names the risk (Complication), and delivers the ask (Answer) — no technical detour required.
