"""
Tests for number .digitDuodequinquagintMin() method - min of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintMin_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintMin())')
        assert output[-1] == "[1]"

    def test_digitDuodequinquagintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111111119.digitDuodequinquagintMin())')
        assert output[-1] == "[1, 9]"
