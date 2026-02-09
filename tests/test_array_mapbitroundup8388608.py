"""
Tests for array .mapBitRoundUp8388608() method - round up to next multiple of 8388608.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp8388608:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp8388608_basic(self):
        output = self._run('print([0, 1, 8388607, 8388608, 8388609].mapBitRoundUp8388608())')
        assert output[-1] == '[0, 8388608, 8388608, 8388608, 16777216]'

    def test_mapBitRoundUp8388608_exact(self):
        output = self._run('print([16777216, 25165824].mapBitRoundUp8388608())')
        assert output[-1] == '[16777216, 25165824]'
