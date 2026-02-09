"""
Tests for array .mapBitRoundUp524288() method - round up to next multiple of 524288.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp524288:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp524288_basic(self):
        output = self._run('print([0, 1, 524287, 524288, 524289].mapBitRoundUp524288())')
        assert output[-1] == '[0, 524288, 524288, 524288, 1048576]'

    def test_mapBitRoundUp524288_exact(self):
        output = self._run('print([1048576, 1572864].mapBitRoundUp524288())')
        assert output[-1] == '[1048576, 1572864]'
