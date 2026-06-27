# Earnings Team: Four-Framework Parallel Interpretation

Run a parallel earnings analysis team on $ARGUMENTS and produce a publishable article.

Input: `{Company} {Period}` — e.g., `TCS Q4 FY2026`, `Reliance FY2026 Annual`

## Team Structure

| Role | Responsibility |
|---|---|
| **team-lead** (you) | Coordinate, synthesise, write final article |
| **fundamentals-analyst** | Numbers — revenue, margins, cash flow, balance sheet |
| **thesis-checker** | Did this quarter confirm or challenge the long-term thesis? |
| **contrarian** | What is the market getting wrong — in either direction? |
| **context-setter** | Industry backdrop, peer comparison, macro relevance |

## Execution

### Step 1: Fetch the raw filing

Primary source only: BSE/NSE filing — results PDF + investor presentation + earnings call transcript.
No sell-side summaries.

### Step 2: Launch 4 agents in parallel

**Agent 1 — Fundamentals Analyst:**
```
Analyse the raw earnings filing for {Company} {Period}.

Extract and cross-validate all key metrics:
- Revenue, gross profit, EBITDA, PAT — absolute and margins
- YoY and QoQ comparison
- Cash flow: OCF, FCF, capex
- Balance sheet changes: cash, debt, working capital
- Segment breakdown if available

Run tool validations:
python3 ~/labha/tools/financial_rigor.py cross-validate \
  --field revenue --values '{"BSE Filing": X, "Screener": Y}' --unit Cr

State clearly: beat / in-line / miss vs street estimates for each key metric.
Deliver: structured data table + 3 most important financial observations.
TaskUpdate → completed. SendMessage → team-lead.
```

**Agent 2 — Thesis Checker:**
```
Review the earnings filing for {Company} {Period} against the long-term investment thesis.

The thesis for {Company} is approximately: [retrieve from reports/{Company}/{Company}-thesis.md if it exists, else state the commonly held bull thesis]

For each piece of information in this quarter:
- Does it confirm, remain neutral to, or challenge the thesis?
- Which specific metrics are most important for the thesis?
- Did management's commentary support or undermine the thesis?

Output: thesis confirmation table + verdict (intact / weakening / broken).
TaskUpdate → completed. SendMessage → team-lead.
```

**Agent 3 — Contrarian:**
```
Look at the {Company} {Period} earnings and find what the market is likely getting wrong.

This means:
- What is being over-celebrated that may not be durable?
- What is being over-punished that may recover?
- What did management bury in the notes / MD&A that nobody is talking about?
- What question did analysts NOT ask on the earnings call that they should have?
- What does the trend in a non-headline metric reveal?

Deliver: 3–5 contrarian observations with specific evidence.
TaskUpdate → completed. SendMessage → team-lead.
```

**Agent 4 — Context Setter:**
```
Provide context for the {Company} {Period} results.

- How did peers perform this quarter? (list 2–3 direct competitors with their key metrics)
- What is the macro backdrop? (sector tailwinds/headwinds, INR movement, inflation, credit cycle)
- How does this quarter's performance compare to the company's own 3-year trend?
- Any sector-wide theme this quarter confirms or contradicts?

Deliver: context table + 2–3 most important contextual observations.
TaskUpdate → completed. SendMessage → team-lead.
```

### Step 3: Synthesise and write article

Combine all four reports into a publishable piece:

```
## {Company} {Period} Results: [One punchy headline]

**One-paragraph verdict** (lead with the most important finding)

### The Numbers
[Key metrics table — fundamentals analyst]

### What This Means for the Thesis
[Thesis checker output]

### What the Market Is Missing
[Contrarian observations]

### The Bigger Picture
[Context: peers, macro, trend]

### Bottom Line
[Clear verdict: thesis intact / challenged / broken + action implication]
```

Target length: 600–900 words. Dense, no filler.

## Output

Write to `reports/{Company}/{Company}-earnings-{Period}.md`

The article should be readable by someone who hasn't been following the company closely — context is important. But don't pad it with background that insiders already know.
