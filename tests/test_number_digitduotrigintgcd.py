"""
Tests for number .digitDuotrigintGCD() method - GCD of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintGCD_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintGCD())')
        assert output[-1] == "[2]"

    def test_digitDuotrigintGCD_remainder(self):
        output = self._run('print(222222222222222222222222222222223.digitDuotrigintGCD())')
        assert output[-1] == "[2, 3]"
