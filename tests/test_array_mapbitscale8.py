"""
Tests for array .mapBitScale8() method - scale each element to 0-255 range from array min/max.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitScale8:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitScale8_basic(self):
        output = self._run('print([0, 50, 100].mapBitScale8())')
        # 0->0, 50->127 or 128, 100->255
        result = eval(output[-1])
        assert result[0] == 0
        assert result[2] == 255

    def test_mapBitScale8_same(self):
        output = self._run('print([5, 5, 5].mapBitScale8())')
        assert output[-1] == '[0, 0, 0]'
