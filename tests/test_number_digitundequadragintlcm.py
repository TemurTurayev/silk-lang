"""
Tests for number .digitUndequadragintLCM() method - LCM of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintLCM_basic(self):
        output = self._run('print(222222222222222222222222222222222222222.digitUndequadragintLCM())')
        assert output[-1] == "[2]"

    def test_digitUndequadragintLCM_remainder(self):
        output = self._run('print(2222222222222222222222222222222222222223.digitUndequadragintLCM())')
        assert output[-1] == "[2, 3]"
