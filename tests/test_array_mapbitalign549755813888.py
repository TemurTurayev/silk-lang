"""
Tests for array .mapBitAlign549755813888() method - align up to nearest multiple of 549755813888.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign549755813888:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign549755813888_basic(self):
        output = self._run('print([0, 1, 274877906943, 274877906944, 549755813888].mapBitAlign549755813888())')
        assert output[-1] == '[0, 549755813888, 549755813888, 549755813888, 549755813888]'

    def test_mapBitAlign549755813888_exact(self):
        output = self._run('print([1099511627776, 1649267441664].mapBitAlign549755813888())')
        assert output[-1] == '[1099511627776, 1649267441664]'
