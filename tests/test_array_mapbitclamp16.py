"""
Tests for array .mapBitClamp16() method - clamp each element to 0-65535 range.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitClamp16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitClamp16_basic(self):
        output = self._run('print([70000, 100, -5, 65535].mapBitClamp16())')
        assert output[-1] == '[65535, 100, 0, 65535]'

    def test_mapBitClamp16_all_in_range(self):
        output = self._run('print([0, 32768, 65535].mapBitClamp16())')
        assert output[-1] == '[0, 32768, 65535]'
