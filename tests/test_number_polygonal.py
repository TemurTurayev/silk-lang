"""
Tests for number .polygonal(k) method - k-gonal number.
"""

from silk.interpreter import Interpreter


class TestNumberPolygonal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_polygonal_triangle(self):
        output = self._run('print(4.polygonal(3))')
        assert output[-1] == "10"

    def test_polygonal_square(self):
        output = self._run('print(4.polygonal(4))')
        assert output[-1] == "16"

    def test_polygonal_pentagonal(self):
        output = self._run('print(4.polygonal(5))')
        assert output[-1] == "22"
