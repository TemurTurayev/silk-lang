"""
Tests for array .mapGroupRuns() method - group consecutive equal elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapGroupRuns:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapGroupRuns_basic(self):
        output = self._run('print([1, 1, 2, 3, 3].mapGroupRuns())')
        assert output[-1] == "[[1, 1], [2], [3, 3]]"

    def test_mapGroupRuns_no_runs(self):
        output = self._run('print([1, 2, 3].mapGroupRuns())')
        assert output[-1] == "[[1], [2], [3]]"
