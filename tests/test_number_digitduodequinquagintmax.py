"""
Tests for number .digitDuodequinquagintMax() method - max of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintMax_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintMax())')
        assert output[-1] == "[1]"

    def test_digitDuodequinquagintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111111119.digitDuodequinquagintMax())')
        assert output[-1] == "[1, 9]"
