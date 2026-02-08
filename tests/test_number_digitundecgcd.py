"""
Tests for number .digitUndecGCD() method - GCD of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecGCD_basic(self):
        output = self._run('print(22446688224.digitUndecGCD())')
        # gcd(2,2,4,4,6,6,8,8,2,2,4) = 2
        assert output[-1] == "[2]"

    def test_digitUndecGCD_remainder(self):
        output = self._run('print(224466882246.digitUndecGCD())')
        # gcd(2,2,4,4,6,6,8,8,2,2,4) = 2, gcd(6) = 6
        assert output[-1] == "[2, 6]"
