"""
Tests for array .mapBitRoundUp2048() method - round up to nearest multiple of 2048.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp2048:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp2048_basic(self):
        output = self._run('print([1, 2047, 2048, 2049].mapBitRoundUp2048())')
        assert output[-1] == '[2048, 2048, 2048, 4096]'

    def test_mapBitRoundUp2048_zero(self):
        output = self._run('print([0, 4096].mapBitRoundUp2048())')
        assert output[-1] == '[0, 4096]'
