"""
Tests for array .mapHammingDistance() method - Hamming distance between adjacent elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapHammingDistance:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapHammingDistance_basic(self):
        output = self._run('print([7, 8, 15].mapHammingDistance())')
        # 7^8=15=1111(4 bits), 8^15=7=111(3 bits)
        assert output[-1] == '[4, 3]'

    def test_mapHammingDistance_simple(self):
        output = self._run('print([0, 1, 3].mapHammingDistance())')
        # 0^1=1(1 bit), 1^3=2=10(1 bit)
        assert output[-1] == '[1, 1]'
