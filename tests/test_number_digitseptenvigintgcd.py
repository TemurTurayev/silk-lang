"""
Tests for number .digitSeptenvigintGCD() method - GCD of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintGCD_basic(self):
        output = self._run('print(222222222222222222222222222.digitSeptenvigintGCD())')
        assert output[-1] == "[2]"

    def test_digitSeptenvigintGCD_remainder(self):
        output = self._run('print(3333333333333333333333333336.digitSeptenvigintGCD())')
        assert output[-1] == "[3, 6]"
