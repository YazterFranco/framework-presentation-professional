#!/usr/bin/env python3
"""
generate_pptx.py — Part of the framework-presentation-professional pipeline.

Converts a compose-slides markdown deck into a .pptx file using python-pptx==1.0.2.
Called by the render-pptx skill.

Usage:
    python3 scripts/generate_pptx.py \
        --input  output/slides_final.md \
        --title  "Your Presentation Title" \
        --tone   formal \
        --output output/your-presentation.pptx

Slide markdown format expected (from compose-slides skill):
    ### Slide N — [Slot]
    **Title:** [action title]
    **Format:** [bullets|big-number|contrast|steps|story]
    **Content:**
    - bullet 1
    - bullet 2
    **Speaker note:** [text]
"""

import argparse
import re
import sys
from pathlib import Path

# ── Dependency check ──────────────────────────────────────────────────────────
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN
    from pptx.util import Inches, Pt
except ImportError:
    print("ERROR: python-pptx not installed.")
    print("Fix:   pip install python-pptx==1.0.2")
    sys.exit(1)


# ── Theme definitions ─────────────────────────────────────────────────────────

THEMES = {
    "formal": {
        "bg":        RGBColor(0xFF, 0xFF, 0xFF),   # white
        "title_fg":  RGBColor(0x1A, 0x1A, 0x2E),   # dark navy
        "body_fg":   RGBColor(0x33, 0x33, 0x33),   # near-black
        "accent":    RGBColor(0x4A, 0x6C, 0xF7),   # blue
        "muted":     RGBColor(0x88, 0x88, 0x99),   # gray
        "slot_fg":   RGBColor(0x4A, 0x6C, 0xF7),   # same as accent
        "title_pt":  28,
        "body_pt":   20,
        "note_pt":   14,
    },
    "conversational": {
        "bg":        RGBColor(0xF8, 0xF9, 0xFA),
        "title_fg":  RGBColor(0x21, 0x25, 0x29),
        "body_fg":   RGBColor(0x44, 0x44, 0x44),
        "accent":    RGBColor(0x63, 0x66, 0xF1),
        "muted":     RGBColor(0x88, 0x88, 0x99),
        "slot_fg":   RGBColor(0x63, 0x66, 0xF1),
        "title_pt":  28,
        "body_pt":   20,
        "note_pt":   14,
    },
    "data-driven": {
        "bg":        RGBColor(0xFF, 0xFF, 0xFF),
        "title_fg":  RGBColor(0x11, 0x11, 0x11),
        "body_fg":   RGBColor(0x33, 0x33, 0x33),
        "accent":    RGBColor(0x0D, 0x94, 0x88),   # teal
        "muted":     RGBColor(0x88, 0x88, 0x99),
        "slot_fg":   RGBColor(0x0D, 0x94, 0x88),
        "title_pt":  26,
        "body_pt":   18,
        "note_pt":   13,
    },
}

# Slide canvas: 16:9 widescreen
SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

# Layout margins
MARGIN_L = Inches(0.7)
MARGIN_T = Inches(0.55)
MARGIN_R = Inches(0.7)
CONTENT_W = SLIDE_W - MARGIN_L - MARGIN_R


# ── Markdown parser ───────────────────────────────────────────────────────────

def parse_slides(md_text: str) -> list[dict]:
    """
    Parse compose-slides markdown into a list of slide dicts.
    Each dict: {slot, title, format, content (list of str), speaker_note (str)}
    """
    slides = []

    # Split on slide headers: ### Slide N — Slot
    blocks = re.split(r"(?=^###\s+Slide\s+\d+)", md_text, flags=re.MULTILINE)

    for block in blocks:
        block = block.strip()
        if not block.startswith("###"):
            continue

        slide = {}

        # Slot from header line
        header_match = re.match(r"###\s+Slide\s+\d+\s+[—–-]+\s+(.+)", block)
        slide["slot"] = header_match.group(1).strip() if header_match else ""

        # Title
        title_match = re.search(r"\*\*Title:\*\*\s*(.+)", block)
        slide["title"] = title_match.group(1).strip().strip('"') if title_match else ""

        # Format
        fmt_match = re.search(r"\*\*Format:\*\*\s*(.+)", block)
        slide["format"] = fmt_match.group(1).strip().lower() if fmt_match else "bullets"

        # Content — everything between **Content:** and **Visual:** or **Speaker note:**
        content_match = re.search(
            r"\*\*Content:\*\*\s*\n(.*?)(?=\*\*Visual:\*\*|\*\*Speaker note:\*\*)",
            block, re.DOTALL
        )
        if content_match:
            raw = content_match.group(1).strip()
            # Extract bullet/step lines (lines starting with - or a number)
            items = re.findall(r"^[-\d]+[.)]\s*(.+)", raw, re.MULTILINE)
            slide["content"] = [i.strip() for i in items][:3]  # max 3 items
        else:
            slide["content"] = []

        # Speaker note
        note_match = re.search(r"\*\*Speaker note:\*\*\s*(.+?)(?=\n###|\Z)", block, re.DOTALL)
        slide["speaker_note"] = note_match.group(1).strip().strip('"') if note_match else ""

        slides.append(slide)

    return slides


# ── PPTX builder helpers ──────────────────────────────────────────────────────

def _set_bg(slide, color: RGBColor):
    """Fill slide background with a solid color."""
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_textbox(slide, left, top, width, height, text: str,
                 font_size: int, color: RGBColor, bold=False,
                 italic=False, align=PP_ALIGN.LEFT, word_wrap=True) -> None:
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = "Calibri"


def _add_slot_label(slide, slot: str, theme: dict):
    _add_textbox(
        slide,
        left=MARGIN_L, top=Inches(0.22),
        width=CONTENT_W, height=Inches(0.28),
        text=slot.upper(),
        font_size=10, color=theme["slot_fg"], bold=True,
    )


def _add_title(slide, title: str, theme: dict, top=Inches(0.52)):
    _add_textbox(
        slide,
        left=MARGIN_L, top=top,
        width=CONTENT_W, height=Inches(1.3),
        text=title,
        font_size=theme["title_pt"], color=theme["title_fg"], bold=True,
    )


def _add_accent_rule(slide, theme: dict, top=Inches(1.9)):
    """Thin colored rule under the title."""
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left=MARGIN_L, top=top,
        width=Inches(0.45), height=Inches(0.045),
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = theme["accent"]
    shape.line.fill.background()


def _add_speaker_note(slide, note: str):
    if note:
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = note


# ── Slide type renderers ──────────────────────────────────────────────────────

def render_cover(prs, title: str, profile_type: str, framework: str,
                 n_slides: int, theme: dict):
    blank_layout = prs.slide_layouts[6]  # blank
    slide = prs.slides.add_slide(blank_layout)
    _set_bg(slide, theme["bg"])

    # Large title, centered vertically
    _add_textbox(
        slide,
        left=MARGIN_L, top=Inches(2.2),
        width=CONTENT_W, height=Inches(2.2),
        text=title,
        font_size=36, color=theme["title_fg"], bold=True,
        align=PP_ALIGN.CENTER,
    )
    # Subtitle line
    subtitle = f"{profile_type}  ·  {framework}  ·  {n_slides} slides"
    _add_textbox(
        slide,
        left=MARGIN_L, top=Inches(4.55),
        width=CONTENT_W, height=Inches(0.4),
        text=subtitle,
        font_size=13, color=theme["muted"], align=PP_ALIGN.CENTER,
    )


def render_bullets(prs, slide_data: dict, theme: dict):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    _set_bg(slide, theme["bg"])
    _add_slot_label(slide, slide_data["slot"], theme)
    _add_title(slide, slide_data["title"], theme)
    _add_accent_rule(slide, theme)

    # Bullet list
    body_top = Inches(2.05)
    body_h = Inches(4.5)
    txBox = slide.shapes.add_textbox(MARGIN_L, body_top, CONTENT_W, body_h)
    tf = txBox.text_frame
    tf.word_wrap = True

    for i, bullet in enumerate(slide_data["content"][:3]):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.space_before = Pt(6)
        run = p.add_run()
        run.text = f"→  {bullet}"
        run.font.size = Pt(theme["body_pt"])
        run.font.color.rgb = theme["body_fg"]
        run.font.name = "Calibri"

    _add_speaker_note(slide, slide_data.get("speaker_note", ""))


def render_big_number(prs, slide_data: dict, theme: dict):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    _set_bg(slide, theme["bg"])
    _add_slot_label(slide, slide_data["slot"], theme)
    _add_title(slide, slide_data["title"], theme)
    _add_accent_rule(slide, theme)

    # Big number = first content item
    big = slide_data["content"][0] if slide_data["content"] else ""
    context = slide_data["content"][1] if len(slide_data["content"]) > 1 else ""

    _add_textbox(
        slide,
        left=MARGIN_L, top=Inches(2.1),
        width=CONTENT_W, height=Inches(1.8),
        text=big,
        font_size=80, color=theme["accent"], bold=True, align=PP_ALIGN.CENTER,
    )
    if context:
        _add_textbox(
            slide,
            left=MARGIN_L, top=Inches(3.95),
            width=CONTENT_W, height=Inches(0.6),
            text=context,
            font_size=16, color=theme["muted"], align=PP_ALIGN.CENTER,
        )

    _add_speaker_note(slide, slide_data.get("speaker_note", ""))


def render_contrast(prs, slide_data: dict, theme: dict):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    _set_bg(slide, theme["bg"])
    _add_slot_label(slide, slide_data["slot"], theme)
    _add_title(slide, slide_data["title"], theme)
    _add_accent_rule(slide, theme)

    col_w = (CONTENT_W - Inches(0.4)) / 2
    body_top = Inches(2.1)
    body_h = Inches(4.4)

    # Left column (Before)
    left_col_l = MARGIN_L
    left_label = slide_data["content"][0] if slide_data["content"] else "Before"
    _add_textbox(slide, left_col_l, body_top, col_w, Inches(0.35),
                 "BEFORE", 10, RGBColor(0xCC, 0x00, 0x44), bold=True)
    _add_textbox(slide, left_col_l, body_top + Inches(0.4), col_w, body_h,
                 left_label, theme["body_pt"], theme["body_fg"])

    # Right column (After)
    right_col_l = MARGIN_L + col_w + Inches(0.4)
    right_label = slide_data["content"][1] if len(slide_data["content"]) > 1 else "After"
    _add_textbox(slide, right_col_l, body_top, col_w, Inches(0.35),
                 "AFTER", 10, RGBColor(0x00, 0xAA, 0x77), bold=True)
    _add_textbox(slide, right_col_l, body_top + Inches(0.4), col_w, body_h,
                 right_label, theme["body_pt"], theme["body_fg"])

    # Divider line between columns
    div = slide.shapes.add_shape(
        1, left=MARGIN_L + col_w + Inches(0.18),
        top=body_top, width=Inches(0.04), height=body_h,
    )
    div.fill.solid()
    div.fill.fore_color.rgb = RGBColor(0xE0, 0xE0, 0xE8)
    div.line.fill.background()

    _add_speaker_note(slide, slide_data.get("speaker_note", ""))


def render_story(prs, slide_data: dict, theme: dict):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)
    _set_bg(slide, theme["bg"])
    _add_slot_label(slide, slide_data["slot"], theme)
    _add_title(slide, slide_data["title"], theme)
    _add_accent_rule(slide, theme)

    story_text = " ".join(slide_data["content"])
    _add_textbox(
        slide,
        left=MARGIN_L + Inches(0.5), top=Inches(2.2),
        width=CONTENT_W - Inches(1.0), height=Inches(4.0),
        text=story_text,
        font_size=22, color=theme["body_fg"], italic=True,
        align=PP_ALIGN.CENTER,
    )
    _add_speaker_note(slide, slide_data.get("speaker_note", ""))


def render_steps(prs, slide_data: dict, theme: dict):
    # Steps use same layout as bullets but with numbered prefix
    for i, item in enumerate(slide_data["content"]):
        slide_data["content"][i] = f"{i+1}.  {item}"
    slide_data["format"] = "bullets"
    render_bullets(prs, slide_data, theme)


# ── Main builder ──────────────────────────────────────────────────────────────

RENDERERS = {
    "bullets":    render_bullets,
    "big-number": render_big_number,
    "contrast":   render_contrast,
    "story":      render_story,
    "steps":      render_steps,
}


def build_pptx(slides: list[dict], title: str, tone: str,
               profile_type: str, framework: str, output_path: Path) -> Path:
    theme = THEMES.get(tone, THEMES["formal"])

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # Cover slide
    render_cover(prs, title, profile_type, framework, len(slides), theme)

    # Content slides
    for slide_data in slides:
        fmt = slide_data.get("format", "bullets")
        renderer = RENDERERS.get(fmt, render_bullets)
        renderer(prs, slide_data, theme)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(output_path))
    return output_path


# ── CLI entry point ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate a .pptx from a compose-slides markdown deck."
    )
    parser.add_argument("--input",   required=True, help="Path to slides markdown file")
    parser.add_argument("--title",   required=True, help="Presentation title")
    parser.add_argument("--tone",    default="formal",
                        choices=["formal", "conversational", "data-driven"],
                        help="Audience tone (determines theme)")
    parser.add_argument("--profile", default="tech-to-exec",
                        help="Audience profile type label (display only)")
    parser.add_argument("--framework", default="SCQA",
                        help="Narrative framework used (display only)")
    parser.add_argument("--output",  required=True, help="Output .pptx path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    slides = parse_slides(md_text)

    if not slides:
        print(f"ERROR: no slides parsed from {input_path}")
        print("Check that slide headers match: ### Slide N — SlotName")
        sys.exit(1)

    output_path = Path(args.output)
    result = build_pptx(
        slides=slides,
        title=args.title,
        tone=args.tone,
        profile_type=args.profile,
        framework=args.framework,
        output_path=output_path,
    )

    print(f"✓ Generated: {result}")
    print(f"  Slides:    {len(slides)} content slides + 1 cover")
    print(f"  Theme:     {args.tone}")
    print(f"  Open in:   PowerPoint, Google Slides, or Keynote")
    print(f"  Notes:     Presenter View → View → Notes (or Alt+W, P in PPT)")


if __name__ == "__main__":
    main()
