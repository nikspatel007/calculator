"""Tests for the is_even function."""

import pytest

from runner import is_even


class TestIsEven:
    """Tests for the is_even function."""

    def test_is_even_positive_even(self):
        assert is_even(4) is True

    def test_is_even_positive_odd(self):
        assert is_even(5) is False

    def test_is_even_negative_even(self):
        assert is_even(-4) is True

    def test_is_even_negative_odd(self):
        assert is_even(-5) is False

    def test_is_even_zero(self):
        assert is_even(0) is True

    def test_is_even_two(self):
        assert is_even(2) is True

    def test_is_even_one(self):
        assert is_even(1) is False

    def test_is_even_large_even(self):
        assert is_even(1000000) is True

    def test_is_even_large_odd(self):
        assert is_even(1000001) is False

    def test_is_even_float_integer_even(self):
        # 4.0 should be treated as 4
        assert is_even(4.0) is True

    def test_is_even_float_integer_odd(self):
        # 5.0 should be treated as 5
        assert is_even(5.0) is False

    def test_is_even_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot determine if non-integer is even"):
            is_even(4.5)

    def test_is_even_negative_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot determine if non-integer is even"):
            is_even(-3.5)
