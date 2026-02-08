"""
Tests for array .mapBitSwapNibbles() method - swap low and high nibbles of each byte.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSwapNibbles:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSwapNibbles_basic(self):
        output = self._run('print([171, 18, 255].mapBitSwapNibbles())')
        # 171=0xAB -> 0xBA=186; 18=0x12 -> 0x21=33; 255=0xFF -> 0xFF=255
        assert output[-1] == '[186, 33, 255]'

    def test_mapBitSwapNibbles_small(self):
        output = self._run('print([0, 1, 15, 16].mapBitSwapNibbles())')
        # 0->0; 1=0x01->0x10=16; 15=0x0F->0xF0=240; 16=0x10->0x01=1
        assert output[-1] == '[0, 16, 240, 1]'
