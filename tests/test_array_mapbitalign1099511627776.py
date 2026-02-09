"""
Tests for array .mapBitAlign1099511627776() method - align up to nearest multiple of 1099511627776.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1099511627776:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1099511627776_basic(self):
        output = self._run('print([0, 1, 549755813887, 549755813888, 1099511627776].mapBitAlign1099511627776())')
        assert output[-1] == '[0, 1099511627776, 1099511627776, 1099511627776, 1099511627776]'

    def test_mapBitAlign1099511627776_exact(self):
        output = self._run('print([2199023255552, 3298534883328].mapBitAlign1099511627776())')
        assert output[-1] == '[2199023255552, 3298534883328]'
