"""
Tests for number .digitUndequadragintGCD() method - GCD of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintGCD_basic(self):
        output = self._run('print(222222222222222222222222222222222222222.digitUndequadragintGCD())')
        assert output[-1] == "[2]"

    def test_digitUndequadragintGCD_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222223.digitUndequadragintGCD())')
        assert output[-1] == "[2, 3]"
