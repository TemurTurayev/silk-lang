"""
Tests for number .digitQuadragintGCD() method - GCD of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintGCD_basic(self):
        output = self._run('print(2222222222222222222222222222222222222222.digitQuadragintGCD())')
        assert output[-1] == "[2]"

    def test_digitQuadragintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222226.digitQuadragintGCD())')
        assert output[-1] == "[2, 6]"
