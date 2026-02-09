"""
Tests for number .digitQuattuortrigintGCD() method - GCD of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintGCD_basic(self):
        output = self._run('print(4444444444444444444444444444444444.digitQuattuortrigintGCD())')
        assert output[-1] == "[4]"

    def test_digitQuattuortrigintGCD_remainder(self):
        output = self._run('print(44444444444444444444444444444444446.digitQuattuortrigintGCD())')
        assert output[-1] == "[4, 6]"
