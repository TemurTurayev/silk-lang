"""
Tests for number .digitTripleGCD() method - GCD of each consecutive triple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTripleGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTripleGCD_basic(self):
        output = self._run('print(246369.digitTripleGCD())')
        # [gcd(2,4,6)=2, gcd(3,6,9)=3]
        assert output[-1] == "[2, 3]"

    def test_digitTripleGCD_remainder(self):
        output = self._run('print(84635.digitTripleGCD())')
        # [gcd(8,4,6)=2, gcd(3,5)=1]
        assert output[-1] == "[2, 1]"
