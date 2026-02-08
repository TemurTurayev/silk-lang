"""
Tests for number .digitWindowGCD3() method - GCD of sliding windows of size 3.
"""

from silk.interpreter import Interpreter


class TestNumberDigitWindowGCD3:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitWindowGCD3_basic(self):
        output = self._run('print(24684.digitWindowGCD3())')
        # gcd(2,4,6), gcd(4,6,8), gcd(6,8,4) = [2, 2, 2]
        assert output[-1] == "[2, 2, 2]"

    def test_digitWindowGCD3_coprimes(self):
        output = self._run('print(1357.digitWindowGCD3())')
        # gcd(1,3,5), gcd(3,5,7) = [1, 1]
        assert output[-1] == "[1, 1]"
