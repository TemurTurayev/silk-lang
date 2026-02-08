"""
Tests for array .mapNibbleSwap() method - swap high and low nibbles of each byte.
"""

from silk.interpreter import Interpreter


class TestArrayMapNibbleSwap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapNibbleSwap_basic(self):
        output = self._run('print([18, 171, 240].mapNibbleSwap())')
        # 18=0x12->0x21=33, 171=0xAB->0xBA=186, 240=0xF0->0x0F=15
        assert output[-1] == '[33, 186, 15]'

    def test_mapNibbleSwap_zeros(self):
        output = self._run('print([0, 255, 16].mapNibbleSwap())')
        # 0->0, 255=0xFF->0xFF=255, 16=0x10->0x01=1
        assert output[-1] == '[0, 255, 1]'
