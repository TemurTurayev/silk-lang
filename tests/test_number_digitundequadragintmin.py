"""
Tests for number .digitUndequadragintMin() method - min of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintMin_basic(self):
        output = self._run('print(111111111111111111111111111111111111111.digitUndequadragintMin())')
        assert output[-1] == "[1]"

    def test_digitUndequadragintMin_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111115.digitUndequadragintMin())')
        assert output[-1] == "[1, 5]"
