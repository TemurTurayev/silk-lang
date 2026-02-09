"""
Tests for number .digitSeptenvigintLCM() method - LCM of each consecutive 27-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptenvigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptenvigintLCM_basic(self):
        output = self._run('print(222222222222222222222222222.digitSeptenvigintLCM())')
        assert output[-1] == "[2]"

    def test_digitSeptenvigintLCM_remainder(self):
        output = self._run('print(3333333333333333333333333336.digitSeptenvigintLCM())')
        assert output[-1] == "[3, 6]"
