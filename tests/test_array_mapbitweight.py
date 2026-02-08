"""
Tests for array .mapBitWeight() method - sum of bit positions where bits are set.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitWeight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitWeight_basic(self):
        output = self._run('print([5, 3, 8].mapBitWeight())')
        # 5=101 -> positions 0,2 -> 0+2=2; 3=11 -> 0+1=1; 8=1000 -> 3
        assert output[-1] == '[2, 1, 3]'

    def test_mapBitWeight_single(self):
        output = self._run('print([0, 1, 7, 15].mapBitWeight())')
        # 0->0, 1=1->0, 7=111->0+1+2=3, 15=1111->0+1+2+3=6
        assert output[-1] == '[0, 0, 3, 6]'
