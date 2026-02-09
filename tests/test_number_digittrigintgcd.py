"""
Tests for number .digitTrigintGCD() method - GCD of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintGCD_basic(self):
        output = self._run('print(222222222222222222222222222222.digitTrigintGCD())')
        assert output[-1] == "[2]"

    def test_digitTrigintGCD_remainder(self):
        output = self._run('print(2222222222222222222222222222226.digitTrigintGCD())')
        assert output[-1] == "[2, 6]"
