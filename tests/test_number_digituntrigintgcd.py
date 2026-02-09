"""
Tests for number .digitUntrigintGCD() method - GCD of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintGCD_basic(self):
        output = self._run('print(2222222222222222222222222222222.digitUntrigintGCD())')
        assert output[-1] == "[2]"

    def test_digitUntrigintGCD_remainder(self):
        output = self._run('print(22222222222222222222222222222226.digitUntrigintGCD())')
        assert output[-1] == "[2, 6]"
