"""
Tests for array .mapBitRoundDown128() method - round down to nearest multiple of 128.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown128:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown128_basic(self):
        output = self._run('print([127, 128, 129, 255].mapBitRoundDown128())')
        # 127->0, 128->128, 129->128, 255->128
        assert output[-1] == '[0, 128, 128, 128]'

    def test_mapBitRoundDown128_exact(self):
        output = self._run('print([0, 256, 384, 512].mapBitRoundDown128())')
        assert output[-1] == '[0, 256, 384, 512]'
