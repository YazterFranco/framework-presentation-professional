# Skill: render-html-reveal

## Purpose
Convert a composed slide deck (markdown format from `compose-slides` or `humanize-content`)
into a self-contained, single-file HTML presentation using Reveal.js. The output opens
in any browser, needs no internet connection, and can be saved as a Kiro Artifact.

## Trigger
Use after `humanize-content` (or `revise`) produces the final slides, or when the user
says "export as HTML" / "make it presentable" / "give me a file I can open".

## Inputs
- `slides_final` — the full slide deck in the compose-slides markdown format
- `audience_profile` — JSON from `analyze-audience` (used for theme selection)
- `title` — presentation title (used in `<title>` and cover slide)
- `speaker_notes` — include speaker notes in Reveal.js notes pane (default: true)

## Theme selection

Based on `audience_profile.tone`:

| Tone | Reveal.js theme | Rationale |
|---|---|---|
| `formal` | `white` with custom overrides | Clean, high-contrast — executive audiences |
| `conversational` | `night` with custom overrides | Warmer, modern — investor/demo audiences |
| `data-driven` | `simple` with custom overrides | Maximum whitespace for charts/data |

Always apply custom CSS overrides (see Output spec below) regardless of base theme.

## Steps

### 1. Parse the slide deck
For each slide in the markdown input, extract:
- `title` — the action title (becomes `<h2>`)
- `format` — bullets | contrast | big-number | steps | story
- `content` — the body (bullets, number, table, paragraph)
- `visual` — visual direction note (rendered as a `<!-- visual: ... -->` comment in source)
- `speaker_note` — goes into Reveal.js `<aside class="notes">` block

### 2. Map format → HTML structure

| Format | HTML pattern |
|---|---|
| `bullets` | `<ul class="reveal-bullets">` with `<li>` per bullet |
| `big-number` | `<div class="big-number">` + `<p class="context-line">` |
| `contrast` | `<div class="contrast-grid">` with two columns |
| `steps` | `<ol class="reveal-steps">` with `<li>` per step |
| `story` | `<p class="story-block">` (larger font, italic) |

### 3. Build the full HTML file

Structure:
```html
<!DOCTYPE html>
<html>
<head>
  <!-- Reveal.js CDN (pinned version) -->
  <!-- Custom CSS overrides -->
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Slide 0: Cover -->
      <section class="cover-slide">...</section>
      <!-- Slides 1–N from deck -->
      <section>...</section>
      ...
    </div>
  </div>
  <!-- Reveal.js init script -->
</body>
</html>
```

### 4. Cover slide (always first)
```html
<section class="cover-slide">
  <h1>[presentation title]</h1>
  <p class="audience-label">For: [profile_type label]</p>
  <p class="framework-label">[framework] framework · [N] slides</p>
</section>
```

### 5. Keyboard shortcuts to tell the presenter
- `Space` / `→` — next slide
- `S` — open speaker notes window (second monitor)
- `F` — fullscreen
- `ESC` — slide overview

## Output spec

### Required CSS overrides (apply to all themes)
```css
/* Typography */
.reveal h2 { font-size: 1.6em; line-height: 1.25; font-weight: 700; }
.reveal .big-number { font-size: 4em; font-weight: 800; line-height: 1; }
.reveal .context-line { font-size: 0.9em; opacity: 0.7; margin-top: 0.3em; }

/* Bullets */
.reveal .reveal-bullets { list-style: none; padding: 0; }
.reveal .reveal-bullets li { padding: 0.3em 0 0.3em 1.4em; position: relative; }
.reveal .reveal-bullets li::before { content: "→"; position: absolute; left: 0; opacity: 0.6; }

/* Contrast grid */
.reveal .contrast-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2em; }
.reveal .contrast-grid .before { opacity: 0.6; }
.reveal .contrast-grid .after { font-weight: 600; }

/* Steps */
.reveal .reveal-steps { counter-reset: step; list-style: none; padding: 0; }
.reveal .reveal-steps li { counter-increment: step; padding: 0.3em 0 0.3em 2em; position: relative; }
.reveal .reveal-steps li::before { content: counter(step); position: absolute; left: 0; font-weight: 800; opacity: 0.5; }

/* Story block */
.reveal .story-block { font-size: 1.1em; font-style: italic; line-height: 1.6; max-width: 80%; margin: 0 auto; }

/* Cover */
.reveal .cover-slide h1 { font-size: 2em; }
.reveal .audience-label, .reveal .framework-label { opacity: 0.55; font-size: 0.7em; margin-top: 0.5em; }

/* Progress bar override */
.reveal .progress { height: 4px; }
```

### Reveal.js init config
```javascript
Reveal.initialize({
  hash: true,
  slideNumber: 'c/t',
  showNotes: false,       // notes only in separate window (press S)
  transition: 'fade',
  transitionSpeed: 'fast',
  controls: true,
  progress: true,
  center: true,
  width: 1280,
  height: 720,
  margin: 0.1
});
```

### CDN versions to use (pinned)
```
Reveal.js: https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/reveal.min.js
CSS:       https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/reveal.min.css
Theme:     https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/theme/<theme>.min.css
```

## Output format

The skill produces a single `.html` file:
- Filename: `[title-slugified]-[profile_type].html`
- Self-contained: all CSS inline, JS from CDN (pinned version)
- Speaker notes embedded in `<aside class="notes">` blocks
- `<!-- visual: [direction] -->` comments preserved in source for future design pass

## Rules
- Never use unpinned CDN URLs — always use the version-locked paths above.
- The file must open correctly with no internet connection for the CSS overrides
  (CDN JS is acceptable — it only affects transitions, not readability).
- Never exceed 40 words of body copy per slide — if the input violates this, truncate
  to the first 3 bullets and add a `<!-- truncated: original had N bullets -->` comment.
- Preserve the action title exactly — do not rewrite titles during rendering.
- Speaker notes are always included in the HTML source even if `speaker_notes: false`
  is passed — they are just hidden from the main view.

## Delivery
After generating the HTML:
1. Show the user the file path
2. Render a preview of the first 2 slides as a static HTML snippet in the dashboard
3. List the keyboard shortcuts
4. Note: "Press S to open the speaker notes window on a second monitor"
