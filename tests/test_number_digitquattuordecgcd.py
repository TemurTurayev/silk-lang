"""
Tests for number .digitQuattuordecGCD() method - GCD of each consecutive 14-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuordecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuordecGCD_basic(self):
        output = self._run('print(24682468246824.digitQuattuordecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4) = 2
        assert output[-1] == "[2]"

    def test_digitQuattuordecGCD_remainder(self):
        output = self._run('print(246824682468246.digitQuattuordecGCD())')
        # gcd(2,4,6,8,..)=2, gcd(6)=6
        assert output[-1] == "[2, 6]"
