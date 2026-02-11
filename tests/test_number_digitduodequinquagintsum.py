"""
Tests for number .digitDuodequinquagintSum() method - sum of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintSum())')
        assert output[-1] == "[48]"

    def test_digitDuodequinquagintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111111119.digitDuodequinquagintSum())')
        assert output[-1] == "[48, 9]"
