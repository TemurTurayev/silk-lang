"""
Tests for number .digitDuodequadragintAvg() method - average of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111111111111.digitDuodequadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitDuodequadragintAvg_remainder(self):
        output = self._run('print(111111111111111111111111111111111111115.digitDuodequadragintAvg())')
        assert output[-1] == "[1, 5]"
