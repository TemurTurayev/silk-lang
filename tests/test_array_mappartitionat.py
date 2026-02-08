"""
Tests for array .mapPartitionAt(n) method - split array at index n.
"""

from silk.interpreter import Interpreter


class TestArrayMapPartitionAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPartitionAt_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].mapPartitionAt(2))')
        assert output[-1] == "[[1, 2], [3, 4, 5]]"

    def test_mapPartitionAt_zero(self):
        output = self._run('print([1, 2, 3].mapPartitionAt(0))')
        assert output[-1] == "[[], [1, 2, 3]]"
