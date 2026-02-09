"""
Tests for number .digitDuotrigintAvg() method - average of each consecutive 32-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuotrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuotrigintAvg_basic(self):
        output = self._run('print(22222222222222222222222222222222.digitDuotrigintAvg())')
        assert output[-1] == "[2]"

    def test_digitDuotrigintAvg_remainder(self):
        output = self._run('print(222222222222222222222222222222229.digitDuotrigintAvg())')
        assert output[-1] == "[2, 9]"
