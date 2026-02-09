"""
Tests for number .digitDuodequadragintSum() method - sum of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111111111.digitDuodequadragintSum())')
        assert output[-1] == "[38]"

    def test_digitDuodequadragintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111111111112.digitDuodequadragintSum())')
        assert output[-1] == "[38, 2]"
