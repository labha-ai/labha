# Deep Company Series: 8-Part Long-Form Research

Produce a publication-grade 8-part deep dive series on $ARGUMENTS — approximately 80,000–120,000 words total across all parts.

This is the most comprehensive single-company research format. Use it when you want to fully understand a company before making a large, long-term position.

## Series Structure

| Part | Title | Focus | Target Length |
|---|---|---|---|
| 1 | **Cognitive Reset** | Unlearn what you think you know about this company. Start from zero. | 8,000–12,000 words |
| 2 | **Business DNA** | What this company actually does, how it makes money, and why customers pay | 12,000–18,000 words |
| 3 | **The Moat** | Forensic analysis of competitive advantage — every layer, every test | 12,000–18,000 words |
| 4 | **Management and Culture** | Deep dive on leadership, governance, culture, capital allocation | 10,000–15,000 words |
| 5 | **Industry and Competition** | Full competitive map, value chain, threat assessment | 12,000–18,000 words |
| 6 | **Financial Forensics** | 10-year financial deep read, cash flow quality, balance sheet risks | 12,000–18,000 words |
| 7 | **Valuation and Scenarios** | Three scenarios, reverse DCF, what the market is pricing in | 8,000–12,000 words |
| 8 | **Decision Memo** | Synthesise all 7 parts into a clear investment decision | 5,000–8,000 words |

## Execution

Each part is produced as a separate agent task, run sequentially (each part informs the next).

### Part 1: Cognitive Reset

Goal: identify and discard all assumptions you're carrying about this company.

- What is the most widely held belief about this company?
- Which of these beliefs are assumptions vs verified facts?
- What would a completely neutral observer notice that a long-time follower has become blind to?
- What would a sophisticated short-seller's opening brief say?
- Historical analogues: name 3 companies that were in a similar position — what happened to each?

End with: a list of 10 specific questions this series must answer honestly.

### Part 2: Business DNA

- One paragraph that a 10-year-old could understand
- Revenue breakdown — every segment, every geography, every product line
- Unit economics at the transaction level: what does one sale look like?
- Customer lifetime value vs customer acquisition cost
- Cohort analysis (if data available): do customers get more valuable over time?
- The flywheel: draw it, then test each arrow — is each reinforcing loop real?
- What would happen to this business if one key input disappeared?

### Part 3: The Moat

For each of the 5 moat types, run a 3-part test:
1. **Does it exist?** (specific evidence, not assertion)
2. **How deep?** (quantify — how much time/money to bridge?)
3. **Which direction?** (widening vs narrowing — with specific evidence)

Then: the acid test — "If I gave a well-capitalised, well-managed competitor ₹50,000 Cr and 5 years, could they take 30% market share from this company?" Work through this scenario seriously.

### Part 4: Management and Culture

Full management deep dive per `/management-deep-dive` skill, extended:
- 10-year decision audit (every major capital allocation decision)
- Culture investigation: what do ex-employees say? What do customers say?
- Compensation structure analysis: how are executives incentivised? Do the incentives align with long-term shareholder value?
- The promoter question (India-specific): is promoter interest aligned with minority shareholders?

### Part 5: Industry and Competition

Full industry map per `/industry-research`, extended:
- 5-year competitive dynamics — who was winning in 2019? 2021? Today?
- New entrant analysis: who has entered in the last 3 years, what happened?
- Technology disruption scenario: what does this industry look like in 10 years if AI/automation is fully deployed?
- Regulatory history: how has regulation shaped this industry? What is the regulatory risk going forward?

### Part 6: Financial Forensics

- 10-year income statement: look for trends, inflections, anomalies
- Cash flow quality: OCF/PAT ratio each year — any deterioration?
- Working capital cycle: receivables, payables, inventory — getting better or worse?
- Debt history: peak debt, debt repayment, current trajectory
- Return on incremental invested capital (ROIIC) — is the business getting better or worse as it grows?
- Benford's Law test on revenue figures (available via tool)
- Any accounting policy changes in last 5 years? What effect did they have?

```bash
python3 ~/labha/tools/financial_rigor.py benford \
  --values '[list of revenue/profit figures across years]'
```

### Part 7: Valuation and Scenarios

Three scenarios (tool-calculated):
```bash
python3 ~/labha/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares_cr} \
  --growth {bull} {base} {bear} \
  --pe {bull_pe} {base_pe} {bear_pe} --years 5 --currency INR
```

Reverse DCF: what growth rate does the current price imply over 10 years?
Historical valuation range: where does current valuation stand vs 10-year range?
Peer comparison: 5 global and Indian peers, their valuations, and why the premium/discount is or isn't justified.

### Part 8: Decision Memo

The synthesis. After 7 parts of research, what is the clear-eyed view?

- 3-sentence investment thesis
- 3 things that could make you wrong (specific falsifiers)
- Price range where you'd buy (specific)
- What would make you sell (specific)
- Honest confidence level: how confident are you, and in what?

## Output

Write each part to `reports/{Company}/deep-series/Part{N}-{Title}.md`
Create a `reports/{Company}/deep-series/README.md` as the series index.

## Non-Negotiable Standards

- Every factual claim must cite a source
- Every estimate must be labelled as an estimate
- All calculations through tools
- Each part must end with: "What Part N told us that we didn't know before"
- The Decision Memo must be honest about uncertainty — a confident wrong answer is worse than an honest "I don't know"
