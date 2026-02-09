"""
Tests for array .mapBitRoundNearest524288() method - round to nearest multiple of 524288.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest524288:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest524288_basic(self):
        output = self._run('print([1, 262143, 262144, 262145, 524288].mapBitRoundNearest524288())')
        assert output[-1] == '[0, 0, 524288, 524288, 524288]'

    def test_mapBitRoundNearest524288_exact(self):
        output = self._run('print([0, 1048576].mapBitRoundNearest524288())')
        assert output[-1] == '[0, 1048576]'
