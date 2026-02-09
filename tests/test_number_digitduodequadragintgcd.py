"""
Tests for number .digitDuodequadragintGCD() method - GCD of each consecutive 38-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodequadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodequadragintGCD_basic(self):
        output = self._run('print(22222222222222222222222222222222222222.digitDuodequadragintGCD())')
        assert output[-1] == "[2]"

    def test_digitDuodequadragintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222222222222223.digitDuodequadragintGCD())')
        assert output[-1] == "[2, 3]"
