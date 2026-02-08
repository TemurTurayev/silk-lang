"""
Tests for array .mapInterleave(other) method - interleave two arrays.
"""

from silk.interpreter import Interpreter


class TestArrayMapInterleave:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapInterleave_basic(self):
        output = self._run('print([1, 2, 3].mapInterleave([4, 5, 6]))')
        assert output[-1] == "[1, 4, 2, 5, 3, 6]"

    def test_mapInterleave_unequal(self):
        output = self._run('print([1, 2].mapInterleave([3, 4, 5]))')
        assert output[-1] == "[1, 3, 2, 4, 5]"
