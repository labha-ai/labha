# Industry Funnel: Full Market → 3 Deep Dives

Screen the full investment universe for $ARGUMENTS down to 3 actionable picks with deep analysis.

## Philosophy

Most stock screens find the obvious — large caps with good recent performance. This funnel is designed to find what the screen misses: the right business at the right price, wherever it hides in the market cap spectrum.

## Execution

### Stage 1: Full market scan (30–60 companies)

Cast a wide net using all three entry points:
- **Activity signal**: high recent trading volume or analyst attention spike
- **Returns signal**: top performers and worst performers (contrarian opportunity) over 1Y/3Y
- **Market cap**: top 30 by market cap in the sector (includes established leaders)

Take the union. Target 30–60 companies. Include:
- NSE-listed companies
- BSE-listed companies not in NSE (often overlooked)
- Recently listed (last 2 years) — IPO candidates that haven't been discovered
- Note unlisted leaders that are IPO candidates

**AI bias check** — actively counter these biases at Stage 1:
- Large-cap bias: am I ignoring mid/small caps with better economics?
- English-language bias: am I missing regional companies with no English press coverage?
- Narrative bias: am I anchoring on "hot sector" names from social media?
- Listed-only bias: note the unlisted competitors that could make listed players irrelevant

### Stage 2: Rough cut — apply 5 hard filters → ≤10 companies

Every eliminated company must have a stated reason (not a black box):

| Filter | Bar | Rationale |
|---|---|---|
| 1. Profitability | ROE > 12% OR clear path to profitability within 2 years | Eliminate chronic loss-makers |
| 2. Debt | Net Debt/EBITDA < 4x (financials: adjust appropriately) | Avoid over-levered companies |
| 3. Promoter governance | No major fraud allegations, no auditor resignation in last 2 years | Binary quality filter |
| 4. Business model | Understandable in 1 sentence; not pure commodity | Circle of competence |
| 5. Valuation sanity | Not trading at > 5x revenue unless high-growth platform | Eliminate momentum-only plays |

Output: table of eliminated companies with reasons, and ≤10 survivors.

### Stage 3: Detailed analysis of ≤10 survivors (300–500 words each)

For each:
- Business model and moat (2–3 sentences of substance)
- Key financials: revenue CAGR 3Y, ROE, net margin, FCF yield
- Valuation: P/E, EV/EBITDA vs historical and peers
- Top risk (the single most important thing that could go wrong)
- Preliminary verdict: Proceed / Watch / Drop (with 1-line reason)

### Stage 4: Final 3 — selected for portfolio complementarity

**Critical**: do NOT pick the top 3 by score. Pick for **portfolio complementarity**:
- 1 high-certainty compounder (lower upside, very high confidence)
- 1 moderate-risk with meaningful upside
- 1 higher-risk with high convexity (could be a multi-bagger or zero)

Justify why these 3 complement each other better than the alternatives.

Also list: **Future IPO candidates** — unlisted companies in this space worth watching for listing.

### Stage 5: Deep analysis on final 3 (800–1,200 words each)

Full four-framework analysis per `/investment-research` modules 2–7:
- Business essence
- Moat assessment
- Inversion and risks
- Management quality
- Industry trend
- Valuation with three scenarios (tool-calculated)

### Stage 6: Portfolio recommendation

| Tier | Weight | Company | Entry Price Range | Trigger to Add |
|---|---|---|---|---|
| Core | 50% | | ₹ | |
| Satellite | 30% | | ₹ | |
| Option | 20% | | ₹ | |

## Output

Write to `reports/{Theme}-funnel-{YYYYMMDD}.md`

Every elimination must have a stated reason. The funnel is only credible if you can explain why you dropped each company, not just why you kept 3.
