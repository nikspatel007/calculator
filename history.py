"""Calculation history tracking module.

This module provides functionality to track and manage calculation history,
including recording calculations, retrieving history, searching, and clearing.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import TypedDict


class HistoryEntry(TypedDict):
    """Type definition for a history entry."""

    expression: str
    result: float
    timestamp: str


# Internal storage for calculation history
_history: list[HistoryEntry] = []


def record(expression: str, result: float) -> HistoryEntry:
    """Record a calculation to the history.

    Args:
        expression: The expression that was calculated (e.g., "2 + 3").
        result: The result of the calculation.

    Returns:
        The history entry that was created.
    """
    entry: HistoryEntry = {
        "expression": expression,
        "result": result,
        "timestamp": datetime.now().isoformat(),
    }
    _history.append(entry)
    return entry


def get_history(limit: int = 10) -> list[HistoryEntry]:
    """Get recent calculations from history.

    Args:
        limit: Maximum number of entries to return (default 10).
               Use -1 or a negative value to get all history.
               Use 0 to get an empty list.

    Returns:
        A list of the most recent history entries, up to the limit.
        Returns entries in chronological order (oldest first).
    """
    if limit < 0:
        return list(_history)
    if limit == 0:
        return []
    return list(_history[-limit:])


def clear_history() -> None:
    """Clear all calculation history."""
    _history.clear()


def get_last() -> HistoryEntry | None:
    """Get the most recent calculation.

    Returns:
        The most recent history entry, or None if history is empty.
    """
    if not _history:
        return None
    return _history[-1]


def search(pattern: str) -> list[HistoryEntry]:
    """Search history for matching expressions.

    Args:
        pattern: A substring or regex pattern to match against expressions.

    Returns:
        A list of history entries whose expressions match the pattern.
    """
    try:
        regex = re.compile(pattern)
        return [entry for entry in _history if regex.search(entry["expression"])]
    except re.error:
        # If pattern is not a valid regex, treat it as a literal substring
        return [entry for entry in _history if pattern in entry["expression"]]
