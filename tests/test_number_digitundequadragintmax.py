"""
Tests for number .digitUndequadragintMax() method - max of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintMax_basic(self):
        output = self._run('print(111111111111111111111111111111111111111.digitUndequadragintMax())')
        assert output[-1] == "[1]"

    def test_digitUndequadragintMax_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111115.digitUndequadragintMax())')
        assert output[-1] == "[1, 5]"
