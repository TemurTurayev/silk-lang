"""
Tests for array .mapSwapAt(i, j) method - swap elements at indices i and j.
"""

from silk.interpreter import Interpreter


class TestArrayMapSwapAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSwapAt_basic(self):
        output = self._run('print([1, 2, 3, 4].mapSwapAt(0, 3))')
        assert output[-1] == "[4, 2, 3, 1]"

    def test_mapSwapAt_adjacent(self):
        output = self._run('print([10, 20, 30].mapSwapAt(0, 1))')
        assert output[-1] == "[20, 10, 30]"
