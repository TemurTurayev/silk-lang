"""
Tests for number .digitDuoquadragintMax() method - max of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintMax_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111.digitDuoquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitDuoquadragintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111119.digitDuoquadragintMax())')
        assert output[-1] == "[1, 9]"
