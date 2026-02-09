"""
Tests for array .mapBitRoundDown16777216() method - round down to nearest multiple of 16777216.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown16777216:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown16777216_basic(self):
        output = self._run('print([0, 1, 16777215, 16777216, 16777217].mapBitRoundDown16777216())')
        assert output[-1] == '[0, 0, 0, 16777216, 16777216]'

    def test_mapBitRoundDown16777216_exact(self):
        output = self._run('print([33554432, 50331647].mapBitRoundDown16777216())')
        assert output[-1] == '[33554432, 33554432]'
