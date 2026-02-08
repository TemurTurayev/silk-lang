"""
Tests for number .digitSquareSum() method - sum of squares of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSquareSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSquareSum_basic(self):
        output = self._run('print(1234.digitSquareSum())')
        assert output[-1] == "30"

    def test_digitSquareSum_single(self):
        output = self._run('print(9.digitSquareSum())')
        assert output[-1] == "81"
