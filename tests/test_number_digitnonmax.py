"""
Tests for number .digitNonMax() method - max of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonMax_basic(self):
        output = self._run('print(123456789123456789.digitNonMax())')
        # [max(1,2,3,4,5,6,7,8,9)=9, max(1,2,3,4,5,6,7,8,9)=9]
        assert output[-1] == "[9, 9]"

    def test_digitNonMax_remainder(self):
        output = self._run('print(12345678912.digitNonMax())')
        # [max(1,2,3,4,5,6,7,8,9)=9, max(1,2)=2]
        assert output[-1] == "[9, 2]"
