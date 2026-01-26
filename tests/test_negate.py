"""Tests for the negate function."""

import pytest

from runner import negate


class TestNegate:
    """Tests for the negate function."""

    def test_negate_positive_number(self):
        assert negate(5) == -5

    def test_negate_negative_number(self):
        assert negate(-5) == 5

    def test_negate_zero(self):
        assert negate(0) == 0

    def test_negate_positive_float(self):
        assert negate(3.14) == -3.14

    def test_negate_negative_float(self):
        assert negate(-3.14) == 3.14

    def test_negate_large_positive(self):
        assert negate(1000000) == -1000000

    def test_negate_large_negative(self):
        assert negate(-1000000) == 1000000
