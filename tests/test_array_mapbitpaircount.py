"""
Tests for array .mapBitPairCount() method - count number of 1-bit pairs (consecutive 11) in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitPairCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitPairCount_basic(self):
        output = self._run('print([7, 5, 15].mapBitPairCount())')
        # 7=111 -> pairs: 11,11 -> 2, 5=101 -> no consecutive 11 -> 0, 15=1111 -> 11,11,11 -> 3
        assert output[-1] == '[2, 0, 3]'

    def test_mapBitPairCount_values(self):
        output = self._run('print([0, 3, 255].mapBitPairCount())')
        # 0->0, 3=11->1, 255=11111111->7
        assert output[-1] == '[0, 1, 7]'
