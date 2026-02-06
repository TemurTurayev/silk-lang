"""
Tests for string .toInt() and .toFloat() conversion methods.
"""

import pytest
from silk.interpreter import Interpreter


class TestStringConversion:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toInt_basic(self):
        output = self._run('print("42".toInt())')
        assert output[-1] == "42"

    def test_toInt_negative(self):
        output = self._run('print("-7".toInt())')
        assert output[-1] == "-7"

    def test_toInt_zero(self):
        output = self._run('print("0".toInt())')
        assert output[-1] == "0"

    def test_toInt_arithmetic(self):
        output = self._run('''
let x = "10".toInt() + 5
print(x)
''')
        assert output[-1] == "15"

    def test_toFloat_basic(self):
        output = self._run('print("3.14".toFloat())')
        assert output[-1] == "3.14"

    def test_toFloat_integer_string(self):
        output = self._run('print("42".toFloat())')
        assert output[-1] == "42"

    def test_toFloat_negative(self):
        output = self._run('print("-2.5".toFloat())')
        assert output[-1] == "-2.5"

    def test_toFloat_arithmetic(self):
        output = self._run('''
let x = "1.5".toFloat() + 2.5
print(x)
''')
        assert output[-1] == "4"

    def test_toInt_invalid_throws(self):
        """Invalid toInt should throw a runtime error."""
        interp = Interpreter()
        result = interp.run('let x = "abc".toInt()')
        assert result is False

    def test_toFloat_invalid_throws(self):
        """Invalid toFloat should throw a runtime error."""
        interp = Interpreter()
        result = interp.run('let x = "xyz".toFloat()')
        assert result is False

    def test_toInt_with_whitespace(self):
        output = self._run('print(" 42 ".trim().toInt())')
        assert output[-1] == "42"
