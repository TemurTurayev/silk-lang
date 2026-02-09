"""
Tests for number .digitQuadragintLCM() method - LCM of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintLCM_basic(self):
        output = self._run('print(3333333333333333333333333333333333333333.digitQuadragintLCM())')
        assert output[-1] == "[3]"

    def test_digitQuadragintLCM_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222226.digitQuadragintLCM())')
        assert output[-1] == "[2, 6]"
