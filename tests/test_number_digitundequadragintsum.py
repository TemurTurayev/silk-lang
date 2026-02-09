"""
Tests for number .digitUndequadragintSum() method - sum of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintSum_basic(self):
        output = self._run('print(111111111111111111111111111111111111111.digitUndequadragintSum())')
        assert output[-1] == "[39]"

    def test_digitUndequadragintSum_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111115.digitUndequadragintSum())')
        assert output[-1] == "[39, 5]"
