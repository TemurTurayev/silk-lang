"""
Tests for array .mapBitRoundNearest16() method - round to nearest multiple of 16.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest16_basic(self):
        output = self._run('print([1, 7, 8, 9, 16, 24].mapBitRoundNearest16())')
        assert output[-1] == '[0, 0, 16, 16, 16, 32]'

    def test_mapBitRoundNearest16_exact(self):
        output = self._run('print([0, 32, 48].mapBitRoundNearest16())')
        assert output[-1] == '[0, 32, 48]'
