"""
Tests for array .mapBitWrap32() method - wrap each element to 0-4294967295 range using modulo.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitWrap32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitWrap32_basic(self):
        output = self._run('print([4294967296, 5000000000].mapBitWrap32())')
        # 4294967296%4294967296=0, 5000000000%4294967296=705032704
        assert output[-1] == '[0, 705032704]'

    def test_mapBitWrap32_in_range(self):
        output = self._run('print([0, 1000000, 4294967295].mapBitWrap32())')
        assert output[-1] == '[0, 1000000, 4294967295]'
