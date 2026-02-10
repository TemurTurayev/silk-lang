"""
Tests for number .digitDuoquadragintLCM() method - LCM of each consecutive 42-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuoquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuoquadragintLCM_basic(self):
        output = self._run('print(333333333333333333333333333333333333333333.digitDuoquadragintLCM())')
        assert output[-1] == "[3]"

    def test_digitDuoquadragintLCM_remainder(self):
        output = self._run('print(3333333333333333333333333333333333333333336.digitDuoquadragintLCM())')
        assert output[-1] == "[3, 6]"
