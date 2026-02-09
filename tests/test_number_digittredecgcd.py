"""
Tests for number .digitTredecGCD() method - GCD of each consecutive 13-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTredecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTredecGCD_basic(self):
        output = self._run('print(2468246824682.digitTredecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2) = 2
        assert output[-1] == "[2]"

    def test_digitTredecGCD_remainder(self):
        output = self._run('print(24682468246826.digitTredecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2)=2, gcd(6)=6
        assert output[-1] == "[2, 6]"
