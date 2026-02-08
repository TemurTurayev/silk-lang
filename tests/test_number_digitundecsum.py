"""
Tests for number .digitUndecSum() method - sum of each consecutive 11-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndecSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndecSum_basic(self):
        output = self._run('print(1234567891012345678910.digitUndecSum())')
        # [1+2+3+4+5+6+7+8+9+1+0=46, 1+2+3+4+5+6+7+8+9+1+0=46]
        assert output[-1] == "[46, 46]"

    def test_digitUndecSum_remainder(self):
        output = self._run('print(1234567891012.digitUndecSum())')
        # [1+2+3+4+5+6+7+8+9+1+0=46, 1+2=3]
        assert output[-1] == "[46, 3]"
