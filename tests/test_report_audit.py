"""Tests for report_audit.py pure functions — no file I/O."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tools.report_audit import (
    _clean_num, _is_valid_label, _parse_md_tables, extract_data_points,
    sample_points, _pct_diff, render_verdict
)


class TestCleanNum:
    def test_integer_string(self):
        assert _clean_num("1234") == 1234.0

    def test_with_commas(self):
        assert _clean_num("1,234,567") == 1234567.0

    def test_with_chinese_commas(self):
        assert _clean_num("1，234") == 1234.0

    def test_decimal(self):
        assert abs(_clean_num("3.14") - 3.14) < 0.001

    def test_mixed_commas(self):
        assert _clean_num("9,803.5") == 9803.5

    def test_invalid_alpha_returns_none(self):
        assert _clean_num("abc") is None

    def test_empty_string_returns_none(self):
        assert _clean_num("") is None

    def test_whitespace_stripped(self):
        assert _clean_num("  100  ") == 100.0


class TestIsValidLabel:
    def test_valid_english_label(self):
        assert _is_valid_label("Revenue") is True

    def test_valid_two_word_label(self):
        assert _is_valid_label("Net Profit") is True

    def test_too_short_single_char(self):
        assert _is_valid_label("x") is False

    def test_pure_year_rejected(self):
        assert _is_valid_label("2024") is False

    def test_markdown_bold_rejected(self):
        assert _is_valid_label("**Revenue**") is False

    def test_backtick_rejected(self):
        assert _is_valid_label("`code`") is False

    def test_skip_word_total(self):
        assert _is_valid_label("total") is False

    def test_skip_word_na(self):
        assert _is_valid_label("N/A") is False

    def test_skip_word_sources(self):
        assert _is_valid_label("来源") is False

    def test_pipe_prefix_rejected(self):
        assert _is_valid_label("| Revenue") is False

    def test_hash_prefix_rejected(self):
        assert _is_valid_label("# Heading") is False

    def test_percentage_label_rejected(self):
        assert _is_valid_label("+56%") is False


class TestParseMdTables:
    def test_basic_two_column_table(self):
        lines = [
            "| Metric | Value |",
            "|--------|-------|",
            "| Revenue | 9803 |",
        ]
        results = _parse_md_tables(lines)
        assert len(results) > 0
        assert any(r[2] == 9803.0 for r in results)

    def test_percentage_value(self):
        lines = [
            "| Metric | FY2025 |",
            "|--------|--------|",
            "| Gross Margin | 45% |",
        ]
        results = _parse_md_tables(lines)
        assert any(r[2] == 45.0 for r in results)

    def test_no_table_returns_empty(self):
        lines = ["Just some text", "No table here"]
        assert _parse_md_tables(lines) == []

    def test_multi_column_table(self):
        lines = [
            "| Metric | FY23 | FY24 | FY25 |",
            "|--------|------|------|------|",
            "| Revenue | 8000 | 9000 | 9803 |",
        ]
        results = _parse_md_tables(lines)
        vals = [r[2] for r in results]
        assert 9803.0 in vals
        assert 9000.0 in vals

    def test_row_label_captured(self):
        lines = [
            "| Metric | Value |",
            "|--------|-------|",
            "| EBITDA | 2500 |",
        ]
        results = _parse_md_tables(lines)
        labels = [r[0] for r in results]
        assert any("EBITDA" in l for l in labels)

    def test_zero_value_skipped(self):
        lines = [
            "| Metric | Value |",
            "|--------|-------|",
            "| Revenue | 0 |",
        ]
        results = _parse_md_tables(lines)
        assert all(r[2] != 0 for r in results)


class TestExtractDataPoints:
    def test_kv_line_extracted(self):
        md = "Revenue: 9803\nNet Profit: 1200"
        points = extract_data_points(md)
        vals = [p["reported_value"] for p in points]
        assert 9803.0 in vals or 1200.0 in vals

    def test_deduplication(self):
        md = "Revenue: 9803\nRevenue: 9803"
        points = extract_data_points(md)
        keys = [f"{p['label']}|{p['reported_value']}" for p in points]
        assert len(keys) == len(set(keys))

    def test_empty_report(self):
        assert extract_data_points("") == []

    def test_sequential_ids(self):
        md = "Revenue: 9803\nPE: 22\nMargin: 15"
        points = extract_data_points(md)
        if len(points) >= 2:
            ids = [p["id"] for p in points]
            assert ids == list(range(1, len(ids) + 1))

    def test_point_has_required_keys(self):
        md = "Revenue: 9803"
        points = extract_data_points(md)
        if points:
            required = {"id", "label", "reported_value", "unit", "raw_text", "line_number"}
            assert required.issubset(set(points[0].keys()))

    def test_table_data_extracted(self):
        md = "| Metric | Value |\n|--------|-------|\n| Revenue | 5000 |\n"
        points = extract_data_points(md)
        vals = [p["reported_value"] for p in points]
        assert 5000.0 in vals

    def test_code_block_skipped(self):
        md = "```\nRevenue: 9803\n```"
        points = extract_data_points(md)
        # Data inside code fences should not be extracted
        vals = [p["reported_value"] for p in points]
        assert 9803.0 not in vals

    def test_heading_line_skipped(self):
        md = "# Revenue: 9803"
        points = extract_data_points(md)
        vals = [p["reported_value"] for p in points]
        assert 9803.0 not in vals


class TestSamplePoints:
    def _make_points(self, n=20):
        return [
            {"id": i, "label": f"Metric{i}", "reported_value": float(i * 100),
             "unit": "Cr", "raw_text": f"Metric{i}: {i*100}", "line_number": i}
            for i in range(1, n + 1)
        ]

    def test_samples_at_least_3(self):
        points = self._make_points(20)
        sampled = sample_points(points, ratio=0.05)
        assert len(sampled) >= 3

    def test_samples_at_most_30(self):
        points = self._make_points(300)
        sampled = sample_points(points, ratio=0.15)
        assert len(sampled) <= 30

    def test_deterministic_with_seed(self):
        points = self._make_points(50)
        s1 = sample_points(points, seed=42)
        s2 = sample_points(points, seed=42)
        assert [p["id"] for p in s1] == [p["id"] for p in s2]

    def test_different_seeds_differ(self):
        points = self._make_points(50)
        s1 = sample_points(points, seed=1)
        s2 = sample_points(points, seed=99)
        assert [p["id"] for p in s1] != [p["id"] for p in s2]

    def test_sampled_sorted_by_line_number(self):
        points = self._make_points(30)
        sampled = sample_points(points, seed=7)
        line_nums = [p["line_number"] for p in sampled]
        assert line_nums == sorted(line_nums)


class TestPctDiff:
    def test_exact_match(self):
        assert _pct_diff(100.0, 100.0) == 0.0

    def test_one_percent_off(self):
        assert abs(_pct_diff(100.0, 101.0) - 0.01) < 1e-9

    def test_reported_zero_fetched_zero(self):
        assert _pct_diff(0.0, 0.0) == 0.0

    def test_reported_zero_fetched_nonzero(self):
        assert _pct_diff(0.0, 50.0) == float("inf")

    def test_symmetry_is_absolute(self):
        # Both over and under are treated the same
        assert abs(_pct_diff(100, 90) - _pct_diff(100, 110)) < 1e-9


class TestRenderVerdict:
    def _item(self, id_, label, reported, fetched, source="Screener"):
        return {
            "id": id_, "label": label, "reported_value": reported,
            "fetched_value": fetched, "fetched_source": source,
            "unit": "Cr", "raw_text": f"{label}: {reported}", "line_number": id_
        }

    def test_all_pass(self, capsys):
        results = [
            self._item(1, "Revenue", 9803, 9810),
            self._item(2, "Net Profit", 1200, 1205),
        ]
        verdict = render_verdict(results, "Test Report")
        assert verdict["verdict"] == "PASS"
        assert verdict["fail_count"] == 0
        assert verdict["pass_count"] == 2

    def test_one_fail(self, capsys):
        # FAIL requires both sources to disagree — add fetched_value2 that also fails
        item_pass = self._item(1, "Revenue", 9803, 9810)
        item_fail = self._item(2, "Net Profit", 1200, 1500)  # source1 25% off
        item_fail["fetched_value2"] = 1450   # source2 also 20% off → both fail → FAIL
        item_fail["fetched_source2"] = "Trendlyne"
        verdict = render_verdict([item_pass, item_fail])
        assert verdict["verdict"] == "FAIL"
        assert verdict["fail_count"] == 1
        assert len(verdict["fail_items"]) == 1

    def test_no_fetched_value_skipped(self, capsys):
        results = [{"id": 1, "label": "Revenue", "reported_value": 9803,
                    "fetched_value": None, "unit": "Cr", "raw_text": "", "line_number": 1}]
        verdict = render_verdict(results)
        assert verdict["total"] == 0  # skipped item not counted

    def test_two_source_both_pass(self, capsys):
        item = self._item(1, "Revenue", 9803, 9810)
        item["fetched_value2"] = 9800
        item["fetched_source2"] = "Trendlyne"
        verdict = render_verdict([item])
        assert verdict["verdict"] == "PASS"

    def test_report_name_in_output(self, capsys):
        render_verdict([], "MyReport")
        out = capsys.readouterr().out
        assert "MyReport" in out
