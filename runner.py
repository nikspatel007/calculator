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
import math
import sys
from typing import Callable

# Type alias for number inputs
Number = float

# Type alias for operation functions
Operation = Callable[[Number, Number], Number]
UnaryOperation = Callable[[Number], Number]

# Operations registry for CLI dispatch
OPERATIONS: dict[str, Operation] = {}

# Track which operations are unary (single argument)
UNARY_OPERATIONS: set[str] = set()

# Track which operations take a list of arguments
LIST_OPERATIONS: set[str] = set()


def register_operation(name: str, unary: bool = False, list_op: bool = False) -> Callable[[Operation], Operation]:
    """Decorator to register an operation in the operations registry.

    Args:
        name: The name of the operation.
        unary: If True, marks this as a single-argument operation.
        list_op: If True, marks this as a list operation (takes multiple values).
    """
    def decorator(func: Operation) -> Operation:
        OPERATIONS[name] = func
        if unary:
            UNARY_OPERATIONS.add(name)
        if list_op:
            LIST_OPERATIONS.add(name)
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

    Raises:
        ValueError: If base is zero and exponent is negative.
    """
    if base == 0 and exponent < 0:
        raise ValueError("Cannot raise zero to a negative power")
    return base ** exponent


@register_operation("sqrt", unary=True)
def sqrt(a: Number) -> Number:
    """Compute the square root of a number.

    Args:
        a: The number to compute the square root of.

    Returns:
        The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(a)


@register_operation("ln", unary=True)
def ln(a: Number) -> Number:
    """Compute the natural logarithm of a number.

    Args:
        a: The number to compute the natural log of.

    Returns:
        The natural logarithm of a.

    Raises:
        ValueError: If a is not positive.
    """
    if a <= 0:
        raise ValueError("Cannot compute logarithm of non-positive number")
    return math.log(a)


@register_operation("log10", unary=True)
def log10(a: Number) -> Number:
    """Compute the base-10 logarithm of a number.

    Args:
        a: The number to compute the log base 10 of.

    Returns:
        The base-10 logarithm of a.

    Raises:
        ValueError: If a is not positive.
    """
    if a <= 0:
        raise ValueError("Cannot compute logarithm of non-positive number")
    return math.log10(a)


@register_operation("log")
def log(a: Number, base: Number) -> Number:
    """Compute the logarithm of a number with a custom base.

    Args:
        a: The number to compute the logarithm of.
        base: The base of the logarithm.

    Returns:
        The logarithm of a with the given base.

    Raises:
        ValueError: If a is not positive, or base is invalid (<=0 or ==1).
    """
    if a <= 0:
        raise ValueError("Cannot compute logarithm of non-positive number")
    if base <= 0:
        raise ValueError("Logarithm base must be positive")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1")
    return math.log(a, base)


@register_operation("sin", unary=True)
def sin(a: Number) -> Number:
    """Compute the sine of an angle in radians.

    Args:
        a: The angle in radians.

    Returns:
        The sine of the angle.
    """
    return math.sin(a)


@register_operation("cos", unary=True)
def cos(a: Number) -> Number:
    """Compute the cosine of an angle in radians.

    Args:
        a: The angle in radians.

    Returns:
        The cosine of the angle.
    """
    return math.cos(a)


@register_operation("tan", unary=True)
def tan(a: Number) -> Number:
    """Compute the tangent of an angle in radians.

    Args:
        a: The angle in radians.

    Returns:
        The tangent of the angle.

    Raises:
        ValueError: If the tangent is undefined (at odd multiples of pi/2).
    """
    # Check if cos(a) is essentially zero (tangent undefined)
    cos_val = math.cos(a)
    if abs(cos_val) < 1e-10:
        raise ValueError("Tangent undefined at this angle (cos(x) = 0)")
    return math.tan(a)


@register_operation("sind", unary=True)
def sind(a: Number) -> Number:
    """Compute the sine of an angle in degrees.

    Args:
        a: The angle in degrees.

    Returns:
        The sine of the angle.
    """
    return math.sin(math.radians(a))


@register_operation("cosd", unary=True)
def cosd(a: Number) -> Number:
    """Compute the cosine of an angle in degrees.

    Args:
        a: The angle in degrees.

    Returns:
        The cosine of the angle.
    """
    return math.cos(math.radians(a))


@register_operation("tand", unary=True)
def tand(a: Number) -> Number:
    """Compute the tangent of an angle in degrees.

    Args:
        a: The angle in degrees.

    Returns:
        The tangent of the angle.

    Raises:
        ValueError: If the tangent is undefined (at 90, 270, etc. degrees).
    """
    # Check if the angle is at an odd multiple of 90 degrees
    normalized = a % 360
    if abs(normalized - 90) < 1e-10 or abs(normalized - 270) < 1e-10:
        raise ValueError("Tangent undefined at this angle (90 or 270 degrees)")
    return math.tan(math.radians(a))


@register_operation("factorial", unary=True)
def factorial(a: Number) -> Number:
    """Compute the factorial of a non-negative integer.

    Args:
        a: The number to compute the factorial of (must be a non-negative integer).

    Returns:
        The factorial of a (a!).

    Raises:
        ValueError: If a is negative or not an integer.
    """
    if a < 0:
        raise ValueError("Cannot compute factorial of negative number")
    if a != int(a):
        raise ValueError("Cannot compute factorial of non-integer")
    return float(math.factorial(int(a)))


@register_operation("mean", list_op=True)
def mean(values: list[Number]) -> Number:
    """Compute the arithmetic mean of a list of numbers.

    Args:
        values: A list of numbers.

    Returns:
        The arithmetic mean of the values.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


@register_operation("median", list_op=True)
def median(values: list[Number]) -> Number:
    """Compute the median of a list of numbers.

    Args:
        values: A list of numbers.

    Returns:
        The median value. For even-length lists, returns the average of the two middle values.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]


@register_operation("variance", list_op=True)
def variance(values: list[Number]) -> Number:
    """Compute the population variance of a list of numbers.

    Args:
        values: A list of numbers.

    Returns:
        The population variance of the values.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot compute variance of empty list")
    avg = sum(values) / len(values)
    return sum((x - avg) ** 2 for x in values) / len(values)


@register_operation("stdev", list_op=True)
def stdev(values: list[Number]) -> Number:
    """Compute the population standard deviation of a list of numbers.

    Args:
        values: A list of numbers.

    Returns:
        The population standard deviation of the values.

    Raises:
        ValueError: If the list is empty.
    """
    if not values:
        raise ValueError("Cannot compute standard deviation of empty list")
    return math.sqrt(variance(values))


def hello_world() -> str:
    """Print and return 'Hello, World!'.

    Returns:
        The string 'Hello, World!'.
    """
    message = "Hello, World!"
    print(message)
    return message


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
        "numbers",
        type=str,
        nargs="*",
        help="Numbers for the operation (1 for unary, 2 for binary, multiple for list operations)",
    )

    return parser


def run_calculation(operation: str, num1: str, num2: str | None = None, numbers: list[str] | None = None) -> Number:
    """Run a calculation with the specified operation and operands.

    Args:
        operation: Name of the operation to perform.
        num1: First operand as string (for backward compatibility).
        num2: Second operand as string (optional for unary operations).
        numbers: List of number strings (for list operations like mean, median).

    Returns:
        Result of the calculation.

    Raises:
        ValueError: If operation is unknown or inputs are invalid.
    """
    if operation not in OPERATIONS:
        valid_ops = ", ".join(OPERATIONS.keys())
        raise ValueError(f"Unknown operation: '{operation}'. Valid operations: {valid_ops}")

    # Handle list operations
    if operation in LIST_OPERATIONS:
        if numbers is not None:
            values = [validate_number(n, f"number {i+1}") for i, n in enumerate(numbers)]
        else:
            # Build values from num1 and num2 for backward compatibility
            values = [validate_number(num1, "first number")]
            if num2 is not None:
                values.append(validate_number(num2, "second number"))
        return OPERATIONS[operation](values)

    a = validate_number(num1, "first number")

    if operation in UNARY_OPERATIONS:
        if num2 is not None:
            raise ValueError(f"Operation '{operation}' takes only one argument")
        return OPERATIONS[operation](a)

    if num2 is None:
        raise ValueError(f"Operation '{operation}' requires two arguments")

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
        numbers = args.numbers
        if args.operation in LIST_OPERATIONS:
            result = run_calculation(args.operation, "", None, numbers=numbers)
        elif args.operation in UNARY_OPERATIONS:
            if len(numbers) < 1:
                raise ValueError(f"Operation '{args.operation}' requires one argument")
            if len(numbers) > 1:
                raise ValueError(f"Operation '{args.operation}' takes only one argument")
            result = run_calculation(args.operation, numbers[0], None)
        else:
            if len(numbers) < 2:
                raise ValueError(f"Operation '{args.operation}' requires two arguments")
            if len(numbers) > 2:
                raise ValueError(f"Operation '{args.operation}' takes only two arguments")
            result = run_calculation(args.operation, numbers[0], numbers[1])
        print(format_result(result))
        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
