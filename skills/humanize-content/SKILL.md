# Skill: humanize-content

## Purpose
Rewrite slide content so it lands with the specific audience — removes jargon, adds hooks, adjusts reading level, makes it feel like a person talking, not a document being read aloud.

## Trigger
Use after `compose-slides` produces a draft, or when the user says "this is too technical" / "make it simpler" / "make it sound more human".

## Inputs
- `slides_draft` — raw slide content (titles + bullets + speaker notes)
- `audience_profile` — JSON from `analyze-audience`

## Steps

### 1. Jargon sweep
For each slide, identify technical terms. For each one:
- If the audience profile shows `vocabulary: business_outcomes` → replace with business equivalent
- If the audience can't understand the concept without the term → add a one-sentence plain-language definition on first use

**Common replacements for tech-to-exec:**
| Technical | Human |
|-----------|-------|
| API latency | response time / slowness |
| microservices | independent building blocks |
| CI/CD pipeline | automated quality checks |
| technical debt | shortcuts we'll pay for later |
| infrastructure | the servers and systems that run everything |
| sprint | 2-week work cycle |
| refactor | rebuild it the right way |

### 2. Apply the hook type
Based on `audience_profile.hook_type`, rewrite the opening of slide 1:

- **number** → lead with the most striking metric ("$2.4M left on the table every quarter")
- **story** → open with a 2-sentence scenario the audience recognizes ("Imagine you're a customer who can't check out on a Friday night...")
- **contrast** → before/after, us/them, now/future ("Today it takes 4 weeks. With this change: 3 days.")
- **question** → a question they can't easily answer ("How many customers did we lose last month because the app was slow?")
- **consequence** → what happens if nothing changes ("If we don't act by Q2, we'll miss the launch window entirely.")

### 3. Reading level check
For `tech-to-exec` and `tech-to-investor`:
- Average sentence ≤ 15 words
- No sentences with embedded clauses ("The system, which was built using X, does Y")
- Bullets start with action verbs or numbers

### 4. Voice consistency
Match tone from `audience_profile.tone`:
- **formal** — third person where appropriate, no contractions, precise language
- **conversational** — first person plural ("we"), contractions OK, direct address ("you")
- **data-driven** — every claim has a number or a source, no vague qualifiers

### 5. Speaker notes humanization
Speaker notes are what you SAY, not what the slide reads.
- Rewrite to sound like natural speech
- Add transitions ("The reason this matters is...", "Let me give you a concrete example...")
- Flag where to pause, where to ask a question, where to check in with the audience

## Output
Return the full revised slide deck with:
- Revised titles
- Revised bullets (max 3 per slide, max 10 words per bullet)
- Revised speaker notes
- A `[HUMANIZER NOTES]` section at the end listing every jargon term replaced and why

## Rules
- Never simplify for a `tech-to-tech` audience — preserve precision.
- Never add humor unless `tone: conversational` and the user explicitly OK'd it.
- A slide with more than 40 words on it is a failed slide — cut, don't trim.
- One idea per slide. If a slide covers two ideas, split it.
