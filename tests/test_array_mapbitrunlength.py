"""
Tests for array .mapBitRunLength() method - longest run of 1s in binary representation.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRunLength:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRunLength_basic(self):
        output = self._run('print([7, 5, 15].mapBitRunLength())')
        # 7=111->3, 5=101->1, 15=1111->4
        assert output[-1] == '[3, 1, 4]'

    def test_mapBitRunLength_values(self):
        output = self._run('print([0, 1, 255].mapBitRunLength())')
        # 0->0, 1=1->1, 255=11111111->8
        assert output[-1] == '[0, 1, 8]'
