"""
Tests for number .digitSumSquares() method - sum of squares of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSumSquares:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSumSquares_basic(self):
        output = self._run('print(123.digitSumSquares())')
        # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
        assert output[-1] == "14"

    def test_digitSumSquares_single(self):
        output = self._run('print(5.digitSumSquares())')
        assert output[-1] == "25"
