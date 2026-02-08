"""
Tests for number .digitNonGCD() method - GCD of each consecutive 9-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitNonGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitNonGCD_basic(self):
        output = self._run('print(123456789123456789.digitNonGCD())')
        # [gcd(1,2,3,4,5,6,7,8,9)=1, gcd(1,2,3,4,5,6,7,8,9)=1]
        assert output[-1] == "[1, 1]"

    def test_digitNonGCD_remainder(self):
        output = self._run('print(24681012348.digitNonGCD())')
        # digits: 2,4,6,8,1,0,1,2,3 -> gcd=1; 4,8 -> gcd=4
        assert output[-1] == "[1, 4]"
