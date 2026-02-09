"""
Tests for array .mapBitMaskByte() method - keep only the lowest byte (8 bits).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskByte:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskByte_basic(self):
        output = self._run('print([256, 511, 1023].mapBitMaskByte())')
        # 256 & 0xFF = 0; 511 & 0xFF = 255; 1023 & 0xFF = 255
        assert output[-1] == '[0, 255, 255]'

    def test_mapBitMaskByte_small(self):
        output = self._run('print([0, 127, 255, 300].mapBitMaskByte())')
        # 0&FF=0; 127&FF=127; 255&FF=255; 300&FF=44
        assert output[-1] == '[0, 127, 255, 44]'
