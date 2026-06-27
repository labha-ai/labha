# Labha.ai — AI-Powered Value Investing for Indian Markets

> **लाभ (Lābha)** — Sanskrit for *profit, gain*. Also the 11th house in Vedic astrology: the house of gains.

**Labha.ai** is an open-source collection of investment research skills built on [Claude Code](https://claude.ai/code), adapted for Indian markets (NSE/BSE).

One person + Claude = an entire investment research team focused on India.

---

## What This Is

A port of the [ai-berkshire](https://github.com/xbtlin/ai-berkshire) framework — adapted for Indian markets, translated to English, and extended with NSE/BSE data tooling.

The core methodology is unchanged: systematic application of Buffett, Munger, and value investing principles — applied to Nifty 50, Nifty 500, and the broader Indian market universe.

---

## Why Can't You Just Ask AI About Indian Stocks?

You can ask Claude: *"Should I buy Reliance Industries?"* You'll get a balanced, hedged response that can't drive actual decisions.

Labha.ai solves the **research quality and decision discipline** problem:

| Problem | Labha.ai Solution |
|---|---|
| AI gives both-sides-pleasing analysis | Forces a verdict: **Buy / Watch / Avoid** with specific price ranges |
| Single perspective misses blind spots | Four-framework dialectic — frameworks challenge each other |
| LLMs can't do financial math reliably | `financial_rigor.py` uses exact `Decimal` arithmetic throughout |
| Inconsistent depth across companies | Same structured output every time — comparable across companies |
| No Indian data integration | `india_data.py` — NSE/BSE live quotes, financials, valuation via yfinance |

---

## Four-Framework Methodology

| Framework | Master | Question It Asks |
|---|---|---|
| **Business Essence** | Buffett | Is this a good business? What are the economics? |
| **Moat** | Buffett | How wide and durable is the competitive advantage? |
| **Inversion** | Munger | How could this company fail? What am I missing? |
| **Civilizational Trend** | Munger / Li Lu | Is this business on the right side of history? |

These four frameworks are designed to **challenge each other** — not split labour. Buffett says "cheap enough," Munger asks "why are smart people avoiding it?" That tension is what prevents blind spots.

---

## Skills (16 Total)

### Deep Research

| Skill | Purpose |
|---|---|
| `/investment-research` | Full four-framework analysis on a single company |
| `/investment-team` | 4 AI Agents in parallel — fastest, most comprehensive |
| `/management-deep-dive` | Deep dive on founders/management quality |
| `/private-company-research` | Research info-scarce private companies (Zepto, PhonePe, etc.) |
| `/deep-company-series` | 8-part long-form series, publication-grade |

### Earnings Analysis

| Skill | Purpose |
|---|---|
| `/earnings-review` | Deep read of quarterly/annual results from raw filings |
| `/earnings-team` | Four-framework parallel earnings interpretation → article |

### Screening

| Skill | Purpose |
|---|---|
| `/industry-research` | Full value chain map for an industry |
| `/industry-funnel` | Full market → ≤10 → 3 deep dives |
| `/quality-screen` | 7 hard financial metrics — eliminate non-first-class companies |
| `/investment-checklist` | Six-gate pre-buy checklist — 10 minutes to a go/no-go |

### Portfolio Management

| Skill | Purpose |
|---|---|
| `/portfolio-review` | Position sizing, concentration, rebalancing |
| `/thesis-tracker` | Post-buy discipline — track whether thesis is being falsified |
| `/news-pulse` | 10-minute attribution when a stock moves sharply |

### Thinking Tools

| Skill | Purpose |
|---|---|
| `/dyp-ask` | Think through any question using first-principles value investing |
| `/financial-data` | Cross-validate key data from 2+ independent sources |

---

## Quick Start

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Install Skills

```bash
git clone https://github.com/labha-ai/labha.git
cp labha/skills/*.md ~/.claude/commands/
```

### 3. Use

```bash
# Research
/investment-research Reliance Industries
/investment-team HDFC Bank
/management-deep-dive Nithin Kamath, Zerodha

# Earnings
/earnings-review TCS Q4 FY2026
/earnings-team Infosys FY2026 Annual

# Screening
/industry-research Indian Pharma
/industry-funnel Nifty 50
/quality-screen Nifty Bank Index
/investment-checklist Bajaj Finance, Asian Paints, Titan

# Portfolio
/portfolio-review Reliance 30%, TCS 20%, HDFC Bank 20%, Cash 30%
/thesis-tracker Zomato
/news-pulse Adani Enterprises

# Thinking
/dyp-ask Where is Zomato's real moat?
```

---

## Tools

### `tools/india_data.py` — Live NSE/BSE Data

```bash
python3 tools/india_data.py quote RELIANCE        # Live NSE quote
python3 tools/india_data.py financials TCS        # 5-year financials
python3 tools/india_data.py valuation HDFCBANK    # Valuation metrics
python3 tools/india_data.py search "bajaj"        # Search by name
```

### `tools/financial_rigor.py` — Exact Arithmetic

All calculations use Python `decimal.Decimal` — not `float`. Market cap verification, multi-source cross-validation, three-scenario valuation, Benford's Law anomaly detection.

```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price 2950 --shares 6.76e9 --reported 19.95e12 --currency INR
```

---

## Data Sources (Indian Markets)

| Market | Primary | Secondary | Raw Filing |
|---|---|---|---|
| NSE/BSE | [Screener.in](https://screener.in) | [Trendlyne](https://trendlyne.com) | BSE India / NSE filing system |
| US ADR | [Macrotrends](https://macrotrends.net) | [StockAnalysis](https://stockanalysis.com) | SEC EDGAR |

---

## Roadmap

- [x] Four-framework research methodology
- [x] All 16 skills adapted for Indian markets
- [x] NSE/BSE data tool (`india_data.py`)
- [x] Financial rigor tools (exact arithmetic, cross-validation)
- [ ] Nifty 50 quality screen baseline report
- [ ] Indian pharma / IT / banking industry deep dives
- [ ] Real-time data via MCP (NSE live feed)
- [ ] Historical backtesting vs Nifty returns
- [ ] Web interface

---

## Attribution

This project is a market adaptation of [ai-berkshire](https://github.com/xbtlin/ai-berkshire) by [xbtlin](https://github.com/xbtlin), used under the [MIT License](https://github.com/xbtlin/ai-berkshire/blob/main/LICENSE).

---

## License

MIT License — free to use, modify, and build upon. See [LICENSE](LICENSE).

---

> *"The stock market is a device for transferring money from the impatient to the patient."* — Warren Buffett
>
> Labha.ai: Giving every Indian investor their own research team.
