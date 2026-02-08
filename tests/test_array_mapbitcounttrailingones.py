"""
Tests for array .mapBitCountTrailingOnes() method - count trailing 1-bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCountTrailingOnes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCountTrailingOnes_basic(self):
        output = self._run('print([7, 6, 5, 11].mapBitCountTrailingOnes())')
        # 7=111 -> 3; 6=110 -> 0; 5=101 -> 1; 11=1011 -> 2
        assert output[-1] == '[3, 0, 1, 2]'

    def test_mapBitCountTrailingOnes_edge(self):
        output = self._run('print([0, 1, 3, 15].mapBitCountTrailingOnes())')
        # 0->0; 1=1->1; 3=11->2; 15=1111->4
        assert output[-1] == '[0, 1, 2, 4]'
