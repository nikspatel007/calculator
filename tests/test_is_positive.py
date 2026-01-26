"""Tests for the is_positive function."""

import pytest

from runner import is_positive


class TestIsPositive:
    """Tests for the is_positive function."""

    def test_is_positive_positive_integer(self):
        assert is_positive(5) is True

    def test_is_positive_positive_one(self):
        assert is_positive(1) is True

    def test_is_positive_zero(self):
        assert is_positive(0) is False

    def test_is_positive_negative_integer(self):
        assert is_positive(-5) is False

    def test_is_positive_negative_one(self):
        assert is_positive(-1) is False

    def test_is_positive_positive_float(self):
        assert is_positive(3.14) is True

    def test_is_positive_negative_float(self):
        assert is_positive(-3.14) is False

    def test_is_positive_small_positive(self):
        assert is_positive(0.001) is True

    def test_is_positive_small_negative(self):
        assert is_positive(-0.001) is False

    def test_is_positive_large_positive(self):
        assert is_positive(1000000) is True

    def test_is_positive_large_negative(self):
        assert is_positive(-1000000) is False
