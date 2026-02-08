"""
Tests for array .mapBitSet(bit) method - set specific bit to 1 in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSet:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSet_bit0(self):
        output = self._run('print([4, 6, 0].mapBitSet(0))')
        # 4|1=5, 6|1=7, 0|1=1
        assert output[-1] == '[5, 7, 1]'

    def test_mapBitSet_bit3(self):
        output = self._run('print([0, 1, 7].mapBitSet(3))')
        # 0|8=8, 1|8=9, 7|8=15
        assert output[-1] == '[8, 9, 15]'
