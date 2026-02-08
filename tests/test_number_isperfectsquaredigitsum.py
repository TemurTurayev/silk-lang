"""
Tests for number .isPerfectSquareDigitSum() method - check if digit sum is a perfect square.
"""

from silk.interpreter import Interpreter


class TestNumberIsPerfectSquareDigitSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPerfectSquareDigitSum_true(self):
        output = self._run('print(13.isPerfectSquareDigitSum())')
        assert output[-1] == "true"

    def test_isPerfectSquareDigitSum_false(self):
        output = self._run('print(14.isPerfectSquareDigitSum())')
        assert output[-1] == "false"

    def test_isPerfectSquareDigitSum_81(self):
        output = self._run('print(81.isPerfectSquareDigitSum())')
        assert output[-1] == "true"
