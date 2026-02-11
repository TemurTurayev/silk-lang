"""
Tests for number .digitSexquadragintProduct() method - product of each consecutive 46-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitSexquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitSexquadragintProduct_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111111111.digitSexquadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitSexquadragintProduct_remainder(self):
        output = self._run('print(11111111111111111111111111111111111111111111112.digitSexquadragintProduct())')
        assert output[-1] == "[1, 2]"
