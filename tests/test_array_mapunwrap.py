"""
Tests for array .mapUnwrap() method - unwrap single-element arrays.
"""

from silk.interpreter import Interpreter


class TestArrayMapUnwrap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapUnwrap_basic(self):
        output = self._run('print([[1], [2], [3]].mapUnwrap())')
        assert output[-1] == '[1, 2, 3]'

    def test_mapUnwrap_strings(self):
        output = self._run('print([["a"], ["b"]].mapUnwrap())')
        assert output[-1] == '[a, b]'
