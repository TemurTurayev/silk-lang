"""
Tests for number .digitQuindecGCD() method - GCD of each consecutive 15-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuindecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuindecGCD_basic(self):
        output = self._run('print(246824682468246.digitQuindecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6) = 2
        assert output[-1] == "[2]"

    def test_digitQuindecGCD_remainder(self):
        output = self._run('print(2468246824682469.digitQuindecGCD())')
        # gcd(2,4,6,..)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
