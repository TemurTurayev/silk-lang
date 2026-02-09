"""
Tests for number .digitTretrigintLCM() method - LCM of each consecutive 33-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTretrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTretrigintLCM_basic(self):
        output = self._run('print(222222222222222222222222222222222.digitTretrigintLCM())')
        assert output[-1] == "[2]"

    def test_digitTretrigintLCM_remainder(self):
        output = self._run('print(2222222222222222222222222222222226.digitTretrigintLCM())')
        assert output[-1] == "[2, 6]"
