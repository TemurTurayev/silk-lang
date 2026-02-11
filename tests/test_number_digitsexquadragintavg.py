"""
Tests for number .digitSexquadragintAvg() method - average of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintAvg_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintAvg_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222222224.digitSexquadragintAvg())')
        assert output[-1] == "[2, 4]"
