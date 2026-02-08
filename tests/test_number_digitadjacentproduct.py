"""
Tests for number .digitAdjacentProduct() method - products of adjacent digit pairs.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAdjacentProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAdjacentProduct_basic(self):
        output = self._run('print(123.digitAdjacentProduct())')
        # (1*2), (2*3) = [2, 6]
        assert output[-1] == "[2, 6]"

    def test_digitAdjacentProduct_four(self):
        output = self._run('print(2345.digitAdjacentProduct())')
        # (2*3), (3*4), (4*5) = [6, 12, 20]
        assert output[-1] == "[6, 12, 20]"
