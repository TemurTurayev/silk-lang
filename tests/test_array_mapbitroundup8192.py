"""
Tests for array .mapBitRoundUp8192() method - round up to nearest multiple of 8192.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp8192:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp8192_basic(self):
        output = self._run('print([1, 8191, 8192, 8193].mapBitRoundUp8192())')
        assert output[-1] == '[8192, 8192, 8192, 16384]'

    def test_mapBitRoundUp8192_zero(self):
        output = self._run('print([0, 16384].mapBitRoundUp8192())')
        assert output[-1] == '[0, 16384]'
