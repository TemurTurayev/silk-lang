"""
Tests for array .mapBitTest(bit) method - test if specific bit is set in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitTest:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitTest_bit0(self):
        output = self._run('print([5, 4, 7, 2].mapBitTest(0))')
        # 5&1=1->true, 4&1=0->false, 7&1=1->true, 2&1=0->false
        assert output[-1] == '[true, false, true, false]'

    def test_mapBitTest_bit2(self):
        output = self._run('print([3, 4, 5, 7].mapBitTest(2))')
        # 3&4=0->false, 4&4=4->true, 5&4=4->true, 7&4=4->true
        assert output[-1] == '[false, true, true, true]'
