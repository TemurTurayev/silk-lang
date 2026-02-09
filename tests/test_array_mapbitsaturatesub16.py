"""
Tests for array .mapBitSaturateSub16() method - saturating subtract with next element (clamped to 0).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateSub16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateSub16_basic(self):
        output = self._run('print([100, 200, 50].mapBitSaturateSub16())')
        # 100-200 = -100 -> 0 (clamped); 200-50=150
        assert output[-1] == '[0, 150]'

    def test_mapBitSaturateSub16_no_underflow(self):
        output = self._run('print([500, 100, 200].mapBitSaturateSub16())')
        # 500-100=400; 100-200=-100->0
        assert output[-1] == '[400, 0]'
