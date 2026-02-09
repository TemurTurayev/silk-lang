"""
Tests for number .digitSexvigintLCM() method - LCM of each consecutive 26-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexvigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexvigintLCM_basic(self):
        output = self._run('print(22222222222222222222222222.digitSexvigintLCM())')
        assert output[-1] == "[2]"

    def test_digitSexvigintLCM_remainder(self):
        output = self._run('print(333333333333333333333333336.digitSexvigintLCM())')
        assert output[-1] == "[3, 6]"
