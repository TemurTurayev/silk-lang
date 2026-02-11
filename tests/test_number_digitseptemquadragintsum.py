"""
Tests for number .digitSeptemquadragintSum() method - sum of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintSum_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintSum())')
        assert output[-1] == "[47]"

    def test_digitSeptemquadragintSum_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111111119.digitSeptemquadragintSum())')
        assert output[-1] == "[47, 9]"
