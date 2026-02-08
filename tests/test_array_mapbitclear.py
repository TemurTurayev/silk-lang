"""
Tests for array .mapBitClear(bit) method - clear specific bit to 0 in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitClear:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitClear_bit0(self):
        output = self._run('print([5, 7, 4].mapBitClear(0))')
        # 5&~1=4, 7&~1=6, 4&~1=4
        assert output[-1] == '[4, 6, 4]'

    def test_mapBitClear_bit3(self):
        output = self._run('print([15, 9, 8].mapBitClear(3))')
        # 15&~8=7, 9&~8=1, 8&~8=0
        assert output[-1] == '[7, 1, 0]'
