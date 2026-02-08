"""
Tests for array .mapBitMaskOdd() method - keep only odd-position bits (bits 1,3,5,...).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskOdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskOdd_basic(self):
        output = self._run('print([255, 15, 170].mapBitMaskOdd())')
        # 255=11111111 & 10101010=170; 15=1111 & 1010=10; 170=10101010 & 10101010=170
        assert output[-1] == '[170, 10, 170]'

    def test_mapBitMaskOdd_simple(self):
        output = self._run('print([1, 2, 3, 4].mapBitMaskOdd())')
        # 1=01 & 10=0; 2=10 & 10=2; 3=11 & 10=2; 4=100 & 010=0 (wait, 0xAA mask)
        # mask=0xAAAAAAAA=...10101010
        # 1 & mask=0; 2 & mask=2; 3 & mask=2; 4 & mask=0
        assert output[-1] == '[0, 2, 2, 0]'
