"""
Tests for number .digitSeptGCD() method - GCD of each consecutive septuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptGCD_basic(self):
        output = self._run('print(12345672468246.digitSeptGCD())')
        # [gcd(1,2,3,4,5,6,7)=1, gcd(2,4,6,8,2,4,6)=2]
        assert output[-1] == "[1, 2]"

    def test_digitSeptGCD_remainder(self):
        output = self._run('print(246813579.digitSeptGCD())')
        # [gcd(2,4,6,8,1,3,5)=1, gcd(7,9)=1]
        assert output[-1] == "[1, 1]"
