"""
Tests for number .digitUndetrigintGCD() method - GCD of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintGCD_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintGCD())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222226.digitUndetrigintGCD())')
        assert output[-1] == "[2, 6]"
