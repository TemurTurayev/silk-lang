"""
Tests for array .mapChunksOf(n) method - split array into chunks of size n.
"""

from silk.interpreter import Interpreter


class TestArrayMapChunksOf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapChunksOf_even(self):
        output = self._run('print([1, 2, 3, 4].mapChunksOf(2))')
        assert output[-1] == "[[1, 2], [3, 4]]"

    def test_mapChunksOf_uneven(self):
        output = self._run('print([1, 2, 3, 4, 5].mapChunksOf(2))')
        assert output[-1] == "[[1, 2], [3, 4], [5]]"
