"""
Tests for array .mapFlipPairs() method - swap adjacent pairs.
"""

from silk.interpreter import Interpreter


class TestArrayMapFlipPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFlipPairs_even(self):
        output = self._run('print([1, 2, 3, 4].mapFlipPairs())')
        assert output[-1] == "[2, 1, 4, 3]"

    def test_mapFlipPairs_odd(self):
        output = self._run('print([1, 2, 3, 4, 5].mapFlipPairs())')
        assert output[-1] == "[2, 1, 4, 3, 5]"
