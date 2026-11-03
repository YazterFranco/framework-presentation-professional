# Example: Kiro Crew explicado a audiencia mixta (AIDA)

**Scenario:** Presentar cómo funciona Kiro Crew paso a paso a una sala mixta —
personas técnicas (devs, engineers) y no-técnicas (managers, PMs, directores)
en tecnología, con poco tiempo de atención porque están en muchas reuniones.

**Profile:** `internal-demo` · AIDA · 6 slides · ~10 min

---

## Pipeline output

### Step 1 — analyze-audience

```json
{
  "profile_type": "internal-demo",
  "attention_span_slides": 6,
  "vocabulary": "mixed",
  "primary_goals": [
    "entender qué hace Kiro Crew en términos concretos",
    "saber si les sirve a ellos",
    "decidir si lo prueban"
  ],
  "what_they_care_about": [
    "cuánto tiempo les ahorra",
    "si funciona con su stack / flujo actual",
    "qué tan difícil es empezar"
  ],
  "what_loses_them": [
    "features list sin contexto de cuándo usarlas",
    "marketing language (revolucionario, game-changer)",
    "demos demasiado largas sin punto claro",
    "arquitectura interna antes del value prop"
  ],
  "recommended_framework": "AIDA",
  "tone": "conversational",
  "hook_type": "contrast"
}
```

**Por qué AIDA:** Audiencia mixta no comparte el mismo contexto técnico. AIDA
engancha a ambos con el mismo contraste (Attention), nombra el problema que
cada uno vive desde su perspectiva (Interest), muestra el sistema con un
meta-ejemplo real (Desire), y cierra con una apuesta de 15 minutos (Action).

---

### Step 2 — build-narrative (AIDA · 6 slides)

| Slide | Slot | Audiencia primaria | Hook |
|-------|------|--------------------|------|
| 1 | Attention | Ambas | Contraste 45 min vs 3 min |
| 2 | Interest | Dev (visceral) + Manager (sistémico) | Dos perspectivas del mismo problema |
| 3 | Desire — sistema | Ambas | Analogía del dev senior siempre disponible |
| 4 | Desire — en acción | Técnica | Meta-ejemplo: este deck fue generado por el pipeline |
| 5 | Desire — conceptos | Ambas | 3 building blocks (no 5 — fix del critique) |
| 6 | Action | Diferenciada (dev / manager) | Apuesta de 15 minutos |

---

### Step 3 — compose-slides + Step 4 — humanize-content

Ver [`slides.md`](slides.md) — formato compose-slides completo con speaker notes.

**HUMANIZER NOTES — Términos ajustados para audiencia mixta:**

| Técnico | Versión accesible | Dónde |
|---------|-------------------|-------|
| LLM / modelo de lenguaje | agente de desarrollo | Slide 3 |
| context window | lo que Kiro "recuerda" | Slide 3 |
| spawn subagents | delegar trabajo a agentes independientes | Slide 3, 5 |
| workflow_rerun_subtree | reiniciar desde la fase que falló | Slide 5 |
| cron_add / cron_expr | tarea recurrente automatizada | Slide 5 |

**Hook aplicado: contrast** — Slide 1 abre con 45 min vs 3 min.
Funciona para el dev que lo vive y el manager que observa las consecuencias.

---

### Step 5 — critique-deck

| Dimensión | Score | Veredicto |
|-----------|-------|-----------|
| Clarity | 9/10 | Un mensaje por slide, títulos accionables |
| Narrative Flow | 9/10 | AIDA limpio, tensión en slide 2 |
| Audience Fit | 8/10 | Mixto bien manejado; slide 5 reducido a 3 bullets (fix aplicado) |
| "So What" | 9/10 | Cada slide tiene consecuencia para ambas audiencias |
| Call-to-Action | 9/10 | Dos acciones concretas (dev / manager) + apuesta 15 min |
| Emotional Resonance | 7/10 | Meta-ejemplo es el momento más fuerte del deck |

**Overall: 8.7/10 — Ship it.**

**Fix crítico aplicado:** Slide 5 reducido de 5 bullets a 3 (Skills, Workflows, Crons).
Artifacts y Subagents mencionados de viva voz como "para cuando los necesites."

---

## Output files

| Archivo | Formato | Cómo usar |
|---------|---------|-----------|
| [`kiro-crew-explicado.html`](kiro-crew-explicado.html) | Reveal.js | Doble-click → browser. `F` fullscreen, `S` speaker notes, `Space` avanzar |
| [`kiro-crew-explicado.pptx`](kiro-crew-explicado.pptx) | PowerPoint | PowerPoint / Google Slides / Keynote. Presenter View para notas |
| [`slides.md`](slides.md) | Markdown | Fuente en formato compose-slides — editable y re-exportable |

---

## Meta-nota

Este ejemplo es especial: el deck explica Kiro Crew, y fue generado **usando** Kiro Crew
con el pipeline de este mismo framework. El Slide 4 hace referencia a eso explícitamente —
es el momento más efectivo del deck para audiencias técnicas.
