"""
Tests for array .mapBitMaskLow() method - mask to keep only lowest N bits (N = bit_length // 2).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskLow:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskLow_basic(self):
        output = self._run('print([15, 255, 7].mapBitMaskLow())')
        # 15=1111 (4 bits, keep 2) -> 11=3; 255=11111111 (8 bits, keep 4) -> 1111=15; 7=111 (3 bits, keep 1) -> 1=1
        assert output[-1] == '[3, 15, 1]'

    def test_mapBitMaskLow_powers(self):
        output = self._run('print([16, 64, 4].mapBitMaskLow())')
        # 16=10000 (5 bits, keep 2) -> 0; 64=1000000 (7 bits, keep 3) -> 0; 4=100 (3 bits, keep 1) -> 0
        assert output[-1] == '[0, 0, 0]'
