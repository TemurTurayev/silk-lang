"""
Tests for string .isAlphanumeric() method.
"""

from silk.interpreter import Interpreter


class TestStringAlphanumeric:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAlphanumeric_true(self):
        output = self._run('print("abc123".isAlphanumeric())')
        assert output[-1] == "true"

    def test_isAlphanumeric_letters(self):
        output = self._run('print("hello".isAlphanumeric())')
        assert output[-1] == "true"

    def test_isAlphanumeric_false(self):
        output = self._run('print("hello world".isAlphanumeric())')
        assert output[-1] == "false"

    def test_isAlphanumeric_empty(self):
        output = self._run('print("".isAlphanumeric())')
        assert output[-1] == "false"
