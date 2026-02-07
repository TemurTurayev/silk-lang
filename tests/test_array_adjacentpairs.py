"""
Tests for array .adjacentPairs() method.
"""

from silk.interpreter import Interpreter


class TestArrayAdjacentPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_adjacentPairs_basic(self):
        output = self._run('print([1, 2, 3, 4].adjacentPairs())')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_adjacentPairs_two(self):
        output = self._run('print([1, 2].adjacentPairs())')
        assert output[-1] == "[[1, 2]]"

    def test_adjacentPairs_single(self):
        output = self._run('print([1].adjacentPairs())')
        assert output[-1] == "[]"
