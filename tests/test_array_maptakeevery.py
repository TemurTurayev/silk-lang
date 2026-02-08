"""
Tests for array .mapTakeEvery(n) method - take every nth element (1-indexed).
"""

from silk.interpreter import Interpreter


class TestArrayMapTakeEvery:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTakeEvery_basic(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].mapTakeEvery(2))')
        assert output[-1] == "[2, 4, 6]"

    def test_mapTakeEvery_three(self):
        output = self._run('print([1, 2, 3, 4, 5, 6, 7, 8, 9].mapTakeEvery(3))')
        assert output[-1] == "[3, 6, 9]"
