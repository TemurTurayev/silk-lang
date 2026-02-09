"""
Tests for number .digitDuodequadragintMin() method - min of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintMin_basic(self):
        output = self._run('print(11111111111111111111111111111111111111.digitDuodequadragintMin())')
        assert output[-1] == "[1]"

    def test_digitDuodequadragintMin_remainder(self):
        output = self._run('print(222222222222222222222222222222222222221.digitDuodequadragintMin())')
        assert output[-1] == "[2, 1]"
