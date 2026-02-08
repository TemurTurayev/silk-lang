"""
Tests for array .mapBitIsPowerOf2() method - check if each element is a power of 2.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitIsPowerOf2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitIsPowerOf2_basic(self):
        output = self._run('print([1, 2, 3, 4, 5, 8, 16].mapBitIsPowerOf2())')
        assert output[-1] == '[true, true, false, true, false, true, true]'

    def test_mapBitIsPowerOf2_zero(self):
        output = self._run('print([0, 6, 7, 32, 64].mapBitIsPowerOf2())')
        assert output[-1] == '[false, false, false, true, true]'
