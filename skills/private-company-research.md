# Private Company Research

Research $ARGUMENTS — a private, unlisted, or information-scarce company using detective-style primary and secondary research.

Designed for: Zepto, PhonePe, BYJU's, Meesho, Boat, Razorpay, Cars24, Swiggy (pre-IPO), and other Indian unicorns or private companies.

## Philosophy

Private companies in India have less disclosure than listed companies, but they're not black boxes. Funding round disclosures, MCA filings, DRHP documents, press releases, and industry data give you more than enough to form a view — if you know where to look.

## Data Sources for Indian Private Companies

| Source | What You Get |
|---|---|
| **MCA filing** (mca.gov.in) | Annual returns, financial statements for private limited companies |
| **DRHP** (if IPO planned) | Most detailed disclosure available — treat as a goldmine |
| **Funding round news** | Valuation, investor mix, implied growth metrics |
| **RoC filings** | Shareholding, director changes, charges |
| **SEBI filings** (if pre-IPO) | Draft Red Herring Prospectus |
| **Job postings** | Reveals expansion plans, technology stack, headcount |
| **Glassdoor / LinkedIn** | Culture, attrition signals |
| **Competitor filings** | Triangulate market share |
| **App Store ratings / downloads** | Consumer traction proxy |
| **Industry reports** (NASSCOM, BCG, Redseer) | Market size, segment leadership claims |

## Execution

### Step 1: Data inventory

For each piece of data, tag confidence level:
- 🟢 **High**: verified from MCA, DRHP, or official filing
- 🟡 **Medium**: from credible press coverage or industry report
- 🔴 **Low**: estimate, triangulation, or single uncorroborated source

| Data Point | Value | Source | Confidence |
|---|---|---|---|
| Latest valuation | | | 🟡 |
| Revenue (latest available) | | | 🟢/🟡/🔴 |
| Revenue growth rate | | | |
| Gross margin | | | |
| EBITDA / loss run rate | | | |
| Key investors | | | 🟢 |
| Headcount | | | 🟡 |
| GMV / TPV (if marketplace) | | | 🟡 |

### Step 2: Business essence (first-principles, not summary)

Answer the 4 first-principles questions:
1. Who is the customer and why do they pay? (specific, not generic)
2. What drives repeat usage? Habit / lock-in / network effects / ongoing new value?
3. Could a competitor replicate this with ₹5,000 Cr? Why / why not?
4. What have the founders done that shows their judgment? (specific decisions, not bio)

### Step 3: Financial reconstruction

Triangulate financials from whatever data is available:

| Method | Estimate | Confidence |
|---|---|---|
| MCA filing (direct) | | 🟢 |
| Funding-round-implied revenue | Revenue = Valuation / Industry Revenue Multiple | 🟡 |
| App download × estimated ARPU | | 🔴 |
| Market size × stated market share | | 🔴 |

Use the range from multiple methods. State the range honestly: "Revenue is likely between ₹X Cr and ₹Y Cr based on available data."

### Step 4: Multi-method valuation

| Method | Value Range | Notes |
|---|---|---|
| Latest funding round | | Include vintage — 2021 valuations are stale |
| Listed comparable P/S multiple | | Which listed co is the right comp? |
| DCF (base case) | | State all assumptions explicitly |
| Endgame backsolve | What market cap needed at IPO for current investors to 3x? | |

**Composite fair value range**: ₹X Cr – ₹Y Cr

### Step 5: Exit path analysis

| Path | Timeline | Probability | Investor Return at Current Valuation |
|---|---|---|---|
| IPO | | | |
| Strategic acquisition | | | |
| Secondary market (pre-IPO) | | | |
| Stay private | | | |

### Step 6: What to verify through primary research

Since this is a private company, list what cannot be verified from secondary sources and must come from:
- Customer interviews ("do you use this product? Why? What would you switch to?")
- Employee conversations (Glassdoor, LinkedIn, personal network)
- Supplier/partner conversations
- Personal product usage experience

## Output

Write to `reports/{Company}/{Company}-private-{YYYYMMDD}.md`

Every data point must carry its confidence tag. The report must clearly separate "what we know" from "what we're estimating" from "what we genuinely don't know." Fabricated certainty in a private company research report is worse than admitting ignorance.
