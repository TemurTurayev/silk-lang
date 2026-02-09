"""
Tests for number .digitUndetrigintAvg() method - average of each consecutive 29-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitUndetrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitUndetrigintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111.digitUndetrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitUndetrigintAvg_remainder(self):
        output = self._run('print(111111111111111111111111111119.digitUndetrigintAvg())')
        assert output[-1] == "[1, 9]"
