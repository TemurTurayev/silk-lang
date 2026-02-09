"""
Tests for number .digitSedecGCD() method - GCD of each consecutive 16-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSedecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSedecGCD_basic(self):
        output = self._run('print(2468246824682468.digitSedecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8) = 2
        assert output[-1] == "[2]"

    def test_digitSedecGCD_remainder(self):
        output = self._run('print(24682468246824689.digitSedecGCD())')
        # gcd(2,4,6,..)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
