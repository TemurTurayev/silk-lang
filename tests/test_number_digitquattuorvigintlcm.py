"""
Tests for number .digitQuattuorvigintLCM() method - LCM of each consecutive 24-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuorvigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuorvigintLCM_basic(self):
        output = self._run('print(111111111111111111111111.digitQuattuorvigintLCM())')
        assert output[-1] == "[1]"

    def test_digitQuattuorvigintLCM_remainder(self):
        output = self._run('print(2222222222222222222222226.digitQuattuorvigintLCM())')
        assert output[-1] == "[2, 6]"
