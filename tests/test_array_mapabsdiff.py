"""
Tests for array .mapAbsDiff() method - absolute differences between consecutive elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapAbsDiff:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAbsDiff_basic(self):
        output = self._run('print([5, 2, 8, 1].mapAbsDiff())')
        assert output[-1] == "[3, 6, 7]"

    def test_mapAbsDiff_equal(self):
        output = self._run('print([3, 3, 3].mapAbsDiff())')
        assert output[-1] == "[0, 0]"
