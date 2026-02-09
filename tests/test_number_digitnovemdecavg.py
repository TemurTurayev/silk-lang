"""
Tests for number .digitNovemdecAvg() method - average of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecAvg_basic(self):
        output = self._run('print(3333333333333333333.digitNovemdecAvg())')
        # avg(3*19) = 3.0
        assert output[-1] == "[3]"

    def test_digitNovemdecAvg_remainder(self):
        output = self._run('print(33333333333333333337.digitNovemdecAvg())')
        # avg(19 threes)=3, avg(7)=7
        assert output[-1] == "[3, 7]"
