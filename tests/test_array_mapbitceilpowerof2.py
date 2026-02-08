"""
Tests for array .mapBitCeilPowerOf2() method - ceiling to nearest power of 2.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitCeilPowerOf2:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitCeilPowerOf2_basic(self):
        output = self._run('print([3, 5, 6, 10].mapBitCeilPowerOf2())')
        # 3->4; 5->8; 6->8; 10->16
        assert output[-1] == '[4, 8, 8, 16]'

    def test_mapBitCeilPowerOf2_powers(self):
        output = self._run('print([0, 1, 2, 4, 8].mapBitCeilPowerOf2())')
        # 0->0; 1->1; 2->2; 4->4; 8->8
        assert output[-1] == '[0, 1, 2, 4, 8]'
