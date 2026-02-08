"""
Tests for array .mapRotateRight(n) method - rotate elements right by n.
"""

from silk.interpreter import Interpreter


class TestArrayMapRotateRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRotateRight_1(self):
        output = self._run('print([1, 2, 3, 4].mapRotateRight(1))')
        assert output[-1] == "[4, 1, 2, 3]"

    def test_mapRotateRight_2(self):
        output = self._run('print([1, 2, 3, 4].mapRotateRight(2))')
        assert output[-1] == "[3, 4, 1, 2]"
