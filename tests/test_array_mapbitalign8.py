"""
Tests for array .mapBitAlign8() method - align up to nearest multiple of 8.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign8_basic(self):
        output = self._run('print([1, 7, 8, 9, 15, 16].mapBitAlign8())')
        # 1->8, 7->8, 8->8, 9->16, 15->16, 16->16
        assert output[-1] == '[8, 8, 8, 16, 16, 16]'

    def test_mapBitAlign8_zero(self):
        output = self._run('print([0, 24, 32].mapBitAlign8())')
        assert output[-1] == '[0, 24, 32]'
