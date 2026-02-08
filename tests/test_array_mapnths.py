"""
Tests for array .mapNths(n) method - take every nth element.
"""

from silk.interpreter import Interpreter


class TestArrayMapNths:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapNths_basic(self):
        output = self._run('print([1, 2, 3, 4, 5, 6].mapNths(2))')
        assert output[-1] == "[1, 3, 5]"

    def test_mapNths_three(self):
        output = self._run('print([1, 2, 3, 4, 5, 6, 7, 8, 9].mapNths(3))')
        assert output[-1] == "[1, 4, 7]"
