"""
Tests for number .digitQuinvigintLCM() method - LCM of each consecutive 25-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinvigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinvigintLCM_basic(self):
        output = self._run('print(1111111111111111111111111.digitQuinvigintLCM())')
        assert output[-1] == "[1]"

    def test_digitQuinvigintLCM_remainder(self):
        output = self._run('print(22222222222222222222222226.digitQuinvigintLCM())')
        assert output[-1] == "[2, 6]"
