"""
Tests for array .mapPadRight(length, value) method - pad array from the right.
"""

from silk.interpreter import Interpreter


class TestArrayMapPadRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPadRight_basic(self):
        output = self._run('print([1, 2].mapPadRight(5, 0))')
        assert output[-1] == "[1, 2, 0, 0, 0]"

    def test_mapPadRight_no_pad(self):
        output = self._run('print([1, 2, 3].mapPadRight(2, 0))')
        assert output[-1] == "[1, 2, 3]"
