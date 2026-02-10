"""
Tests for number .digitUnquadragintLCM() method - LCM of each consecutive 41-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUnquadragintLCM:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUnquadragintLCM_basic(self):
        output = self._run('print(33333333333333333333333333333333333333333.digitUnquadragintLCM())')
        assert output[-1] == "[3]"

    def test_digitUnquadragintLCM_remainder(self):
        output = self._run('print(333333333333333333333333333333333333333336.digitUnquadragintLCM())')
        assert output[-1] == "[3, 6]"
