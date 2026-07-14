#!/usr/bin/env python3
"""India Market Data Tool — NSE/BSE quotes and financials for Labha.ai skills.

Provides live quotes, financials, and valuation metrics for NSE/BSE listed companies.
Uses yfinance (.NS / .BO suffixes) — no API key required.

Usage:
    python3 tools/india_data.py quote RELIANCE          # Live NSE quote
    python3 tools/india_data.py quote 500325 --bse      # Live BSE quote by code
    python3 tools/india_data.py financials TCS          # 5-year financials
    python3 tools/india_data.py valuation HDFCBANK      # Valuation metrics
    python3 tools/india_data.py search "bajaj"          # Search by name/keyword

Requires: pip install yfinance
Python >= 3.8
"""

import argparse
import json
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_EVEN

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def _check_yfinance():
    try:
        import yfinance  # noqa: F401
    except ImportError:
        print("❌ yfinance not installed. Run: pip install yfinance")
        sys.exit(1)

# ---------------------------------------------------------------------------
# Ticker resolution
# ---------------------------------------------------------------------------

# Common ticker aliases — NSE symbol → yfinance symbol
_ALIASES = {
    "RELIANCE":   "RELIANCE.NS",
    "TCS":        "TCS.NS",
    "HDFCBANK":   "HDFCBANK.NS",
    "INFY":       "INFY.NS",
    "ICICIBANK":  "ICICIBANK.NS",
    "HINDUNILVR": "HINDUNILVR.NS",
    "BAJFINANCE": "BAJFINANCE.NS",
    "SBIN":       "SBIN.NS",
    "KOTAKBANK":  "KOTAKBANK.NS",
    "BHARTIARTL": "BHARTIARTL.NS",
    "ASIANPAINT": "ASIANPAINT.NS",
    "TITAN":      "TITAN.NS",
    "WIPRO":      "WIPRO.NS",
    "AXISBANK":   "AXISBANK.NS",
    "MARUTI":     "MARUTI.NS",
    "SUNPHARMA":  "SUNPHARMA.NS",
    "ULTRACEMCO": "ULTRACEMCO.NS",
    "NESTLEIND":  "NESTLEIND.NS",
    "TATAMOTORS": "TATAMOTORS.NS",
    "ONGC":       "ONGC.NS",
    "NTPC":       "NTPC.NS",
    "POWERGRID":  "POWERGRID.NS",
    "COALINDIA":  "COALINDIA.NS",
    "ZOMATO":     "ETERNAL.NS",  # renamed to Eternal Ltd in 2025
    "ETERNAL":    "ETERNAL.NS",
    "NYKAA":      "NYKAA.NS",
    "PAYTM":      "PAYTM.NS",
    "POLICYBZR":  "POLICYBZR.NS",
    "DMART":      "DMART.NS",
    "PIDILITIND": "PIDILITIND.NS",
    "DABUR":      "DABUR.NS",
    "BERGEPAINT": "BERGEPAINT.NS",
    "TATASTEEL":  "TATASTEEL.NS",
    "JSWSTEEL":   "JSWSTEEL.NS",
    "HINDALCO":   "HINDALCO.NS",
    "DRREDDY":    "DRREDDY.NS",
    "CIPLA":      "CIPLA.NS",
    "DIVISLAB":   "DIVISLAB.NS",
    "TECHM":      "TECHM.NS",
    "HCLTECH":    "HCLTECH.NS",
    "LTIM":       "LTIM.NS",
    "LT":         "LT.NS",
    "ADANIPORTS": "ADANIPORTS.NS",
    "ADANIENT":   "ADANIENT.NS",
    "TATACONSUM": "TATACONSUM.NS",
    "BAJAJFINSV": "BAJAJFINSV.NS",
    "EICHERMOT":  "EICHERMOT.NS",
    "APOLLOHOSP": "APOLLOHOSP.NS",
}


def _resolve_ticker(symbol: str, bse: bool = False) -> str:
    """Resolve NSE symbol or BSE code to yfinance ticker."""
    symbol = symbol.strip().upper()
    if bse:
        return f"{symbol}.BO"
    if symbol in _ALIASES:
        return _ALIASES[symbol]
    if symbol.endswith((".NS", ".BO")):
        return symbol
    # Default to NSE
    return f"{symbol}.NS"


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def _fmt_inr(value, unit="Cr") -> str:
    """Format a number as INR crores or lakhs."""
    if value is None:
        return "N/A"
    try:
        v = float(value)
    except (TypeError, ValueError):
        return "N/A"
    if unit == "Cr":
        crore = v / 1e7
        if abs(crore) >= 1e5:
            return f"₹{crore/1e5:.2f} Lakh Cr"
        return f"₹{crore:,.2f} Cr"
    return f"₹{v:,.2f}"


def _fmt_pct(value) -> str:
    if value is None:
        return "N/A"
    try:
        return f"{float(value):.2f}%"
    except (TypeError, ValueError):
        return "N/A"


def _fmt_num(value, decimals=2) -> str:
    if value is None:
        return "N/A"
    try:
        return f"{float(value):,.{decimals}f}"
    except (TypeError, ValueError):
        return "N/A"


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_quote(symbol: str, bse: bool = False):
    """Live quote snapshot from NSE or BSE."""
    import yfinance as yf

    ticker_str = _resolve_ticker(symbol, bse)
    t = yf.Ticker(ticker_str)
    info = t.info

    name = info.get("longName") or info.get("shortName") or symbol
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    prev_close = info.get("previousClose")
    open_ = info.get("open")
    high = info.get("dayHigh")
    low = info.get("dayLow")
    volume = info.get("volume")
    market_cap = info.get("marketCap")
    pe = info.get("trailingPE")
    forward_pe = info.get("forwardPE")
    pb = info.get("priceToBook")
    high_52w = info.get("fiftyTwoWeekHigh")
    low_52w = info.get("fiftyTwoWeekLow")
    shares = info.get("sharesOutstanding")
    dividend_yield = info.get("dividendYield")

    if price is None:
        print(f"❌ Could not fetch quote for {ticker_str}. Check the ticker symbol.")
        return

    change = (price - prev_close) if prev_close else None
    change_pct = (change / prev_close * 100) if prev_close and change else None

    print("=" * 65)
    print(f"  {name}  ({ticker_str})")
    print("=" * 65)
    print(f"  Current Price:    ₹{price:,.2f}")
    if change is not None:
        sign = "+" if change >= 0 else ""
        print(f"  Change:           {sign}₹{change:.2f} ({sign}{change_pct:.2f}%)")
    print(f"  Open:             ₹{_fmt_num(open_)}")
    print(f"  Day High/Low:     ₹{_fmt_num(high)} / ₹{_fmt_num(low)}")
    print(f"  Prev Close:       ₹{_fmt_num(prev_close)}")
    print(f"  Volume:           {int(volume):,}" if volume else "  Volume:           N/A")
    print(f"  52W High/Low:     ₹{_fmt_num(high_52w)} / ₹{_fmt_num(low_52w)}")
    print()
    print(f"  Market Cap:       {_fmt_inr(market_cap)}")
    print(f"  Shares Out:       {int(shares):,}" if shares else "  Shares Out:       N/A")
    print(f"  P/E (TTM):        {_fmt_num(pe)}")
    print(f"  P/E (Forward):    {_fmt_num(forward_pe)}")
    print(f"  P/B:              {_fmt_num(pb)}")
    # yfinance returns dividendYield already in percent (1.04 = 1.04%)
    print(f"  Dividend Yield:   {_fmt_pct(dividend_yield) if dividend_yield else 'N/A'}")

    # Market cap verification
    if price and shares and market_cap:
        calc_cap = float(price) * float(shares)
        reported_cap = float(market_cap)
        diff_pct = abs(calc_cap - reported_cap) / reported_cap * 100
        status = "✅" if diff_pct <= 2 else "⚠️"
        print(f"\n  Market Cap Check: {status} Price × Shares = {_fmt_inr(calc_cap)} "
              f"(reported {_fmt_inr(reported_cap)}, diff {diff_pct:.1f}%)")

    print(f"\n  Source: Yahoo Finance ({ticker_str}) — cross-validate with screener.in")


def cmd_financials(symbol: str, bse: bool = False):
    """5-year income statement and key financial metrics."""
    import yfinance as yf

    ticker_str = _resolve_ticker(symbol, bse)
    t = yf.Ticker(ticker_str)
    info = t.info

    name = info.get("longName") or info.get("shortName") or symbol

    print("=" * 65)
    print(f"  Financials: {name}  ({ticker_str})")
    print("=" * 65)

    try:
        income = t.financials  # annual, most recent first
        cashflow = t.cashflow
    except Exception as e:
        print(f"  ⚠️ Could not fetch financials: {e}")
        print("  → Cross-check manually at screener.in")
        return

    if income is None or income.empty:
        print("  ⚠️ No financial data available. Check screener.in for this company.")
        return

    rows_revenue = ["Total Revenue", "Revenue"]
    rows_profit = ["Net Income", "Net Income Common Stockholders"]
    rows_ebit = ["EBIT", "Operating Income"]
    rows_fcf_ops = ["Operating Cash Flow", "Total Cash From Operating Activities"]

    def _get_row(df, candidates):
        for name in candidates:
            if name in df.index:
                return df.loc[name]
        return None

    revenue_row = _get_row(income, rows_revenue)
    profit_row = _get_row(income, rows_profit)
    ebit_row = _get_row(income, rows_ebit)
    ocf_row = _get_row(cashflow, rows_fcf_ops) if cashflow is not None and not cashflow.empty else None

    cols = income.columns[:5]  # up to 5 years

    print(f"\n  {'Year':<12}", end="")
    for col in cols:
        year = str(col)[:4]
        print(f"  {year:>12}", end="")
    print()
    print("  " + "-" * (12 + 14 * len(cols)))

    def _print_row(label, row, unit="Cr"):
        if row is None:
            return
        print(f"  {label:<20}", end="")
        prev = None
        for col in cols:
            val = row.get(col)
            cr = val / 1e7 if val is not None and not (val != val) else None  # NaN check
            if cr is not None:
                growth = ""
                if prev is not None and prev != 0:
                    g = (cr - prev) / abs(prev) * 100
                    growth = f"({'+' if g >= 0 else ''}{g:.0f}%)"
                print(f"  {f'₹{cr:,.0f}Cr':>10} {growth:<6}", end="")
                prev = cr
            else:
                print(f"  {'N/A':>10}       ", end="")
        print()

    _print_row("Revenue (₹Cr)", revenue_row)
    _print_row("Net Profit (₹Cr)", profit_row)
    _print_row("EBIT (₹Cr)", ebit_row)
    _print_row("Op. Cash Flow", ocf_row)

    # Key ratios from info
    print(f"\n  Key Ratios (latest):")
    print(f"  {'ROE:':<25} {_fmt_pct(info.get('returnOnEquity', 0) * 100 if info.get('returnOnEquity') else None)}")
    print(f"  {'ROCE (approx ROA):':<25} {_fmt_pct(info.get('returnOnAssets', 0) * 100 if info.get('returnOnAssets') else None)}")
    print(f"  {'Gross Margin:':<25} {_fmt_pct(info.get('grossMargins', 0) * 100 if info.get('grossMargins') else None)}")
    print(f"  {'Operating Margin:':<25} {_fmt_pct(info.get('operatingMargins', 0) * 100 if info.get('operatingMargins') else None)}")
    print(f"  {'Net Margin:':<25} {_fmt_pct(info.get('profitMargins', 0) * 100 if info.get('profitMargins') else None)}")
    print(f"  {'Debt/Equity:':<25} {_fmt_num(info.get('debtToEquity'))}")
    print(f"  {'Current Ratio:':<25} {_fmt_num(info.get('currentRatio'))}")

    print(f"\n  ⚠️  Always cross-validate with screener.in and annual report (BSE/NSE filing)")


def cmd_valuation(symbol: str, bse: bool = False):
    """Valuation metrics summary."""
    import yfinance as yf

    ticker_str = _resolve_ticker(symbol, bse)
    t = yf.Ticker(ticker_str)
    info = t.info

    name = info.get("longName") or info.get("shortName") or symbol
    price = info.get("currentPrice") or info.get("regularMarketPrice")

    if not price:
        print(f"❌ Could not fetch data for {ticker_str}")
        return

    pe_ttm = info.get("trailingPE")
    pe_fwd = info.get("forwardPE")
    pb = info.get("priceToBook")
    ps = info.get("priceToSalesTrailing12Months")
    ev_ebitda = info.get("enterpriseToEbitda")
    ev_revenue = info.get("enterpriseToRevenue")
    market_cap = info.get("marketCap")
    enterprise_val = info.get("enterpriseValue")
    eps_ttm = info.get("trailingEps")
    eps_fwd = info.get("forwardEps")
    peg = info.get("pegRatio")
    roe = info.get("returnOnEquity")
    fcf = info.get("freeCashflow")
    fcf_yield = (fcf / market_cap * 100) if fcf and market_cap else None
    dividend_yield = info.get("dividendYield")
    beta = info.get("beta")

    print("=" * 65)
    print(f"  Valuation: {name}  ({ticker_str})")
    print("=" * 65)
    print(f"  Current Price:      ₹{price:,.2f}")
    print(f"  Market Cap:         {_fmt_inr(market_cap)}")
    print(f"  Enterprise Value:   {_fmt_inr(enterprise_val)}")
    print()
    print(f"  P/E (TTM):          {_fmt_num(pe_ttm)}x")
    print(f"  P/E (Forward):      {_fmt_num(pe_fwd)}x")
    print(f"  PEG Ratio:          {_fmt_num(peg)}")
    print(f"  P/B:                {_fmt_num(pb)}x")
    print(f"  P/S (TTM):          {_fmt_num(ps)}x")
    print(f"  EV/EBITDA:          {_fmt_num(ev_ebitda)}x")
    print(f"  EV/Revenue:         {_fmt_num(ev_revenue)}x")
    print()
    print(f"  EPS (TTM):          ₹{_fmt_num(eps_ttm)}")
    print(f"  EPS (Forward):      ₹{_fmt_num(eps_fwd)}")
    print(f"  ROE:                {_fmt_pct(roe * 100) if roe else 'N/A'}")
    print(f"  FCF Yield:          {_fmt_pct(fcf_yield)}")
    # yfinance returns dividendYield already in percent (1.04 = 1.04%)
    print(f"  Dividend Yield:     {_fmt_pct(dividend_yield) if dividend_yield else 'N/A'}")
    print(f"  Beta:               {_fmt_num(beta)}")
    print(f"\n  Source: Yahoo Finance ({ticker_str})")
    print(f"  Cross-validate P/E and ROE at: screener.in/company/{symbol.upper()}/")


def cmd_search(keyword: str):
    """Search for NSE-listed companies by name or keyword."""
    import yfinance as yf

    # Try direct NSE lookup first
    candidates = []
    test_ticker = f"{keyword.upper()}.NS"
    try:
        t = yf.Ticker(test_ticker)
        info = t.info
        if info.get("longName") or info.get("shortName"):
            candidates.append({
                "ticker": test_ticker,
                "name": info.get("longName") or info.get("shortName"),
                "market_cap": info.get("marketCap"),
            })
    except Exception:
        pass

    # Also check alias list
    kw = keyword.upper()
    for sym, yf_sym in _ALIASES.items():
        if kw in sym:
            try:
                t = yf.Ticker(yf_sym)
                info = t.info
                name = info.get("longName") or info.get("shortName") or sym
                candidates.append({
                    "ticker": yf_sym,
                    "name": name,
                    "market_cap": info.get("marketCap"),
                })
            except Exception:
                candidates.append({"ticker": yf_sym, "name": sym, "market_cap": None})

    if not candidates:
        print(f"❌ No results for '{keyword}'")
        print(f"   Try the exact NSE symbol (e.g., RELIANCE, HDFCBANK, TCS)")
        print(f"   Or visit: nseindia.com or screener.in to find the ticker")
        return

    print("=" * 65)
    print(f"  Search results for: '{keyword}'")
    print("=" * 65)
    seen = set()
    for c in candidates:
        if c["ticker"] in seen:
            continue
        seen.add(c["ticker"])
        cap_str = _fmt_inr(c["market_cap"]) if c["market_cap"] else "N/A"
        print(f"  {c['ticker']:<20}  {c['name']:<35}  {cap_str}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    _check_yfinance()

    parser = argparse.ArgumentParser(
        description="India Market Data Tool — NSE/BSE quotes and financials",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/india_data.py quote RELIANCE
  python3 tools/india_data.py quote 500325 --bse
  python3 tools/india_data.py financials TCS
  python3 tools/india_data.py valuation HDFCBANK
  python3 tools/india_data.py search "hdfc"
        """
    )
    sub = parser.add_subparsers(dest="command")

    p_quote = sub.add_parser("quote", help="Live quote")
    p_quote.add_argument("symbol", help="NSE symbol (e.g. RELIANCE) or BSE code with --bse")
    p_quote.add_argument("--bse", action="store_true", help="Use BSE (.BO) instead of NSE (.NS)")

    p_fin = sub.add_parser("financials", help="5-year financials")
    p_fin.add_argument("symbol", help="NSE symbol")
    p_fin.add_argument("--bse", action="store_true")

    p_val = sub.add_parser("valuation", help="Valuation metrics")
    p_val.add_argument("symbol", help="NSE symbol")
    p_val.add_argument("--bse", action="store_true")

    p_search = sub.add_parser("search", help="Search by name/keyword")
    p_search.add_argument("keyword", help="Company name or NSE symbol fragment")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    dispatch = {
        "quote": lambda: cmd_quote(args.symbol, getattr(args, "bse", False)),
        "financials": lambda: cmd_financials(args.symbol, getattr(args, "bse", False)),
        "valuation": lambda: cmd_valuation(args.symbol, getattr(args, "bse", False)),
        "search": lambda: cmd_search(args.keyword),
    }
    dispatch[args.command]()


if __name__ == "__main__":
    main()
