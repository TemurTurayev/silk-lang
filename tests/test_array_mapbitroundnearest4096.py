"""
Tests for array .mapBitRoundNearest4096() method - round to nearest multiple of 4096.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest4096:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest4096_basic(self):
        output = self._run('print([1, 2047, 2048, 2049, 4096, 6144].mapBitRoundNearest4096())')
        assert output[-1] == '[0, 0, 4096, 4096, 4096, 8192]'

    def test_mapBitRoundNearest4096_exact(self):
        output = self._run('print([0, 8192, 12288].mapBitRoundNearest4096())')
        assert output[-1] == '[0, 8192, 12288]'
