"""
Tests for number .digitQuinquadragintGCD() method - GCD of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintGCD_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintGCD())')
        assert output[-1] == "[1]"

    def test_digitQuinquadragintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222222222444.digitQuinquadragintGCD())')
        assert output[-1] == "[2, 4]"
