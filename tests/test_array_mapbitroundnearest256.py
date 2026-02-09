"""
Tests for array .mapBitRoundNearest256() method - round to nearest multiple of 256.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest256_basic(self):
        output = self._run('print([1, 127, 128, 129, 256, 384].mapBitRoundNearest256())')
        assert output[-1] == '[0, 0, 256, 256, 256, 512]'

    def test_mapBitRoundNearest256_exact(self):
        output = self._run('print([0, 512, 768].mapBitRoundNearest256())')
        assert output[-1] == '[0, 512, 768]'
