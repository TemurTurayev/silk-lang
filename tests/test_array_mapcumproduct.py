"""
Tests for array .mapCumProduct() method - cumulative product of elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapCumProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCumProduct_basic(self):
        output = self._run('print([1, 2, 3, 4].mapCumProduct())')
        assert output[-1] == "[1, 2, 6, 24]"

    def test_mapCumProduct_single(self):
        output = self._run('print([5].mapCumProduct())')
        assert output[-1] == "[5]"
