"""
Tests for number .digitUntrigintAvg() method - average of each consecutive 31-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUntrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUntrigintAvg_basic(self):
        output = self._run('print(1111111111111111111111111111111.digitUntrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitUntrigintAvg_remainder(self):
        output = self._run('print(11111111111111111111111111111119.digitUntrigintAvg())')
        assert output[-1] == "[1, 9]"
