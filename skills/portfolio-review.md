# Portfolio Review: Position Sizing and Rebalancing

Review and optimise the portfolio described in $ARGUMENTS.

**Input format**: `Company A X%, Company B Y%, Cash Z%`
Example: `Reliance 30%, TCS 20%, HDFC Bank 20%, Bajaj Finance 15%, Cash 15%`

## Philosophy

Most investors research individual stocks well but manage portfolios poorly. Position sizing, correlation, and concentration are where returns are actually made or lost. This review graduates you from "researching companies" to "managing a portfolio."

## Execution

### Step 1: Portfolio snapshot

| Position | Weight | Sector | Market Cap Category | Thesis Status |
|---|---|---|---|---|
| | | | Large/Mid/Small | Strong/Weakening/Unknown |

### Step 2: Concentration analysis

- Top 3 positions as % of portfolio (>60% = concentrated, flag)
- Largest single position (>30% = high conviction or danger depending on thesis)
- Cash level vs market conditions

### Step 3: Correlation and diversification

| Pair | Correlation Type | Risk |
|---|---|---|
| | High/Low/Inverse | |

Hidden correlations to check:
- Multiple IT companies (TCS + Infosys + Wipro = same macro bet)
- Multiple banks (HDFC Bank + ICICI = same credit cycle exposure)
- Multiple consumer names (same rural vs urban demand exposure)
- India macro concentration (if all holdings are purely domestic, you have no hedge against INR depreciation)

### Step 4: Thesis strength review

For each position:
- State the original thesis in 1–2 sentences
- Has any thesis been falsified or weakened?
- When did you last update the thesis?

### Step 5: Position sizing vs conviction

| Position | Current Weight | Conviction Level | Appropriate Weight | Gap |
|---|---|---|---|---|
| | | High/Medium/Low | | Over/Under/Right |

Common mismatches:
- High conviction position undersized (fear of concentration)
- Low conviction position large (legacy position never trimmed)
- Cash too high (opportunity cost) or too low (no dry powder for dips)

### Step 6: Rebalancing recommendations

Specific, actionable recommendations:

| Action | Position | From % | To % | Reason |
|---|---|---|---|---|
| Trim | | | | Thesis weakened / overweight |
| Add | | | | Underweight vs conviction |
| Exit | | | | Thesis broken |
| Initiate | | | | New position |
| Hold | | | | No action needed |

### Step 7: Portfolio-level metrics

- Weighted average P/E
- Weighted average ROE
- Estimated portfolio earnings growth (weighted)
- India macro sensitivity: domestic vs export-oriented mix

## Output

Write to `reports/portfolio-latest.md` (update in place — this is a living document).

Include a "Last reviewed" date at the top. Recommendation table must have specific prices and weights, not vague "consider trimming."
