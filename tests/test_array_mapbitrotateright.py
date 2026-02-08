"""
Tests for array .mapBitRotateRight(n) method - 8-bit right rotation of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRotateRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRotateRight_basic(self):
        output = self._run('print([1, 128, 85].mapBitRotateRight(1))')
        # 1=00000001->10000000=128, 128=10000000->01000000=64, 85=01010101->10101010=170
        assert output[-1] == '[128, 64, 170]'

    def test_mapBitRotateRight_two(self):
        output = self._run('print([3, 255, 4].mapBitRotateRight(2))')
        # 3=00000011->11000000=192, 255->255, 4=00000100->00000001=1
        assert output[-1] == '[192, 255, 1]'
