"""
Tests for number .digitNonAvg() method - average of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonAvg_basic(self):
        output = self._run('print(123456789123456789.digitNonAvg())')
        # [avg(1..9)=5, avg(1..9)=5]
        assert output[-1] == "[5, 5]"

    def test_digitNonAvg_remainder(self):
        output = self._run('print(12345678924.digitNonAvg())')
        # [avg(1..9)=5, avg(2,4)=3]
        assert output[-1] == "[5, 3]"
