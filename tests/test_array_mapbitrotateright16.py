"""
Tests for array .mapBitRotateRight16() method - rotate right by 1 within 16 bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateRight16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateRight16_basic(self):
        output = self._run('print([1, 2, 21845].mapBitRotateRight16())')
        # 1 -> 32768; 2 -> 1; 21845=0101010101010101 -> 1010101010101010=43690
        assert output[-1] == '[32768, 1, 43690]'

    def test_mapBitRotateRight16_edge(self):
        output = self._run('print([65535, 0].mapBitRotateRight16())')
        assert output[-1] == '[65535, 0]'
