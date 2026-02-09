"""
Tests for array .mapBitRoundUp16777216() method - round up to next multiple of 16777216.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp16777216:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp16777216_basic(self):
        output = self._run('print([0, 1, 16777215, 16777216, 16777217].mapBitRoundUp16777216())')
        assert output[-1] == '[0, 16777216, 16777216, 16777216, 33554432]'

    def test_mapBitRoundUp16777216_exact(self):
        output = self._run('print([33554432, 50331648].mapBitRoundUp16777216())')
        assert output[-1] == '[33554432, 50331648]'
