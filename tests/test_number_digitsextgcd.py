"""
Tests for number .digitSextGCD() method - GCD of each consecutive sextuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextGCD_basic(self):
        output = self._run('print(246824246824.digitSextGCD())')
        # [gcd(2,4,6,8,2,4)=2, gcd(2,4,6,8,2,4)=2]
        assert output[-1] == "[2, 2]"

    def test_digitSextGCD_remainder(self):
        output = self._run('print(24682436.digitSextGCD())')
        # [gcd(2,4,6,8,2,4)=2, gcd(3,6)=3]
        assert output[-1] == "[2, 3]"
