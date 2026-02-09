"""
Tests for array .mapBitRoundNearest8192() method - round to nearest multiple of 8192.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest8192:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest8192_basic(self):
        output = self._run('print([1, 4095, 4096, 4097, 8192, 12288].mapBitRoundNearest8192())')
        assert output[-1] == '[0, 0, 8192, 8192, 8192, 16384]'

    def test_mapBitRoundNearest8192_exact(self):
        output = self._run('print([0, 16384, 24576].mapBitRoundNearest8192())')
        assert output[-1] == '[0, 16384, 24576]'
