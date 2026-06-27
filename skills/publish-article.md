# Publish Article: Research → Readable Piece

Convert $ARGUMENTS (a research report or earnings analysis) into a publication-ready article for Substack, LinkedIn, or a personal investing newsletter.

Input: path to a research report, or a company + topic description.
Example: `reports/TCS/TCS-earnings-Q4FY26.md` or `Zomato moat analysis`

## Philosophy

Good investment research is dense and data-heavy by design. A publishable article is different — it must lead with the insight, tell a story, and make a non-expert care. This skill bridges the gap.

## Format Options

Specify your target platform:
- **Substack**: 800–1,500 words, narrative flow, data tables okay, personal voice
- **LinkedIn**: 400–600 words, punchy, no tables, 3–5 bullet points max
- **Thread** (X/Twitter): 8–12 tweets, each standalone but connected
- **Newsletter blurb**: 200–300 words, hook + 3 key findings + CTA

Default: Substack format.

## Execution

### Step 1: Identify the single most important finding

Every good article has one central idea. Everything else supports it.

From the research report, identify: **what is the one thing the reader should take away?**

- Not: "TCS had a mixed quarter"
- Yes: "TCS's deal wins hit a 6-quarter high while margins expanded — the market's pessimism is looking wrong"

### Step 2: Structure for the target platform

**Substack / Long-form:**
```
[Hook — 2-3 sentences that make you want to read more]

[Context — why does this company / result matter right now?]

[The key finding — with specific data]

[What the market is missing or getting wrong]

[The supporting evidence — 2-3 specific data points or observations]

[What to watch next — specific metrics or events]

[Bottom line — one clear takeaway]
```

**LinkedIn:**
```
[One punchy opening line]

[2-3 sentences of context]

Key findings:
• [Finding 1]
• [Finding 2]
• [Finding 3]

[One-sentence conclusion + question to drive engagement]
```

### Step 3: Data selection

From the full research report, select only the 3–5 data points that best support the central idea. Do not include every metric — only the most relevant.

### Step 4: Tone calibration

- Write for an intelligent Indian investor, not a financial professional
- No jargon without explanation
- ₹ figures in crore, clearly labelled
- Specific is better than general: "revenue grew 12% YoY to ₹23,000 Cr" beats "revenue grew"
- Honest about uncertainty: "if management's guidance proves accurate..." not "management will..."

### Step 5: Headline options

Generate 3 headline options:
1. Data-led: "[Specific metric]: What it means for [Company]"
2. Contrarian: "Why [Market consensus view] might be wrong"
3. Narrative: "[Company] just showed [something interesting]. Here's what to make of it."

## Output

Write the article to `reports/{Company}/{Company}-article-{YYYYMMDD}.md`

Include at the top: target platform, word count, and which research report it's based on.

## Disclosure reminder

Add at the end of every published piece:
> *This is not investment advice. I may hold positions in securities mentioned. Do your own research.*
