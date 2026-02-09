"""
Tests for array .mapBitRoundUp32() method - round up to nearest multiple of 32.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp32_basic(self):
        output = self._run('print([1, 32, 33, 63].mapBitRoundUp32())')
        # 1->32, 32->32, 33->64, 63->64
        assert output[-1] == '[32, 32, 64, 64]'

    def test_mapBitRoundUp32_zero(self):
        output = self._run('print([0, 64, 96].mapBitRoundUp32())')
        assert output[-1] == '[0, 64, 96]'
