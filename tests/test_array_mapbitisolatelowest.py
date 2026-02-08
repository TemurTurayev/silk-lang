"""
Tests for array .mapBitIsolateLowest() method - isolate lowest set bit (x & -x).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitIsolateLowest:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitIsolateLowest_basic(self):
        output = self._run('print([6, 12, 10].mapBitIsolateLowest())')
        # 6=110 -> lowest set bit = 2; 12=1100 -> 4; 10=1010 -> 2
        assert output[-1] == '[2, 4, 2]'

    def test_mapBitIsolateLowest_edge(self):
        output = self._run('print([0, 1, 7, 8].mapBitIsolateLowest())')
        # 0->0; 1->1; 7=111->1; 8=1000->8
        assert output[-1] == '[0, 1, 1, 8]'
