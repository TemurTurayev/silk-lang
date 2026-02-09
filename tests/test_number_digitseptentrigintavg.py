"""
Tests for number .digitSeptentrigintAvg() method - average of each consecutive 37-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptentrigintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptentrigintAvg_basic(self):
        output = self._run('print(1111111111111111111111111111111111111.digitSeptentrigintAvg())')
        assert output[-1] == "[1]"

    def test_digitSeptentrigintAvg_remainder(self):
        output = self._run('print(11111111111111111111111111111111111115.digitSeptentrigintAvg())')
        assert output[-1] == "[1, 5]"
