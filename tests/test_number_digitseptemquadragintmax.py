"""
Tests for number .digitSeptemquadragintMax() method - max of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintMax_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintMax())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintMax_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111111119.digitSeptemquadragintMax())')
        assert output[-1] == "[1, 9]"
