"""Tests for the history module."""

import pytest
from datetime import datetime
from unittest.mock import patch

import history
from history import (
    record,
    get_history,
    clear_history,
    get_last,
    search,
    HistoryEntry,
)


class TestRecord:
    """Tests for the record function."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_record_basic(self):
        """Test recording a basic calculation."""
        entry = record("2 + 3", 5.0)
        assert entry["expression"] == "2 + 3"
        assert entry["result"] == 5.0
        assert "timestamp" in entry

    def test_record_returns_entry(self):
        """Test that record returns the created entry."""
        entry = record("10 / 2", 5.0)
        assert isinstance(entry, dict)
        assert "expression" in entry
        assert "result" in entry
        assert "timestamp" in entry

    def test_record_adds_to_history(self):
        """Test that record adds entry to history."""
        record("1 + 1", 2.0)
        assert len(get_history()) == 1

    def test_record_multiple(self):
        """Test recording multiple calculations."""
        record("1 + 1", 2.0)
        record("2 + 2", 4.0)
        record("3 + 3", 6.0)
        assert len(get_history()) == 3

    def test_record_timestamp_format(self):
        """Test that timestamp is in ISO format."""
        entry = record("5 * 5", 25.0)
        # Should be parseable as ISO format
        datetime.fromisoformat(entry["timestamp"])

    def test_record_negative_result(self):
        """Test recording a calculation with negative result."""
        entry = record("-5 + 2", -3.0)
        assert entry["result"] == -3.0

    def test_record_float_result(self):
        """Test recording a calculation with float result."""
        entry = record("10 / 3", 3.3333333333333335)
        assert entry["result"] == 3.3333333333333335


class TestGetHistory:
    """Tests for the get_history function."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_get_history_empty(self):
        """Test getting history when empty."""
        result = get_history()
        assert result == []

    def test_get_history_default_limit(self):
        """Test get_history with default limit of 10."""
        for i in range(15):
            record(f"{i} + 1", float(i + 1))
        result = get_history()
        assert len(result) == 10

    def test_get_history_custom_limit(self):
        """Test get_history with custom limit."""
        for i in range(10):
            record(f"{i} + 1", float(i + 1))
        result = get_history(limit=5)
        assert len(result) == 5

    def test_get_history_limit_larger_than_history(self):
        """Test get_history when limit is larger than history size."""
        record("1 + 1", 2.0)
        record("2 + 2", 4.0)
        result = get_history(limit=10)
        assert len(result) == 2

    def test_get_history_returns_most_recent(self):
        """Test that get_history returns most recent entries."""
        for i in range(15):
            record(f"expr_{i}", float(i))
        result = get_history(limit=5)
        # Should get entries 10-14 (most recent 5)
        assert result[0]["expression"] == "expr_10"
        assert result[4]["expression"] == "expr_14"

    def test_get_history_negative_limit_returns_all(self):
        """Test that negative limit returns all history."""
        for i in range(5):
            record(f"{i} + 1", float(i + 1))
        result = get_history(limit=-1)
        assert len(result) == 5

    def test_get_history_zero_limit(self):
        """Test get_history with zero limit."""
        record("1 + 1", 2.0)
        result = get_history(limit=0)
        assert result == []

    def test_get_history_preserves_order(self):
        """Test that get_history preserves chronological order."""
        record("first", 1.0)
        record("second", 2.0)
        record("third", 3.0)
        result = get_history()
        assert result[0]["expression"] == "first"
        assert result[1]["expression"] == "second"
        assert result[2]["expression"] == "third"

    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not the internal list."""
        record("1 + 1", 2.0)
        result = get_history()
        result.append({"expression": "fake", "result": 0.0, "timestamp": ""})
        # Original history should be unchanged
        assert len(get_history()) == 1


class TestClearHistory:
    """Tests for the clear_history function."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_clear_history_empty(self):
        """Test clearing empty history."""
        clear_history()
        assert get_history() == []

    def test_clear_history_with_entries(self):
        """Test clearing history with entries."""
        record("1 + 1", 2.0)
        record("2 + 2", 4.0)
        clear_history()
        assert get_history() == []

    def test_clear_history_allows_new_entries(self):
        """Test that new entries can be added after clear."""
        record("1 + 1", 2.0)
        clear_history()
        record("3 + 3", 6.0)
        assert len(get_history()) == 1
        assert get_history()[0]["expression"] == "3 + 3"


class TestGetLast:
    """Tests for the get_last function."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_get_last_empty(self):
        """Test get_last when history is empty."""
        result = get_last()
        assert result is None

    def test_get_last_single_entry(self):
        """Test get_last with single entry."""
        record("1 + 1", 2.0)
        result = get_last()
        assert result is not None
        assert result["expression"] == "1 + 1"
        assert result["result"] == 2.0

    def test_get_last_multiple_entries(self):
        """Test get_last returns the most recent entry."""
        record("first", 1.0)
        record("second", 2.0)
        record("third", 3.0)
        result = get_last()
        assert result is not None
        assert result["expression"] == "third"
        assert result["result"] == 3.0

    def test_get_last_after_clear(self):
        """Test get_last after clearing history."""
        record("1 + 1", 2.0)
        clear_history()
        result = get_last()
        assert result is None


class TestSearch:
    """Tests for the search function."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_search_empty_history(self):
        """Test search on empty history."""
        result = search("pattern")
        assert result == []

    def test_search_no_match(self):
        """Test search with no matching entries."""
        record("1 + 1", 2.0)
        record("2 + 2", 4.0)
        result = search("multiply")
        assert result == []

    def test_search_single_match(self):
        """Test search with single match."""
        record("add 1 2", 3.0)
        record("subtract 5 3", 2.0)
        result = search("add")
        assert len(result) == 1
        assert result[0]["expression"] == "add 1 2"

    def test_search_multiple_matches(self):
        """Test search with multiple matches."""
        record("add 1 2", 3.0)
        record("add 5 3", 8.0)
        record("subtract 5 3", 2.0)
        result = search("add")
        assert len(result) == 2

    def test_search_case_sensitive(self):
        """Test that search is case sensitive by default."""
        record("ADD 1 2", 3.0)
        record("add 5 3", 8.0)
        result = search("add")
        assert len(result) == 1
        assert result[0]["expression"] == "add 5 3"

    def test_search_partial_match(self):
        """Test search with partial pattern match."""
        record("multiply 2 3", 6.0)
        record("multifunction", 0.0)
        result = search("multi")
        assert len(result) == 2

    def test_search_regex_pattern(self):
        """Test search with regex pattern."""
        record("1 + 2", 3.0)
        record("10 + 20", 30.0)
        record("100 + 200", 300.0)
        # Pattern to match single digit additions
        result = search(r"^\d \+ \d$")
        assert len(result) == 1
        assert result[0]["expression"] == "1 + 2"

    def test_search_invalid_regex_falls_back_to_literal(self):
        """Test that invalid regex is treated as literal string."""
        record("test [bracket", 1.0)
        record("normal text", 2.0)
        # Invalid regex (unclosed bracket) should match literally
        result = search("[bracket")
        assert len(result) == 1
        assert result[0]["expression"] == "test [bracket"

    def test_search_special_characters(self):
        """Test search with special characters in pattern."""
        record("2 + 3", 5.0)
        record("2 * 3", 6.0)
        result = search(r"\+")
        assert len(result) == 1
        assert result[0]["expression"] == "2 + 3"

    def test_search_empty_pattern(self):
        """Test search with empty pattern matches all."""
        record("1 + 1", 2.0)
        record("2 + 2", 4.0)
        result = search("")
        assert len(result) == 2


class TestHistoryIntegration:
    """Integration tests for the history module."""

    def setup_method(self):
        """Clear history before each test."""
        clear_history()

    def test_full_workflow(self):
        """Test a full workflow of recording and retrieving."""
        # Record several calculations
        record("5 + 3", 8.0)
        record("10 - 2", 8.0)
        record("4 * 3", 12.0)

        # Check history
        hist = get_history()
        assert len(hist) == 3

        # Check last
        last = get_last()
        assert last is not None
        assert last["expression"] == "4 * 3"

        # Search
        addition_results = search(r"\+")
        assert len(addition_results) == 1

        # Clear
        clear_history()
        assert get_history() == []
        assert get_last() is None

    def test_history_persistence_across_operations(self):
        """Test that history persists across various operations."""
        record("expr1", 1.0)
        get_history()  # Reading shouldn't affect history
        record("expr2", 2.0)
        search("expr")  # Searching shouldn't affect history
        record("expr3", 3.0)
        get_last()  # Getting last shouldn't affect history

        assert len(get_history()) == 3
