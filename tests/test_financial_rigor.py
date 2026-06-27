"""Tests for tools/financial_rigor.py — exact decimal arithmetic and validation."""
import sys
import os
from decimal import Decimal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from tools.financial_rigor import exact, verify_market_cap, verify_valuation, cross_validate


class TestExact:
    def test_int_to_decimal(self):
        assert exact(100) == Decimal("100")

    def test_float_avoids_trap(self):
        # The classic float trap: 0.1 + 0.2 != 0.3 in float
        assert float(0.1) + float(0.2) != 0.3
        # But exact() fixes it
        assert exact("0.1") + exact("0.2") == Decimal("0.3")

    def test_decimal_passthrough(self):
        d = Decimal("42.5")
        assert exact(d) is d

    def test_scientific_notation(self):
        assert exact("6.76e9") == Decimal("6760000000")

    def test_negative(self):
        assert exact(-50) == Decimal("-50")


class TestVerifyMarketCap:
    def test_passes_within_tolerance(self, capsys):
        # Reliance: ~₹2950 × 6.76B shares ≈ ₹19.94T
        result = verify_market_cap(
            price=2950,
            shares=6.76e9,
            reported_cap=19.944e12,
            currency="INR"
        )
        assert result is True
        captured = capsys.readouterr()
        assert "✅" in captured.out

    def test_fails_on_large_deviation(self, capsys):
        # Price is 10x wrong — should fail
        result = verify_market_cap(
            price=29500,
            shares=6.76e9,
            reported_cap=19.944e12,
            currency="INR"
        )
        assert result is False
        captured = capsys.readouterr()
        assert "❌" in captured.out

    def test_warns_on_medium_deviation(self, capsys):
        # ~3% deviation — within acceptable, but warns
        result = verify_market_cap(
            price=2950,
            shares=6.76e9,
            reported_cap=19.3e12,   # ~3% off
            currency="INR"
        )
        assert result is True
        captured = capsys.readouterr()
        assert "⚠️" in captured.out

    def test_currency_label_in_output(self, capsys):
        verify_market_cap(100, 1e6, 1e8, currency="INR")
        captured = capsys.readouterr()
        assert "INR" in captured.out


class TestVerifyValuation:
    def test_pe_calculation(self, capsys):
        results = verify_valuation(price=2950, eps=134.0)
        assert "PE" in results
        # PE = 2950 / 134 ≈ 22.01
        assert abs(results["PE"] - (2950 / 134)) < 0.01

    def test_pb_calculation(self):
        results = verify_valuation(price=500, bvps=250.0)
        assert "PB" in results
        assert abs(results["PB"] - 2.0) < 0.001

    def test_roe_from_eps_and_bvps(self):
        results = verify_valuation(price=500, eps=50.0, bvps=250.0)
        assert "ROE" in results
        # ROE = EPS / BVPS × 100 = 50/250 × 100 = 20%
        assert abs(results["ROE"] - 20.0) < 0.001

    def test_fcf_yield(self):
        results = verify_valuation(price=1000, fcf_per_share=50.0)
        assert "FCF_Yield" in results
        # FCF yield = 50/1000 × 100 = 5%
        assert abs(results["FCF_Yield"] - 5.0) < 0.001

    def test_dividend_yield(self):
        results = verify_valuation(price=1000, dividend=20.0)
        assert "Dividend_Yield" in results
        # Yield = 20/1000 × 100 = 2%
        assert abs(results["Dividend_Yield"] - 2.0) < 0.001

    def test_zero_eps_handled(self, capsys):
        # Should not crash when EPS is 0
        results = verify_valuation(price=500, eps=0)
        captured = capsys.readouterr()
        assert "PE" not in results  # PE undefined when EPS=0


class TestCrossValidate:
    def test_consistent_sources_pass(self, capsys):
        results = cross_validate(
            "revenue",
            {"Screener": 9803, "Trendlyne": 9810, "Annual Report": 9798},
            unit="Cr"
        )
        assert results["all_consistent"] is True

    def test_divergent_source_flagged(self, capsys):
        results = cross_validate(
            "revenue",
            {"Screener": 9803, "Trendlyne": 12000},  # ~22% gap
            unit="Cr",
            tolerance_pct=2.0
        )
        assert results["all_consistent"] is False
        captured = capsys.readouterr()
        assert "❌" in captured.out

    def test_consensus_is_median(self):
        results = cross_validate(
            "revenue",
            {"Screener": 9800, "Trendlyne": 9900, "BSE": 9850},
            unit="Cr"
        )
        # Median of [9800, 9850, 9900] = 9850
        assert abs(results["consensus"] - 9850) < 1

    def test_single_source_shows_count(self, capsys):
        cross_validate("revenue", {"Screener": 9803}, unit="Cr")
        captured = capsys.readouterr()
        assert "1" in captured.out
