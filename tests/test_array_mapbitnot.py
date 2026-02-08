"""
Tests for array .mapBitNot() method - bitwise NOT each element (8-bit).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitNot:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitNot_basic(self):
        output = self._run('print([0, 255, 128].mapBitNot())')
        assert output[-1] == '[255, 0, 127]'

    def test_mapBitNot_values(self):
        output = self._run('print([1, 15, 240].mapBitNot())')
        assert output[-1] == '[254, 240, 15]'
