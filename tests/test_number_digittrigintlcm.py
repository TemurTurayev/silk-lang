"""
Tests for number .digitTrigintLCM() method - LCM of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintLCM_basic(self):
        output = self._run('print(333333333333333333333333333333.digitTrigintLCM())')
        assert output[-1] == "[3]"

    def test_digitTrigintLCM_remainder(self):
        output = self._run('print(3333333333333333333333333333336.digitTrigintLCM())')
        assert output[-1] == "[3, 6]"
