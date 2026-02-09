"""
Tests for number .digitDuodequadragintMax() method - max of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintMax_basic(self):
        output = self._run('print(11111111111111111111111111111111111111.digitDuodequadragintMax())')
        assert output[-1] == "[1]"

    def test_digitDuodequadragintMax_remainder(self):
        output = self._run('print(111111111111111111111111111111111111119.digitDuodequadragintMax())')
        assert output[-1] == "[1, 9]"
