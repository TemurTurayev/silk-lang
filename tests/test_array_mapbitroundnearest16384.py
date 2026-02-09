"""
Tests for array .mapBitRoundNearest16384() method - round to nearest multiple of 16384.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest16384:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest16384_basic(self):
        output = self._run('print([1, 8191, 8192, 8193, 16384, 24576].mapBitRoundNearest16384())')
        assert output[-1] == '[0, 0, 16384, 16384, 16384, 32768]'

    def test_mapBitRoundNearest16384_exact(self):
        output = self._run('print([0, 32768, 49152].mapBitRoundNearest16384())')
        assert output[-1] == '[0, 32768, 49152]'
