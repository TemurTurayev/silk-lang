"""
Tests for array .mapBitRoundDown2048() method - round down to nearest multiple of 2048.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown2048:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown2048_basic(self):
        output = self._run('print([1, 2047, 2048, 2049].mapBitRoundDown2048())')
        assert output[-1] == '[0, 0, 2048, 2048]'

    def test_mapBitRoundDown2048_larger(self):
        output = self._run('print([4096, 5000].mapBitRoundDown2048())')
        assert output[-1] == '[4096, 4096]'
