"""
Tests for array .mapSelectIndices(indices) method - select elements at given indices.
"""

from silk.interpreter import Interpreter


class TestArrayMapSelectIndices:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSelectIndices_basic(self):
        output = self._run('print([10, 20, 30, 40, 50].mapSelectIndices([0, 2, 4]))')
        assert output[-1] == "[10, 30, 50]"

    def test_mapSelectIndices_single(self):
        output = self._run('print([10, 20, 30].mapSelectIndices([1]))')
        assert output[-1] == "[20]"
