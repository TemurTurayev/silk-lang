"""
Tests for array .mapBitRoundNearest2048() method - round to nearest multiple of 2048.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest2048:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest2048_basic(self):
        output = self._run('print([1, 1023, 1024, 1025, 2048, 3072].mapBitRoundNearest2048())')
        assert output[-1] == '[0, 0, 2048, 2048, 2048, 4096]'

    def test_mapBitRoundNearest2048_exact(self):
        output = self._run('print([0, 4096, 6144].mapBitRoundNearest2048())')
        assert output[-1] == '[0, 4096, 6144]'
