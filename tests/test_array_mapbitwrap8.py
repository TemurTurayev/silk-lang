"""
Tests for array .mapBitWrap8() method - wrap each element to 0-255 range using modulo.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitWrap8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitWrap8_basic(self):
        output = self._run('print([256, 300, 512].mapBitWrap8())')
        # 256%256=0, 300%256=44, 512%256=0
        assert output[-1] == '[0, 44, 0]'

    def test_mapBitWrap8_in_range(self):
        output = self._run('print([0, 128, 255].mapBitWrap8())')
        assert output[-1] == '[0, 128, 255]'
