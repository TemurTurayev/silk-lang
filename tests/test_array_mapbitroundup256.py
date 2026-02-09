"""
Tests for array .mapBitRoundUp256() method - round up to nearest multiple of 256.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp256_basic(self):
        output = self._run('print([1, 256, 257, 511].mapBitRoundUp256())')
        # 1->256, 256->256, 257->512, 511->512
        assert output[-1] == '[256, 256, 512, 512]'

    def test_mapBitRoundUp256_zero(self):
        output = self._run('print([0, 512, 768].mapBitRoundUp256())')
        assert output[-1] == '[0, 512, 768]'
