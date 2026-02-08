"""
Tests for array .mapCube() method - cube each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapCube:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCube_basic(self):
        output = self._run('print([1, 2, 3].mapCube())')
        assert output[-1] == "[1, 8, 27]"

    def test_mapCube_negative(self):
        output = self._run('print([-2, 0, 3].mapCube())')
        assert output[-1] == "[-8, 0, 27]"
