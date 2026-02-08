"""
Tests for array .mapBitReverse32() method - reverse bits in 32-bit representation.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitReverse32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitReverse32_basic(self):
        output = self._run('print([1, 2, 3].mapBitReverse32())')
        # 1 -> bit 0 set -> reversed to bit 31 -> 2147483648
        # 2 -> bit 1 set -> reversed to bit 30 -> 1073741824
        # 3 -> bits 0,1 -> reversed bits 31,30 -> 3221225472
        assert output[-1] == '[2147483648, 1073741824, 3221225472]'

    def test_mapBitReverse32_zero(self):
        output = self._run('print([0, 255].mapBitReverse32())')
        # 0 -> 0; 255=0xFF -> reversed -> 0xFF000000 = 4278190080
        assert output[-1] == '[0, 4278190080]'
