"""
Tests for array .mapByteReverse() method - reverse bits in each 8-bit element.
"""

from silk.interpreter import Interpreter


class TestArrayMapByteReverse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapByteReverse_basic(self):
        output = self._run('print([1, 128, 255].mapByteReverse())')
        # 1=00000001->10000000=128, 128=10000000->00000001=1, 255->255
        assert output[-1] == '[128, 1, 255]'

    def test_mapByteReverse_values(self):
        output = self._run('print([0, 3, 12].mapByteReverse())')
        # 0->0, 3=00000011->11000000=192, 12=00001100->00110000=48
        assert output[-1] == '[0, 192, 48]'
