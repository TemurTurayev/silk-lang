"""
Tests for array .mapBitRoundNearest16777216() method - round to nearest multiple of 16777216.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest16777216:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest16777216_basic(self):
        output = self._run('print([0, 1, 8388607, 8388608, 16777216].mapBitRoundNearest16777216())')
        assert output[-1] == '[0, 0, 0, 16777216, 16777216]'

    def test_mapBitRoundNearest16777216_exact(self):
        output = self._run('print([33554432, 50331648].mapBitRoundNearest16777216())')
        assert output[-1] == '[33554432, 50331648]'
