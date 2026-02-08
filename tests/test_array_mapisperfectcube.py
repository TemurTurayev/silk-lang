"""
Tests for array .mapIsPerfectCube() method - check if each element is a perfect cube.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsPerfectCube:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsPerfectCube_mixed(self):
        output = self._run('print([1, 2, 8, 9, 27].mapIsPerfectCube())')
        assert output[-1] == "[true, false, true, false, true]"

    def test_mapIsPerfectCube_allCubes(self):
        output = self._run('print([1, 8, 27, 64].mapIsPerfectCube())')
        assert output[-1] == "[true, true, true, true]"
