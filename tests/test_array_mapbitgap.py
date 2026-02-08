"""
Tests for array .mapBitGap() method - max gap between consecutive set bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitGap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitGap_basic(self):
        output = self._run('print([5, 9, 7].mapBitGap())')
        # 5=101 -> gap of 1 between pos 0 and 2 -> 2; 9=1001 -> gap of 2 between pos 0 and 3 -> 3; 7=111 -> consecutive -> 1
        assert output[-1] == '[2, 3, 1]'

    def test_mapBitGap_single(self):
        output = self._run('print([0, 1, 3].mapBitGap())')
        # 0 -> 0, 1=1 -> only one bit -> 0, 3=11 -> consecutive -> 1
        assert output[-1] == '[0, 0, 1]'
