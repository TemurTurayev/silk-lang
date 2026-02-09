"""
Tests for array .mapBitAlign37778931862957161709568() method - align up to nearest multiple of 37778931862957161709568.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign37778931862957161709568:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign37778931862957161709568_basic(self):
        output = self._run('print([0, 1, 18889465931478580854783, 18889465931478580854784, 37778931862957161709568].mapBitAlign37778931862957161709568())')
        assert output[-1] == '[0, 37778931862957161709568, 37778931862957161709568, 37778931862957161709568, 37778931862957161709568]'

    def test_mapBitAlign37778931862957161709568_exact(self):
        output = self._run('print([75557863725914323419136, 113336795588871485128704].mapBitAlign37778931862957161709568())')
        assert output[-1] == '[75557863725914323419136, 113336795588871485128704]'
