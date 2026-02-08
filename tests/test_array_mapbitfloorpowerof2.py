"""
Tests for array .mapBitFloorPowerOf2() method - floor to nearest power of 2.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitFloorPowerOf2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitFloorPowerOf2_basic(self):
        output = self._run('print([3, 5, 6, 10].mapBitFloorPowerOf2())')
        # 3->2; 5->4; 6->4; 10->8
        assert output[-1] == '[2, 4, 4, 8]'

    def test_mapBitFloorPowerOf2_powers(self):
        output = self._run('print([1, 2, 4, 8, 16].mapBitFloorPowerOf2())')
        assert output[-1] == '[1, 2, 4, 8, 16]'
