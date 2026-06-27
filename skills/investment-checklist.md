# Buffett Pre-Buy Checklist

Run the Buffett value investing pre-buy checklist on $ARGUMENTS.

**Supports single or multiple companies** — comma-separated. e.g. `Reliance, HDFC Bank, TCS` or `BAJFINANCE TITAN ASIANPAINT`

## Execution

### Step 1: Parse companies

Identify all companies from $ARGUMENTS. For each:
- Full name, NSE/BSE ticker, exchange
- If unlisted, note "unlisted" and skip the full checklist

### Step 1.5: AI Research Bias Check

Quick information richness rating (A/B/C) for each company:

| Grade | Criteria | Checklist Impact |
|---|---|---|
| A (Data-rich) | Long-listed, wide analyst coverage, dense media coverage | Focus on **contrarian checking** — consensus clarity ≠ investment certainty |
| B (Moderate) | Listed 1–3 years or limited coverage, some data needs estimation | Tag every estimate with confidence level |
| C (Data-scarce) | Recently listed / obscure / limited coverage | Don't force-fill six gates. Honestly mark "insufficient data." Use first-principles questions instead. |

Core principle: The checklist's goal is to **eliminate bad choices**, not discover the best ones. For C-grade companies, "data insufficient" ≠ "fail" — it means "grey zone, needs primary research."

### Step 2: Parallel data collection

Launch a background Task agent per company to collect:

1. **Profitability**: ROE (5–10 year trend), gross margin, net margin, free cash flow
2. **Valuation**: Current price, market cap, P/E (TTM), forward P/E, P/B, dividend yield
3. **Growth**: 3-year revenue and profit CAGR
4. **Financial health**: Debt levels, capex intensity, cash reserves, net cash/debt
5. **Competitive landscape**: Market share, key competitors, share trends
6. **Moat evidence**: Brand / switching costs / network effects / scale / technology — specific evidence for each
7. **Management track record**: Promoter background, key decisions, shareholding, capital allocation
8. **Recent events**: Last 6 months — results, acquisitions, regulatory, management changes

### Step 3: Run six gates for each company

---

#### Gate 1: Can I understand this business? (Circle of Competence)

- [ ] Can I explain in one sentence how this company makes money?
- [ ] What will it most likely be doing in 10 years?
- [ ] What are the 2–3 variables that determine success or failure?
- [ ] Is my understanding from deep research or hearsay?

**Scoring (★1–5)**:
- ★★★★★: Extremely simple and clear model, high 10-year certainty (e.g., Asian Paints: makes and sells paints)
- ★★★★☆: Clear model with some technical depth needed to understand well
- ★★★☆☆: Understandable but 10-year certainty uncertain — fast-changing industry
- ★★☆☆☆: Complex business lines or industry in flux
- ★☆☆☆☆: Completely outside circle of competence

**Hard veto**: If you cannot clearly explain how it earns money → mark "Outside circle of competence, skip."

---

#### Gate 2: Is this a good business? (Economics)

Use the tool for exact calculation — no mental math:

```bash
python3 ~/labha/tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book_value_per_share} --fcf-per-share {FCF_per_share} --dividend {dividend}
```

| Metric | Company Value | Reference Bar | Verdict |
|---|---|---|---|
| ROE (5-year avg) | | >15% good, >20% excellent | |
| Gross Margin | | >40% suggests pricing power | |
| Free Cash Flow | | Persistently positive, tracks net profit | |
| Capex Intensity | | Asset-light beats capital-heavy | |
| Debt Level | | Interest-bearing debt / net profit < 3 years | |

**Scoring (★1–5)**:
- ★★★★★: ROE >25%, high margins, strong FCF, asset-light, low debt — all pass
- ★★★★☆: 4 of 5 pass
- ★★★☆☆: 3 of 5 pass
- ★★☆☆☆: 2 pass or deteriorating trend
- ★☆☆☆☆: Most fail or FCF persistently negative

---

#### Gate 3: Is the moat deep enough? (Competitive Advantage)

| Moat Type | Present? | Specific Evidence | Widening or Narrowing? |
|---|---|---|---|
| Brand / Pricing power | | | |
| Switching costs | | | |
| Network effects | | | |
| Cost / Scale advantage | | | |
| Technology / IP barrier | | | |

Additional test: If a competitor had ₹10,000 Cr, could they replicate this business?

**Scoring (★1–5)**:
- ★★★★★: Multiple overlapping moats, all widening
- ★★★★☆: At least one strong, stable moat
- ★★★☆☆: Moat exists but not deep, or trend unclear
- ★★☆☆☆: Moat being eroded
- ★☆☆☆☆: No meaningful moat

---

#### Gate 4: Is management trustworthy? (The Human Factor)

| Check | Assessment |
|---|---|
| Integrity (promises vs delivery) | |
| Capital allocation (buybacks, dividends, acquisitions) | |
| Shareholder alignment (promoter holding, compensation) | |
| Owner mentality (founder vs professional manager) | |
| Governance (related-party transactions, audit quality, pledging) | |
| Would it run fine without current CEO? | |

**Scoring (★1–5)**:
- ★★★★★: Founder-led, excellent capital allocator, fully aligned
- ★★★★☆: Strong management with minor issues
- ★★★☆☆: Adequate management with governance concerns
- ★★☆☆☆: Integrity or governance red flags
- ★☆☆☆☆: Serious integrity issue → **hard veto**

Special India flags: promoter share pledging, related-party transactions, frequent auditor changes, promoter selling while recommending buy.

---

#### Gate 5: Is the price cheap enough? (Margin of Safety)

| Metric | Value | Historical Percentile | Verdict |
|---|---|---|---|
| P/E (TTM) | | | |
| Forward P/E | | | |
| P/B | | | |
| Dividend Yield | | | |
| FCF Yield | | | |

Three-scenario valuation — **must use tool, no mental math**:
```bash
python3 ~/labha/tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares_in_crore} \
  --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe} --currency INR
```

- If wrong, what is the maximum loss at current price?
- If the stock drops 50%, would you add to the position?

**Scoring (★1–5)**:
- ★★★★★: Trading at < 50% of intrinsic value — extreme margin of safety
- ★★★★☆: ~70% of intrinsic value — good margin of safety
- ★★★☆☆: Fair value, adequate margin of safety
- ★★☆☆☆: Slightly expensive, margin of safety thin
- ★☆☆☆☆: Significantly overvalued

---

#### Gate 6: Decision Discipline (No FOMO)

- [ ] Am I buying because of FOMO?
- [ ] Am I buying because someone recommended it?
- [ ] If this stock was suspended for 5 years, would I be okay?
- [ ] Can I write my buy thesis in under 200 words?

---

### Step 4: Mirror Test

For each company, write the mirror test statement:

> "I am buying ___ at ₹___ because:
> 1. The essence of this business is ___, and I understand it;
> 2. Its moat is ___, and it is widening / stable / narrowing;
> 3. Management is ___, trustworthy / not trustworthy because ___;
> 4. The current price is approximately ___% of intrinsic value, providing adequate / inadequate margin of safety;
> 5. Even if I'm wrong, downside is manageable / unmanageable because ___."

**Cannot complete in 5 sentences = don't buy. No exceptions.**

---

### Step 5: Quick-Kill Checklist

Any single trigger below = immediate veto:

- [ ] Cannot explain how this company makes money
- [ ] FCF negative for 3+ consecutive years with no clear path to positive
- [ ] Management integrity issues (fraud, misleading guidance, promoter pledging spike)
- [ ] Competitive advantage being irreversibly eroded
- [ ] Thesis depends on "greater fool" — next buyer pays more
- [ ] Cannot accept this investment going to zero
- [ ] Buy thesis is primarily "everyone else is buying it" or "it's been going up"
- [ ] Cannot write the buy thesis in under 200 words

India-specific red flags:
- [ ] Promoter holding declining steadily while the company trades at high valuations
- [ ] Significant related-party transactions with opaque disclosures
- [ ] Auditor resignation or qualification in last 2 years
- [ ] Listed entity is a holding company discount play with governance risk

---

### Step 6: Comparison Table (required for multiple companies)

| Company | Checklist Pass? | Circle | Business | Moat | Mgmt | Value | Verdict |
|---|---|---|---|---|---|---|---|
| | | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | |

---

### Step 7: Final verdict and file output

For each company, give a clear verdict — no fence-sitting:
- ✅ **Checklist Pass** (X/6 gates) — proceed to deep research
- ❌ **Fail** — state which red line was triggered
- ❓ **Grey Zone** — state the key unresolved question the investor must answer
- N/A — unlisted or not investable

Write the full report to `reports/{CompanyName}/{CompanyName}-checklist-{YYYYMMDD}.md`

## Output Standards

1. Each company gets its own section: six-gate scorecard + key data table + top 3–5 risks + mirror test + verdict
2. Multi-company: add comparison table at the end
3. All ratings use ★ (1–5, no half stars)
4. Data must cite source and date; estimates labelled as estimates
5. Currency: ₹ throughout, crore-denominated for large figures
6. Close with Buffett: *"The first rule of investing is don't lose money. The second rule is don't forget rule one."*

## Core Principles

- **Better to miss than to be wrong**: The checklist eliminates bad choices, not finds the best
- **Honest circle of competence**: If you don't understand it, say so
- **Margin of safety is non-negotiable**: A great company bought at the wrong price will still lose money
- **Mirror test cannot be skipped**: If you can't articulate it, don't buy it
