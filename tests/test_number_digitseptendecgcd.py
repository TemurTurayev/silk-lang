"""
Tests for number .digitSeptendecGCD() method - GCD of each consecutive 17-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptendecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptendecGCD_basic(self):
        output = self._run('print(24682468246824682.digitSeptendecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8,2) = 2
        assert output[-1] == "[2]"

    def test_digitSeptendecGCD_remainder(self):
        output = self._run('print(246824682468246829.digitSeptendecGCD())')
        # gcd(2,4,6,..)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
