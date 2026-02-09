"""
Tests for number .digitUntrigintLCM() method - LCM of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintLCM_basic(self):
        output = self._run('print(3333333333333333333333333333333.digitUntrigintLCM())')
        assert output[-1] == "[3]"

    def test_digitUntrigintLCM_remainder(self):
        output = self._run('print(33333333333333333333333333333336.digitUntrigintLCM())')
        assert output[-1] == "[3, 6]"
