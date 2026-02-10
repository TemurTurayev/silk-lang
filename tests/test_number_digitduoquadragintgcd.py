"""
Tests for number .digitDuoquadragintGCD() method - GCD of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintGCD_basic(self):
        output = self._run('print(222222222222222222222222222222222222222222.digitDuoquadragintGCD())')
        assert output[-1] == "[2]"

    def test_digitDuoquadragintGCD_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222226.digitDuoquadragintGCD())')
        assert output[-1] == "[2, 6]"
