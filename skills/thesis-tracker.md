# Thesis Tracker: Post-Buy Discipline System

Track and update the investment thesis for $ARGUMENTS. This is the discipline system for after you buy — not before.

## Philosophy

Most investors have good entry discipline but no exit discipline. They hold positions long after the thesis has broken because they haven't written it down and can't see it being falsified. This tracker forces the written thesis to exist, and then actively tests it against new information.

## Execution

### Step 1: Establish or retrieve the thesis

If a thesis file already exists at `reports/{Company}/{Company}-thesis.md`, retrieve and display it.

If not, create one:

**Core thesis (3–5 sentences max):**
State why you own this stock. Specific, falsifiable, not vague.

❌ Vague: "Reliance is a great company with diversification across businesses."
✅ Specific: "Reliance Jio is on track to be the dominant 5G and fixed broadband provider in India, creating a recurring ₹80,000+ Cr revenue base. The Retail segment will reach profitability and begin returning cash. At current price, the market is undervaluing the Jio optionality. Thesis breaks if Jio ARPU growth stalls below ₹200 or Retail fails to reach 10% EBIT margin by FY28."

**3–5 specific falsifiers** (what would prove you wrong):
1. [Specific metric or event that would break this thesis]
2. ...

**Entry price and date:**
**Current position size:**
**Target horizon:**

### Step 2: New information assessment

Based on the latest developments (earnings, news, competitor moves, regulatory):

| Development | Confirms / Neutral / Challenges Thesis | Severity |
|---|---|---|
| | | High / Medium / Low |

### Step 3: Falsifier check

For each stated falsifier:

| Falsifier | Current Status | Risk Level |
|---|---|---|
| | Intact / Approaching / Triggered | Low / Medium / High |

### Step 4: Thesis status verdict

- **✅ Intact**: All falsifiers intact, core thesis progressing as expected → Hold or Add
- **⚠️ Weakening**: 1–2 falsifiers approaching, thesis slower than expected → Hold with monitoring, no add
- **🔴 Broken**: A falsifier has been triggered → Exit regardless of price

**The hardest discipline**: exit when the thesis breaks, even if the stock price hasn't moved yet.

### Step 5: Updated thesis (if changed)

If thesis has evolved, write the updated version explicitly. Mark what changed and why.

### Step 6: Action recommendation

| Recommendation | Condition |
|---|---|
| Add | Thesis intact + price dipped below entry / new margin of safety |
| Hold | Thesis intact, valuation fair |
| Hold / Watch | Thesis weakening, no new add |
| Exit | Thesis broken — price is irrelevant |
| Exit partially | One segment of thesis broken, other intact |

## File format

Keep `reports/{Company}/{Company}-thesis.md` updated with each review. Append dated entries — never overwrite old ones. The historical record of thesis evolution is itself valuable.

```
## Thesis as of {YYYY-MM-DD}
[current thesis]

## Falsifiers
[list]

## Review log
### {date}: [what changed and verdict]
### {date}: [what changed and verdict]
```

## Cadence

Review after: every earnings release, any major news event, and at minimum once per quarter.
