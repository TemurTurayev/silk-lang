"""
Tests for number .digitQuattuortrigintLCM() method - LCM of each consecutive 34-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuattuortrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuattuortrigintLCM_basic(self):
        output = self._run('print(2222222222222222222222222222222222.digitQuattuortrigintLCM())')
        assert output[-1] == "[2]"

    def test_digitQuattuortrigintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222222222226.digitQuattuortrigintLCM())')
        assert output[-1] == "[2, 6]"
