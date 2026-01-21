"""Tests for the runner module."""

import math
import pytest
import sys
from io import StringIO

import runner
from runner import (
    add,
    subtract,
    multiply,
    divide,
    power,
    sqrt,
    validate_number,
    run_calculation,
    format_result,
    main,
    create_parser,
    OPERATIONS,
    UNARY_OPERATIONS,
)


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 3) == 1

    def test_add_floats(self):
        assert add(2.5, 3.5) == 6.0

    def test_add_zero(self):
        assert add(0, 5) == 5


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        assert subtract(-2, 3) == -5

    def test_subtract_floats(self):
        assert subtract(5.5, 2.5) == 3.0


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_numbers(self):
        assert multiply(-2, 3) == -6

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_floats(self):
        assert multiply(2.5, 2) == 5.0


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        assert divide(6, 3) == 2

    def test_divide_negative_numbers(self):
        assert divide(-6, -3) == 2

    def test_divide_mixed_numbers(self):
        assert divide(-6, 3) == -2

    def test_divide_floats(self):
        assert divide(5, 2) == 2.5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestPower:
    """Tests for the power function."""

    def test_power_positive_exponent(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5

    def test_power_fractional_exponent(self):
        assert power(4, 0.5) == 2.0


class TestSqrt:
    """Tests for the sqrt function."""

    def test_sqrt_perfect_square(self):
        assert sqrt(16) == 4

    def test_sqrt_perfect_square_25(self):
        assert sqrt(25) == 5

    def test_sqrt_non_perfect_square(self):
        assert sqrt(2) == pytest.approx(1.4142135623730951)

    def test_sqrt_zero(self):
        assert sqrt(0) == 0

    def test_sqrt_one(self):
        assert sqrt(1) == 1

    def test_sqrt_float(self):
        assert sqrt(2.25) == 1.5

    def test_sqrt_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
            sqrt(-1)

    def test_sqrt_large_number(self):
        assert sqrt(10000) == 100


class TestValidateNumber:
    """Tests for the validate_number function."""

    def test_validate_integer_string(self):
        assert validate_number("5") == 5.0

    def test_validate_float_string(self):
        assert validate_number("3.14") == 3.14

    def test_validate_negative_string(self):
        assert validate_number("-5") == -5.0

    def test_validate_invalid_string(self):
        with pytest.raises(ValueError, match="Invalid value: 'abc' is not a valid number"):
            validate_number("abc")

    def test_validate_with_custom_name(self):
        with pytest.raises(ValueError, match="Invalid first number: 'xyz' is not a valid number"):
            validate_number("xyz", "first number")


class TestRunCalculation:
    """Tests for the run_calculation function."""

    def test_run_add(self):
        assert run_calculation("add", "5", "3") == 8

    def test_run_subtract(self):
        assert run_calculation("subtract", "5", "3") == 2

    def test_run_multiply(self):
        assert run_calculation("multiply", "5", "3") == 15

    def test_run_divide(self):
        assert run_calculation("divide", "6", "3") == 2

    def test_run_power(self):
        assert run_calculation("power", "2", "3") == 8

    def test_run_sqrt(self):
        assert run_calculation("sqrt", "16") == 4

    def test_run_unknown_operation(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            run_calculation("unknown", "5", "3")

    def test_run_sqrt_negative(self):
        with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
            run_calculation("sqrt", "-1")

    def test_run_binary_operation_missing_second_arg(self):
        with pytest.raises(ValueError, match="Operation 'add' requires two arguments"):
            run_calculation("add", "5", None)

    def test_run_unary_operation_with_extra_arg(self):
        with pytest.raises(ValueError, match="Operation 'sqrt' takes only one argument"):
            run_calculation("sqrt", "16", "5")


class TestFormatResult:
    """Tests for the format_result function."""

    def test_format_integer_result(self):
        assert format_result(4.0) == "4"

    def test_format_float_result(self):
        assert format_result(3.14) == "3.14"

    def test_format_negative_integer(self):
        assert format_result(-5.0) == "-5"

    def test_format_negative_float(self):
        assert format_result(-3.14) == "-3.14"


class TestCreateParser:
    """Tests for the create_parser function."""

    def test_parser_created(self):
        parser = create_parser()
        assert parser is not None

    def test_parser_accepts_binary_operation(self):
        parser = create_parser()
        args = parser.parse_args(["add", "5", "3"])
        assert args.operation == "add"
        assert args.num1 == "5"
        assert args.num2 == "3"

    def test_parser_accepts_unary_operation(self):
        parser = create_parser()
        args = parser.parse_args(["sqrt", "16"])
        assert args.operation == "sqrt"
        assert args.num1 == "16"
        assert args.num2 is None


class TestMain:
    """Tests for the main function."""

    def test_main_add(self, capsys):
        exit_code = main(["add", "5", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "8"

    def test_main_sqrt(self, capsys):
        exit_code = main(["sqrt", "16"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "4"

    def test_main_sqrt_non_perfect(self, capsys):
        exit_code = main(["sqrt", "2"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "1.414" in captured.out

    def test_main_sqrt_zero(self, capsys):
        exit_code = main(["sqrt", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_sqrt_negative_error(self, capsys):
        exit_code = main(["sqrt", "-1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Cannot compute square root of negative number" in captured.err

    def test_main_invalid_number(self, capsys):
        exit_code = main(["sqrt", "abc"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Invalid" in captured.err

    def test_main_divide_by_zero(self, capsys):
        exit_code = main(["divide", "5", "0"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Cannot divide by zero" in captured.err


class TestOperationsRegistry:
    """Tests for the operations registry."""

    def test_all_operations_registered(self):
        expected_ops = {"add", "subtract", "multiply", "divide", "power", "sqrt"}
        assert set(OPERATIONS.keys()) == expected_ops

    def test_sqrt_is_unary(self):
        assert "sqrt" in UNARY_OPERATIONS

    def test_binary_ops_not_in_unary(self):
        for op in ["add", "subtract", "multiply", "divide", "power"]:
            assert op not in UNARY_OPERATIONS
