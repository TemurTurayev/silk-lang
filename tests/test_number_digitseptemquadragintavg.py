"""
Tests for number .digitSeptemquadragintAvg() method - average of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintAvg_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintAvg())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintAvg_remainder(self):
        output = self._run('print(222222222222222222222222222222222222222222222224.digitSeptemquadragintAvg())')
        assert output[-1] == "[2, 4]"
