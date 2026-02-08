"""
Tests for array .mapSplitAt(n) method - split array into two at index n.
"""

from silk.interpreter import Interpreter


class TestArrayMapSplitAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSplitAt_middle(self):
        output = self._run('print([1, 2, 3, 4, 5].mapSplitAt(2))')
        assert output[-1] == "[[1, 2], [3, 4, 5]]"

    def test_mapSplitAt_start(self):
        output = self._run('print([1, 2, 3].mapSplitAt(0))')
        assert output[-1] == "[[], [1, 2, 3]]"
