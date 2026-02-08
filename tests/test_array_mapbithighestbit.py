"""
Tests for array .mapBitHighestBit() method - value of the highest set bit.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitHighestBit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitHighestBit_basic(self):
        output = self._run('print([5, 6, 7, 9].mapBitHighestBit())')
        # 5=101 -> 4; 6=110 -> 4; 7=111 -> 4; 9=1001 -> 8
        assert output[-1] == '[4, 4, 4, 8]'

    def test_mapBitHighestBit_edge(self):
        output = self._run('print([0, 1, 2, 3, 16].mapBitHighestBit())')
        # 0->0; 1->1; 2->2; 3->2; 16->16
        assert output[-1] == '[0, 1, 2, 2, 16]'
