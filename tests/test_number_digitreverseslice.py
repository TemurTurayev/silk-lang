"""
Tests for number .digitReverseSlice() method - get digits in reverse order.
"""

from silk.interpreter import Interpreter


class TestNumberDigitReverseSlice:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitReverseSlice_basic(self):
        output = self._run('print(12345.digitReverseSlice())')
        assert output[-1] == "[5, 4, 3, 2, 1]"

    def test_digitReverseSlice_short(self):
        output = self._run('print(89.digitReverseSlice())')
        assert output[-1] == "[9, 8]"
