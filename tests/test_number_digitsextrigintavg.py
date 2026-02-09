"""
Tests for number .digitSextrigintAvg() method - average of each consecutive 36-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSextrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSextrigintAvg_basic(self):
        output = self._run('print(111111111111111111111111111111111111.digitSextrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitSextrigintAvg_remainder(self):
        output = self._run('print(1111111111111111111111111111111111115.digitSextrigintAvg())')
        assert output[-1] == "[1, 5]"
