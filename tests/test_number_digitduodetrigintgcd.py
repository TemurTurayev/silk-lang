"""
Tests for number .digitDuodetrigintGCD() method - GCD of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintGCD_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintGCD())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222226.digitDuodetrigintGCD())')
        assert output[-1] == "[2, 6]"
