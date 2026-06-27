# Earnings Review: Deep Read from Primary Sources

Deep-read the earnings release for $ARGUMENTS directly from raw filings — no sell-side summaries, no analyst reports. Read it the way Buffett reads annual reports.

## Philosophy

Sell-side consensus creates noise, not signal. The edge is in reading the original document and noticing what the market is missing — or what management is burying.

## Execution

### Step 1: Identify and fetch the filing

Determine the company and reporting period from $ARGUMENTS (e.g., "TCS Q4 FY2026", "Reliance FY2026 Annual").

Fetch the primary source:
- **Quarterly results**: BSE filing or NSE filing — investor presentation + standalone/consolidated results PDF
- **Annual report**: BSE India annual report PDF (the full document, not a summary)
- **Earnings call transcript**: company website IR page or NSE/BSE filing

Do NOT use:
- Moneycontrol summaries
- ET Markets / Bloomberg articles  
- Analyst report summaries

### Step 2: Financial metric extraction

From the raw filing only, extract:

| Metric | This Quarter/Year | Prior Quarter | YoY % | QoQ % |
|---|---|---|---|---|
| Revenue (₹ Cr) | | | | |
| Gross Profit / Gross Margin | | | | |
| EBITDA / EBITDA Margin | | | | |
| PAT (₹ Cr) / Net Margin | | | | |
| Operating Cash Flow | | | | |
| Free Cash Flow | | | | |
| Cash & Equivalents | | | | |
| Total Debt | | | | |

**Mandatory tool validation:**

```bash
python3 ~/labha/tools/financial_rigor.py cross-validate \
  --field revenue --values '{"BSE Filing": val1, "Screener": val2}' --unit Cr
```

### Step 3: Management commentary dissection

Read the MD&A (Management Discussion & Analysis) and earnings call transcript carefully:

**What management said about:**
- Revenue growth — was the explanation specific or vague?
- Margin trajectory — guided up/flat/down? Why?
- Capex plans — investing for growth or defensive?
- Competition — did they acknowledge pressure or dodge it?
- Guidance (if given) — what's the implied growth rate?

**Language analysis:**
- What did they emphasise? What did they minimise?
- Did they change how they discuss any segment vs last quarter?
- Are they using more/less qualified language on outlook?
- Did they answer analyst questions directly or deflect?

### Step 4: Thesis check — signal vs noise

Against your pre-existing investment thesis (if holding), evaluate each development:

| Development | Type | Thesis Impact |
|---|---|---|
| | Value Event / Sentiment / Noise | Confirms / Neutral / Challenges thesis |

**Value Event**: Something that changes long-term earnings power
**Sentiment**: Affects price without changing business
**Noise**: Temporary, one-time, irrelevant to long-term

### Step 5: Surprise analysis

What did the market expect vs what actually happened?

| Metric | Street Estimate | Actual | Delta | Significance |
|---|---|---|---|---|
| Revenue | | | | |
| EBITDA Margin | | | | |
| PAT | | | | |
| Key operating metric | | | | |

### Step 6: Red flags scan

Active search for warning signs buried in the filing:

- [ ] Revenue growth driven by price vs volume — which is it?
- [ ] Working capital deteriorating? (days receivable, days payable trends)
- [ ] Cash conversion ratio (OCF / PAT) — falling below 0.7 is a warning
- [ ] Any change in accounting policy buried in notes?
- [ ] Contingent liabilities — new litigation, regulatory proceedings?
- [ ] Auditor qualifications or emphasis of matter paragraphs?
- [ ] Related-party transactions increase?
- [ ] Promoter pledge change during the quarter?

### Step 7: Decision output

Clear answer to: **does this earnings release change your view?**

| Question | Answer |
|---|---|
| Did the business perform as expected? | Yes / No / Mixed |
| Did management deliver on prior guidance? | Yes / Partially / No |
| Did anything materially change the thesis? | Yes (state what) / No |
| Action required? | Hold / Add / Reduce / Exit / Watch |
| Key thing to monitor next quarter | |

## Output

Write report to `reports/{Company}/{Company}-earnings-{Period}.md`

Length: 800–1,500 words. Dense with data, short on filler. Every paragraph must earn its place.

## Non-Negotiables

- Only primary sources — raw filings only
- All financial figures cross-validated with tool
- Distinguish signal from noise explicitly
- Give a clear action recommendation — no "on one hand, on the other hand"
