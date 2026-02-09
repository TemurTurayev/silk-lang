"""
Tests for array .mapBitRoundNearest1048576() method - round to nearest multiple of 1048576.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest1048576:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest1048576_basic(self):
        output = self._run('print([1, 524287, 524288, 524289, 1048576].mapBitRoundNearest1048576())')
        assert output[-1] == '[0, 0, 1048576, 1048576, 1048576]'

    def test_mapBitRoundNearest1048576_exact(self):
        output = self._run('print([0, 2097152].mapBitRoundNearest1048576())')
        assert output[-1] == '[0, 2097152]'
