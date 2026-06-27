# Financial Data: Retrieval & Cross-Validation Standards

This standard applies to all skills that involve financial data. **Every key data point must come from two independent sources. Flag any discrepancy > 1%.**

---

## Data Source Priority

### NSE/BSE Listed Companies (Primary Use Case)

| Priority | Source | URL | Notes |
|---|---|---|---|
| 1 (Primary) | **Screener.in** | screener.in/company/{TICKER}/ | Best for Indian stocks — 10-year history, peer comparison |
| 2 (Secondary) | **Trendlyne** | trendlyne.com/company/{TICKER} | Good for valuation ratios, analyst estimates |
| Raw filing | **BSE India** | bseindia.com → search ticker | Annual reports, quarterly results PDFs |
| Raw filing | **NSE India** | nseindia.com → search ticker | Exchange filings, shareholding patterns |
| Tool | **india_data.py** | `python3 ~/labha/tools/india_data.py` | Live quotes, financials via yfinance |

### US-Listed Indian ADRs (Infosys, WiPro, HDFC Bank ADR, etc.)

| Priority | Source | URL |
|---|---|---|
| 1 (Primary) | **Macrotrends** | macrotrends.net/stocks/charts/{TICKER} |
| 2 (Secondary) | **StockAnalysis** | stockanalysis.com/stocks/{TICKER} |
| Raw filing | **SEC EDGAR** | sec.gov | 20-F filings for Indian ADRs |

---

## Execution Protocol

### Step 1: Fetch Data

For each financial metric (revenue, net profit, gross margin, operating cash flow, debt, etc.) fetch independently from **Source 1** and **Source 2**.

### Step 2: Calculate Discrepancy

```
Discrepancy % = |Source1 - Source2| / Source1 × 100%
```

| Discrepancy | Action |
|---|---|
| ≤ 1% | ✅ Consistent — use Source 1 value, cite both |
| 1%–5% | ⚠️ Flag "data discrepancy" — show both values, state likely reason |
| > 5% | ❌ "Material discrepancy" — must check raw annual report before using |

### Step 3: Presentation Format

Every key data point must be formatted as:

```
Revenue: ₹9,803 Cr ✅
  - Screener.in: ₹9,810 Cr
  - Trendlyne: ₹9,798 Cr
  - Discrepancy: 0.12%
```

Discrepancy example:
```
Net Profit: ₹2,456 Cr ⚠️ Discrepancy
  - Screener.in: ₹2,456 Cr (GAAP/IndAS)
  - Trendlyne: ₹2,789 Cr (adjusted/non-GAAP)
  - Discrepancy: 13.5% — reason: GAAP vs adjusted (stock compensation, one-time items)
```

---

## Common Discrepancy Reasons

| Reason | Notes |
|---|---|
| IndAS vs GAAP | Most common — especially for profit figures |
| Standalone vs Consolidated | Always prefer consolidated for group companies |
| Adjusted vs reported EPS | ESOPs, exceptional items, deferred tax |
| Currency conversion | For companies reporting in USD (IT companies, ADRs) |
| Fiscal year alignment | Indian FY = April–March; some companies differ |

---

## Special Rules

1. **Unlisted companies** (Zepto, PhonePe, NYKAA pre-IPO, etc.): Single source — mark all figures as `[Estimate]`, skip cross-validation
2. **Quarterly vs Annual**: Prefer annual for cross-validation; quarterly data can lag on some platforms
3. **Raw filing wins**: If both sources conflict with the original annual report (BSE PDF), the filing is authoritative — flag the source error

---

## Quick Reference Index

| Company | Primary Source | Secondary Source |
|---|---|---|
| Reliance Industries | screener.in/company/RELIANCE | trendlyne.com/company/RELIANCE |
| TCS | screener.in/company/TCS | trendlyne.com/company/TCS |
| HDFC Bank | screener.in/company/HDFCBANK | trendlyne.com/company/HDFCBANK |
| Infosys | screener.in/company/INFY | macrotrends.net/stocks/charts/INFY (ADR) |
| Bajaj Finance | screener.in/company/BAJFINANCE | trendlyne.com/company/BAJFINANCE |
| Zomato | screener.in/company/ZOMATO | trendlyne.com/company/ZOMATO |
| Asian Paints | screener.in/company/ASIANPAINT | trendlyne.com/company/ASIANPAINT |
| Titan | screener.in/company/TITAN | trendlyne.com/company/TITAN |
