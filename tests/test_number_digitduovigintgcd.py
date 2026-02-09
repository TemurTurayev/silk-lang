"""
Tests for number .digitDuovigintGCD() method - GCD of each consecutive 22-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuovigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuovigintGCD_basic(self):
        output = self._run('print(4444444444444444444444.digitDuovigintGCD())')
        assert output[-1] == "[4]"

    def test_digitDuovigintGCD_remainder(self):
        output = self._run('print(66666666666666666666663.digitDuovigintGCD())')
        # gcd(6*22)=6, gcd(3)=3
        assert output[-1] == "[6, 3]"
