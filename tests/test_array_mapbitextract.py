"""
Tests for array .mapBitExtract(bit) method - extract specific bit from each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitExtract:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitExtract_bit0(self):
        output = self._run('print([5, 4, 7, 2].mapBitExtract(0))')
        # 5=101->1, 4=100->0, 7=111->1, 2=10->0
        assert output[-1] == '[1, 0, 1, 0]'

    def test_mapBitExtract_bit2(self):
        output = self._run('print([4, 5, 6, 7].mapBitExtract(2))')
        # 4=100->1, 5=101->1, 6=110->1, 7=111->1
        assert output[-1] == '[1, 1, 1, 1]'
