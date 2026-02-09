"""
Tests for array .mapBitScale16() method - scale each element to 0-65535 range from array min/max.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitScale16:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitScale16_basic(self):
        output = self._run('print([0, 50, 100].mapBitScale16())')
        result = eval(output[-1])
        assert result[0] == 0
        assert result[2] == 65535

    def test_mapBitScale16_same(self):
        output = self._run('print([5, 5, 5].mapBitScale16())')
        assert output[-1] == '[0, 0, 0]'
