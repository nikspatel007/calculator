"""Tests for the memory module."""

import pytest

import memory
from memory import (
    store,
    recall,
    clear,
    add_to_memory,
    subtract_from_memory,
)


@pytest.fixture(autouse=True)
def reset_memory():
    """Reset memory before each test to ensure isolation."""
    memory._memory = 0.0
    yield
    memory._memory = 0.0


class TestStore:
    """Tests for the store function."""

    def test_store_positive_number(self):
        store(42)
        assert recall() == 42

    def test_store_negative_number(self):
        store(-10)
        assert recall() == -10

    def test_store_zero(self):
        store(100)
        store(0)
        assert recall() == 0

    def test_store_float(self):
        store(3.14159)
        assert recall() == 3.14159

    def test_store_overwrites_previous(self):
        store(100)
        store(200)
        assert recall() == 200

    def test_store_converts_int_to_float(self):
        store(5)
        assert isinstance(recall(), float)


class TestRecall:
    """Tests for the recall function."""

    def test_recall_initial_value(self):
        assert recall() == 0.0

    def test_recall_after_store(self):
        store(123.456)
        assert recall() == 123.456

    def test_recall_multiple_times(self):
        store(50)
        assert recall() == 50
        assert recall() == 50
        assert recall() == 50

    def test_recall_returns_float(self):
        assert isinstance(recall(), float)


class TestClear:
    """Tests for the clear function."""

    def test_clear_resets_to_zero(self):
        store(100)
        clear()
        assert recall() == 0.0

    def test_clear_on_empty_memory(self):
        clear()
        assert recall() == 0.0

    def test_clear_after_operations(self):
        store(50)
        add_to_memory(25)
        clear()
        assert recall() == 0.0


class TestAddToMemory:
    """Tests for the add_to_memory function."""

    def test_add_to_empty_memory(self):
        add_to_memory(10)
        assert recall() == 10

    def test_add_positive_to_positive(self):
        store(50)
        add_to_memory(25)
        assert recall() == 75

    def test_add_negative_to_positive(self):
        store(100)
        add_to_memory(-30)
        assert recall() == 70

    def test_add_positive_to_negative(self):
        store(-50)
        add_to_memory(75)
        assert recall() == 25

    def test_add_zero(self):
        store(42)
        add_to_memory(0)
        assert recall() == 42

    def test_add_float(self):
        store(10.5)
        add_to_memory(2.3)
        assert recall() == pytest.approx(12.8)

    def test_multiple_adds(self):
        add_to_memory(10)
        add_to_memory(20)
        add_to_memory(30)
        assert recall() == 60


class TestSubtractFromMemory:
    """Tests for the subtract_from_memory function."""

    def test_subtract_from_empty_memory(self):
        subtract_from_memory(10)
        assert recall() == -10

    def test_subtract_positive_from_positive(self):
        store(100)
        subtract_from_memory(30)
        assert recall() == 70

    def test_subtract_negative_from_positive(self):
        store(50)
        subtract_from_memory(-25)
        assert recall() == 75

    def test_subtract_from_negative(self):
        store(-10)
        subtract_from_memory(5)
        assert recall() == -15

    def test_subtract_zero(self):
        store(42)
        subtract_from_memory(0)
        assert recall() == 42

    def test_subtract_float(self):
        store(10.5)
        subtract_from_memory(2.3)
        assert recall() == pytest.approx(8.2)

    def test_multiple_subtracts(self):
        store(100)
        subtract_from_memory(10)
        subtract_from_memory(20)
        subtract_from_memory(30)
        assert recall() == 40


class TestMemoryIntegration:
    """Integration tests for memory operations."""

    def test_combined_operations(self):
        store(100)
        add_to_memory(50)
        subtract_from_memory(30)
        assert recall() == 120

    def test_clear_and_restart(self):
        store(50)
        add_to_memory(25)
        clear()
        store(10)
        assert recall() == 10

    def test_memory_persistence_within_operations(self):
        store(100)
        result1 = recall()
        add_to_memory(50)
        result2 = recall()
        subtract_from_memory(75)
        result3 = recall()
        assert result1 == 100
        assert result2 == 150
        assert result3 == 75

    def test_large_numbers(self):
        store(1e15)
        add_to_memory(1e15)
        assert recall() == 2e15

    def test_small_numbers(self):
        store(1e-10)
        add_to_memory(1e-10)
        assert recall() == pytest.approx(2e-10)
