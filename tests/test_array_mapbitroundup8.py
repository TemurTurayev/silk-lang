"""
Tests for array .mapBitRoundUp8() method - round up to nearest multiple of 8.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp8_basic(self):
        output = self._run('print([1, 8, 9, 15].mapBitRoundUp8())')
        # 1->8, 8->8, 9->16, 15->16
        assert output[-1] == '[8, 8, 16, 16]'

    def test_mapBitRoundUp8_zero(self):
        output = self._run('print([0, 16, 24].mapBitRoundUp8())')
        # 0->0, 16->16, 24->24
        assert output[-1] == '[0, 16, 24]'
