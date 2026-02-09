"""
Tests for number .digitDuodetrigintAvg() method - average of each consecutive 28-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDuodetrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDuodetrigintAvg_basic(self):
        output = self._run('print(1111111111111111111111111111.digitDuodetrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitDuodetrigintAvg_remainder(self):
        output = self._run('print(11111111111111111111111111119.digitDuodetrigintAvg())')
        assert output[-1] == "[1, 9]"
