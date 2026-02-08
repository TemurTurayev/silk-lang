"""
Tests for array .mapCumMin() method - running minimum.
"""

from silk.interpreter import Interpreter


class TestArrayMapCumMin:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCumMin_basic(self):
        output = self._run('print([3, 1, 4, 1, 5].mapCumMin())')
        assert output[-1] == "[3, 1, 1, 1, 1]"

    def test_mapCumMin_ascending(self):
        output = self._run('print([1, 2, 3].mapCumMin())')
        assert output[-1] == "[1, 1, 1]"
