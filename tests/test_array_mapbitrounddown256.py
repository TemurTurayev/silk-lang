"""
Tests for array .mapBitRoundDown256() method - round down to nearest multiple of 256.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown256_basic(self):
        output = self._run('print([255, 256, 257, 511].mapBitRoundDown256())')
        # 255->0, 256->256, 257->256, 511->256
        assert output[-1] == '[0, 256, 256, 256]'

    def test_mapBitRoundDown256_exact(self):
        output = self._run('print([0, 512, 768, 1024].mapBitRoundDown256())')
        assert output[-1] == '[0, 512, 768, 1024]'
