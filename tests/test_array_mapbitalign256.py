"""
Tests for array .mapBitAlign256() method - align up to nearest multiple of 256.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign256_basic(self):
        output = self._run('print([1, 255, 256, 257, 511, 512].mapBitAlign256())')
        # 1->256, 255->256, 256->256, 257->512, 511->512, 512->512
        assert output[-1] == '[256, 256, 256, 512, 512, 512]'

    def test_mapBitAlign256_zero(self):
        output = self._run('print([0, 768, 1024].mapBitAlign256())')
        assert output[-1] == '[0, 768, 1024]'
