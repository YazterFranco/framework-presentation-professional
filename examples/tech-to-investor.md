# Example: Tech Founder → Non-Technical Investor (AIDA)

**Scenario:** A solo technical founder needs to pitch their AI-powered legal document
review tool to a VC partner who has no legal or technical background.
The meeting is 10 minutes. No deck was requested — the founder has 5 slides max.

---

## Pipeline output

### Step 1 — analyze-audience

```json
{
  "profile_type": "tech-to-investor",
  "attention_span_slides": 5,
  "vocabulary": "business_outcomes",
  "primary_goals": [
    "assess market size and defensibility",
    "understand founder credibility",
    "decide whether to schedule a deeper diligence call"
  ],
  "what_they_care_about": [
    "TAM / market size",
    "traction and early validation",
    "why this team wins",
    "path to $100M+ revenue"
  ],
  "what_loses_them": [
    "how the AI model works technically",
    "LLM architecture details",
    "accuracy benchmarks without context",
    "legal jargon"
  ],
  "recommended_framework": "AIDA",
  "tone": "conversational",
  "hook_type": "number"
}
```

**Why AIDA:** Investors see dozens of pitches. They don't need context — they need to be grabbed in 10 seconds (Attention), then pulled into the problem (Interest), then made to want the outcome (Desire), then asked for a specific next step (Action). SCQA assumes shared context; investors often don't have it. AIDA earns it.

---

### Step 2 — build-narrative

**Framework:** AIDA
**Slide count:** 5

| Slide | Slot | Purpose |
|-------|------|---------|
| 1 | Attention | One number that reframes how big this problem is |
| 2 | Interest | The pain — experienced by someone they can picture |
| 3 | Desire | What we built + early proof it works |
| 4 | Desire (continued) | Why we win — market timing + defensibility |
| 5 | Action | The ask + what happens next |

---

### Step 3 — compose-slides

---

#### Slide 1 — Attention
**Title:** Every business signs contracts they don't fully understand — and it costs $9.4B a year in legal disputes.
**Format:** big-number
**Content:**
- $9.4B: annual cost of commercial contract disputes in the US (Thomson Reuters, 2024)
- 62% of SMBs sign contracts without legal review — because lawyers cost $400+/hour
- We built the $400/hour lawyer for the price of a SaaS subscription
**Visual:** Single large number "$9.4B" centered, source line below
**Speaker note:** "I want to start with a number. Nine point four billion dollars. That's what businesses lose every year because they signed contracts they didn't understand. Not because they're careless — because getting a lawyer to review every vendor contract costs more than most contracts are worth. That's the gap we're filling."

---

#### Slide 2 — Interest
**Title:** A restaurant owner signs a POS vendor contract with a hidden auto-renewal clause — and loses $18,000.
**Format:** story
**Content:**
- True story: Maria, owner of 3 restaurants, signed a 3-year POS contract in 2023
- Hidden clause: auto-renews at 40% price increase unless canceled 90 days before expiry
- She found out when the invoice arrived — $18K she couldn't dispute
**Visual:** No visual needed — the story carries it
**Speaker note:** "This isn't a hypothetical. Maria is a real customer who found us after it happened. She's not unusual — she's the rule. Small business owners are not unsophisticated. They're just not lawyers. And right now, the only protection they have is a $400-an-hour professional they can't afford."

---

#### Slide 3 — Desire
**Title:** LegalLens reviews any contract in 90 seconds and flags every clause that could cost you money.
**Format:** contrast
**Content:**
- Before LegalLens: 3 days + $400+ to review a standard vendor contract
- With LegalLens: 90 seconds, $12/month, plain-language summary + risk score
- 340 paying customers, $14K MRR, NPS 72
**Visual:** Side-by-side: "Before" (calendar with 3 days, dollar sign) vs "After" (90-second timer, green checkmark)
**Speaker note:** "Here's what we built. You upload a contract, it reads it, and in 90 seconds you get a plain-English summary of every clause that matters — renewals, penalties, liability caps, IP ownership. Our customers call it 'the thing their lawyer should have told them.' 340 customers are paying us $12 a month for that. MRR is $14K and growing 18% month-over-month."

---

#### Slide 4 — Desire (Why we win)
**Title:** Legal AI that explains instead of generates is 3 years ahead of where competitors are focused.
**Format:** bullets
**Content:**
- Every major player (Harvey, Ironclad, Spellbook) is targeting law firms — not the 33M SMBs without legal teams
- Our moat: proprietary risk-scoring model trained on 2.1M US commercial contracts
- Switching cost: customers build contract history in our platform — average 47 contracts after 6 months
**Visual:** Market map: "Law Firms" quadrant (crowded) vs "SMB / No Legal Team" quadrant (LegalLens alone)
**Speaker note:** "The enterprise legal AI space is crowded. We made a deliberate choice to go the other direction — toward the 33 million small businesses that have no legal team at all. Our competitors are training models to write contracts. We train ours to explain them. That's a different product, different distribution, and a customer who has no alternative to us."

---

#### Slide 5 — Action
**Title:** We're raising a $1.5M pre-seed to reach $100K MRR — and we're 60% committed.
**Format:** bullets
**Content:**
- Raising $1.5M pre-seed at $8M cap SAFE
- Use of funds: 2 engineers + 6-month runway to $100K MRR
- 60% committed from 3 angels — looking for one lead to close the round
**Visual:** No visual needed
**Speaker note:** "We're raising $1.5M. We're 60% there with angels who came in after seeing the traction. I'm looking for one lead investor who wants to own this category before it's obvious. The ask today: a 30-minute diligence call with your partner who covers fintech or SMB. Can we schedule that before the end of the week?"

---

### Step 4 — humanize-content

**HUMANIZER NOTES:**
| Replaced | With |
|----------|------|
| LLM / language model | AI that reads contracts |
| NLP pipeline | how it understands the text |
| fine-tuned | trained specifically for |
| vector embeddings | contract memory |
| inference latency | how fast it processes |

Hook applied: **number** — Slide 1 opens with $9.4B, the most arresting fact in the deck.
Reading level: all sentences ≤ 14 words. Bullets start with numbers or nouns. ✅

---

### Step 5 — critique-deck

| Dimension | Score | Verdict |
|-----------|-------|---------|
| Clarity | 9/10 | One idea per slide, action titles carry the full argument |
| Narrative Flow | 9/10 | AIDA arc clean — tension in slide 2, resolution in slide 3 |
| Audience Fit | 9/10 | No technical terms, all business-language |
| "So What" | 8/10 | Each slide answers it; slide 4 slightly dense |
| Call-to-Action | 9/10 | Specific ask ($1.5M, 60% committed, 30-min call) |
| Emotional Resonance | 9/10 | Maria's story in slide 2 is the emotional anchor |

**Overall: 8.8/10 — Ship it.**

**Minor issue:** Slide 4 ("Why we win") has 3 dense bullets — consider making the market map visual do more work so the slide breathes. Rewrite: lead with the market map visual and cut to 2 bullets.
