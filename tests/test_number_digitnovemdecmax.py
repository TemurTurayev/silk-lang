"""
Tests for number .digitNovemdecMax() method - max of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecMax_basic(self):
        output = self._run('print(1211121112111211121.digitNovemdecMax())')
        # max(1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1) = 2
        assert output[-1] == "[2]"

    def test_digitNovemdecMax_remainder(self):
        output = self._run('print(12111211121112111219.digitNovemdecMax())')
        # max(...)=2, max(9)=9
        assert output[-1] == "[2, 9]"
