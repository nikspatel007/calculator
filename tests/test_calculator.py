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
    ln,
    log10,
    log,
    sin,
    cos,
    tan,
    sind,
    cosd,
    tand,
    factorial,
    mean,
    median,
    variance,
    stdev,
    validate_number,
    run_calculation,
    format_result,
    main,
    create_parser,
    hello_world,
    OPERATIONS,
    UNARY_OPERATIONS,
    LIST_OPERATIONS,
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

    def test_power_negative_exponent_decimal(self):
        assert power(2, -2) == 0.25

    def test_power_zero_base_positive_exponent(self):
        assert power(0, 5) == 0

    def test_power_zero_base_zero_exponent(self):
        assert power(0, 0) == 1

    def test_power_zero_base_negative_exponent_raises_error(self):
        with pytest.raises(ValueError, match="Cannot raise zero to a negative power"):
            power(0, -1)

    def test_power_zero_base_negative_fractional_exponent_raises_error(self):
        with pytest.raises(ValueError, match="Cannot raise zero to a negative power"):
            power(0, -0.5)


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


class TestLn:
    """Tests for the ln (natural logarithm) function."""

    def test_ln_of_one(self):
        assert ln(1) == 0

    def test_ln_of_e(self):
        assert ln(math.e) == pytest.approx(1.0)

    def test_ln_of_e_squared(self):
        assert ln(math.e ** 2) == pytest.approx(2.0)

    def test_ln_positive_number(self):
        assert ln(2) == pytest.approx(0.6931471805599453)

    def test_ln_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            ln(0)

    def test_ln_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            ln(-1)

    def test_ln_small_positive(self):
        assert ln(0.5) == pytest.approx(-0.6931471805599453)


class TestLog10:
    """Tests for the log10 (base-10 logarithm) function."""

    def test_log10_of_one(self):
        assert log10(1) == 0

    def test_log10_of_ten(self):
        assert log10(10) == 1

    def test_log10_of_hundred(self):
        assert log10(100) == 2

    def test_log10_of_thousand(self):
        assert log10(1000) == 3

    def test_log10_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            log10(0)

    def test_log10_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            log10(-5)

    def test_log10_fraction(self):
        assert log10(0.1) == pytest.approx(-1.0)


class TestLog:
    """Tests for the log (custom base logarithm) function."""

    def test_log_base_2(self):
        assert log(8, 2) == pytest.approx(3.0)

    def test_log_base_3(self):
        assert log(27, 3) == pytest.approx(3.0)

    def test_log_base_10(self):
        assert log(100, 10) == pytest.approx(2.0)

    def test_log_of_one_any_base(self):
        assert log(1, 5) == 0

    def test_log_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            log(0, 2)

    def test_log_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            log(-8, 2)

    def test_log_base_zero_raises_error(self):
        with pytest.raises(ValueError, match="Logarithm base must be positive"):
            log(8, 0)

    def test_log_base_negative_raises_error(self):
        with pytest.raises(ValueError, match="Logarithm base must be positive"):
            log(8, -2)

    def test_log_base_one_raises_error(self):
        with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
            log(8, 1)

    def test_log_fractional_result(self):
        assert log(2, 4) == pytest.approx(0.5)


class TestSin:
    """Tests for the sin function (radians)."""

    def test_sin_of_zero(self):
        assert sin(0) == 0

    def test_sin_of_pi_over_2(self):
        assert sin(math.pi / 2) == pytest.approx(1.0)

    def test_sin_of_pi(self):
        assert sin(math.pi) == pytest.approx(0.0, abs=1e-10)

    def test_sin_of_pi_over_6(self):
        assert sin(math.pi / 6) == pytest.approx(0.5)

    def test_sin_of_negative_pi_over_2(self):
        assert sin(-math.pi / 2) == pytest.approx(-1.0)


class TestCos:
    """Tests for the cos function (radians)."""

    def test_cos_of_zero(self):
        assert cos(0) == 1

    def test_cos_of_pi_over_2(self):
        assert cos(math.pi / 2) == pytest.approx(0.0, abs=1e-10)

    def test_cos_of_pi(self):
        assert cos(math.pi) == pytest.approx(-1.0)

    def test_cos_of_pi_over_3(self):
        assert cos(math.pi / 3) == pytest.approx(0.5)

    def test_cos_of_negative_pi(self):
        assert cos(-math.pi) == pytest.approx(-1.0)


class TestTan:
    """Tests for the tan function (radians)."""

    def test_tan_of_zero(self):
        assert tan(0) == 0

    def test_tan_of_pi_over_4(self):
        assert tan(math.pi / 4) == pytest.approx(1.0)

    def test_tan_of_pi(self):
        assert tan(math.pi) == pytest.approx(0.0, abs=1e-10)

    def test_tan_of_negative_pi_over_4(self):
        assert tan(-math.pi / 4) == pytest.approx(-1.0)

    def test_tan_of_pi_over_2_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            tan(math.pi / 2)

    def test_tan_of_3pi_over_2_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            tan(3 * math.pi / 2)


class TestSind:
    """Tests for the sind function (degrees)."""

    def test_sind_of_zero(self):
        assert sind(0) == 0

    def test_sind_of_30(self):
        assert sind(30) == pytest.approx(0.5)

    def test_sind_of_90(self):
        assert sind(90) == pytest.approx(1.0)

    def test_sind_of_180(self):
        assert sind(180) == pytest.approx(0.0, abs=1e-10)

    def test_sind_of_270(self):
        assert sind(270) == pytest.approx(-1.0)

    def test_sind_of_negative_90(self):
        assert sind(-90) == pytest.approx(-1.0)


class TestCosd:
    """Tests for the cosd function (degrees)."""

    def test_cosd_of_zero(self):
        assert cosd(0) == 1

    def test_cosd_of_60(self):
        assert cosd(60) == pytest.approx(0.5)

    def test_cosd_of_90(self):
        assert cosd(90) == pytest.approx(0.0, abs=1e-10)

    def test_cosd_of_180(self):
        assert cosd(180) == pytest.approx(-1.0)

    def test_cosd_of_360(self):
        assert cosd(360) == pytest.approx(1.0)

    def test_cosd_of_negative_60(self):
        assert cosd(-60) == pytest.approx(0.5)


class TestTand:
    """Tests for the tand function (degrees)."""

    def test_tand_of_zero(self):
        assert tand(0) == 0

    def test_tand_of_45(self):
        assert tand(45) == pytest.approx(1.0)

    def test_tand_of_180(self):
        assert tand(180) == pytest.approx(0.0, abs=1e-10)

    def test_tand_of_negative_45(self):
        assert tand(-45) == pytest.approx(-1.0)

    def test_tand_of_90_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            tand(90)

    def test_tand_of_270_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            tand(270)

    def test_tand_of_450_raises_error(self):
        # 450 degrees = 90 degrees (modulo 360)
        with pytest.raises(ValueError, match="Tangent undefined"):
            tand(450)


class TestFactorial:
    """Tests for the factorial function."""

    def test_factorial_of_zero(self):
        assert factorial(0) == 1

    def test_factorial_of_one(self):
        assert factorial(1) == 1

    def test_factorial_of_five(self):
        assert factorial(5) == 120

    def test_factorial_of_ten(self):
        assert factorial(10) == 3628800

    def test_factorial_of_float_integer(self):
        # 5.0 should be treated as 5
        assert factorial(5.0) == 120

    def test_factorial_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute factorial of negative number"):
            factorial(-1)

    def test_factorial_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute factorial of non-integer"):
            factorial(5.5)


class TestMean:
    """Tests for the mean function."""

    def test_mean_single_value(self):
        assert mean([5]) == 5

    def test_mean_two_values(self):
        assert mean([2, 4]) == 3

    def test_mean_multiple_values(self):
        assert mean([1, 2, 3, 4, 5]) == 3

    def test_mean_negative_values(self):
        assert mean([-2, -4, -6]) == -4

    def test_mean_mixed_values(self):
        assert mean([-5, 5]) == 0

    def test_mean_floats(self):
        assert mean([1.5, 2.5, 3.0]) == pytest.approx(2.3333333333)

    def test_mean_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute mean of empty list"):
            mean([])


class TestMedian:
    """Tests for the median function."""

    def test_median_single_value(self):
        assert median([5]) == 5

    def test_median_odd_count(self):
        assert median([1, 3, 5]) == 3

    def test_median_even_count(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_median_unsorted_input(self):
        assert median([5, 1, 3]) == 3

    def test_median_two_values(self):
        assert median([1, 3]) == 2

    def test_median_negative_values(self):
        assert median([-5, -3, -1]) == -3

    def test_median_mixed_values(self):
        assert median([-10, 0, 10]) == 0

    def test_median_floats(self):
        assert median([1.5, 2.5, 3.5]) == 2.5

    def test_median_even_count_floats(self):
        assert median([1.0, 2.0, 3.0, 4.0]) == 2.5

    def test_median_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute median of empty list"):
            median([])


class TestVariance:
    """Tests for the variance function."""

    def test_variance_single_value(self):
        assert variance([5]) == 0

    def test_variance_identical_values(self):
        assert variance([3, 3, 3, 3]) == 0

    def test_variance_simple_values(self):
        # Values: [1, 3], mean = 2, variance = ((1-2)^2 + (3-2)^2) / 2 = (1 + 1) / 2 = 1
        assert variance([1, 3]) == 1

    def test_variance_multiple_values(self):
        # Values: [2, 4, 4, 4, 5, 5, 7, 9], mean = 5
        # variance = ((2-5)^2 + (4-5)^2 + (4-5)^2 + (4-5)^2 + (5-5)^2 + (5-5)^2 + (7-5)^2 + (9-5)^2) / 8
        # = (9 + 1 + 1 + 1 + 0 + 0 + 4 + 16) / 8 = 32 / 8 = 4
        assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4

    def test_variance_negative_values(self):
        # Values: [-2, -4, -6], mean = -4
        # variance = ((-2-(-4))^2 + (-4-(-4))^2 + (-6-(-4))^2) / 3 = (4 + 0 + 4) / 3 = 8/3
        assert variance([-2, -4, -6]) == pytest.approx(8 / 3)

    def test_variance_mixed_values(self):
        # Values: [-5, 5], mean = 0
        # variance = (25 + 25) / 2 = 25
        assert variance([-5, 5]) == 25

    def test_variance_floats(self):
        # Values: [1.5, 2.5, 3.5], mean = 2.5
        # variance = ((1.5-2.5)^2 + (2.5-2.5)^2 + (3.5-2.5)^2) / 3 = (1 + 0 + 1) / 3 = 2/3
        assert variance([1.5, 2.5, 3.5]) == pytest.approx(2 / 3)

    def test_variance_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute variance of empty list"):
            variance([])


class TestStdev:
    """Tests for the stdev function."""

    def test_stdev_single_value(self):
        assert stdev([5]) == 0

    def test_stdev_identical_values(self):
        assert stdev([3, 3, 3, 3]) == 0

    def test_stdev_simple_values(self):
        # Values: [1, 3], variance = 1, stdev = 1
        assert stdev([1, 3]) == 1

    def test_stdev_multiple_values(self):
        # Values: [2, 4, 4, 4, 5, 5, 7, 9], variance = 4, stdev = 2
        assert stdev([2, 4, 4, 4, 5, 5, 7, 9]) == 2

    def test_stdev_negative_values(self):
        # variance = 8/3, stdev = sqrt(8/3)
        assert stdev([-2, -4, -6]) == pytest.approx(math.sqrt(8 / 3))

    def test_stdev_mixed_values(self):
        # variance = 25, stdev = 5
        assert stdev([-5, 5]) == 5

    def test_stdev_floats(self):
        # variance = 2/3, stdev = sqrt(2/3)
        assert stdev([1.5, 2.5, 3.5]) == pytest.approx(math.sqrt(2 / 3))

    def test_stdev_empty_list_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute standard deviation of empty list"):
            stdev([])


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

    def test_run_power_negative_exponent(self):
        assert run_calculation("power", "2", "-2") == 0.25

    def test_run_power_zero_base_negative_exponent_raises_error(self):
        with pytest.raises(ValueError, match="Cannot raise zero to a negative power"):
            run_calculation("power", "0", "-1")

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

    def test_run_ln(self):
        assert run_calculation("ln", "1") == 0

    def test_run_ln_negative(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            run_calculation("ln", "-1")

    def test_run_log10(self):
        assert run_calculation("log10", "100") == 2

    def test_run_log10_negative(self):
        with pytest.raises(ValueError, match="Cannot compute logarithm of non-positive number"):
            run_calculation("log10", "-5")

    def test_run_log(self):
        assert run_calculation("log", "8", "2") == pytest.approx(3.0)

    def test_run_log_invalid_base(self):
        with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
            run_calculation("log", "8", "1")

    def test_run_mean_with_numbers(self):
        assert run_calculation("mean", "", None, numbers=["1", "2", "3", "4", "5"]) == 3

    def test_run_mean_single_value(self):
        assert run_calculation("mean", "", None, numbers=["5"]) == 5

    def test_run_mean_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute mean of empty list"):
            run_calculation("mean", "", None, numbers=[])

    def test_run_median_with_numbers(self):
        assert run_calculation("median", "", None, numbers=["1", "2", "3"]) == 2

    def test_run_median_even_count(self):
        assert run_calculation("median", "", None, numbers=["1", "2", "3", "4"]) == 2.5

    def test_run_median_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute median of empty list"):
            run_calculation("median", "", None, numbers=[])

    def test_run_variance_with_numbers(self):
        assert run_calculation("variance", "", None, numbers=["2", "4", "4", "4", "5", "5", "7", "9"]) == 4

    def test_run_variance_single_value(self):
        assert run_calculation("variance", "", None, numbers=["5"]) == 0

    def test_run_variance_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute variance of empty list"):
            run_calculation("variance", "", None, numbers=[])

    def test_run_stdev_with_numbers(self):
        assert run_calculation("stdev", "", None, numbers=["2", "4", "4", "4", "5", "5", "7", "9"]) == 2

    def test_run_stdev_single_value(self):
        assert run_calculation("stdev", "", None, numbers=["5"]) == 0

    def test_run_stdev_empty_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute standard deviation of empty list"):
            run_calculation("stdev", "", None, numbers=[])

    def test_run_sin(self):
        assert run_calculation("sin", "0") == 0

    def test_run_sin_pi_over_2(self):
        assert run_calculation("sin", str(math.pi / 2)) == pytest.approx(1.0)

    def test_run_cos(self):
        assert run_calculation("cos", "0") == 1

    def test_run_cos_pi(self):
        assert run_calculation("cos", str(math.pi)) == pytest.approx(-1.0)

    def test_run_tan(self):
        assert run_calculation("tan", "0") == 0

    def test_run_tan_pi_over_4(self):
        assert run_calculation("tan", str(math.pi / 4)) == pytest.approx(1.0)

    def test_run_tan_pi_over_2_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            run_calculation("tan", str(math.pi / 2))

    def test_run_sind(self):
        assert run_calculation("sind", "0") == 0

    def test_run_sind_90(self):
        assert run_calculation("sind", "90") == pytest.approx(1.0)

    def test_run_cosd(self):
        assert run_calculation("cosd", "0") == 1

    def test_run_cosd_90(self):
        assert run_calculation("cosd", "90") == pytest.approx(0.0, abs=1e-10)

    def test_run_tand(self):
        assert run_calculation("tand", "0") == 0

    def test_run_tand_45(self):
        assert run_calculation("tand", "45") == pytest.approx(1.0)

    def test_run_tand_90_raises_error(self):
        with pytest.raises(ValueError, match="Tangent undefined"):
            run_calculation("tand", "90")

    def test_run_factorial(self):
        assert run_calculation("factorial", "5") == 120

    def test_run_factorial_zero(self):
        assert run_calculation("factorial", "0") == 1

    def test_run_factorial_negative_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute factorial of negative number"):
            run_calculation("factorial", "-1")

    def test_run_factorial_non_integer_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute factorial of non-integer"):
            run_calculation("factorial", "5.5")


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
        assert args.numbers == ["5", "3"]

    def test_parser_accepts_unary_operation(self):
        parser = create_parser()
        args = parser.parse_args(["sqrt", "16"])
        assert args.operation == "sqrt"
        assert args.numbers == ["16"]

    def test_parser_accepts_list_operation(self):
        parser = create_parser()
        args = parser.parse_args(["mean", "1", "2", "3", "4", "5"])
        assert args.operation == "mean"
        assert args.numbers == ["1", "2", "3", "4", "5"]


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

    def test_main_power(self, capsys):
        exit_code = main(["power", "2", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "8"

    def test_main_power_negative_exponent(self, capsys):
        exit_code = main(["power", "2", "-2"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0.25"

    def test_main_power_zero_base_negative_exponent_error(self, capsys):
        exit_code = main(["power", "0", "-1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Cannot raise zero to a negative power" in captured.err

    def test_main_ln(self, capsys):
        exit_code = main(["ln", "1"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_ln_e(self, capsys):
        exit_code = main(["ln", "2.718281828"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(1.0, abs=0.0001)

    def test_main_ln_zero_error(self, capsys):
        exit_code = main(["ln", "0"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "non-positive" in captured.err

    def test_main_ln_negative_error(self, capsys):
        exit_code = main(["ln", "-1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "non-positive" in captured.err

    def test_main_log10(self, capsys):
        exit_code = main(["log10", "100"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "2"

    def test_main_log10_ten(self, capsys):
        exit_code = main(["log10", "10"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_log10_thousand(self, capsys):
        exit_code = main(["log10", "1000"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3"

    def test_main_log_base_2(self, capsys):
        exit_code = main(["log", "8", "2"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3"

    def test_main_log_base_3(self, capsys):
        exit_code = main(["log", "27", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3"

    def test_main_log_base_1_error(self, capsys):
        exit_code = main(["log", "8", "1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "cannot be 1" in captured.err

    def test_main_mean(self, capsys):
        exit_code = main(["mean", "1", "2", "3", "4", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3"

    def test_main_mean_float_result(self, capsys):
        exit_code = main(["mean", "1", "2", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "2"

    def test_main_mean_single_value(self, capsys):
        exit_code = main(["mean", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_mean_empty_error(self, capsys):
        exit_code = main(["mean"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "empty list" in captured.err

    def test_main_median_odd(self, capsys):
        exit_code = main(["median", "1", "2", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "2"

    def test_main_median_even(self, capsys):
        exit_code = main(["median", "1", "2", "3", "4"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "2.5"

    def test_main_median_unsorted(self, capsys):
        exit_code = main(["median", "5", "1", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3"

    def test_main_median_single_value(self, capsys):
        exit_code = main(["median", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_median_empty_error(self, capsys):
        exit_code = main(["median"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "empty list" in captured.err

    def test_main_variance(self, capsys):
        exit_code = main(["variance", "2", "4", "4", "4", "5", "5", "7", "9"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "4"

    def test_main_variance_single_value(self, capsys):
        exit_code = main(["variance", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_variance_float_result(self, capsys):
        exit_code = main(["variance", "1", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_variance_empty_error(self, capsys):
        exit_code = main(["variance"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "empty list" in captured.err

    def test_main_stdev(self, capsys):
        exit_code = main(["stdev", "2", "4", "4", "4", "5", "5", "7", "9"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "2"

    def test_main_stdev_single_value(self, capsys):
        exit_code = main(["stdev", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_stdev_float_result(self, capsys):
        exit_code = main(["stdev", "-5", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_stdev_empty_error(self, capsys):
        exit_code = main(["stdev"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "empty list" in captured.err

    def test_main_binary_missing_arg_error(self, capsys):
        exit_code = main(["add", "5"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "requires two arguments" in captured.err

    def test_main_binary_extra_arg_error(self, capsys):
        exit_code = main(["add", "5", "3", "2"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "takes only two arguments" in captured.err

    def test_main_unary_missing_arg_error(self, capsys):
        exit_code = main(["sqrt"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "requires one argument" in captured.err

    def test_main_sin_zero(self, capsys):
        exit_code = main(["sin", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_sin_pi_over_2(self, capsys):
        exit_code = main(["sin", "1.5708"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(1.0, abs=0.001)

    def test_main_cos_zero(self, capsys):
        exit_code = main(["cos", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_cos_pi(self, capsys):
        exit_code = main(["cos", str(math.pi)])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(-1.0)

    def test_main_tan_zero(self, capsys):
        exit_code = main(["tan", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_tan_pi_over_4(self, capsys):
        exit_code = main(["tan", "0.7854"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(1.0, abs=0.001)

    def test_main_tan_pi_over_2_error(self, capsys):
        exit_code = main(["tan", str(math.pi / 2)])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Tangent undefined" in captured.err

    def test_main_sind_zero(self, capsys):
        exit_code = main(["sind", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_sind_30(self, capsys):
        exit_code = main(["sind", "30"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(0.5)

    def test_main_sind_90(self, capsys):
        exit_code = main(["sind", "90"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(1.0)

    def test_main_cosd_zero(self, capsys):
        exit_code = main(["cosd", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_cosd_60(self, capsys):
        exit_code = main(["cosd", "60"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(0.5)

    def test_main_cosd_90(self, capsys):
        exit_code = main(["cosd", "90"])
        captured = capsys.readouterr()
        assert exit_code == 0
        # Should be very close to 0
        assert abs(float(captured.out.strip())) < 1e-9

    def test_main_tand_zero(self, capsys):
        exit_code = main(["tand", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_tand_45(self, capsys):
        exit_code = main(["tand", "45"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert float(captured.out.strip()) == pytest.approx(1.0)

    def test_main_tand_90_error(self, capsys):
        exit_code = main(["tand", "90"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Tangent undefined" in captured.err

    def test_main_factorial(self, capsys):
        exit_code = main(["factorial", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "120"

    def test_main_factorial_zero(self, capsys):
        exit_code = main(["factorial", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_factorial_ten(self, capsys):
        exit_code = main(["factorial", "10"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3628800"

    def test_main_factorial_negative_error(self, capsys):
        exit_code = main(["factorial", "-1"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "negative number" in captured.err

    def test_main_factorial_non_integer_error(self, capsys):
        exit_code = main(["factorial", "5.5"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "non-integer" in captured.err


class TestOperationsRegistry:
    """Tests for the operations registry."""

    def test_all_operations_registered(self):
        expected_ops = {"add", "subtract", "multiply", "divide", "power", "sqrt", "ln", "log10", "log", "sin", "cos", "tan", "sind", "cosd", "tand", "factorial", "mean", "median", "variance", "stdev"}
        assert set(OPERATIONS.keys()) == expected_ops

    def test_sqrt_is_unary(self):
        assert "sqrt" in UNARY_OPERATIONS

    def test_ln_is_unary(self):
        assert "ln" in UNARY_OPERATIONS

    def test_log10_is_unary(self):
        assert "log10" in UNARY_OPERATIONS

    def test_sin_is_unary(self):
        assert "sin" in UNARY_OPERATIONS

    def test_cos_is_unary(self):
        assert "cos" in UNARY_OPERATIONS

    def test_tan_is_unary(self):
        assert "tan" in UNARY_OPERATIONS

    def test_sind_is_unary(self):
        assert "sind" in UNARY_OPERATIONS

    def test_cosd_is_unary(self):
        assert "cosd" in UNARY_OPERATIONS

    def test_tand_is_unary(self):
        assert "tand" in UNARY_OPERATIONS

    def test_factorial_is_unary(self):
        assert "factorial" in UNARY_OPERATIONS

    def test_log_is_binary(self):
        assert "log" not in UNARY_OPERATIONS

    def test_binary_ops_not_in_unary(self):
        for op in ["add", "subtract", "multiply", "divide", "power", "log"]:
            assert op not in UNARY_OPERATIONS

    def test_mean_is_list_operation(self):
        assert "mean" in LIST_OPERATIONS

    def test_median_is_list_operation(self):
        assert "median" in LIST_OPERATIONS

    def test_variance_is_list_operation(self):
        assert "variance" in LIST_OPERATIONS

    def test_stdev_is_list_operation(self):
        assert "stdev" in LIST_OPERATIONS

    def test_list_ops_not_in_unary(self):
        for op in ["mean", "median", "variance", "stdev"]:
            assert op not in UNARY_OPERATIONS


class TestHelloWorld:
    """Tests for the hello_world function."""

    def test_hello_world_returns_message(self):
        result = hello_world()
        assert result == "hello world"

    def test_hello_world_prints_message(self, capsys):
        hello_world()
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello world"
