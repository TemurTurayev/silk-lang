"""
Tests for number .digitQuintGCD() method - GCD of each consecutive quintuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintGCD_basic(self):
        output = self._run('print(2468424684.digitQuintGCD())')
        # [gcd(2,4,6,8,4)=2, gcd(2,4,6,8,4)=2]
        assert output[-1] == "[2, 2]"

    def test_digitQuintGCD_remainder(self):
        output = self._run('print(2468436.digitQuintGCD())')
        # [gcd(2,4,6,8,4)=2, gcd(3,6)=3]
        assert output[-1] == "[2, 3]"
