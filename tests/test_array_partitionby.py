"""
Tests for array .partitionBy(fn) method - split into groups when fn returns different value.
"""

from silk.interpreter import Interpreter


class TestArrayPartitionBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_partitionBy_basic(self):
        output = self._run('print([1, 1, 2, 2, 3].partitionBy(|x| x))')
        assert output[-1] == "[[1, 1], [2, 2], [3]]"

    def test_partitionBy_predicate(self):
        output = self._run('print([1, 3, 2, 4, 5].partitionBy(|x| x % 2 == 0))')
        assert output[-1] == "[[1, 3], [2, 4], [5]]"
