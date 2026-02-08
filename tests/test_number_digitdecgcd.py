"""
Tests for number .digitDecGCD() method - GCD of each consecutive 10-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDecGCD_basic(self):
        output = self._run('print(24681024682468102468.digitDecGCD())')
        # digits: 2,4,6,8,1,0,2,4,6,8 -> gcd=1; 2,4,6,8,1,0,2,4,6,8 -> gcd=1
        assert output[-1] == "[1, 1]"

    def test_digitDecGCD_remainder(self):
        output = self._run('print(246824682468.digitDecGCD())')
        # digits: 2,4,6,8,2,4,6,8,2,4 -> gcd=2; 6,8 -> gcd=2
        assert output[-1] == "[2, 2]"
