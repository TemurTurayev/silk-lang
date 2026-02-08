"""
Tests for number .digitAdjacentGCD() method - GCD of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentGCD_basic(self):
        output = self._run('print(264.digitAdjacentGCD())')
        # gcd(2,6), gcd(6,4) = [2, 2]
        assert output[-1] == "[2, 2]"

    def test_digitAdjacentGCD_coprimes(self):
        output = self._run('print(357.digitAdjacentGCD())')
        # gcd(3,5), gcd(5,7) = [1, 1]
        assert output[-1] == "[1, 1]"
