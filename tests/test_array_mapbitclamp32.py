"""
Tests for array .mapBitClamp32() method - clamp each element to 0-4294967295 range.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitClamp32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitClamp32_basic(self):
        output = self._run('print([5000000000, 100, -5].mapBitClamp32())')
        assert output[-1] == '[4294967295, 100, 0]'

    def test_mapBitClamp32_all_in_range(self):
        output = self._run('print([0, 1000000, 4294967295].mapBitClamp32())')
        assert output[-1] == '[0, 1000000, 4294967295]'
