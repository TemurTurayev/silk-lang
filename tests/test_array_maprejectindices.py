"""
Tests for array .mapRejectIndices(indices) method - reject elements at given indices.
"""

from silk.interpreter import Interpreter


class TestArrayMapRejectIndices:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRejectIndices_basic(self):
        output = self._run('print([10, 20, 30, 40, 50].mapRejectIndices([1, 3]))')
        assert output[-1] == "[10, 30, 50]"

    def test_mapRejectIndices_single(self):
        output = self._run('print([10, 20, 30].mapRejectIndices([0]))')
        assert output[-1] == "[20, 30]"
