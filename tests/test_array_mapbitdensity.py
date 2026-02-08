"""
Tests for array .mapBitDensity() method - ratio of set bits to total bits.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitDensity:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitDensity_basic(self):
        output = self._run('print([7, 8, 15].mapBitDensity())')
        # 7=111 -> 3/3=1, 8=1000 -> 1/4=0.25, 15=1111 -> 4/4=1
        assert output[-1] == '[1, 0.25, 1]'

    def test_mapBitDensity_single(self):
        output = self._run('print([1, 5, 255].mapBitDensity())')
        # 1=1 -> 1/1=1, 5=101 -> 2/3, 255=11111111 -> 8/8=1
        assert '1' in output[-1]
