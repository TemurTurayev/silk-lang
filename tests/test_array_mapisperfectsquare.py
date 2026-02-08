"""
Tests for array .mapIsPerfectSquare() method - check if each element is a perfect square.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsPerfectSquare:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsPerfectSquare_mixed(self):
        output = self._run('print([1, 2, 4, 5, 9].mapIsPerfectSquare())')
        assert output[-1] == "[true, false, true, false, true]"

    def test_mapIsPerfectSquare_allSquares(self):
        output = self._run('print([1, 4, 9, 16].mapIsPerfectSquare())')
        assert output[-1] == "[true, true, true, true]"
