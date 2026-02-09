"""
Tests for array .mapBitRoundNearest1024() method - round to nearest multiple of 1024.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest1024:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest1024_basic(self):
        output = self._run('print([1, 511, 512, 513, 1024, 1536].mapBitRoundNearest1024())')
        assert output[-1] == '[0, 0, 1024, 1024, 1024, 2048]'

    def test_mapBitRoundNearest1024_exact(self):
        output = self._run('print([0, 2048, 3072].mapBitRoundNearest1024())')
        assert output[-1] == '[0, 2048, 3072]'
