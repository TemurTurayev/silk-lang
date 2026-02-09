"""
Tests for array .mapBitSaturateAdd16() method - saturating add with next element (clamped to 65535).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSaturateAdd16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSaturateAdd16_basic(self):
        output = self._run('print([60000, 10000, 100].mapBitSaturateAdd16())')
        # 60000+10000=70000->65535(sat); 10000+100=10100
        assert output[-1] == '[65535, 10100]'

    def test_mapBitSaturateAdd16_no_overflow(self):
        output = self._run('print([100, 200, 300].mapBitSaturateAdd16())')
        # 100+200=300; 200+300=500
        assert output[-1] == '[300, 500]'
