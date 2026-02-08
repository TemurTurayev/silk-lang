"""
Tests for array .mapTwosComplement() method - 8-bit two's complement of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapTwosComplement:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapTwosComplement_basic(self):
        output = self._run('print([1, 127, 200].mapTwosComplement())')
        # 1->255, 127->129, 200->56
        assert output[-1] == '[255, 129, 56]'

    def test_mapTwosComplement_zero(self):
        output = self._run('print([0, 128, 255].mapTwosComplement())')
        # 0->0, 128->128, 255->1
        assert output[-1] == '[0, 128, 1]'
