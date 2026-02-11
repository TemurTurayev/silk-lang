"""
Tests for number .digitSexquadragintMax() method - max of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintMax_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintMax_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111111119.digitSexquadragintMax())')
        assert output[-1] == "[1, 9]"
