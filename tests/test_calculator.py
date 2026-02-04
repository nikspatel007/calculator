"""Tests for individual calculator functions."""

import math
import pytest

from runner import (
    abs_val,
    add,
    ceil,
    floor,
    round_val,
    subtract,
    multiply,
    divide,
    modulo,
    power,
    sqrt,
    exp,
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


class TestModulo:
    """Tests for the modulo function."""

    def test_modulo_positive_numbers(self):
        assert modulo(10, 3) == 1

    def test_modulo_exact_division(self):
        assert modulo(10, 5) == 0

    def test_modulo_negative_dividend(self):
        assert modulo(-10, 3) == 2

    def test_modulo_negative_divisor(self):
        assert modulo(10, -3) == -2

    def test_modulo_both_negative(self):
        assert modulo(-10, -3) == -1

    def test_modulo_floats(self):
        assert modulo(10.5, 3) == pytest.approx(1.5)

    def test_modulo_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot compute modulo with zero divisor"):
            modulo(5, 0)


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


class TestAbsVal:
    """Tests for the abs_val function."""

    def test_abs_val_positive_number(self):
        assert abs_val(5) == 5

    def test_abs_val_negative_number(self):
        assert abs_val(-5) == 5

    def test_abs_val_zero(self):
        assert abs_val(0) == 0

    def test_abs_val_positive_float(self):
        assert abs_val(3.14) == 3.14

    def test_abs_val_negative_float(self):
        assert abs_val(-3.14) == 3.14

    def test_abs_val_large_negative(self):
        assert abs_val(-1000000) == 1000000


class TestCeil:
    """Tests for the ceil function."""

    def test_ceil_positive_float(self):
        assert ceil(3.2) == 4

    def test_ceil_negative_float(self):
        assert ceil(-3.2) == -3

    def test_ceil_positive_integer(self):
        assert ceil(5.0) == 5

    def test_ceil_negative_integer(self):
        assert ceil(-5.0) == -5

    def test_ceil_zero(self):
        assert ceil(0) == 0

    def test_ceil_small_positive_fraction(self):
        assert ceil(0.1) == 1

    def test_ceil_small_negative_fraction(self):
        assert ceil(-0.1) == 0

    def test_ceil_large_positive(self):
        assert ceil(999.999) == 1000

    def test_ceil_large_negative(self):
        assert ceil(-999.999) == -999


class TestFloor:
    """Tests for the floor function."""

    def test_floor_positive_float(self):
        assert floor(3.7) == 3

    def test_floor_negative_float(self):
        assert floor(-3.2) == -4

    def test_floor_positive_integer(self):
        assert floor(5.0) == 5

    def test_floor_negative_integer(self):
        assert floor(-5.0) == -5

    def test_floor_zero(self):
        assert floor(0) == 0

    def test_floor_small_positive_fraction(self):
        assert floor(0.9) == 0

    def test_floor_small_negative_fraction(self):
        assert floor(-0.1) == -1

    def test_floor_large_positive(self):
        assert floor(999.999) == 999

    def test_floor_large_negative(self):
        assert floor(-999.001) == -1000


class TestRound:
    """Tests for the round_val function."""

    def test_round_positive_float_down(self):
        assert round_val(3.2) == 3

    def test_round_positive_float_up(self):
        assert round_val(3.7) == 4

    def test_round_negative_float_down(self):
        assert round_val(-3.7) == -4

    def test_round_negative_float_up(self):
        assert round_val(-3.2) == -3

    def test_round_positive_integer(self):
        assert round_val(5.0) == 5

    def test_round_negative_integer(self):
        assert round_val(-5.0) == -5

    def test_round_zero(self):
        assert round_val(0) == 0

    def test_round_half_to_even_positive(self):
        # Python uses banker's rounding (round half to even)
        assert round_val(2.5) == 2
        assert round_val(3.5) == 4

    def test_round_half_to_even_negative(self):
        # Python uses banker's rounding (round half to even)
        assert round_val(-2.5) == -2
        assert round_val(-3.5) == -4

    def test_round_large_positive(self):
        assert round_val(999.5) == 1000

    def test_round_large_negative(self):
        assert round_val(-999.5) == -1000


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


class TestExp:
    """Tests for the exp function (e^x)."""

    def test_exp_of_zero(self):
        # e^0 = 1
        assert exp(0) == 1

    def test_exp_of_one(self):
        # e^1 = e
        assert exp(1) == pytest.approx(math.e)

    def test_exp_of_two(self):
        # e^2 = e^2
        assert exp(2) == pytest.approx(math.e ** 2)

    def test_exp_positive_value(self):
        # e^0.5
        assert exp(0.5) == pytest.approx(math.sqrt(math.e))

    def test_exp_negative_one(self):
        # e^-1 = 1/e
        assert exp(-1) == pytest.approx(1 / math.e)

    def test_exp_negative_value(self):
        # e^-2 = 1/e^2
        assert exp(-2) == pytest.approx(1 / (math.e ** 2))

    def test_exp_small_positive(self):
        # e^0.001 is close to 1.001...
        assert exp(0.001) == pytest.approx(1.0010005001667084)

    def test_exp_small_negative(self):
        # e^-0.001 is close to 0.999...
        assert exp(-0.001) == pytest.approx(0.9990004998333417)

    def test_exp_large_negative_underflows_to_near_zero(self):
        # Very large negative x results in a value very close to 0
        result = exp(-700)
        assert result >= 0
        assert result < 1e-300

    def test_exp_very_large_negative_underflows(self):
        # Even larger negative values should still return 0 or near-zero
        result = exp(-1000)
        assert result == 0  # Python underflows to 0

    def test_exp_overflow_raises_error(self):
        # Very large positive values cause overflow
        with pytest.raises(ValueError, match="Result too large: exponential overflow"):
            exp(1000)

    def test_exp_ln_inverse(self):
        # exp and ln are inverses: exp(ln(x)) = x for x > 0
        assert exp(math.log(5)) == pytest.approx(5)
        assert exp(math.log(10)) == pytest.approx(10)

    def test_exp_ln_identity(self):
        # ln(exp(x)) = x for any x
        assert math.log(exp(3)) == pytest.approx(3)
        assert math.log(exp(-2)) == pytest.approx(-2)


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
