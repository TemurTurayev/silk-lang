"""
Tests for array .mapBitAlign18889465931478580854784() method - align up to nearest multiple of 18889465931478580854784.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign18889465931478580854784:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign18889465931478580854784_basic(self):
        output = self._run('print([0, 1, 9444732965739290427391, 9444732965739290427392, 18889465931478580854784].mapBitAlign18889465931478580854784())')
        assert output[-1] == '[0, 18889465931478580854784, 18889465931478580854784, 18889465931478580854784, 18889465931478580854784]'

    def test_mapBitAlign18889465931478580854784_exact(self):
        output = self._run('print([37778931862957161709568, 56668397794435742564352].mapBitAlign18889465931478580854784())')
        assert output[-1] == '[37778931862957161709568, 56668397794435742564352]'
