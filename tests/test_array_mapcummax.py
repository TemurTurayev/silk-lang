"""
Tests for array .mapCumMax() method - running maximum.
"""

from silk.interpreter import Interpreter


class TestArrayMapCumMax:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCumMax_basic(self):
        output = self._run('print([3, 1, 4, 1, 5].mapCumMax())')
        assert output[-1] == "[3, 3, 4, 4, 5]"

    def test_mapCumMax_descending(self):
        output = self._run('print([5, 4, 3].mapCumMax())')
        assert output[-1] == "[5, 5, 5]"
