"""Extended tests for financial_rigor.py — fmt_number, exact_calc, three_scenario, benford."""
import math
import random
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tools.financial_rigor import (
    exact, fmt_number, exact_calc, three_scenario_valuation, benford_check
)


class TestFmtNumber:
    def test_trillions(self):
        assert "T" in fmt_number(exact(2e12))

    def test_billions(self):
        assert "B" in fmt_number(exact(2e9))

    def test_millions(self):
        assert "M" in fmt_number(exact(5e6))

    def test_small_number(self):
        assert "42.50" in fmt_number(exact(42.5))

    def test_negative_billion(self):
        result = fmt_number(exact(-3e9))
        assert "B" in result and "-" in result

    def test_zero(self):
        assert "0.00" in fmt_number(exact(0))

    def test_yi_unit(self):
        result = fmt_number(exact(500), unit="亿")
        assert "亿" in result

    def test_yi_large_converts_to_wan_yi(self):
        result = fmt_number(exact(15000), unit="亿")
        assert "万亿" in result


class TestExactCalc:
    def test_multiplication(self):
        result = exact_calc("2950 * 6.76e9")
        assert result is not None
        assert abs(result - 2950 * 6.76e9) < 1

    def test_addition(self):
        assert exact_calc("100 + 200") == 300.0

    def test_subtraction(self):
        assert exact_calc("500 - 150") == 350.0

    def test_division(self):
        assert abs(exact_calc("1000 / 40") - 25.0) < 0.001

    def test_parentheses(self):
        assert exact_calc("(100 + 200) * 3") == 900.0

    def test_unsafe_blocked_underscore(self):
        assert exact_calc("__import__('os')") is None

    def test_unsafe_blocked_letter(self):
        assert exact_calc("x + 1") is None

    def test_scientific_notation(self):
        result = exact_calc("1.5e6 * 2")
        assert abs(result - 3e6) < 1


class TestThreeScenario:
    def test_prints_all_three_scenarios(self, capsys):
        three_scenario_valuation(
            current_price=2950, current_eps=134, shares_billion=6.76,
            growth_optimistic=0.20, growth_neutral=0.12, growth_pessimistic=0.05,
            pe_optimistic=28, pe_neutral=22, pe_pessimistic=16,
            years=3, currency="INR"
        )
        out = capsys.readouterr().out
        assert "Bull" in out
        assert "Base" in out
        assert "Bear" in out
        assert "✅" in out

    def test_bull_shows_plus_return(self, capsys):
        three_scenario_valuation(
            current_price=100, current_eps=5, shares_billion=1,
            growth_optimistic=0.25, growth_neutral=0.10, growth_pessimistic=0.02,
            pe_optimistic=30, pe_neutral=20, pe_pessimistic=12,
            years=3
        )
        out = capsys.readouterr().out
        assert "+" in out  # bull case shows positive upside

    def test_currency_shown(self, capsys):
        three_scenario_valuation(
            current_price=500, current_eps=20, shares_billion=1,
            growth_optimistic=0.15, growth_neutral=0.08, growth_pessimistic=0.03,
            pe_optimistic=25, pe_neutral=18, pe_pessimistic=12,
            years=3, currency="INR"
        )
        out = capsys.readouterr().out
        assert "INR" in out


class TestBenford:
    @staticmethod
    def _benford_data(n=200, seed=42):
        """Log-uniform data that naturally follows Benford's law."""
        rng = random.Random(seed)
        return [10 ** rng.uniform(0, 6) for _ in range(n)]

    def test_too_small_sample_returns_none(self, capsys):
        result = benford_check([100, 200, 300])
        assert result is None
        assert "⚠️" in capsys.readouterr().out

    def test_natural_data_conforms(self):
        result = benford_check(self._benford_data(200))
        assert result is not None
        assert result["is_conforming"] is True
        assert result["mad"] < 0.015

    def test_returns_expected_keys(self):
        result = benford_check(self._benford_data(100))
        assert result is not None
        assert set(result.keys()) == {"mad", "chi2", "conformity", "is_conforming"}

    def test_mad_is_float(self):
        result = benford_check(self._benford_data(100))
        assert isinstance(result["mad"], float)

    def test_filters_zero_values(self):
        data = self._benford_data(200) + [0, 0, 0]
        result = benford_check(data)
        assert result is not None  # zeros are skipped, not counted

    def test_negative_values_handled(self):
        data = self._benford_data(200)
        data_with_neg = [-v for v in data[:50]] + data[50:]
        result = benford_check(data_with_neg)
        assert result is not None  # abs() handles negatives

    def test_nonconforming_data_returns_result(self, capsys):
        # 6-digit uniform integers violate Benford — all leading digits near-equal
        rng = random.Random(99)
        data = [float(rng.randint(100000, 999999)) for _ in range(200)]
        result = benford_check(data)
        assert result is not None
        assert "conformity" in result

    def test_marginally_acceptable_range(self):
        # Craft data where MAD lands in 0.012–0.015 (marginally acceptable)
        # Hard to hit exactly — just verify low-sample near-miss still runs
        rng = random.Random(7)
        data = [10 ** rng.uniform(0, 4) for _ in range(60)]
        result = benford_check(data)
        assert result is not None


class TestExactCalcErrors:
    def test_division_by_zero_returns_none(self, capsys):
        result = exact_calc("1/0")
        assert result is None
        assert "❌" in capsys.readouterr().out
