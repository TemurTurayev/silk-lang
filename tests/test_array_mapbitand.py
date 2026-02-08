"""
Tests for array .mapBitAnd() method - bitwise AND each element with argument.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAnd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAnd_basic(self):
        output = self._run('print([15, 7, 12].mapBitAnd(6))')
        assert output[-1] == '[6, 6, 4]'

    def test_mapBitAnd_mask(self):
        output = self._run('print([255, 128, 64].mapBitAnd(192))')
        assert output[-1] == '[192, 128, 64]'
