#!/usr/bin/env python3
"""Simple calculator module with CLI interface.

This module provides basic arithmetic operations and a command-line interface
for performing calculations.

Usage:
    python calculator.py <operation> <num1> <num2>

Example:
    python calculator.py add 5 3
    python calculator.py divide 10 2
"""

from __future__ import annotations

import argparse
import sys
from typing import Callable

# Type alias for number inputs
Number = float

# Type alias for operation functions
Operation = Callable[[Number, Number], Number]

# Operations registry for CLI dispatch
OPERATIONS: dict[str, Operation] = {}


def register_operation(name: str) -> Callable[[Operation], Operation]:
    """Decorator to register an operation in the operations registry."""
    def decorator(func: Operation) -> Operation:
        OPERATIONS[name] = func
        return func
    return decorator


def validate_number(value: str, name: str = "value") -> Number:
    """Validate and convert a string to a number.

    Args:
        value: The string value to convert.
        name: Name of the parameter for error messages.

    Returns:
        The validated number.

    Raises:
        ValueError: If the value cannot be converted to a number.
    """
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid {name}: '{value}' is not a valid number")


@register_operation("add")
def add(a: Number, b: Number) -> Number:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b


@register_operation("subtract")
def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a.

    Args:
        a: Number to subtract from.
        b: Number to subtract.

    Returns:
        Difference of a and b.
    """
    return a - b


@register_operation("multiply")
def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of a and b.
    """
    return a * b


@register_operation("divide")
def divide(a: Number, b: Number) -> Number:
    """Divide a by b.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        Quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@register_operation("power")
def power(base: Number, exponent: Number) -> Number:
    """Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent.

    Returns:
        base raised to the power of exponent.
    """
    return base ** exponent


@register_operation("modulo")
def modulo(a: Number, b: Number) -> Number:
    """Compute the remainder of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The remainder of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot compute modulo with divisor zero")
    return a % b


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="calculator",
        description="A simple calculator CLI tool for basic arithmetic operations.",
        epilog="Example: python calculator.py add 5 3",
    )

    parser.add_argument(
        "operation",
        choices=list(OPERATIONS.keys()),
        help="The arithmetic operation to perform",
    )

    parser.add_argument(
        "num1",
        type=str,
        help="First number",
    )

    parser.add_argument(
        "num2",
        type=str,
        help="Second number",
    )

    return parser


def run_calculation(operation: str, num1: str, num2: str) -> Number:
    """Run a calculation with the specified operation and operands.

    Args:
        operation: Name of the operation to perform.
        num1: First operand as string.
        num2: Second operand as string.

    Returns:
        Result of the calculation.

    Raises:
        ValueError: If operation is unknown or inputs are invalid.
    """
    if operation not in OPERATIONS:
        valid_ops = ", ".join(OPERATIONS.keys())
        raise ValueError(f"Unknown operation: '{operation}'. Valid operations: {valid_ops}")

    a = validate_number(num1, "first number")
    b = validate_number(num2, "second number")

    return OPERATIONS[operation](a, b)


def format_result(result: Number) -> str:
    """Format the result for display.

    Args:
        result: The calculation result.

    Returns:
        Formatted string representation of the result.
    """
    # Display as integer if the result is a whole number
    if result == int(result):
        return str(int(result))
    return str(result)


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the calculator CLI.

    Args:
        argv: Command line arguments. Uses sys.argv if None.

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    parser = create_parser()
    args = parser.parse_args(argv)

    try:
        result = run_calculation(args.operation, args.num1, args.num2)
        print(format_result(result))
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
