"""
Tests for number .digitTrigintAvg() method - average of each consecutive 30-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitTrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitTrigintAvg_basic(self):
        output = self._run('print(111111111111111111111111111111.digitTrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitTrigintAvg_remainder(self):
        output = self._run('print(1111111111111111111111111111119.digitTrigintAvg())')
        assert output[-1] == "[1, 9]"
