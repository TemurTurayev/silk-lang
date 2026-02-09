"""
Tests for array .mapBitSaturateAdd32() method - saturating add with next element (clamped to 4294967295).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateAdd32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateAdd32_basic(self):
        output = self._run('print([4294967290, 100, 50].mapBitSaturateAdd32())')
        # 4294967290+100=4294967390->4294967295(sat); 100+50=150
        assert output[-1] == '[4294967295, 150]'

    def test_mapBitSaturateAdd32_no_overflow(self):
        output = self._run('print([100, 200, 300].mapBitSaturateAdd32())')
        # 100+200=300; 200+300=500
        assert output[-1] == '[300, 500]'
