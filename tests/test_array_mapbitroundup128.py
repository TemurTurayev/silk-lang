"""
Tests for array .mapBitRoundUp128() method - round up to nearest multiple of 128.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp128:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp128_basic(self):
        output = self._run('print([1, 128, 129, 255].mapBitRoundUp128())')
        # 1->128, 128->128, 129->256, 255->256
        assert output[-1] == '[128, 128, 256, 256]'

    def test_mapBitRoundUp128_zero(self):
        output = self._run('print([0, 256, 384].mapBitRoundUp128())')
        assert output[-1] == '[0, 256, 384]'
