"""
Tests for array .mapBitScale32() method - scale each element to 0-4294967295 range from array min/max.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitScale32:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitScale32_basic(self):
        output = self._run('print([0, 50, 100].mapBitScale32())')
        result = eval(output[-1])
        assert result[0] == 0
        assert result[2] == 4294967295

    def test_mapBitScale32_same(self):
        output = self._run('print([5, 5, 5].mapBitScale32())')
        assert output[-1] == '[0, 0, 0]'
