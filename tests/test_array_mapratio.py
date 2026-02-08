"""
Tests for array .mapRatio() method - ratio of consecutive elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapRatio:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRatio_basic(self):
        output = self._run('print([10, 5, 2].mapRatio())')
        assert output[-1] == "[2, 2.5]"

    def test_mapRatio_equal(self):
        output = self._run('print([4, 4, 4].mapRatio())')
        assert output[-1] == "[1, 1]"
