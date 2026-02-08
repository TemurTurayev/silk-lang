"""
Tests for array .mapSquare() method - square each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapSquare:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSquare_basic(self):
        output = self._run('print([1, 2, 3, 4].mapSquare())')
        assert output[-1] == "[1, 4, 9, 16]"

    def test_mapSquare_negative(self):
        output = self._run('print([-2, 0, 3].mapSquare())')
        assert output[-1] == "[4, 0, 9]"
