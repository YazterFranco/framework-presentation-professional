# Skill: render-pptx

## Purpose
Convert a composed slide deck (markdown format from `compose-slides` or `humanize-content`)
into a `.pptx` file using python-pptx. The output is a real PowerPoint file that can be
opened in Microsoft Office, Google Slides, or Keynote.

## Trigger
Use after `humanize-content` (or `revise`) produces the final slides, or when the user
says "export as PowerPoint" / "make a .pptx" / "I need a PowerPoint file".

## Inputs
- `slides_final` — the full slide deck in compose-slides markdown format
- `audience_profile` — JSON from `analyze-audience` (for theme selection)
- `title` — presentation title (used in cover slide and file name)
- `output_path` — where to write the .pptx (default: `output/<title-slug>.pptx`)

## Dependencies
- `python-pptx==1.0.2` — must be installed in the active Python environment
- Check: `python3 -c "import pptx; print(pptx.__version__)"`
- Install: `pip install python-pptx==1.0.2`

## Steps

### 1. Invoke the generator script
Run the script at `scripts/generate_pptx.py` with the slide data as JSON:

```bash
python3 scripts/generate_pptx.py \
  --slides slides_final.md \
  --profile audience_profile.json \
  --title "Your Presentation Title" \
  --output output/your-presentation.pptx
```

### 2. Theme selection
Based on `audience_profile.tone`:

| Tone | Background | Title color | Accent | Body font |
|---|---|---|---|---|
| `formal` | White `#FFFFFF` | Dark navy `#1A1A2E` | Blue `#4A6CF7` | Calibri |
| `conversational` | Light gray `#F8F9FA` | Dark `#212529` | Indigo `#6366F1` | Calibri |
| `data-driven` | White `#FFFFFF` | Dark `#111111` | Teal `#0D9488` | Calibri |

### 3. Slide layout per format

| compose-slides format | PPTX layout | Notes |
|---|---|---|
| `bullets` | Title + Content | Up to 3 bullets, 20pt font |
| `big-number` | Title Only | Giant number (80pt) + context line (18pt) |
| `contrast` | Two Content | Left = before, Right = after, labeled |
| `steps` | Title + Content | Numbered list, auto-numbered |
| `story` | Title Only | Italic paragraph, 22pt, centered |

### 4. Required slides
- **Slide 0 (Cover):** Title (48pt), audience profile label, framework + slide count
- **Slides 1–N:** From the compose-slides output
- **No thank-you slide** — replace with the Ask slide content if present

### 5. Speaker notes
Every slide gets its speaker note added to the PPTX notes pane.
Presenters can view them in Presenter View (Slide Show → Presenter View).

## Output

```
output/
  <title-slug>-<profile_type>.pptx
```

File is self-contained — fonts embedded, no external assets required.

## After generating
1. State the file path
2. List what to check before presenting:
   - Open in target app (PowerPoint / Google Slides / Keynote) to verify layout
   - Check that fonts rendered correctly (Calibri is universally available)
   - Test Presenter View for speaker notes
3. Note any slides that used `[no visual needed]` direction — those are candidates
   for adding a chart or image before the real presentation

## Rules
- Never use unpinned package versions — always `python-pptx==1.0.2`
- Slide dimensions: 16:9 widescreen (13.33" × 7.5") — set explicitly in script
- Body copy hard limit: 40 words per slide (same as compose-slides rule)
- Bullet font size: 20pt for exec audiences, 18pt for internal/demo
- Never add slide transitions or animations — they rarely survive cross-app opens

## Kiro Crew + Crons (Phase 6 learning concept)
Once this skill works, you can schedule recurring deck generation with a cron:

```python
# ~/.kiro/crew/crons/weekly_update_deck.py
def generate_weekly_deck(ctx):
    """Regenerate the weekly team update deck every Monday at 8am."""
    # ctx.message contains the cron trigger context
    ctx.notify("Weekly update deck regenerated — check output/weekly-update.pptx")
```

Register with:
```
cron_add(
  name="weekly-update-deck",
  cron_expr="0 8 * * MON",
  message="Regenerate weekly update presentation",
  script="~/.kiro/crew/crons/weekly_update_deck.py:generate_weekly_deck"
)
```
