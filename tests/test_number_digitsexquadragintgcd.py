"""
Tests for number .digitSexquadragintGCD() method - GCD of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintGCD_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintGCD())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222222226.digitSexquadragintGCD())')
        assert output[-1] == "[2, 6]"
