"""
Tests for number .digitDuoquadragintMin() method - min of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintMin_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111.digitDuoquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitDuoquadragintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111119.digitDuoquadragintMin())')
        assert output[-1] == "[1, 9]"
