"""
Tests for number .digitSexquadragintMin() method - min of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintMin_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintMin_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111111119.digitSexquadragintMin())')
        assert output[-1] == "[1, 9]"
