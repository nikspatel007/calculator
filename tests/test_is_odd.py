"""Tests for the is_odd function."""

import pytest

from runner import is_odd


class TestIsOdd:
    """Tests for the is_odd function."""

    def test_is_odd_positive_odd(self):
        assert is_odd(5) is True

    def test_is_odd_positive_even(self):
        assert is_odd(4) is False

    def test_is_odd_negative_odd(self):
        assert is_odd(-5) is True

    def test_is_odd_negative_even(self):
        assert is_odd(-4) is False

    def test_is_odd_zero(self):
        assert is_odd(0) is False

    def test_is_odd_one(self):
        assert is_odd(1) is True

    def test_is_odd_two(self):
        assert is_odd(2) is False

    def test_is_odd_large_odd(self):
        assert is_odd(1000001) is True

    def test_is_odd_large_even(self):
        assert is_odd(1000000) is False

    def test_is_odd_float_integer_odd(self):
        # 5.0 should be treated as 5
        assert is_odd(5.0) is True

    def test_is_odd_float_integer_even(self):
        # 4.0 should be treated as 4
        assert is_odd(4.0) is False

    def test_is_odd_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot determine if non-integer is odd"):
            is_odd(4.5)

    def test_is_odd_negative_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot determine if non-integer is odd"):
            is_odd(-3.5)
