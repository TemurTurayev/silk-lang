"""
Tests for number .cubeRoot() method.
"""

from silk.interpreter import Interpreter


class TestNumberCubeRoot:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_cubeRoot_perfect(self):
        output = self._run('print(27.cubeRoot())')
        assert output[-1] == "3"

    def test_cubeRoot_one(self):
        output = self._run('print(1.cubeRoot())')
        assert output[-1] == "1"

    def test_cubeRoot_eight(self):
        output = self._run('print(8.cubeRoot())')
        assert output[-1] == "2"
