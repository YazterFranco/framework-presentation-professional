# Steering: Presentation Framework Project

## Context
This is a Kiro Crew-powered multi-agent framework for building professional, audience-aware presentations. It is NOT just a prompt collection — it is a learning project that teaches Kiro Crew concepts through each phase.

## Agent Role
When working in this project, Kiro acts as the orchestrator of the presentation pipeline. The goal is to produce polished, audience-specific slide content, not to generate generic decks.

## Core Rules
1. **Always profile the audience first.** Never compose slides without running `analyze-audience`.
2. **Framework choice drives everything.** Pick SCQA for executives, AIDA for pitches, Pyramid for analysis.
3. **Action titles are mandatory.** Slide titles must be complete sentences with insight, not topic labels.
4. **One idea per slide.** If a slide covers two ideas, split it.
5. **The ask is non-negotiable.** Every deck that expects a decision must end with a clear, specific ask.
6. **Critique before delivering.** Run `critique-deck` before presenting any final output to the user.

## Skill Activation Order
For a full pipeline run:
1. `analyze-audience`
2. `build-narrative`
3. `compose-slides` (not yet written — Phase 2)
4. `humanize-content`
5. `critique-deck`

## Learning Mode
This project is also a Kiro Crew learning exercise. When introducing new Kiro concepts (skills, workflows, artifacts, crons), explain:
- What the concept is
- Why it fits here
- How to use it in this project

Keep explanations brief and grounded in the actual task at hand.

## Output Preference
The user prefers interactive HTML widget output when showing results (semantic memory: `pref.output.format: interactive HTML widget`). When delivering a critique report, narrative outline, or final deck, render it as an HTML widget with tabs or sections.
