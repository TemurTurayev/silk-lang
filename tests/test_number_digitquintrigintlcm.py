"""
Tests for number .digitQuintrigintLCM() method - LCM of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintLCM_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintLCM())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222222222226.digitQuintrigintLCM())')
        assert output[-1] == "[2, 6]"
