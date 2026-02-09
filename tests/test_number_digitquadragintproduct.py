"""
Tests for number .digitQuadragintProduct() method - product of each consecutive 40-tuple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadragintProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadragintProduct_basic(self):
        output = self._run('print(1111111111111111111111111111111111111111.digitQuadragintProduct())')
        assert output[-1] == "[1]"

    def test_digitQuadragintProduct_remainder(self):
        output = self._run('print(22222222222222222222222222222222222222223.digitQuadragintProduct())')
        assert output[-1] == "[" + str(2**40) + ", 3]"
