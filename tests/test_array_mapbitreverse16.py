"""
Tests for array .mapBitReverse16() method - reverse bits in 16-bit representation.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitReverse16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitReverse16_basic(self):
        output = self._run('print([1, 256, 65535].mapBitReverse16())')
        # 1=0000000000000001->1000000000000000=32768, 256=0000000100000000->0000000010000000=128, 65535->65535
        assert output[-1] == '[32768, 128, 65535]'

    def test_mapBitReverse16_more(self):
        output = self._run('print([0, 2, 32768].mapBitReverse16())')
        # 0->0, 2=0000000000000010->0100000000000000=16384, 32768=1000000000000000->0000000000000001=1
        assert output[-1] == '[0, 16384, 1]'
