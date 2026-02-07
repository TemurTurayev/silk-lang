"""
Tests for array .groupByCount(n) method - group into n equal groups.
"""

from silk.interpreter import Interpreter


class TestArrayGroupByCount:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_groupByCount_2(self):
        output = self._run('print([1, 2, 3, 4].groupByCount(2))')
        assert output[-1] == "[[1, 2], [3, 4]]"

    def test_groupByCount_3(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].groupByCount(3))')
        assert output[-1] == "[[1, 2], [3, 4], [5, 6]]"
