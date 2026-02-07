"""
Tests for string .isISBN() method.
"""

from silk.interpreter import Interpreter


class TestStringIsISBN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isISBN_valid_10(self):
        output = self._run('print("0306406152".isISBN())')
        assert output[-1] == "true"

    def test_isISBN_invalid(self):
        output = self._run('print("1234567890".isISBN())')
        assert output[-1] == "false"
