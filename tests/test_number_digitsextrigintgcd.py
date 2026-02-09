"""
Tests for number .digitSextrigintGCD() method - GCD of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintGCD_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintGCD())')
        assert output[-1] == "[1]"

    def test_digitSextrigintGCD_remainder(self):
        output = self._run('print(3333333333333333333333333333333333336.digitSextrigintGCD())')
        assert output[-1] == "[3, 6]"
