"""
Tests for number .digitQuinquadragintProduct() method - product of each consecutive 45-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuinquadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuinquadragintProduct_basic(self):
        output = self._run('print(111111111111111111111111111111111111111111111.digitQuinquadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitQuinquadragintProduct_remainder(self):
        output = self._run('print(1111111111111111111111111111111111111111111112.digitQuinquadragintProduct())')
        assert output[-1] == "[1, 2]"
