"""
Tests for array .mapBitWrap16() method - wrap each element to 0-65535 range using modulo.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitWrap16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitWrap16_basic(self):
        output = self._run('print([65536, 70000, 131072].mapBitWrap16())')
        # 65536%65536=0, 70000%65536=4464, 131072%65536=0
        assert output[-1] == '[0, 4464, 0]'

    def test_mapBitWrap16_in_range(self):
        output = self._run('print([0, 32768, 65535].mapBitWrap16())')
        assert output[-1] == '[0, 32768, 65535]'
