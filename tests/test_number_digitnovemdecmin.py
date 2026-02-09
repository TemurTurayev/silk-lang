"""
Tests for number .digitNovemdecMin() method - min of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecMin_basic(self):
        output = self._run('print(1211121112111211121.digitNovemdecMin())')
        # min(1,2,1,1,...) = 1
        assert output[-1] == "[1]"

    def test_digitNovemdecMin_remainder(self):
        output = self._run('print(12111211121112111219.digitNovemdecMin())')
        # min(...)=1, min(9)=9
        assert output[-1] == "[1, 9]"
