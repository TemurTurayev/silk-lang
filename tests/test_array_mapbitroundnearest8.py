"""
Tests for array .mapBitRoundNearest8() method - round to nearest multiple of 8.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest8_basic(self):
        output = self._run('print([1, 3, 4, 5, 8, 12].mapBitRoundNearest8())')
        assert output[-1] == '[0, 0, 8, 8, 8, 16]'

    def test_mapBitRoundNearest8_exact(self):
        output = self._run('print([0, 16, 24].mapBitRoundNearest8())')
        assert output[-1] == '[0, 16, 24]'
