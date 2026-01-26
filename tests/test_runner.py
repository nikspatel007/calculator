"""Tests for run_calculation and format_result functions."""

import math
import pytest

from runner import (
    run_calculation,
    format_result,
)


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

    def test_run_modulo(self):
        assert run_calculation("modulo", "10", "3") == 1

    def test_run_modulo_by_zero(self):
        with pytest.raises(ValueError, match="Cannot compute modulo with zero divisor"):
            run_calculation("modulo", "10", "0")

    def test_run_power(self):
        assert run_calculation("power", "2", "3") == 8

    def test_run_power_negative_exponent(self):
        assert run_calculation("power", "2", "-2") == 0.25

    def test_run_power_zero_base_negative_exponent_raises_error(self):
        with pytest.raises(ValueError, match="Cannot raise zero to a negative power"):
            run_calculation("power", "0", "-1")

    def test_run_abs_positive(self):
        assert run_calculation("abs", "5") == 5

    def test_run_abs_negative(self):
        assert run_calculation("abs", "-5") == 5

    def test_run_abs_zero(self):
        assert run_calculation("abs", "0") == 0

    def test_run_ceil_positive_float(self):
        assert run_calculation("ceil", "3.2") == 4

    def test_run_ceil_negative_float(self):
        assert run_calculation("ceil", "-3.2") == -3

    def test_run_ceil_integer(self):
        assert run_calculation("ceil", "5") == 5

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
