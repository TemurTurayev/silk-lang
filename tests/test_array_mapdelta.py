"""
Tests for array .mapDelta() method - differences between consecutive elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapDelta:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDelta_basic(self):
        output = self._run('print([1, 3, 6, 10].mapDelta())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapDelta_negative(self):
        output = self._run('print([10, 7, 3].mapDelta())')
        assert output[-1] == "[-3, -4]"
