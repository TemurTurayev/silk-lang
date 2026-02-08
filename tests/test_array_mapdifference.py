"""
Tests for array .mapDifference() method - consecutive differences.
"""

from silk.interpreter import Interpreter


class TestArrayMapDifference:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDifference_basic(self):
        output = self._run('print([1, 3, 6, 10].mapDifference())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapDifference_negative(self):
        output = self._run('print([5, 3, 1].mapDifference())')
        assert output[-1] == "[-2, -2]"
