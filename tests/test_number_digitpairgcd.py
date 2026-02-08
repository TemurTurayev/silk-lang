"""
Tests for number .digitPairGCD() method - GCD of each consecutive pair of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitPairGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitPairGCD_basic(self):
        output = self._run('print(4268.digitPairGCD())')
        # [gcd(4,2), gcd(6,8)] = [2, 2]
        assert output[-1] == "[2, 2]"

    def test_digitPairGCD_odd(self):
        output = self._run('print(93615.digitPairGCD())')
        # [gcd(9,3), gcd(6,1), 5] = [3, 1, 5]
        assert output[-1] == "[3, 1, 5]"
