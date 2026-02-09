"""
Tests for array .mapBitAlign128() method - align up to nearest multiple of 128.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign128:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign128_basic(self):
        output = self._run('print([1, 127, 128, 129, 255, 256].mapBitAlign128())')
        # 1->128, 127->128, 128->128, 129->256, 255->256, 256->256
        assert output[-1] == '[128, 128, 128, 256, 256, 256]'

    def test_mapBitAlign128_zero(self):
        output = self._run('print([0, 384, 512].mapBitAlign128())')
        assert output[-1] == '[0, 384, 512]'
