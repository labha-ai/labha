# Management Deep Dive

Conduct a thorough assessment of the management team for $ARGUMENTS.

Input format: `[Name, Company]` or just `[Company]`
Example: `Nithin Kamath, Zerodha` or `Reliance Industries`

## Philosophy

Buying a stock is buying the management's future decisions. In India this is especially important: promoter-controlled companies can create or destroy shareholder value through capital allocation in ways that minority shareholders have limited ability to prevent.

## Execution

### Step 1: Management map

| Role | Name | Tenure | Background | Shareholding |
|---|---|---|---|---|
| Promoter / Founder | | | | |
| MD / CEO | | | | |
| CFO | | | | |
| Key business heads | | | | |

### Step 2: Track record — key decisions audit

| Date | Decision | Context | Outcome | Rating |
|---|---|---|---|---|
| | | | | ★☆☆☆☆ |

Look for:
- Capital allocation decisions: acquisitions, divestitures, capex cycles
- Crisis behaviour: how did they handle the 2020 Covid period? The 2013 INR depreciation?
- Guidance accuracy: what did they promise investors over 3–5 years? What actually happened?
- Contrarian moves: did they make bold calls that looked wrong at the time but proved right?

### Step 3: Capital allocation scorecard

| Category | Assessment | Score |
|---|---|---|
| Organic reinvestment | ROCE on capex, new business ramp times | ★★★☆☆ |
| Acquisitions | Success rate, prices paid, integration | ★★★☆☆ |
| Dividends | Consistency, payout ratio, trajectory | ★★★☆☆ |
| Buybacks | Did they buy back at low prices or high? | ★★★☆☆ |
| Related-party transactions | Volume, terms, disclosure quality | ★★★☆☆ |

### Step 4: Integrity indicators

India-specific checks:

| Check | Finding | Red Flag? |
|---|---|---|
| Promoter pledge % | | > 20% = flag |
| Pledge trend | | Rising = flag |
| Promoter selling during bull market | | Flag |
| Insider trading allegations (SEBI orders) | | Flag |
| Related-party transaction volume | | > 10% revenue = scrutinise |
| Auditor changes in last 5 years | | > 1 change = flag |
| Auditor qualifications or emphasis of matter | | Any = flag |
| Subsidiary complexity | | Excessive = flag |
| Listed subsidiary discount | | Unexplained discount = flag |

### Step 5: Management quality framework

| Dimension | Evidence | Rating |
|---|---|---|
| **Integrity** | Promises vs delivery, disclosure quality | ★★★★☆ |
| **Competence** | Industry expertise, operational track record | ★★★★☆ |
| **Capital allocation** | Returns on invested capital over time | ★★★★☆ |
| **Shareholder orientation** | Does minority shareholder interest matter? | ★★★★☆ |
| **Long-term thinking** | Willingness to sacrifice short-term for long-term | ★★★★☆ |
| **Crisis management** | Behaviour under adversity | ★★★★☆ |

### Step 6: Succession and key-person risk

- Is there a clear succession plan?
- If the founder/promoter left tomorrow, what happens?
- Is the business institutionalised or personality-dependent?
- Key non-promoter executives: who are they, how long have they been there, what happens if they leave?

### Step 7: Owner psychology assessment

Based on letters, interviews, AGM speeches:
- How do they think about competitors? (paranoid = good; dismissive = bad)
- How do they talk about failures? (accountable = good; blame-shifting = bad)
- How do they describe the business to shareholders? (clear = good; complex/jargon = bad)
- Do they underpromise and overdeliver, or vice versa?

### Step 8: Verdict

| Dimension | Score | Key Reason |
|---|---|---|
| Integrity | ★★★★☆ | |
| Competence | ★★★★☆ | |
| Capital allocation | ★★★★☆ | |
| Shareholder orientation | ★★★★☆ | |
| Overall | ★★★★☆ | |

**One-line verdict**: [Can they be trusted with shareholder capital for the next 10 years?]

## Output

Write to `reports/{Company}/{Company}-management-{YYYYMMDD}.md`

This report should be dense with specific evidence — not generic praise or criticism. Every rating must have a specific decision or behaviour backing it up.
