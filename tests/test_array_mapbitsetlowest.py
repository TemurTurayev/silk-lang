"""
Tests for array .mapBitSetLowest() method - set lowest unset bit (x | (x+1)).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSetLowest:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSetLowest_basic(self):
        output = self._run('print([5, 6, 9].mapBitSetLowest())')
        # 5=101 -> 101|110=111=7; 6=110 -> 110|111=111=7; 9=1001 -> 1001|1010=1011=11
        assert output[-1] == '[7, 7, 11]'

    def test_mapBitSetLowest_edge(self):
        output = self._run('print([0, 1, 3, 7].mapBitSetLowest())')
        # 0->0|1=1; 1=1->1|10=11=3; 3=11->11|100=111=7; 7=111->111|1000=1111=15
        assert output[-1] == '[1, 3, 7, 15]'
