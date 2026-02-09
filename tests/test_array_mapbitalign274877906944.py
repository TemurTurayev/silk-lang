"""
Tests for array .mapBitAlign274877906944() method - align up to nearest multiple of 274877906944.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign274877906944:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign274877906944_basic(self):
        output = self._run('print([0, 1, 137438953471, 137438953472, 274877906944].mapBitAlign274877906944())')
        assert output[-1] == '[0, 274877906944, 274877906944, 274877906944, 274877906944]'

    def test_mapBitAlign274877906944_exact(self):
        output = self._run('print([549755813888, 824633720832].mapBitAlign274877906944())')
        assert output[-1] == '[549755813888, 824633720832]'
