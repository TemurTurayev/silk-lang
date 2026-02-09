"""
Tests for array .mapBitRoundDown8388608() method - round down to nearest multiple of 8388608.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown8388608:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown8388608_basic(self):
        output = self._run('print([0, 1, 8388607, 8388608, 8388609].mapBitRoundDown8388608())')
        assert output[-1] == '[0, 0, 0, 8388608, 8388608]'

    def test_mapBitRoundDown8388608_exact(self):
        output = self._run('print([16777216, 25165823].mapBitRoundDown8388608())')
        assert output[-1] == '[16777216, 16777216]'
