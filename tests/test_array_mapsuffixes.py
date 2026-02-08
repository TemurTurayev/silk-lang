"""
Tests for array .mapSuffixes() method - all suffixes of the array.
"""

from silk.interpreter import Interpreter


class TestArrayMapSuffixes:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSuffixes_basic(self):
        output = self._run('print([1, 2, 3].mapSuffixes())')
        assert output[-1] == "[[1, 2, 3], [2, 3], [3]]"

    def test_mapSuffixes_single(self):
        output = self._run('print([5].mapSuffixes())')
        assert output[-1] == "[[5]]"
