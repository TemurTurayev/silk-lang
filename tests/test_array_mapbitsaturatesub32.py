"""
Tests for array .mapBitSaturateSub32() method - saturating subtract with next element (clamped to 0, 32-bit).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateSub32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateSub32_basic(self):
        output = self._run('print([100, 200, 50].mapBitSaturateSub32())')
        # 100-200=-100->0; 200-50=150
        assert output[-1] == '[0, 150]'

    def test_mapBitSaturateSub32_no_underflow(self):
        output = self._run('print([1000, 500, 300].mapBitSaturateSub32())')
        # 1000-500=500; 500-300=200
        assert output[-1] == '[500, 200]'
