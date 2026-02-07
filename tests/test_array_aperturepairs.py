"""
Tests for array .mapPairs(fn) method - apply fn to consecutive pairs.
"""

from silk.interpreter import Interpreter


class TestArrayMapPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPairs_sum(self):
        output = self._run('print([1, 2, 3, 4].mapPairs(|a, b| a + b))')
        assert output[-1] == "[3, 5, 7]"

    def test_mapPairs_diff(self):
        output = self._run('print([10, 7, 3].mapPairs(|a, b| a - b))')
        assert output[-1] == "[3, 4]"
