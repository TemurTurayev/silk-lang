"""
Tests for array .mapBitToggle(bit) method - toggle specific bit in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitToggle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitToggle_bit0(self):
        output = self._run('print([4, 5, 0].mapBitToggle(0))')
        # 4^1=5, 5^1=4, 0^1=1
        assert output[-1] == '[5, 4, 1]'

    def test_mapBitToggle_bit3(self):
        output = self._run('print([0, 8, 15].mapBitToggle(3))')
        # 0^8=8, 8^8=0, 15^8=7
        assert output[-1] == '[8, 0, 7]'
