"""
Tests for number .digitDuodequinquagintAvg() method - average of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintAvg_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintAvg())')
        assert output[-1] == "[1]"

    def test_digitDuodequinquagintAvg_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222222222224.digitDuodequinquagintAvg())')
        assert output[-1] == "[2, 4]"
