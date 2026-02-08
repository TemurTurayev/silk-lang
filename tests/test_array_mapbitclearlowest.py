"""
Tests for array .mapBitClearLowest() method - clear the lowest set bit (x & (x-1)).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitClearLowest:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitClearLowest_basic(self):
        output = self._run('print([6, 12, 10].mapBitClearLowest())')
        # 6=110 -> 100=4; 12=1100 -> 1000=8; 10=1010 -> 1000=8
        assert output[-1] == '[4, 8, 8]'

    def test_mapBitClearLowest_edge(self):
        output = self._run('print([0, 1, 7, 8].mapBitClearLowest())')
        # 0->0; 1->0; 7=111->110=6; 8=1000->0
        assert output[-1] == '[0, 0, 6, 0]'
