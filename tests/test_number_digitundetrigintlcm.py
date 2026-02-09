"""
Tests for number .digitUndetrigintLCM() method - LCM of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintLCM_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintLCM())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintLCM_remainder(self):
        output = self._run('print(222222222222222222222222222223.digitUndetrigintLCM())')
        assert output[-1] == "[2, 3]"
