"""
Tests for number .digitSeptemquadragintProduct() method - product of each consecutive 47-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSeptemquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSeptemquadragintProduct_basic(self):
        output = self._run('print(11111111111111111111111111111111111111111111111.digitSeptemquadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitSeptemquadragintProduct_remainder(self):
        output = self._run('print(111111111111111111111111111111111111111111111112.digitSeptemquadragintProduct())')
        assert output[-1] == "[1, 2]"
