"""
Tests for number .digitNonMin() method - min of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonMin_basic(self):
        output = self._run('print(123456789123456789.digitNonMin())')
        # [min(1,2,3,4,5,6,7,8,9)=1, min(1,2,3,4,5,6,7,8,9)=1]
        assert output[-1] == "[1, 1]"

    def test_digitNonMin_remainder(self):
        output = self._run('print(12345678912.digitNonMin())')
        # [min(1,2,3,4,5,6,7,8,9)=1, min(1,2)=1]
        assert output[-1] == "[1, 1]"
