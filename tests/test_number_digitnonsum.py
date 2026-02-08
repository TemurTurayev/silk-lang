"""
Tests for number .digitNonSum() method - sum of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonSum_basic(self):
        output = self._run('print(123456789123456789.digitNonSum())')
        # [1+2+3+4+5+6+7+8+9=45, 1+2+3+4+5+6+7+8+9=45]
        assert output[-1] == "[45, 45]"

    def test_digitNonSum_remainder(self):
        output = self._run('print(12345678901.digitNonSum())')
        # [1+2+3+4+5+6+7+8+9=45, 0+1=1]
        assert output[-1] == "[45, 1]"
