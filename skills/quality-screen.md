# Quality Screen: 7 Hard Metrics

Rapidly eliminate non-first-class companies from $ARGUMENTS using 7 hard financial filters.

**Supports**: single stock / sector / index / thematic batch. e.g., `Nifty 50`, `Nifty Bank`, `Indian IT sector`, `BAJFINANCE TITAN ASIANPAINT`

## Philosophy

Most companies are mediocre. This screen is designed to eliminate them quickly so you spend research time only on companies worth researching. It does not find buys — it eliminates non-buys.

## The 7 Filters

| # | Metric | Pass Bar | Why It Matters |
|---|---|---|---|
| 1 | **ROE (5-year avg)** | ≥ 15% | Measures how well the business uses equity capital |
| 2 | **ROE consistency** | No year below 10% in last 5 years | Consistency matters more than a single great year |
| 3 | **Gross Margin** | ≥ 30% (or industry-justified) | Pricing power proxy |
| 4 | **FCF / Net Profit** | ≥ 0.7x (3-year avg) | Cash conversion — are profits real? |
| 5 | **Net Debt / EBITDA** | ≤ 3x (or net cash) | Balance sheet safety |
| 6 | **Revenue CAGR (3Y)** | ≥ 8% (at minimum inflation + real growth) | Growing businesses, not shrinking ones |
| 7 | **Promoter governance** | No major pledge (< 20%), no auditor change last 2Y | Binary quality check |

## Execution

### For index/sector/batch input:

1. List all constituent companies (or companies in the sector/theme)
2. Fetch key metrics for each via `india_data.py` + Screener.in
3. Apply all 7 filters
4. Output a clean pass/fail table

### For single stock:

1. Fetch 5-year financials
2. Apply all 7 filters with exact numbers
3. Give a verdict with context

## Output format

| Company | ROE avg | ROE consistent? | Gross Margin | FCF/NP | Net D/EBITDA | Rev CAGR | Governance | Result |
|---|---|---|---|---|---|---|---|---|
| | | ✅/❌ | | | | | ✅/❌ | ✅ PASS / ❌ FAIL |

**Pass** = all 7 filters met → worth deeper research
**Conditional** = 5–6 filters met, state which failed and why it may be acceptable
**Fail** = < 5 filters met → eliminate

### Industry-adjusted bars

For banks/NBFCs: replace Net Debt/EBITDA with Gross NPA < 3% and Capital Adequacy > 15%
For early-stage / high-growth: FCF filter relaxed if revenue CAGR > 30% and clear FCF inflection path
For capital-intensive (cement, steel, infra): Gross Margin bar lowered to 20%, ROE bar to 12%

## Output

Write results to `reports/{InputName}-quality-screen-{YYYYMMDD}.md`

Include: pass list, fail list with reasons, and "watch list" (conditional passes worth monitoring).
