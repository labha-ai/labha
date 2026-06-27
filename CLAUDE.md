# Labha.ai — Project Instructions

## Project Overview

AI-powered value investing research skill suite for Indian markets (NSE/BSE), built on Claude Code.
Four-framework methodology: Buffett, Munger, and value investing principles applied to India.
GitHub: YOUR_USERNAME/labha

## Project Structure

```
skills/          — Research skill definitions (.md), copy to ~/.claude/commands/
tools/           — Data and calculation tools
reports/         — Investment research report outputs
assets/          — Images and static assets
data/            — Watchlists, screening data
```

## Report Directory Structure

All reports organized by **company name** folder:

```
reports/
├── Reliance/                    — All Reliance research
│   ├── Reliance-research-20260627.md
│   └── Reliance-thesis.md
├── TCS/                         — All TCS research
├── HDFC-Bank/
├── Nifty50-funnel-20260627.md   — Index/funnel reports at root
├── IT-industry-20260627.md      — Industry reports at root
├── Banking-industry-20260627.md
└── portfolio-latest.md          — Portfolio report at root
```

## Report Naming Convention

| Skill | File Format | Example |
|---|---|---|
| `/investment-team` | `{Company}/` folder with 4 perspectives + final | `reports/Reliance/final-report.md` |
| `/investment-research` | `{Company}-research-{YYYYMMDD}.md` | `reports/TCS/TCS-research-20260627.md` |
| `/investment-checklist` | `{Company}-checklist-{YYYYMMDD}.md` | `reports/HDFC-Bank/HDFC-Bank-checklist-20260627.md` |
| `/industry-research` | `{Industry}-industry-{YYYYMMDD}.md` (root) | `reports/IT-industry-20260627.md` |
| `/industry-funnel` | `{Index/Theme}-funnel-{YYYYMMDD}.md` (root) | `reports/Nifty50-funnel-20260627.md` |
| `/earnings-review` | `{Company}-earnings-{Period}.md` | `reports/Infosys/Infosys-earnings-Q4FY26.md` |
| `/thesis-tracker` | `{Company}-thesis.md` (long-lived) | `reports/Zomato/Zomato-thesis.md` |
| `/portfolio-review` | `portfolio-latest.md` (root, updated in place) | `reports/portfolio-latest.md` |
| `/management-deep-dive` | `{Company}-management-{YYYYMMDD}.md` | `reports/Zerodha/Zerodha-management-20260627.md` |

## Data Sources (Indian Markets)

### NSE/BSE Listed Companies
| Priority | Source | URL |
|---|---|---|
| 1 (Primary) | **Screener.in** | screener.in/company/{TICKER}/ |
| 2 (Secondary) | **Trendlyne** | trendlyne.com/company/{TICKER} |
| Raw filing | **BSE India** | bseindia.com → search ticker |
| Raw filing | **NSE India** | nseindia.com → search ticker |

### US-Listed Indian ADRs (Infosys, WiPro, etc.)
| Priority | Source | URL |
|---|---|---|
| 1 (Primary) | **Macrotrends** | macrotrends.net/stocks/charts/{TICKER} |
| 2 (Secondary) | **StockAnalysis** | stockanalysis.com/stocks/{TICKER} |

### Tickers
- NSE format: RELIANCE, TCS, HDFCBANK, INFY, WIPRO
- yfinance format: RELIANCE.NS, TCS.NS, HDFCBANK.NS
- BSE format: RELIANCE.BO

## Tool Paths

All tools live at `~/labha/tools/`. Skill files reference them as:

```bash
python3 ~/labha/tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {market_cap} --currency INR

python3 ~/labha/tools/india_data.py quote {TICKER}
python3 ~/labha/tools/india_data.py financials {TICKER}
```

## Research Principles (Highest Priority)

- **Objective, objective, objective** — all analysis must be grounded in facts and data
- Clearly separate **facts** (data-backed) from **opinions** (explicitly labelled as such)
- **No preset bias** — don't pre-load bullish or bearish. Data first, logic second, conclusion last
- Present both sides of every core judgment — bull case AND bear case
- Be honest about uncertainty: say "insufficient data" rather than filling gaps with speculation
- All skills must follow these principles

## Report Style

- All reports in **English**
- Style: direct, sharp, no filler
- Data must cite sources; key data needs 2+ independent sources cross-validated
- Estimates must be labelled as estimates
- Ratings use ★ (1–5 stars, no half stars)
- Currency: **INR (₹)** throughout — be explicit about crores/lakhs vs absolute numbers

## Currency Conventions

- Market cap: ₹ Crore (e.g., ₹19,95,000 Cr or ₹19.95 Lakh Cr)
- Revenue/profit: ₹ Crore for large caps
- Per share: ₹ (e.g., EPS ₹124.50)
- Always verify: Price × Shares Outstanding = Market Cap (unit-check for Cr vs absolute)

## GitHub Operations

```bash
cd ~/labha
git add reports/Company/file.md
git commit -m "Add TCS Q4FY26 earnings research"
git pull --rebase origin main
git push origin main
```

## Notes

- Always hand-verify market cap: Price × Total Shares Outstanding
- Cross-check INR vs USD when using international sources
- PE/ROE/FCF use tools/financial_rigor.py for exact calculation
- After writing a report, ask if user wants to push to GitHub
