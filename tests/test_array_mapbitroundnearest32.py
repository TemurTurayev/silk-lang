"""
Tests for array .mapBitRoundNearest32() method - round to nearest multiple of 32.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest32_basic(self):
        output = self._run('print([1, 15, 16, 17, 32, 48].mapBitRoundNearest32())')
        assert output[-1] == '[0, 0, 32, 32, 32, 64]'

    def test_mapBitRoundNearest32_exact(self):
        output = self._run('print([0, 64, 96].mapBitRoundNearest32())')
        assert output[-1] == '[0, 64, 96]'
