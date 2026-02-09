"""
Tests for array .mapBitRoundNearest512() method - round to nearest multiple of 512.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest512:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest512_basic(self):
        output = self._run('print([1, 255, 256, 257, 512, 768].mapBitRoundNearest512())')
        assert output[-1] == '[0, 0, 512, 512, 512, 1024]'

    def test_mapBitRoundNearest512_exact(self):
        output = self._run('print([0, 1024, 1536].mapBitRoundNearest512())')
        assert output[-1] == '[0, 1024, 1536]'
