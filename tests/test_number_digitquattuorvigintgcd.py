"""
Tests for number .digitQuattuorvigintGCD() method - GCD of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintGCD_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintGCD())')
        assert output[-1] == "[1]"

    def test_digitQuattuorvigintGCD_remainder(self):
        output = self._run('print(2222222222222222222222226.digitQuattuorvigintGCD())')
        assert output[-1] == "[2, 6]"
