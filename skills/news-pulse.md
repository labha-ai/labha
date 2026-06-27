# News Pulse: Price-Move Rapid Attribution

$ARGUMENTS just moved sharply. Figure out why in 10–15 minutes. Not deep research — rapid attribution to avoid panic or irrational reaction.

## Philosophy

When a stock moves sharply, most investors do one of two things: panic-sell, or write a 2,000-word anxiety essay. Both are wrong. The right move is to quickly determine: **is this a value event or noise?** Only value events require action.

## Execution

### Step 1: Establish baseline

From $ARGUMENTS, identify:
- Company and approximate move (e.g., "Zomato -8% today", "Reliance +5% this week")
- Time window: intraday / 1 week / 1 month

Current price and volume vs average volume:
```bash
python3 ~/labha/tools/india_data.py quote {TICKER}
```

High volume + big move = institutional activity. Low volume + big move = thin liquidity / algo trigger.

### Step 2: Four-dimensional parallel scan

Scan all four dimensions simultaneously:

**Dimension 1 — Company-specific events**
- BSE/NSE announcements in the last 48 hours (bulk/block deals, insider trading, board changes)
- Any new SEBI filing or disclosure
- Promoter buying/selling
- Rating agency action (CRISIL, ICRA, CARE)
- Management interviews or conference appearances

**Dimension 2 — Regulatory and policy**
- SEBI, RBI, CCI, sector regulator news
- Ministry announcements affecting the sector
- Union Budget / state government policy if relevant
- Court orders or NCLT proceedings

**Dimension 3 — Industry and competitors**
- Did a competitor report results?
- Did a comparable company move similarly? (If yes → sector/macro, not company-specific)
- New competitor announcement (funding, launch, pricing change)
- Supply chain disruption

**Dimension 4 — Market sentiment and flows**
- Nifty / Sensex direction on that day (did the whole market move?)
- FII/DII flow data for the sector
- Any major global event (US Fed, China PMI, crude oil spike)
- Index rebalancing (addition/removal from Nifty 50, MSCI India)

### Step 3: Attribution

Identify the primary cause and quantify its contribution:

| Candidate Explanation | Estimated Contribution | Confidence |
|---|---|---|
| | | High / Medium / Low |

### Step 4: Classify the move

**Value Event** — changes long-term earnings power → requires thesis re-evaluation
**Sentiment Fluctuation** — affects price without changing business → monitor
**True Cause Unknown** — no clear explanation found → potential insider front-running; flag and watch
**Mixed** — multiple factors, state estimated split

### Step 5: Action recommendation

| Question | Answer |
|---|---|
| Nature of move | Value Event / Sentiment / Unknown / Mixed |
| Does this change the thesis? | Yes / No / Uncertain |
| Recommended action | Hold / Add on dip / Reduce / Investigate further |
| Key thing to watch | |
| Trigger for deeper research | |

## Output format

**One-line attribution** (lead with this):
> "Approximately X% of this [move] was driven by [primary cause]. [Secondary factor] contributed Y%. [If applicable: no fundamental change to the business.]"

Then the full attribution table and recommendation.

Keep it under 600 words. This is a rapid tool — depth comes later if warranted.

## When to upgrade to deep research

| Scenario | Next Step |
|---|---|
| Value event confirmed | `/investment-research` or `/earnings-review` |
| Thesis materially challenged | `/thesis-tracker` update |
| Move unexplained after 30 min search | Flag as "Unknown" — potential information asymmetry — do NOT act |
| Sentiment / macro only | No action needed — hold unless thesis broken |
