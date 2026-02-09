"""
Tests for number .digitNovemdecGCD() method - GCD of each consecutive 19-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNovemdecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNovemdecGCD_basic(self):
        output = self._run('print(2468246824682468246.digitNovemdecGCD())')
        # gcd(2,4,6,8,2,4,6,8,2,4,6,8,2,4,6,8,2,4,6) = 2
        assert output[-1] == "[2]"

    def test_digitNovemdecGCD_remainder(self):
        output = self._run('print(24682468246824682469.digitNovemdecGCD())')
        # gcd(...)=2, gcd(9)=9
        assert output[-1] == "[2, 9]"
