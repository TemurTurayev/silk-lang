"""
Tests for array .adjacentDiff() method - differences between consecutive elements.
"""

from silk.interpreter import Interpreter


class TestArrayAdjacentDiff:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_adjacentDiff_basic(self):
        output = self._run('print([1, 3, 6, 10].adjacentDiff())')
        assert output[-1] == "[2, 3, 4]"

    def test_adjacentDiff_negative(self):
        output = self._run('print([5, 3, 1].adjacentDiff())')
        assert output[-1] == "[-2, -2]"
