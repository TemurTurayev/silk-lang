"""
Tests for array .mapBitLowestBit() method - position of lowest set bit (0-indexed).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitLowestBit:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitLowestBit_basic(self):
        output = self._run('print([6, 12, 10].mapBitLowestBit())')
        # 6=110 -> bit 1; 12=1100 -> bit 2; 10=1010 -> bit 1
        assert output[-1] == '[1, 2, 1]'

    def test_mapBitLowestBit_edge(self):
        output = self._run('print([1, 2, 4, 8].mapBitLowestBit())')
        # 1->0; 2->1; 4->2; 8->3
        assert output[-1] == '[0, 1, 2, 3]'
