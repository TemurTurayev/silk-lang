"""
Tests for array .mapBitAlign32() method - align up to nearest multiple of 32.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign32_basic(self):
        output = self._run('print([1, 31, 32, 33, 63, 64].mapBitAlign32())')
        # 1->32, 31->32, 32->32, 33->64, 63->64, 64->64
        assert output[-1] == '[32, 32, 32, 64, 64, 64]'

    def test_mapBitAlign32_zero(self):
        output = self._run('print([0, 96, 128].mapBitAlign32())')
        assert output[-1] == '[0, 96, 128]'
