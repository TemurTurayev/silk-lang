"""
Tests for array .mapRank() method - rank of each element (1-based).
"""

from silk.interpreter import Interpreter


class TestArrayMapRank:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRank_basic(self):
        output = self._run('print([30, 10, 20].mapRank())')
        assert output[-1] == "[3, 1, 2]"

    def test_mapRank_ties(self):
        output = self._run('print([5, 5, 5].mapRank())')
        assert output[-1] == "[1, 1, 1]"
