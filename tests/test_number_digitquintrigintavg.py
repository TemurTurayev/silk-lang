"""
Tests for number .digitQuintrigintAvg() method - average of each consecutive 35-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuintrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuintrigintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111111111.digitQuintrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitQuintrigintAvg_remainder(self):
        output = self._run('print(111111111111111111111111111111111115.digitQuintrigintAvg())')
        assert output[-1] == "[1, 5]"
