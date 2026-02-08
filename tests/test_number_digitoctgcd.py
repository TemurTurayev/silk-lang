"""
Tests for number .digitOctGCD() method - GCD of each consecutive octuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctGCD_basic(self):
        output = self._run('print(1234567824682468.digitOctGCD())')
        # [gcd(1,2,3,4,5,6,7,8)=1, gcd(2,4,6,8,2,4,6,8)=2]
        assert output[-1] == "[1, 2]"

    def test_digitOctGCD_remainder(self):
        output = self._run('print(1234567893.digitOctGCD())')
        # [gcd(1,2,3,4,5,6,7,8)=1, gcd(9,3)=3]
        assert output[-1] == "[1, 3]"
