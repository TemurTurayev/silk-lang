"""
Tests for array .mapBitClamp8() method - clamp each element to 0-255 range.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitClamp8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitClamp8_basic(self):
        output = self._run('print([300, 100, -5, 255].mapBitClamp8())')
        assert output[-1] == '[255, 100, 0, 255]'

    def test_mapBitClamp8_all_in_range(self):
        output = self._run('print([0, 128, 255].mapBitClamp8())')
        assert output[-1] == '[0, 128, 255]'
