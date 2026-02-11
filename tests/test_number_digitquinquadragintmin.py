"""
Tests for number .digitQuinquadragintMin() method - min of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintMin_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitQuinquadragintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111119.digitQuinquadragintMin())')
        assert output[-1] == "[1, 9]"
