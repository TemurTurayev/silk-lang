"""
Tests for number .digitTrevigintGCD() method - GCD of each consecutive 23-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrevigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrevigintGCD_basic(self):
        output = self._run('print(44444444444444444444444.digitTrevigintGCD())')
        assert output[-1] == "[4]"

    def test_digitTrevigintGCD_remainder(self):
        output = self._run('print(666666666666666666666663.digitTrevigintGCD())')
        # gcd(6*23)=6, gcd(3)=3
        assert output[-1] == "[6, 3]"
