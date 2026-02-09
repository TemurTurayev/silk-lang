"""
Tests for number .digitDuodecGCD() method - GCD of each consecutive 12-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodecGCD_basic(self):
        output = self._run('print(246824682468.digitDuodecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8) = 2
        assert output[-1] == "[2]"

    def test_digitDuodecGCD_remainder(self):
        output = self._run('print(2468246824689.digitDuodecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
