"""
Tests for array .mapBitCountLeadingOnes() method - count leading 1-bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCountLeadingOnes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCountLeadingOnes_basic(self):
        output = self._run('print([7, 6, 5, 15].mapBitCountLeadingOnes())')
        # 7=111 -> 3; 6=110 -> 2; 5=101 -> 1; 15=1111 -> 4
        assert output[-1] == '[3, 2, 1, 4]'

    def test_mapBitCountLeadingOnes_edge(self):
        output = self._run('print([0, 1, 2, 3].mapBitCountLeadingOnes())')
        # 0->0; 1=1->1; 2=10->1; 3=11->2
        assert output[-1] == '[0, 1, 1, 2]'
