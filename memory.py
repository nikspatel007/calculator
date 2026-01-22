"""Memory functions for the calculator.

This module provides memory operations similar to M+, M-, MR, MC buttons
on a physical calculator. Memory persists within a session (module-level state).
"""

from __future__ import annotations

# Module-level memory storage
_memory: float = 0.0


def store(value: float) -> None:
    """Store a value in memory.

    Args:
        value: The value to store in memory.
    """
    global _memory
    _memory = float(value)


def recall() -> float:
    """Recall the stored value from memory.

    Returns:
        The value currently stored in memory.
    """
    return _memory


def clear() -> None:
    """Clear the memory (reset to zero)."""
    global _memory
    _memory = 0.0


def add_to_memory(value: float) -> None:
    """Add a value to the current memory (M+ operation).

    Args:
        value: The value to add to memory.
    """
    global _memory
    _memory += float(value)


def subtract_from_memory(value: float) -> None:
    """Subtract a value from the current memory (M- operation).

    Args:
        value: The value to subtract from memory.
    """
    global _memory
    _memory -= float(value)
