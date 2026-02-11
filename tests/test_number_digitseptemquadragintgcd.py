"""
Tests for number .digitSeptemquadragintGCD() method - GCD of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintGCD_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintGCD())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222222222226.digitSeptemquadragintGCD())')
        assert output[-1] == "[2, 6]"
