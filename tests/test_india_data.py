"""Tests for india_data.py pure functions — no network calls."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tools.india_data import _resolve_ticker, _fmt_inr, _fmt_pct, _fmt_num, _ALIASES


class TestResolveTicker:
    def test_known_nse_alias(self):
        assert _resolve_ticker("RELIANCE") == "RELIANCE.NS"

    def test_bse_flag_adds_bo(self):
        assert _resolve_ticker("500325", bse=True) == "500325.BO"

    def test_already_ns_passthrough(self):
        assert _resolve_ticker("TCS.NS") == "TCS.NS"

    def test_already_bo_passthrough(self):
        assert _resolve_ticker("500325.BO") == "500325.BO"

    def test_unknown_defaults_to_ns(self):
        assert _resolve_ticker("UNKNOWNCO") == "UNKNOWNCO.NS"

    def test_lowercase_upcased(self):
        assert _resolve_ticker("reliance") == "RELIANCE.NS"

    def test_whitespace_stripped(self):
        assert _resolve_ticker("  TCS  ") == "TCS.NS"

    def test_all_major_aliases_resolve(self):
        for sym in ["TCS", "HDFCBANK", "INFY", "ICICIBANK", "WIPRO", "ZOMATO"]:
            result = _resolve_ticker(sym)
            assert result.endswith(".NS"), f"{sym} did not resolve to .NS"


class TestFmtInr:
    def test_crore_label(self):
        assert "Cr" in _fmt_inr(1e9)  # 100 Cr

    def test_lakh_crore_label(self):
        assert "Lakh Cr" in _fmt_inr(1e14)  # 10 Lakh Cr

    def test_none_returns_na(self):
        assert _fmt_inr(None) == "N/A"

    def test_zero(self):
        assert "0.00" in _fmt_inr(0)

    def test_negative(self):
        result = _fmt_inr(-5e9)
        assert "-" in result and "Cr" in result

    def test_rupee_symbol_present(self):
        assert "₹" in _fmt_inr(1e9)

    def test_invalid_string_returns_na(self):
        assert _fmt_inr("not-a-number") == "N/A"

    def test_non_crore_unit(self):
        result = _fmt_inr(50000, unit="other")
        assert "₹" in result and "50,000" in result


class TestFmtPct:
    def test_basic(self):
        assert _fmt_pct(12.5) == "12.50%"

    def test_none_returns_na(self):
        assert _fmt_pct(None) == "N/A"

    def test_zero(self):
        assert _fmt_pct(0) == "0.00%"

    def test_negative(self):
        result = _fmt_pct(-5.3)
        assert result == "-5.30%"

    def test_large_value(self):
        assert _fmt_pct(100) == "100.00%"

    def test_invalid_string_returns_na(self):
        assert _fmt_pct("bad") == "N/A"


class TestFmtNum:
    def test_basic_two_decimals(self):
        assert _fmt_num(1234.5) == "1,234.50"

    def test_none_returns_na(self):
        assert _fmt_num(None) == "N/A"

    def test_custom_decimals(self):
        assert _fmt_num(3.14159, decimals=4) == "3.1416"

    def test_zero_decimals(self):
        assert _fmt_num(1000, decimals=0) == "1,000"

    def test_large_number_comma_separated(self):
        result = _fmt_num(1234567.89)
        assert "1,234,567.89" in result

    def test_invalid_string_returns_na(self):
        assert _fmt_num("bad") == "N/A"


class TestAliasesIntegrity:
    def test_all_aliases_end_with_ns_or_bo(self):
        for sym, yf_sym in _ALIASES.items():
            assert yf_sym.endswith(".NS") or yf_sym.endswith(".BO"), (
                f"Alias {sym} → {yf_sym} has unexpected suffix"
            )

    def test_nifty50_heavyweights_present(self):
        required = ["RELIANCE", "TCS", "HDFCBANK", "INFY", "ICICIBANK",
                    "HINDUNILVR", "BAJFINANCE", "SBIN", "KOTAKBANK"]
        for sym in required:
            assert sym in _ALIASES, f"{sym} missing from _ALIASES"

    def test_no_duplicate_yf_symbols(self):
        yf_symbols = list(_ALIASES.values())
        assert len(yf_symbols) == len(set(yf_symbols)), "Duplicate yfinance symbols found"

    def test_alias_keys_are_uppercase(self):
        for sym in _ALIASES:
            assert sym == sym.upper(), f"Alias key '{sym}' is not uppercase"
