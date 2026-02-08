"""
Tests for array .mapBitBalance() method - difference between set and unset bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitBalance:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitBalance_basic(self):
        output = self._run('print([5, 7, 8].mapBitBalance())')
        # 5=101: 2 set, 1 unset -> 2-1=1; 7=111: 3 set, 0 unset -> 3; 8=1000: 1 set, 3 unset -> -2
        assert output[-1] == '[1, 3, -2]'

    def test_mapBitBalance_single(self):
        output = self._run('print([0, 1, 3, 15].mapBitBalance())')
        # 0->0, 1=1: 1-0=1, 3=11: 2-0=2, 15=1111: 4-0=4
        assert output[-1] == '[0, 1, 2, 4]'
