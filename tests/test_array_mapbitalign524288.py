"""
Tests for array .mapBitAlign524288() method - align up to nearest multiple of 524288.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign524288:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign524288_basic(self):
        output = self._run('print([1, 524287, 524288, 524289].mapBitAlign524288())')
        assert output[-1] == '[524288, 524288, 524288, 1048576]'

    def test_mapBitAlign524288_zero(self):
        output = self._run('print([0, 1048576].mapBitAlign524288())')
        assert output[-1] == '[0, 1048576]'
