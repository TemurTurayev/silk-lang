"""Tests for Option<T> type."""

import pytest
from silk.interpreter import Interpreter


class TestOption:
    """Test Option<T> type."""

    @pytest.fixture
    def interp(self):
        return Interpreter()

    def test_some_value(self, interp):
        interp.run("""
let x = Some(42)
print(x)
""")
        assert "Some(42)" in interp.output_lines[-1]

    def test_none_value(self, interp):
        interp.run("""
let x = None
print(x)
""")
        assert interp.output_lines[-1] == "None"

    def test_some_equality(self, interp):
        interp.run("""
let a = Some(42)
let b = Some(42)
print(a == b)
""")
        assert interp.output_lines[-1] == "true"

    def test_some_inequality(self, interp):
        interp.run("""
let a = Some(42)
let b = Some(99)
print(a == b)
""")
        assert interp.output_lines[-1] == "false"

    def test_some_none_inequality(self, interp):
        interp.run("""
let a = Some(42)
let b = None
print(a == b)
""")
        assert interp.output_lines[-1] == "false"
