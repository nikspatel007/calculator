"""Tests for the sign function."""

import pytest

from runner import sign


class TestSign:
    """Tests for the sign function."""

    def test_sign_positive_integer(self):
        assert sign(5) == 1

    def test_sign_negative_integer(self):
        assert sign(-5) == -1

    def test_sign_zero(self):
        assert sign(0) == 0

    def test_sign_positive_float(self):
        assert sign(3.14) == 1

    def test_sign_negative_float(self):
        assert sign(-3.14) == -1

    def test_sign_small_positive(self):
        assert sign(0.0001) == 1

    def test_sign_small_negative(self):
        assert sign(-0.0001) == -1

    def test_sign_large_positive(self):
        assert sign(1000000) == 1

    def test_sign_large_negative(self):
        assert sign(-1000000) == -1
