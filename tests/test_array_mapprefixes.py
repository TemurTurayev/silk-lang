"""
Tests for array .mapPrefixes() method - all prefixes of the array.
"""

from silk.interpreter import Interpreter


class TestArrayMapPrefixes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPrefixes_basic(self):
        output = self._run('print([1, 2, 3].mapPrefixes())')
        assert output[-1] == "[[1], [1, 2], [1, 2, 3]]"

    def test_mapPrefixes_single(self):
        output = self._run('print([5].mapPrefixes())')
        assert output[-1] == "[[5]]"
