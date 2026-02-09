"""
Tests for number .digitVigintGCD() method - GCD of each consecutive 20-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitVigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitVigintGCD_basic(self):
        output = self._run('print(22222222222222222222.digitVigintGCD())')
        assert output[-1] == "[2]"

    def test_digitVigintGCD_remainder(self):
        output = self._run('print(222222222222222222226.digitVigintGCD())')
        # gcd(2*20)=2, gcd(6)=6
        assert output[-1] == "[2, 6]"
