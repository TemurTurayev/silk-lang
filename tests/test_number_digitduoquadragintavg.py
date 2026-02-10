"""
Tests for number .digitDuoquadragintAvg() method - average of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintAvg_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111.digitDuoquadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitDuoquadragintAvg_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111119.digitDuoquadragintAvg())')
        assert output[-1] == "[1, 9]"
