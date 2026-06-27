# Investment Research: Four-Framework Comprehensive Analysis

Conduct systematic investment research on $ARGUMENTS using Buffett and Munger value investing frameworks.

## Research Framework

Seven sequential modules, with a mandatory AI bias check before starting:

### Pre-Step: AI Research Bias Awareness (mandatory)

Assess the company's "AI researchability" before diving in:

| Grade | Characteristics | AI Research Trap | Mitigation |
|---|---|---|---|
| A (Data-rich) | Long-listed, dense analyst coverage, heavy media attention | Consensus too strong — AI output converges with market pricing, alpha minimal | Focus on contrarian testing: why aren't smart investors buying? What risk is being missed? |
| B (Moderate) | Listed 1–3 years, limited coverage, some data estimated | AI fills data gaps with "reasonable estimates" that create false certainty | Tag every estimated figure with confidence level; separate "evidenced estimate" from "fill-in" |
| C (Data-scarce) | Recently listed / niche / limited public coverage | AI over-penalises information scarcity, mistakes "can't see clearly" for "bad business" | Use first-principles questions (see below); extract business essence from limited data |

**First-principles approach for C-grade companies:**
1. Who is the customer? Why do they pay? Are there alternatives?
2. What drives repeat purchase — habit, lock-in, or continuous new value creation?
3. Could a competitor replicate this with ₹10,000 Cr?
4. What key decisions has management made? What do those decisions reveal about judgment and values?

State the information richness grade at the start of the report, and distinguish "AI research confidence" from "investment certainty" at the end.

---

### Module 1: Data Collection

> **Data source standard**: see `skills/financial-data.md`. All financial data must come from two independent sources. Flag discrepancies > 1%.
> - NSE/BSE: Screener.in (primary) + Trendlyne (secondary)
> - US ADRs: Macrotrends (primary) + StockAnalysis (secondary)
> - Raw: BSE India / NSE filing system

Launch a background Task agent to collect:

1. Revenue breakdown: most recent FY + last 4 quarters, segment revenue, growth, gross margin
2. Financial metrics: 5-year revenue, net profit, gross margin, operating margin, free cash flow, cash reserves
3. Competitive landscape: market share, key competitor comparison
4. Business model and moat: source of competitive advantage
5. Technology capability: core tech stack, R&D spend
6. Management: founder/CEO background, shareholding, key decision record
7. Industry outlook: TAM, growth forecasts
8. Risk factors: regulatory, competition, macro, governance
9. Current valuation: market cap, P/E, P/S, P/B, EV/Revenue
10. Bull and bear case: core arguments from both sides

#### Data Cross-Validation (mandatory — use financial rigor tool)

After collection, **run `tools/financial_rigor.py` on all key figures**:

```bash
# Market cap verification
python3 ~/labha/tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {market_cap} --currency INR

# Multi-source cross-validation (run for revenue, net profit, cash)
python3 ~/labha/tools/financial_rigor.py cross-validate \
  --field {field_name} --values '{"Screener": value1, "Trendlyne": value2}' --unit Cr

# Valuation metric verification
python3 ~/labha/tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book_value} --fcf-per-share {FCF_ps} --dividend {div}
```

**Validation rules:**
1. At least 2 independent sources per key data point
2. When sources differ, prefer company annual report / BSE filing; note the discrepancy reason
3. All calculations must go through the tool — no LLM mental math
4. Embed tool output directly in the report appendix under "Key Data Cross-Validation"
5. If tool flags ❌ large deviation, investigate before proceeding

**Common India-specific errors:**
- Standalone vs consolidated figures (always prefer consolidated)
- ₹ Crore vs ₹ (off by 10 million — the most dangerous unit error)
- Promoter economic interest vs voting rights (dual-class structures)
- EBITDA margin vs PAT margin confusion

---

### Module 2: Business Essence — "The Right Business"

- Define the business in one sentence
- Revenue structure breakdown (table)
- 5-year profitability trend (table)
- Business model canvas: one-time sale vs recurring/subscription? Hardware vs software vs platform?
- Ecosystem stickiness and customer lock-in intensity
- Gross margin vs peers — why higher or lower?
- Operating leverage analysis
- **Key question**: What is the business really doing that creates value? If you had to describe it in one sentence, what would it be?

---

### Module 3: Moat Assessment — "Economic Moat"

Verify each moat type:

| Moat Type | Verification Method |
|---|---|
| Brand / Pricing power | Can they raise prices without losing volume? |
| Switching costs | How much does it cost a customer to migrate to a competitor? |
| Network effects | Does the product get better as more people use it? |
| Scale advantage | How significant is the cost advantage from scale? |
| Technology / IP | How many years ahead? Can it be replicated? |

Moat trajectory: has it widened or narrowed over the past 5 years? What's the 5-year forecast?

**Key question**: Will this moat still exist in 10 years? What could destroy it?

---

### Module 4: Inversion and Risk List — "Always Invert"

- List all paths to failure (table: path / probability / impact)
- Historical analogue: find companies that were in a similar position historically — what happened?
- Cross-disciplinary analysis: network effects theory, technology adoption curve, competitive game theory
- Bias check: narrative bias, anchoring, survivorship bias
- Collect the bear case's strongest arguments

**Key question**: Where am I most likely to be wrong? Why would a smart investor avoid or short this company?

---

### Module 5: Management Assessment

- CEO/founder key decision review (table: date / decision / outcome / rating)
- Capital allocation ability: R&D returns, acquisition success rate, buyback timing
- Shareholder alignment: promoter holding, compensation structure, selling record
- Organisational capability: team stability, key person risk
- Corporate culture characteristics
- India-specific checks: promoter pledge levels, related-party transactions, governance record

**Key question**: If the CEO retired tomorrow, would this company maintain its competitive position?

---

### Module 6: Industry and Civilisational Trend

- Is this industry in a "civilisational paradigm shift"?
- Historical technology revolution analogue (steam / electricity / internet / AI / mobile)
- TAM growth curve and ceiling analysis
- Company's position in the value chain
- Technology path risk
- Customer / supplier concentration analysis
- India macro tailwind: demographics, formalisation, digitisation, rising middle class — how does this company benefit?

**Key question**: Looking back from 20 years hence, was this company the "Standard Oil of its era" or a "flash in the pan"?

---

### Module 7: Valuation and Margin of Safety

- Current market pricing (key metrics table) — **must be tool-verified**
- Reverse DCF: what growth rate is implied by the current price?
- Three-scenario valuation — **exact calculation via tool, no mental math**:

```bash
python3 ~/labha/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares_crore} \
  --growth {bull} {base} {bear} \
  --pe {bull_pe} {base_pe} {bear_pe} --years 3 --currency INR
```

- Compare to own historical valuation range
- Compare to peer valuation

**Key question**: If the market closed for 5 years tomorrow, would you be comfortable holding at this price?

---

### Module 8: Final Decision Memo

Summary table:

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business Quality | | |
| Moat | | |
| Management | | |
| Top Risk | | |
| Macro/Trend | | |
| Valuation | | |

Final decision table:

| Strategy | Recommendation |
|---|---|
| Not yet invested | |
| Currently holding | |
| Sell signal | |
| Add signal | |

Simulated commentary from both frameworks (use blockquote format).

## Output Requirements

1. All analysis must be data-backed with source citations
2. Use Markdown tables for key data
3. Each module must end with its key question answered
4. Write the complete report to `reports/{CompanyName}/{CompanyName}-research-{YYYYMMDD}.md`
5. Conclusions must be concrete — don't avoid giving a buy / watch / avoid recommendation
6. Valuation section must give a specific price range
7. **Report opening**: information richness grade (A/B/C) and AI research limitations statement
8. **Report closing**: distinguish "AI analysis confidence" from "investment certainty"
9. For C-grade companies: end with "Primary research checklist" — things the reader should verify through field research, product experience, supply chain interviews

## Data Audit (Pre-Publish)

After writing the report, run the audit before sharing:

```bash
# Step 1 — Extract audit checklist (15% random sample)
python3 ~/labha/tools/report_audit.py extract --report <report_path>

# Step 2 — Fetch and verify each flagged data point
# (use Screener.in + Trendlyne per financial-data.md)

# Step 3 — Output pass/fail verdict
python3 ~/labha/tools/report_audit.py verdict \
  --results '<completed_json>' --report <report_filename>
```

- **Pass**: all audit points within 1% → report ready to publish
- **Fail**: any point > 1% → correct and re-audit until pass
