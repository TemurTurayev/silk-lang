"""
Interpreter Golden Tests

These tests verify that the interpreter correctly executes Silk code.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.interpreter import Interpreter


class TestBasicExpressions:
    """Test basic expression evaluation."""

    def test_integer_literal(self, evaluate_silk):
        assert evaluate_silk("42") == 42

    def test_float_literal(self, evaluate_silk):
        assert evaluate_silk("3.14") == 3.14

    def test_string_literal(self, evaluate_silk):
        assert evaluate_silk('"hello"') == "hello"

    def test_boolean_true(self, evaluate_silk):
        assert evaluate_silk("true") is True

    def test_boolean_false(self, evaluate_silk):
        assert evaluate_silk("false") is False

    def test_null_literal(self, evaluate_silk):
        assert evaluate_silk("null") is None


class TestArithmetic:
    """Test arithmetic operations."""

    def test_addition(self, evaluate_silk):
        assert evaluate_silk("2 + 3") == 5

    def test_subtraction(self, evaluate_silk):
        assert evaluate_silk("10 - 4") == 6

    def test_multiplication(self, evaluate_silk):
        assert evaluate_silk("3 * 4") == 12

    def test_division(self, evaluate_silk):
        assert evaluate_silk("10 / 2") == 5

    def test_division_float_result(self, evaluate_silk):
        assert evaluate_silk("7 / 2") == 3.5

    def test_modulo(self, evaluate_silk):
        assert evaluate_silk("10 % 3") == 1

    def test_power(self, evaluate_silk):
        assert evaluate_silk("2 ** 3") == 8

    def test_unary_minus(self, evaluate_silk):
        assert evaluate_silk("-5") == -5

    def test_string_concatenation(self, evaluate_silk):
        assert evaluate_silk('"hello" + " " + "world"') == "hello world"

    def test_string_repetition(self, evaluate_silk):
        assert evaluate_silk('"ab" * 3') == "ababab"


class TestComparison:
    """Test comparison operations."""

    def test_equal(self, evaluate_silk):
        assert evaluate_silk("5 == 5") is True
        assert evaluate_silk("5 == 6") is False

    def test_not_equal(self, evaluate_silk):
        assert evaluate_silk("5 != 6") is True
        assert evaluate_silk("5 != 5") is False

    def test_less_than(self, evaluate_silk):
        assert evaluate_silk("3 < 5") is True
        assert evaluate_silk("5 < 3") is False

    def test_greater_than(self, evaluate_silk):
        assert evaluate_silk("5 > 3") is True
        assert evaluate_silk("3 > 5") is False

    def test_less_than_or_equal(self, evaluate_silk):
        assert evaluate_silk("3 <= 5") is True
        assert evaluate_silk("5 <= 5") is True

    def test_greater_than_or_equal(self, evaluate_silk):
        assert evaluate_silk("5 >= 3") is True
        assert evaluate_silk("5 >= 5") is True


class TestLogical:
    """Test logical operations."""

    def test_and(self, evaluate_silk):
        assert evaluate_silk("true and true") is True
        assert evaluate_silk("true and false") is False

    def test_or(self, evaluate_silk):
        assert evaluate_silk("true or false") is True
        assert evaluate_silk("false or false") is False

    def test_not(self, evaluate_silk):
        assert evaluate_silk("not true") is False
        assert evaluate_silk("not false") is True


class TestVariables:
    """Test variable declarations and assignments."""

    def test_let_declaration(self, run_silk):
        interp = run_silk("let x = 42")
        assert interp.global_env.get("x") == 42

    def test_mutable_assignment(self, run_silk):
        interp = run_silk("""
            let mut x = 10
            x = 20
        """)
        assert interp.global_env.get("x") == 20

    def test_compound_assignment(self, run_silk):
        interp = run_silk("""
            let mut x = 10
            x += 5
        """)
        assert interp.global_env.get("x") == 15


class TestArrays:
    """Test array operations."""

    def test_array_literal(self, evaluate_silk):
        assert evaluate_silk("[1, 2, 3]") == [1, 2, 3]

    def test_array_index(self, evaluate_silk):
        assert evaluate_silk("[10, 20, 30][1]") == 20

    def test_array_length(self, evaluate_silk):
        assert evaluate_silk("[1, 2, 3].length") == 3


class TestFunctions:
    """Test function definitions and calls."""

    def test_function_call(self, run_silk):
        interp = run_silk("""
            fn add(a, b) {
                return a + b
            }
            let result = add(2, 3)
        """)
        assert interp.global_env.get("result") == 5

    def test_builtin_len(self, evaluate_silk):
        assert evaluate_silk('len("hello")') == 5
        assert evaluate_silk("len([1, 2, 3])") == 3

    def test_builtin_range(self, evaluate_silk):
        assert evaluate_silk("range(5)") == [0, 1, 2, 3, 4]


class TestMedicalFunctions:
    """Test medical built-in functions."""

    def test_bmi(self, evaluate_silk):
        # BMI = weight / height^2 = 70 / 1.75^2 = 22.86
        assert evaluate_silk("bmi(70, 1.75)") == 22.86

    def test_dose_per_kg(self, evaluate_silk):
        # 15 mg/kg * 25 kg = 375 mg
        assert evaluate_silk("dose_per_kg(15, 25)") == 375.0

    def test_celsius_to_fahrenheit(self, evaluate_silk):
        # 37°C = 98.6°F
        assert evaluate_silk("celsius_to_fahrenheit(37)") == 98.6

    def test_fahrenheit_to_celsius(self, evaluate_silk):
        # 98.6°F = 37°C
        assert evaluate_silk("fahrenheit_to_celsius(98.6)") == 37.0

    def test_mean(self, evaluate_silk):
        assert evaluate_silk("mean([10, 20, 30])") == 20.0

    def test_median_odd(self, evaluate_silk):
        assert evaluate_silk("median([1, 3, 5])") == 3

    def test_median_even(self, evaluate_silk):
        assert evaluate_silk("median([1, 2, 3, 4])") == 2.5
