"""
Tests for number .digitTrequadragintGCD() method - GCD of each consecutive 43-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrequadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrequadragintGCD_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111.digitTrequadragintGCD())')
        assert output[-1] == "[1]"

    def test_digitTrequadragintGCD_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222222222444.digitTrequadragintGCD())')
        assert output[-1] == "[2, 4]"
