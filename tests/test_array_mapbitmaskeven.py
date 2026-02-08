"""
Tests for array .mapBitMaskEven() method - keep only even-position bits (bits 0,2,4,...).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskEven_basic(self):
        output = self._run('print([255, 15, 85].mapBitMaskEven())')
        # 255=11111111 & 01010101=85; 15=1111 & 0101=5; 85=01010101 & 01010101=85
        assert output[-1] == '[85, 5, 85]'

    def test_mapBitMaskEven_simple(self):
        output = self._run('print([1, 2, 3, 4].mapBitMaskEven())')
        # mask=0x55555555=...01010101
        # 1 & mask=1; 2 & mask=0; 3 & mask=1; 4 & mask=4
        assert output[-1] == '[1, 0, 1, 4]'
