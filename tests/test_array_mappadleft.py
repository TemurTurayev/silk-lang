"""
Tests for array .mapPadLeft(length, value) method - pad array from the left.
"""

from silk.interpreter import Interpreter


class TestArrayMapPadLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapPadLeft_basic(self):
        output = self._run('print([1, 2].mapPadLeft(5, 0))')
        assert output[-1] == "[0, 0, 0, 1, 2]"

    def test_mapPadLeft_no_pad(self):
        output = self._run('print([1, 2, 3].mapPadLeft(2, 0))')
        assert output[-1] == "[1, 2, 3]"
