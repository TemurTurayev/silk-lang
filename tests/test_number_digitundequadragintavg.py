"""
Tests for number .digitUndequadragintAvg() method - average of each consecutive 39-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndequadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndequadragintAvg_basic(self):
        output = self._run('print(111111111111111111111111111111111111111.digitUndequadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitUndequadragintAvg_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111115.digitUndequadragintAvg())')
        assert output[-1] == "[1, 5]"
