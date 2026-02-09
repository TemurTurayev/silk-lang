"""
Tests for array .mapBitRotateLeft8() method - rotate left by 1 within 8 bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateLeft8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateLeft8_basic(self):
        output = self._run('print([128, 1, 170].mapBitRotateLeft8())')
        # 128=10000000 -> 00000001=1; 1=00000001 -> 00000010=2; 170=10101010 -> 01010101=85
        assert output[-1] == '[1, 2, 85]'

    def test_mapBitRotateLeft8_mid(self):
        output = self._run('print([255, 0, 15].mapBitRotateLeft8())')
        # 255->255; 0->0; 15=00001111 -> 00011110=30
        assert output[-1] == '[255, 0, 30]'
