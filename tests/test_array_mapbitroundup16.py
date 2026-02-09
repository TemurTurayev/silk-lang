"""
Tests for array .mapBitRoundUp16() method - round up to nearest multiple of 16.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp16_basic(self):
        output = self._run('print([1, 16, 17, 31].mapBitRoundUp16())')
        # 1->16, 16->16, 17->32, 31->32
        assert output[-1] == '[16, 16, 32, 32]'

    def test_mapBitRoundUp16_zero(self):
        output = self._run('print([0, 32, 48].mapBitRoundUp16())')
        assert output[-1] == '[0, 32, 48]'
