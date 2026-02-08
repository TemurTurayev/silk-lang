"""
Tests for array .mapBitCompress() method - remove zero bits, pack remaining 1s.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCompress:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCompress_basic(self):
        output = self._run('print([5, 3, 10].mapBitCompress())')
        # 5=101 -> 2 ones -> 11=3, 3=11 -> 2 ones -> 11=3, 10=1010 -> 2 ones -> 11=3
        assert output[-1] == '[3, 3, 3]'

    def test_mapBitCompress_single(self):
        output = self._run('print([0, 1, 7, 15].mapBitCompress())')
        # 0->0 ones->0, 1->1 one->1, 7=111->3 ones->111=7, 15=1111->4 ones->1111=15
        assert output[-1] == '[0, 1, 7, 15]'
