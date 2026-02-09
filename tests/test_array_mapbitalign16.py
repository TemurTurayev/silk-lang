"""
Tests for array .mapBitAlign16() method - align up to nearest multiple of 16.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign16_basic(self):
        output = self._run('print([1, 15, 16, 17, 31, 32].mapBitAlign16())')
        # 1->16, 15->16, 16->16, 17->32, 31->32, 32->32
        assert output[-1] == '[16, 16, 16, 32, 32, 32]'

    def test_mapBitAlign16_zero(self):
        output = self._run('print([0, 48, 64].mapBitAlign16())')
        assert output[-1] == '[0, 48, 64]'
