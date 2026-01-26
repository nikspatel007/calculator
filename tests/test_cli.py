"""Tests for CLI functionality: parser, main function, and operations registry."""

import math
import pytest

from runner import (
    main,
    create_parser,
    hello_world,
    OPERATIONS,
    UNARY_OPERATIONS,
    LIST_OPERATIONS,
    TERNARY_OPERATIONS,
)


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

    def test_main_modulo(self, capsys):
        exit_code = main(["modulo", "10", "3"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "1"

    def test_main_modulo_exact_division(self, capsys):
        exit_code = main(["modulo", "10", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_modulo_by_zero_error(self, capsys):
        exit_code = main(["modulo", "10", "0"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Cannot compute modulo with zero divisor" in captured.err

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

    def test_main_abs_positive(self, capsys):
        exit_code = main(["abs", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_abs_negative(self, capsys):
        exit_code = main(["abs", "-5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_abs_zero(self, capsys):
        exit_code = main(["abs", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

    def test_main_abs_float(self, capsys):
        exit_code = main(["abs", "-3.14"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "3.14"

    def test_main_ceil_positive_float(self, capsys):
        exit_code = main(["ceil", "3.2"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "4"

    def test_main_ceil_negative_float(self, capsys):
        exit_code = main(["ceil", "-3.2"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "-3"

    def test_main_ceil_integer(self, capsys):
        exit_code = main(["ceil", "5"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "5"

    def test_main_ceil_zero(self, capsys):
        exit_code = main(["ceil", "0"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert captured.out.strip() == "0"

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
        expected_ops = {"abs", "add", "ceil", "clamp", "floor", "negate", "round", "subtract", "multiply", "divide", "modulo", "power", "sqrt", "ln", "log10", "log", "sin", "cos", "tan", "sind", "cosd", "tand", "factorial", "mean", "median", "variance", "stdev", "sign"}
        assert set(OPERATIONS.keys()) == expected_ops

    def test_abs_is_unary(self):
        assert "abs" in UNARY_OPERATIONS

    def test_negate_is_unary(self):
        assert "negate" in UNARY_OPERATIONS

    def test_sign_is_unary(self):
        assert "sign" in UNARY_OPERATIONS

    def test_ceil_is_unary(self):
        assert "ceil" in UNARY_OPERATIONS

    def test_floor_is_unary(self):
        assert "floor" in UNARY_OPERATIONS

    def test_round_is_unary(self):
        assert "round" in UNARY_OPERATIONS

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
        for op in ["add", "subtract", "multiply", "divide", "modulo", "power", "log"]:
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

    def test_clamp_is_ternary(self):
        assert "clamp" in TERNARY_OPERATIONS

    def test_clamp_not_in_unary(self):
        assert "clamp" not in UNARY_OPERATIONS

    def test_clamp_not_in_list(self):
        assert "clamp" not in LIST_OPERATIONS


class TestHelloWorld:
    """Tests for the hello_world function."""

    def test_hello_world_returns_message(self):
        result = hello_world()
        assert result == "hello world"

    def test_hello_world_prints_message(self, capsys):
        hello_world()
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello world"
