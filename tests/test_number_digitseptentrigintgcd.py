"""
Tests for number .digitSeptentrigintGCD() method - GCD of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintGCD_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintGCD())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222222222222226.digitSeptentrigintGCD())')
        assert output[-1] == "[2, 6]"
