"""
Tests for array .mapOnesComplement() method - 8-bit one's complement of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapOnesComplement:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapOnesComplement_basic(self):
        output = self._run('print([0, 255, 170].mapOnesComplement())')
        # 0->255, 255->0, 170=0xAA->0x55=85
        assert output[-1] == '[255, 0, 85]'

    def test_mapOnesComplement_values(self):
        output = self._run('print([1, 128, 127].mapOnesComplement())')
        # 1->254, 128->127, 127->128
        assert output[-1] == '[254, 127, 128]'
