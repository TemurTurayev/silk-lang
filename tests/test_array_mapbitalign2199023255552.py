"""
Tests for array .mapBitAlign2199023255552() method - align up to nearest multiple of 2199023255552.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2199023255552:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2199023255552_basic(self):
        output = self._run('print([0, 1, 1099511627775, 1099511627776, 2199023255552].mapBitAlign2199023255552())')
        assert output[-1] == '[0, 2199023255552, 2199023255552, 2199023255552, 2199023255552]'

    def test_mapBitAlign2199023255552_exact(self):
        output = self._run('print([4398046511104, 6597069766656].mapBitAlign2199023255552())')
        assert output[-1] == '[4398046511104, 6597069766656]'
