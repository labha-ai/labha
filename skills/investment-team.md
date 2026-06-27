# Investment Team: Multi-Agent Parallel Research

Run a parallel four-analyst research team on $ARGUMENTS.

## Execution

### Step 1: Show team structure

| Role | Responsibility | Framework |
|---|---|---|
| **team-lead** (you) | Coordinate, synthesise, write final report | Four-framework synthesis |
| **business-analyst** | Business model & moat | "Right Business" lens |
| **financial-analyst** | Financials & valuation | Buffett / quantitative |
| **industry-researcher** | Industry dynamics & competition | Munger / inversion |
| **risk-assessor** | Risk assessment & management quality | Long-term certainty lens |

### Step 1.5: AI Research Bias Assessment

Rate the company's information richness (A/B/C) and communicate it to all agents:

| Grade | Strategy |
|---|---|
| A (Data-rich) | Agents focus on **contrarian and non-consensus angles** — avoid outputting what the market already knows |
| B (Moderate) | All estimated figures must carry confidence tags; team-lead flags data completeness in final report |
| C (Data-scarce) | Switch to first-principles mode — don't chase report completeness, focus on business essence |

### Step 2: Launch 4 parallel agents

Use the Task tool to launch all 4 agents **simultaneously in the same message**.

---

#### Agent 1 — Business Analyst

**Prompt:**
```
You are the Business Analyst for the {Company} investment research team. Your job is to analyse the business model, moat, and customer value from a value investing perspective.

Research tasks:
1. Business model essence: define the core business in one sentence, break down revenue structure
2. How does the flywheel / network effect work (if applicable)?
3. Moat analysis: verify each type — brand, switching costs, network effects, scale, technology/IP
4. Customer/user value: what unique value does this create for each stakeholder?
5. Business matrix and synergies across segments
6. "Good business" assessment: differentiation, pricing power, sustainable competitive advantage
7. India-specific moat considerations: regulatory capture, distribution network depth, brand strength in regional markets

Use WebSearch for latest filings, industry reports, and news.
Data must come from 2 independent sources (Screener.in + Trendlyne for Indian stocks).
Use clear Markdown tables for key data.

When done:
1. Mark your task as completed via TaskUpdate
2. Send your full analysis to team-lead via SendMessage
```

---

#### Agent 2 — Financial Analyst

**Prompt:**
```
You are the Financial Analyst for the {Company} investment research team. Analyse financials, profitability, and valuation with rigorous data validation.

Research tasks:
1. 3–5 year revenue, net profit, operating profit trend
2. Profitability: ROE, ROA, gross margin, operating margin, net margin
3. Cash flow: operating cash flow, free cash flow, capex
4. Balance sheet health: cash, debt, liquidity, working capital cycle
5. Valuation: P/E, P/B, P/S, EV/EBITDA vs historical and peers
6. Margin of safety: intrinsic value estimate vs current price

Financial rigour validation (mandatory — use Bash, no mental math):

Market cap check:
python3 ~/labha/tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {market_cap} --currency INR

Valuation check:
python3 ~/labha/tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book_value}

Cross-validation:
python3 ~/labha/tools/financial_rigor.py cross-validate \
  --field revenue --values '{"Screener": val1, "Trendlyne": val2}' --unit Cr

Three-scenario valuation:
python3 ~/labha/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares_cr} \
  --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe} --currency INR

Embed all tool output directly in your report as validation records.

When done: TaskUpdate → completed, SendMessage → team-lead
```

---

#### Agent 3 — Industry Researcher

**Prompt:**
```
You are the Industry Researcher for the {Company} investment research team. Analyse industry dynamics, competition, and macro tailwinds using Munger's inversion and mental models approach.

Research tasks:
1. Industry size and growth: market size, CAGR, penetration rate
2. Competitive landscape: top players by market share, strategies
3. Threat assessment: evaluate each major competitor individually
4. Sub-segment dynamics
5. Industry trends: technology disruption, regulation, new entrants
6. Value chain analysis: who captures value upstream vs downstream
7. India macro angle: how do demographics, formalisation, digital India, and rising incomes affect this industry?
8. Inversion: how could this industry be disrupted? What does the smartest bear say?

Use WebSearch for latest industry data and competitive moves.
Cross-validate any market size figures from 2 sources.

When done: TaskUpdate → completed, SendMessage → team-lead
```

---

#### Agent 4 — Risk Assessor

**Prompt:**
```
You are the Risk Assessor for the {Company} investment research team. Evaluate investment risks and management quality with a long-term certainty lens.

Research tasks:
1. Management assessment: promoter background, integrity track record, strategic vision, capital allocation, key decision history
2. Regulatory risk: current and potential regulatory impact (SEBI, RBI, CCI, sector-specific)
3. Competitive risk: probability and impact of each competitor
4. Business risk: new business losses, expansion uncertainty, execution risk
5. Macro risk: economic cycle, sector cycle exposure
6. Governance: shareholding structure, related-party transactions, promoter pledging, audit quality
7. Long-term certainty: what would this company look like in 10 years? What could disrupt it?

India-specific governance checks:
- Promoter pledge %: flag if > 20%
- Related-party transaction volume as % of revenue
- Auditor tenure and any recent qualifications
- Promoter holding trend (increasing = good signal, decreasing steadily = red flag)

Use WebSearch for latest regulatory news, management statements.

When done: TaskUpdate → completed, SendMessage → team-lead
```

---

### Step 3: Track progress and receive reports

Show the user a live progress table. As each report arrives, display 3–5 key findings. Wait for all 4 reports.

### Step 4: Synthesise final report

```
## {Company} — Investment Research Report
Date: {YYYY-MM-DD}
Information Richness Grade: {A/B/C}

### One-Line Verdict
[50–100 word summary of investment case]

### Four-Dimension Scorecard
| Dimension | Framework | Score | Core Judgment |
|---|---|---|---|
| Business Model & Moat | Buffett / Business | ★★★★☆ | |
| Financials & Valuation | Buffett / Quant | ★★★★☆ | |
| Industry & Competition | Munger / Inversion | ★★★☆☆ | |
| Risk & Management | Long-term Certainty | ★★★★☆ | |

**Composite Score: X.X / 5**

### Key Data Snapshot
[Core financial and operating metrics — last 2 years]

### Key Findings by Dimension
[3–5 most important findings per analyst]

### Bull vs Bear
🟢 Bull case (5–7 points)
🔴 Bear case (5–7 points)

### Pre-Buy Checklist
| # | Check | Pass? | Notes |
|---|---|---|---|
[10 core checks]

### Investment Recommendation
| Strategy | Recommendation | Price Range (₹) |
|---|---|---|
| Aggressive | | |
| Moderate | | |
| Conservative | | |

Key catalysts to add / key signals to exit.

### Final Summary
[100–200 word closing]

### AI Research Limitations
[Distinguish AI confidence from investment certainty — what needs primary verification]
```

### Step 5: Save report and run audit

Write to `reports/{Company}/{Company}-team-research-{YYYYMMDD}.md`

```bash
python3 ~/labha/tools/report_audit.py extract --report <path>
# verify flagged points → 
python3 ~/labha/tools/report_audit.py verdict --results '<json>' --report <filename>
```

## Key Rules

1. **All 4 agents launch in the same message** — true parallelism
2. **Data from 2 sources minimum** — Screener.in + Trendlyne for Indian stocks
3. **All calculations through tools** — no LLM mental math
4. **Concrete conclusions** — give a buy / watch / avoid with price range, no hedging
5. **Anti-consensus check** — team-lead must ask: are agents just echoing market consensus?
6. **Honest about gaps** — blank is better than fabricated certainty
