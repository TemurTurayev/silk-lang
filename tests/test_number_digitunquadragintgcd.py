"""
Tests for number .digitUnquadragintGCD() method - GCD of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintGCD_basic(self):
        output = self._run('print(22222222222222222222222222222222222222222.digitUnquadragintGCD())')
        assert output[-1] == "[2]"

    def test_digitUnquadragintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222226.digitUnquadragintGCD())')
        assert output[-1] == "[2, 6]"
