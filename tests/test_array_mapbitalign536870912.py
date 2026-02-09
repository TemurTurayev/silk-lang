"""
Tests for array .mapBitAlign536870912() method - align up to nearest multiple of 536870912.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign536870912:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign536870912_basic(self):
        output = self._run('print([0, 1, 268435455, 268435456, 536870912].mapBitAlign536870912())')
        assert output[-1] == '[0, 536870912, 536870912, 536870912, 536870912]'

    def test_mapBitAlign536870912_exact(self):
        output = self._run('print([1073741824, 1610612736].mapBitAlign536870912())')
        assert output[-1] == '[1073741824, 1610612736]'
