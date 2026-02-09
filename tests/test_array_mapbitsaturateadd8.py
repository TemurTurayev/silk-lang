"""
Tests for array .mapBitSaturateAdd8() method - saturating add with next element (clamped to 255).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateAdd8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateAdd8_basic(self):
        output = self._run('print([100, 200, 50, 10].mapBitSaturateAdd8())')
        # 100+200=300->255(sat); 200+50=250; 50+10=60
        assert output[-1] == '[255, 250, 60]'

    def test_mapBitSaturateAdd8_no_overflow(self):
        output = self._run('print([1, 2, 3].mapBitSaturateAdd8())')
        # 1+2=3; 2+3=5
        assert output[-1] == '[3, 5]'
