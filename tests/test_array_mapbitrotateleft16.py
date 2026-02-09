"""
Tests for array .mapBitRotateLeft16() method - rotate left by 1 within 16 bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateLeft16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateLeft16_basic(self):
        output = self._run('print([32768, 1, 43690].mapBitRotateLeft16())')
        # 32768=1000000000000000 -> 0000000000000001=1; 1 -> 2; 43690=1010101010101010 -> 0101010101010101=21845
        assert output[-1] == '[1, 2, 21845]'

    def test_mapBitRotateLeft16_edge(self):
        output = self._run('print([65535, 0].mapBitRotateLeft16())')
        # 65535->65535; 0->0
        assert output[-1] == '[65535, 0]'
