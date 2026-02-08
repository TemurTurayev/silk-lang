"""
Tests for array .mapCartesian(other) method - cartesian product of two arrays.
"""

from silk.interpreter import Interpreter


class TestArrayMapCartesian:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCartesian_basic(self):
        output = self._run('print([1, 2].mapCartesian([3, 4]))')
        assert output[-1] == "[[1, 3], [1, 4], [2, 3], [2, 4]]"

    def test_mapCartesian_single(self):
        output = self._run('print([1].mapCartesian([2, 3]))')
        assert output[-1] == "[[1, 2], [1, 3]]"
