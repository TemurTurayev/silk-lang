"""
Tests for array .mapBitSaturateSub8() method - saturating subtract with next element (clamped to 0).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateSub8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateSub8_basic(self):
        output = self._run('print([200, 50, 100, 150].mapBitSaturateSub8())')
        # 200-50=150; 50-100=-50->0(sat); 100-150=-50->0(sat)
        assert output[-1] == '[150, 0, 0]'

    def test_mapBitSaturateSub8_no_underflow(self):
        output = self._run('print([10, 3, 2].mapBitSaturateSub8())')
        # 10-3=7; 3-2=1
        assert output[-1] == '[7, 1]'
