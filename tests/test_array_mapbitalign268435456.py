"""
Tests for array .mapBitAlign268435456() method - align up to nearest multiple of 268435456.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign268435456:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign268435456_basic(self):
        output = self._run('print([0, 1, 134217727, 134217728, 268435456].mapBitAlign268435456())')
        assert output[-1] == '[0, 268435456, 268435456, 268435456, 268435456]'

    def test_mapBitAlign268435456_exact(self):
        output = self._run('print([536870912, 805306368].mapBitAlign268435456())')
        assert output[-1] == '[536870912, 805306368]'
