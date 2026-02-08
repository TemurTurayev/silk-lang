"""
Tests for array .mapCumSum() method - cumulative sum of elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapCumSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCumSum_basic(self):
        output = self._run('print([1, 2, 3, 4].mapCumSum())')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_mapCumSum_single(self):
        output = self._run('print([5].mapCumSum())')
        assert output[-1] == "[5]"
