"""
Tests for number .digitQuintrigintGCD() method - GCD of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintGCD_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintGCD())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintGCD_remainder(self):
        output = self._run('print(333333333333333333333333333333333336.digitQuintrigintGCD())')
        assert output[-1] == "[3, 6]"
