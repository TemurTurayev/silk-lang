"""
Tests for array .mapBitRoundUp64() method - round up to nearest multiple of 64.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp64_basic(self):
        output = self._run('print([1, 64, 65, 127].mapBitRoundUp64())')
        # 1->64, 64->64, 65->128, 127->128
        assert output[-1] == '[64, 64, 128, 128]'

    def test_mapBitRoundUp64_zero(self):
        output = self._run('print([0, 128, 192].mapBitRoundUp64())')
        assert output[-1] == '[0, 128, 192]'
