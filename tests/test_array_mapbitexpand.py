"""
Tests for array .mapBitExpand() method - expand each number to array of its bit positions.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitExpand:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitExpand_basic(self):
        output = self._run('print([5, 3, 8].mapBitExpand())')
        # 5=101 -> bits at positions 0,2 -> [0,2]; 3=11 -> [0,1]; 8=1000 -> [3]
        assert output[-1] == '[[0, 2], [0, 1], [3]]'

    def test_mapBitExpand_single(self):
        output = self._run('print([0, 1, 7].mapBitExpand())')
        # 0 -> [], 1=1 -> [0], 7=111 -> [0,1,2]
        assert output[-1] == '[[], [0], [0, 1, 2]]'
