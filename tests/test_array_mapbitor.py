"""
Tests for array .mapBitOr() method - bitwise OR each element with argument.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitOr:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitOr_basic(self):
        output = self._run('print([8, 4, 2].mapBitOr(1))')
        assert output[-1] == '[9, 5, 3]'

    def test_mapBitOr_mask(self):
        output = self._run('print([0, 128, 64].mapBitOr(15))')
        assert output[-1] == '[15, 143, 79]'
