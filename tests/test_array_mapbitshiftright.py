"""
Tests for array .mapBitShiftRight() method - right shift each element by argument.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitShiftRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitShiftRight_basic(self):
        output = self._run('print([16, 32, 48].mapBitShiftRight(2))')
        assert output[-1] == '[4, 8, 12]'

    def test_mapBitShiftRight_one(self):
        output = self._run('print([10, 20, 30].mapBitShiftRight(1))')
        assert output[-1] == '[5, 10, 15]'
