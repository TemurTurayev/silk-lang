"""
Tests for array .mapDigitProduct() method - product of digits of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDigitProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDigitProduct_basic(self):
        output = self._run('print([12, 34, 23].mapDigitProduct())')
        assert output[-1] == "[2, 12, 6]"

    def test_mapDigitProduct_withZero(self):
        output = self._run('print([10, 5, 99].mapDigitProduct())')
        assert output[-1] == "[0, 5, 81]"
