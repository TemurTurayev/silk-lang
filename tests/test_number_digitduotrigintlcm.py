"""
Tests for number .digitDuotrigintLCM() method - LCM of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintLCM_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintLCM())')
        assert output[-1] == "[2]"

    def test_digitDuotrigintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222222223.digitDuotrigintLCM())')
        assert output[-1] == "[2, 3]"
