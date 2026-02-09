"""
Tests for array .mapBitRoundDown32() method - round down to nearest multiple of 32.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown32_basic(self):
        output = self._run('print([31, 32, 33, 63].mapBitRoundDown32())')
        # 31->0, 32->32, 33->32, 63->32
        assert output[-1] == '[0, 32, 32, 32]'

    def test_mapBitRoundDown32_exact(self):
        output = self._run('print([0, 64, 96, 128].mapBitRoundDown32())')
        assert output[-1] == '[0, 64, 96, 128]'
