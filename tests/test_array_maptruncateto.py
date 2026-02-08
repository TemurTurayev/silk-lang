"""
Tests for array .mapTruncateTo(n) method - keep only first n elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapTruncateTo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTruncateTo_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].mapTruncateTo(3))')
        assert output[-1] == "[1, 2, 3]"

    def test_mapTruncateTo_exceeds(self):
        output = self._run('print([1, 2].mapTruncateTo(5))')
        assert output[-1] == "[1, 2]"
