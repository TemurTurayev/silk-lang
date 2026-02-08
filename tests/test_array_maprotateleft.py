"""
Tests for array .mapRotateLeft(n) method - rotate elements left by n.
"""

from silk.interpreter import Interpreter


class TestArrayMapRotateLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRotateLeft_1(self):
        output = self._run('print([1, 2, 3, 4].mapRotateLeft(1))')
        assert output[-1] == "[2, 3, 4, 1]"

    def test_mapRotateLeft_2(self):
        output = self._run('print([1, 2, 3, 4].mapRotateLeft(2))')
        assert output[-1] == "[3, 4, 1, 2]"
