"""
Tests for array .mapBitRoundDown8() method - round down to nearest multiple of 8 (same as quantize8).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown8_basic(self):
        output = self._run('print([7, 8, 9, 15].mapBitRoundDown8())')
        # 7->0, 8->8, 9->8, 15->8
        assert output[-1] == '[0, 8, 8, 8]'

    def test_mapBitRoundDown8_exact(self):
        output = self._run('print([0, 16, 24, 32].mapBitRoundDown8())')
        assert output[-1] == '[0, 16, 24, 32]'
