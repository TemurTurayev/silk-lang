"""
Tests for array .mapFillTo(length, value) method - pad array to given length.
"""

from silk.interpreter import Interpreter


class TestArrayMapFillTo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFillTo_basic(self):
        output = self._run('print([1, 2].mapFillTo(5, 0))')
        assert output[-1] == "[1, 2, 0, 0, 0]"

    def test_mapFillTo_no_fill(self):
        output = self._run('print([1, 2, 3].mapFillTo(2, 0))')
        assert output[-1] == "[1, 2, 3]"
