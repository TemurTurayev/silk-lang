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


class TestBuiltinFunctions:
    """Test built-in functions for coverage."""

    def test_type_int(self, interp):
        interp.run('print(type(42))')
        assert interp.output_lines[-1] == "int"

    def test_type_str(self, interp):
        interp.run('print(type("hello"))')
        assert interp.output_lines[-1] == "str"

    def test_type_float(self, interp):
        interp.run('print(type(3.14))')
        assert interp.output_lines[-1] == "float"

    def test_type_bool(self, interp):
        interp.run('print(type(true))')
        assert interp.output_lines[-1] == "bool"

    def test_type_array(self, interp):
        interp.run('print(type([1, 2, 3]))')
        assert interp.output_lines[-1] == "array"

    def test_str_conversion(self, interp):
        interp.run('print(str(42))')
        assert interp.output_lines[-1] == "42"

    def test_int_conversion(self, interp):
        interp.run('print(int("42"))')
        assert interp.output_lines[-1] == "42"

    def test_float_conversion(self, interp):
        interp.run('print(float("3.14"))')
        assert interp.output_lines[-1] == "3.14"

    def test_bool_conversion_truthy(self, interp):
        interp.run('print(bool(1))')
        assert interp.output_lines[-1] == "true"

    def test_bool_conversion_falsy(self, interp):
        interp.run('print(bool(0))')
        assert interp.output_lines[-1] == "false"

    def test_len_array(self, interp):
        interp.run('print(len([1, 2, 3]))')
        assert interp.output_lines[-1] == "3"

    def test_len_string(self, interp):
        interp.run('print(len("hello"))')
        assert interp.output_lines[-1] == "5"

    def test_range_basic(self, interp):
        interp.run('print(range(5))')
        assert "[0, 1, 2, 3, 4]" in interp.output_lines[-1]

    def test_range_start_end(self, interp):
        interp.run('print(range(2, 5))')
        assert "[2, 3, 4]" in interp.output_lines[-1]

    def test_push(self, interp):
        interp.run('let mut arr = [1, 2]\npush(arr, 3)\nprint(arr)')
        assert "[1, 2, 3]" in interp.output_lines[-1]

    def test_pop(self, interp):
        interp.run('let mut arr = [1, 2, 3]\nlet x = pop(arr)\nprint(x)')
        assert interp.output_lines[-1] == "3"

    def test_slice(self, interp):
        interp.run('print(slice([1, 2, 3, 4], 1, 3))')
        assert "[2, 3]" in interp.output_lines[-1]

    def test_reverse(self, interp):
        interp.run('print(reverse([1, 2, 3]))')
        assert "[3, 2, 1]" in interp.output_lines[-1]

    def test_sort(self, interp):
        interp.run('print(sort([3, 1, 2]))')
        assert "[1, 2, 3]" in interp.output_lines[-1]

    def test_join(self, interp):
        interp.run('print(join(["a", "b", "c"], "-"))')
        assert interp.output_lines[-1] == "a-b-c"

    def test_split(self, interp):
        interp.run('print(split("a-b-c", "-"))')
        assert "[a, b, c]" in interp.output_lines[-1]

    def test_contains_true(self, interp):
        interp.run('print(contains([1, 2, 3], 2))')
        assert interp.output_lines[-1] == "true"

    def test_contains_false(self, interp):
        interp.run('print(contains([1, 2, 3], 5))')
        assert interp.output_lines[-1] == "false"


class TestMathFunctions:
    """Test math functions."""

    def test_abs_positive(self, interp):
        interp.run('print(abs(5))')
        assert interp.output_lines[-1] == "5"

    def test_abs_negative(self, interp):
        interp.run('print(abs(-5))')
        assert interp.output_lines[-1] == "5"

    def test_round(self, interp):
        interp.run('print(round(3.7))')
        assert interp.output_lines[-1] == "4"

    def test_min(self, interp):
        interp.run('print(min(3, 1, 4, 1, 5))')
        assert interp.output_lines[-1] == "1"

    def test_max(self, interp):
        interp.run('print(max(3, 1, 4, 1, 5))')
        assert interp.output_lines[-1] == "5"

    def test_sum(self, interp):
        interp.run('print(sum([1, 2, 3, 4]))')
        assert interp.output_lines[-1] == "10"

    def test_sqrt(self, interp):
        interp.run('print(sqrt(16))')
        assert interp.output_lines[-1] == "4"

    def test_pow(self, interp):
        interp.run('print(pow(2, 3))')
        assert interp.output_lines[-1] == "8"

    def test_ceil(self, interp):
        interp.run('print(ceil(3.2))')
        assert interp.output_lines[-1] == "4"

    def test_floor(self, interp):
        interp.run('print(floor(3.8))')
        assert interp.output_lines[-1] == "3"


class TestMedicalFunctionsExtended:
    """Test medical calculation functions."""

    def test_bmi(self, interp):
        interp.run('print(bmi(70, 1.75))')
        assert "22.86" in interp.output_lines[-1]

    def test_bsa(self, interp):
        interp.run('print(bsa(70, 175))')
        # DuBois formula
        assert float(interp.output_lines[-1]) > 1.8

    def test_ideal_body_weight_male(self, interp):
        interp.run('print(ideal_body_weight(180, true))')
        assert float(interp.output_lines[-1]) > 70

    def test_ideal_body_weight_female(self, interp):
        interp.run('print(ideal_body_weight(165, false))')
        assert float(interp.output_lines[-1]) > 50

    def test_dose_per_kg(self, interp):
        interp.run('print(dose_per_kg(15, 25))')
        assert interp.output_lines[-1] == "375"

    def test_celsius_to_fahrenheit(self, interp):
        interp.run('print(celsius_to_fahrenheit(37))')
        assert "98.6" in interp.output_lines[-1]

    def test_fahrenheit_to_celsius(self, interp):
        interp.run('print(fahrenheit_to_celsius(98.6))')
        assert "37" in interp.output_lines[-1]

    def test_mean(self, interp):
        interp.run('print(mean([2, 4, 6, 8]))')
        assert interp.output_lines[-1] == "5"

    def test_median_odd(self, interp):
        interp.run('print(median([1, 3, 5, 7, 9]))')
        assert interp.output_lines[-1] == "5"

    def test_median_even(self, interp):
        interp.run('print(median([1, 2, 3, 4]))')
        assert interp.output_lines[-1] == "2.5"


class TestStringMethods:
    """Test string methods."""

    def test_upper(self, interp):
        interp.run('print("hello".upper())')
        assert interp.output_lines[-1] == "HELLO"

    def test_lower(self, interp):
        interp.run('print("HELLO".lower())')
        assert interp.output_lines[-1] == "hello"

    def test_strip(self, interp):
        interp.run('print("  hello  ".strip())')
        assert interp.output_lines[-1] == "hello"

    def test_replace(self, interp):
        interp.run('print("hello".replace("l", "L"))')
        assert interp.output_lines[-1] == "heLLo"

    def test_starts_with_true(self, interp):
        interp.run('print("hello".starts_with("he"))')
        assert interp.output_lines[-1] == "true"

    def test_starts_with_false(self, interp):
        interp.run('print("hello".starts_with("wo"))')
        assert interp.output_lines[-1] == "false"

    def test_ends_with_true(self, interp):
        interp.run('print("hello".ends_with("lo"))')
        assert interp.output_lines[-1] == "true"

    def test_ends_with_false(self, interp):
        interp.run('print("hello".ends_with("la"))')
        assert interp.output_lines[-1] == "false"
