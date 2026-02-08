"""
Tests for number .digitQuadProduct() method - product of each consecutive quadruple of digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitQuadProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitQuadProduct_basic(self):
        output = self._run('print(12345678.digitQuadProduct())')
        # [1*2*3*4=24, 5*6*7*8=1680]
        assert output[-1] == "[24, 1680]"

    def test_digitQuadProduct_remainder(self):
        output = self._run('print(123456.digitQuadProduct())')
        # [1*2*3*4=24, 5*6=30]
        assert output[-1] == "[24, 30]"
