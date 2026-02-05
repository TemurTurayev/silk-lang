"""Tests for Result<T, E> type."""

import pytest
from silk.interpreter import Interpreter


class TestResult:
    """Test Result<T, E> type."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_ok_value(self, interp):
        interp.run("""
let x = Ok(42)
print(x)
""")
        assert "Ok(42)" in interp.output_lines[-1]

    def test_err_value(self, interp):
        interp.run("""
let x = Err("something went wrong")
print(x)
""")
        assert "Err" in interp.output_lines[-1]

    def test_ok_equality(self, interp):
        interp.run("""
let a = Ok(42)
let b = Ok(42)
print(a == b)
""")
        assert interp.output_lines[-1] == "true"

    def test_ok_err_inequality(self, interp):
        interp.run("""
let a = Ok(42)
let b = Err("error")
print(a == b)
""")
        assert interp.output_lines[-1] == "false"

    def test_safe_division(self, interp):
        interp.run("""
fn safe_divide(a, b) {
    if b == 0 {
        return Err("Division by zero")
    }
    return Ok(a / b)
}

let result = safe_divide(10, 2)
print(result)
""")
        assert "Ok(5)" in interp.output_lines[-1]

    def test_safe_division_error(self, interp):
        interp.run("""
fn safe_divide(a, b) {
    if b == 0 {
        return Err("Division by zero")
    }
    return Ok(a / b)
}

let result = safe_divide(10, 0)
print(result)
""")
        assert "Err" in interp.output_lines[-1]
        assert "Division by zero" in interp.output_lines[-1]
