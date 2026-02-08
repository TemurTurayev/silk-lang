"""
Tests for array .mapBitMask(n) method - mask each element to n lowest bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMask:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMask_basic(self):
        output = self._run('print([255, 170, 100].mapBitMask(4))')
        # 255 & 0xF = 15, 170 & 0xF = 10, 100 & 0xF = 4
        assert output[-1] == '[15, 10, 4]'

    def test_mapBitMask_three_bits(self):
        output = self._run('print([7, 15, 255].mapBitMask(3))')
        # 7 & 7 = 7, 15 & 7 = 7, 255 & 7 = 7
        assert output[-1] == '[7, 7, 7]'
