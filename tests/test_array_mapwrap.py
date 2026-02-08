"""
Tests for array .mapWrap() method - wrap each element in a single-element array.
"""

from silk.interpreter import Interpreter


class TestArrayMapWrap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWrap_basic(self):
        output = self._run('print([1, 2, 3].mapWrap())')
        assert output[-1] == '[[1], [2], [3]]'

    def test_mapWrap_strings(self):
        output = self._run('print(["a", "b"].mapWrap())')
        assert output[-1] == '[[a], [b]]'
