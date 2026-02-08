"""
Tests for array .mapBitShiftLeft() method - left shift each element by argument.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitShiftLeft:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitShiftLeft_basic(self):
        output = self._run('print([1, 2, 3].mapBitShiftLeft(2))')
        assert output[-1] == '[4, 8, 12]'

    def test_mapBitShiftLeft_one(self):
        output = self._run('print([5, 10, 15].mapBitShiftLeft(1))')
        assert output[-1] == '[10, 20, 30]'
