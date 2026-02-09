"""
Tests for array .mapBitRotateRight8() method - rotate right by 1 within 8 bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateRight8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateRight8_basic(self):
        output = self._run('print([1, 2, 85].mapBitRotateRight8())')
        # 1=00000001 -> 10000000=128; 2=00000010 -> 00000001=1; 85=01010101 -> 10101010=170
        assert output[-1] == '[128, 1, 170]'

    def test_mapBitRotateRight8_edge(self):
        output = self._run('print([255, 0, 128].mapBitRotateRight8())')
        # 255->255; 0->0; 128=10000000 -> 01000000=64
        assert output[-1] == '[255, 0, 64]'
