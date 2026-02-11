"""
Tests for number .digitSeptemquadragintMin() method - min of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintMin_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintMin())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintMin_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111111119.digitSeptemquadragintMin())')
        assert output[-1] == "[1, 9]"
