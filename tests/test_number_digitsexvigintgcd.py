"""
Tests for number .digitSexvigintGCD() method - GCD of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintGCD:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintGCD_basic(self):
        output = self._run('print(22222222222222222222222222.digitSexvigintGCD())')
        assert output[-1] == "[2]"

    def test_digitSexvigintGCD_remainder(self):
        output = self._run('print(333333333333333333333333336.digitSexvigintGCD())')
        assert output[-1] == "[3, 6]"
