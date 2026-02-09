"""
Tests for array .mapBitRoundNearest64() method - round to nearest multiple of 64.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest64_basic(self):
        output = self._run('print([1, 31, 32, 33, 64, 96].mapBitRoundNearest64())')
        assert output[-1] == '[0, 0, 64, 64, 64, 128]'

    def test_mapBitRoundNearest64_exact(self):
        output = self._run('print([0, 128, 192].mapBitRoundNearest64())')
        assert output[-1] == '[0, 128, 192]'
