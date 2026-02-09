"""
Tests for number .digitQuinvigintGCD() method - GCD of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintGCD_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintGCD())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintGCD_remainder(self):
        output = self._run('print(22222222222222222222222226.digitQuinvigintGCD())')
        assert output[-1] == "[2, 6]"
