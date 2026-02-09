"""
Tests for array .mapBitQuantize32() method - quantize to nearest multiple of 32.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize32_basic(self):
        output = self._run('print([10, 33, 64, 95].mapBitQuantize32())')
        # 10->0, 33->32, 64->64, 95->64
        assert output[-1] == '[0, 32, 64, 64]'

    def test_mapBitQuantize32_exact(self):
        output = self._run('print([0, 32, 64, 96].mapBitQuantize32())')
        assert output[-1] == '[0, 32, 64, 96]'
