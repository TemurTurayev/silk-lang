"""
Tests for number .digitDuodequinquagintGCD() method - GCD of each consecutive 48-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequinquagintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequinquagintGCD_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111111.digitDuodequinquagintGCD())')
        assert output[-1] == "[1]"

    def test_digitDuodequinquagintGCD_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222222222226.digitDuodequinquagintGCD())')
        assert output[-1] == "[2, 6]"
