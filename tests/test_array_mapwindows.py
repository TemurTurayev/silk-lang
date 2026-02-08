"""
Tests for array .mapWindows(n) method - sliding windows of size n.
"""

from silk.interpreter import Interpreter


class TestArrayMapWindows:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapWindows_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].mapWindows(3))')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"

    def test_mapWindows_pairs(self):
        output = self._run('print([1, 2, 3].mapWindows(2))')
        assert output[-1] == "[[1, 2], [2, 3]]"
