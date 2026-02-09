"""
Tests for array .mapBitAlign8192() method - align up to nearest multiple of 8192.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign8192:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign8192_basic(self):
        output = self._run('print([1, 8191, 8192, 8193].mapBitAlign8192())')
        # 1->8192, 8191->8192, 8192->8192, 8193->16384
        assert output[-1] == '[8192, 8192, 8192, 16384]'

    def test_mapBitAlign8192_zero(self):
        output = self._run('print([0, 16384, 24576].mapBitAlign8192())')
        assert output[-1] == '[0, 16384, 24576]'
