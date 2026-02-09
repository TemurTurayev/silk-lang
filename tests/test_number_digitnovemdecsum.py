"""
Tests for number .digitNovemdecSum() method - sum of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecSum_basic(self):
        output = self._run('print(1111111111111111111.digitNovemdecSum())')
        # sum(1*19) = 19
        assert output[-1] == "[19]"

    def test_digitNovemdecSum_remainder(self):
        output = self._run('print(11111111111111111115.digitNovemdecSum())')
        # sum(19 ones)=19, sum(5)=5
        assert output[-1] == "[19, 5]"
