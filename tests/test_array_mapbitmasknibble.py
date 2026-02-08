"""
Tests for array .mapBitMaskNibble() method - keep only the lowest nibble (4 bits).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitMaskNibble:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitMaskNibble_basic(self):
        output = self._run('print([255, 171, 16].mapBitMaskNibble())')
        # 255 & 0xF = 15; 171 & 0xF = 11; 16 & 0xF = 0
        assert output[-1] == '[15, 11, 0]'

    def test_mapBitMaskNibble_small(self):
        output = self._run('print([0, 5, 15, 31].mapBitMaskNibble())')
        # 0&F=0; 5&F=5; 15&F=15; 31&F=15
        assert output[-1] == '[0, 5, 15, 15]'
