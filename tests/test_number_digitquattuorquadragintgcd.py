"""
Tests for number .digitQuattuorquadragintGCD() method - GCD of each consecutive 44-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorquadragintGCD_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111.digitQuattuorquadragintGCD())')
        assert output[-1] == "[1]"

    def test_digitQuattuorquadragintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222222222444.digitQuattuorquadragintGCD())')
        assert output[-1] == "[2, 4]"
