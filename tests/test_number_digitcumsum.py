"""
Tests for number .digitCumSum() method - cumulative sum of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitCumSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitCumSum_basic(self):
        output = self._run('print(1234.digitCumSum())')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_digitCumSum_single(self):
        output = self._run('print(5.digitCumSum())')
        assert output[-1] == "[5]"
