"""
Tests for number .digitCountZero() method - count zero digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCountZero:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCountZero_none(self):
        output = self._run('print(123.digitCountZero())')
        assert output[-1] == "0"

    def test_digitCountZero_some(self):
        output = self._run('print(10203.digitCountZero())')
        assert output[-1] == "2"
