"""
Tests for number .digitUnvigintGCD() method - GCD of each consecutive 21-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnvigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnvigintGCD_basic(self):
        output = self._run('print(222222222222222222222.digitUnvigintGCD())')
        assert output[-1] == "[2]"

    def test_digitUnvigintGCD_remainder(self):
        output = self._run('print(2222222222222222222226.digitUnvigintGCD())')
        # gcd(2*21)=2, gcd(6)=6
        assert output[-1] == "[2, 6]"
