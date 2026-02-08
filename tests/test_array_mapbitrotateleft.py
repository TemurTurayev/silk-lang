"""
Tests for array .mapBitRotateLeft(n) method - 8-bit left rotation of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateLeft_basic(self):
        output = self._run('print([1, 128, 170].mapBitRotateLeft(1))')
        # 1=00000001->00000010=2, 128=10000000->00000001=1, 170=10101010->01010101=85
        assert output[-1] == '[2, 1, 85]'

    def test_mapBitRotateLeft_two(self):
        output = self._run('print([1, 255, 192].mapBitRotateLeft(2))')
        # 1=00000001->00000100=4, 255->255, 192=11000000->00000011=3
        assert output[-1] == '[4, 255, 3]'
