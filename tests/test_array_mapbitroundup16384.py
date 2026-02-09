"""
Tests for array .mapBitRoundUp16384() method - round up to next multiple of 16384.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp16384:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp16384_basic(self):
        output = self._run('print([0, 1, 16383, 16384, 16385].mapBitRoundUp16384())')
        assert output[-1] == '[0, 16384, 16384, 16384, 32768]'

    def test_mapBitRoundUp16384_exact(self):
        output = self._run('print([32768, 49152].mapBitRoundUp16384())')
        assert output[-1] == '[32768, 49152]'
