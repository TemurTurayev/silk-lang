"""
Interpreter Negative Tests

These tests verify that the interpreter correctly reports runtime errors.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from silk.interpreter import Interpreter
from silk.errors import RuntimeError_


class TestRuntimeErrors:
    """Test runtime error handling."""

    def test_undefined_variable(self, run_silk):
        interp = Interpreter()
        # Should print error but not crash
        result = interp.run("print(undefined_var)")
        assert result is False

    def test_immutable_reassignment(self, run_silk):
        interp = Interpreter()
        code = """
            let x = 10
            x = 20
        """
        result = interp.run(code)
        assert result is False

    def test_division_by_zero(self, run_silk):
        interp = Interpreter()
        result = interp.run("let x = 10 / 0")
        assert result is False

    def test_invalid_type_addition(self, run_silk):
        interp = Interpreter()
        # Can't add string and int
        result = interp.run('let x = "hello" + 5')
        assert result is False

    def test_index_out_of_bounds(self, run_silk):
        interp = Interpreter()
        result = interp.run("let x = [1, 2, 3][10]")
        assert result is False

    def test_call_non_function(self, run_silk):
        interp = Interpreter()
        result = interp.run("""
            let x = 42
            x()
        """)
        assert result is False

    def test_len_on_number(self, run_silk):
        interp = Interpreter()
        result = interp.run("let x = len(42)")
        assert result is False

    def test_invalid_member_access(self, run_silk):
        interp = Interpreter()
        result = interp.run('let x = "hello".nonexistent')
        assert result is False

    def test_for_on_non_iterable(self, run_silk):
        interp = Interpreter()
        result = interp.run("""
            for i in 42 {
                print(i)
            }
        """)
        assert result is False

    def test_index_assign_on_non_array(self, run_silk):
        interp = Interpreter()
        result = interp.run("""
            let x = "hello"
            x[0] = "H"
        """)
        # Strings are immutable in Silk
        assert result is False


class TestParseErrors:
    """Test parse error handling."""

    def test_missing_closing_brace(self, run_silk):
        interp = Interpreter()
        result = interp.run("""
            fn test() {
                print("hello")
        """)
        assert result is False

    def test_missing_closing_paren(self, run_silk):
        interp = Interpreter()
        result = interp.run("print(42")
        assert result is False

    def test_invalid_expression(self, run_silk):
        interp = Interpreter()
        result = interp.run("let x = + +")
        assert result is False

    def test_missing_function_body(self, run_silk):
        interp = Interpreter()
        result = interp.run("fn test()")
        assert result is False

    def test_missing_if_body(self, run_silk):
        interp = Interpreter()
        result = interp.run("if true")
        assert result is False

    def test_invalid_let_syntax(self, run_silk):
        interp = Interpreter()
        result = interp.run("let = 10")
        assert result is False
