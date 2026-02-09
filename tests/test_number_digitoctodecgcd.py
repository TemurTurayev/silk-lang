"""
Tests for number .digitOctodecGCD() method - GCD of each consecutive 18-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitOctodecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitOctodecGCD_basic(self):
        output = self._run('print(246824682468246824.digitOctodecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8,2,4) = 2
        assert output[-1] == "[2]"

    def test_digitOctodecGCD_remainder(self):
        output = self._run('print(2468246824682468249.digitOctodecGCD())')
        # gcd(...)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
