"""
Tests for number .digitDuodetrigintLCM() method - LCM of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintLCM_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintLCM())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222223.digitDuodetrigintLCM())')
        assert output[-1] == "[2, 3]"
