"""
Tests for array .mapBitMaskHigh() method - mask to keep only highest N bits (N = bit_length // 2).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskHigh:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskHigh_basic(self):
        output = self._run('print([15, 255, 7].mapBitMaskHigh())')
        # 15=1111 (4 bits, keep high 2) -> 1100=12; 255=11111111 (8 bits, keep high 4) -> 11110000=240; 7=111 (3 bits, keep high 1) -> 100=4
        assert output[-1] == '[12, 240, 4]'

    def test_mapBitMaskHigh_single_bit(self):
        output = self._run('print([1, 2, 3].mapBitMaskHigh())')
        # 1=1 (1 bit, keep 0) -> 0; 2=10 (2 bits, keep 1) -> 10=2; 3=11 (2 bits, keep 1) -> 10=2
        assert output[-1] == '[0, 2, 2]'
