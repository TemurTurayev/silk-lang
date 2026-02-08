"""
Tests for array .mapHammingWeight() method - number of 1-bits in each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapHammingWeight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapHammingWeight_basic(self):
        output = self._run('print([7, 8, 255].mapHammingWeight())')
        assert output[-1] == '[3, 1, 8]'

    def test_mapHammingWeight_zeros(self):
        output = self._run('print([0, 1, 3].mapHammingWeight())')
        assert output[-1] == '[0, 1, 2]'
