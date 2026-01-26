"""Tests for the clamp function."""

import pytest

from runner import clamp


class TestClamp:
    """Tests for the clamp function."""

    def test_clamp_value_within_range(self):
        assert clamp(5, 0, 10) == 5

    def test_clamp_value_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_clamp_value_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_clamp_value_equals_min(self):
        assert clamp(0, 0, 10) == 0

    def test_clamp_value_equals_max(self):
        assert clamp(10, 0, 10) == 10

    def test_clamp_negative_range(self):
        assert clamp(-5, -10, -1) == -5

    def test_clamp_value_below_negative_range(self):
        assert clamp(-15, -10, -1) == -10

    def test_clamp_value_above_negative_range(self):
        assert clamp(0, -10, -1) == -1

    def test_clamp_float_value(self):
        assert clamp(5.5, 0, 10) == 5.5

    def test_clamp_float_min_max(self):
        assert clamp(5, 0.5, 9.5) == 5

    def test_clamp_float_below_min(self):
        assert clamp(0.1, 0.5, 9.5) == 0.5

    def test_clamp_float_above_max(self):
        assert clamp(10.0, 0.5, 9.5) == 9.5

    def test_clamp_min_equals_max(self):
        assert clamp(5, 3, 3) == 3

    def test_clamp_min_greater_than_max_raises_error(self):
        with pytest.raises(ValueError, match="Minimum value cannot be greater than maximum value"):
            clamp(5, 10, 0)

    def test_clamp_large_values(self):
        assert clamp(500, 0, 1000000) == 500

    def test_clamp_zero_range(self):
        assert clamp(0, 0, 0) == 0
