"""
Tests for number .digitQuadGCD() method - GCD of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadGCD_basic(self):
        output = self._run('print(24683693.digitQuadGCD())')
        # [gcd(2,4,6,8)=2, gcd(3,6,9,3)=3]
        assert output[-1] == "[2, 3]"

    def test_digitQuadGCD_remainder(self):
        output = self._run('print(246835.digitQuadGCD())')
        # [gcd(2,4,6,8)=2, gcd(3,5)=1]
        assert output[-1] == "[2, 1]"
