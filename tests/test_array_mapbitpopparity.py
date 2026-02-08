"""
Tests for array .mapBitPopParity() method - 0 if even number of set bits, 1 if odd.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitPopParity:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitPopParity_basic(self):
        output = self._run('print([7, 3, 5, 15].mapBitPopParity())')
        # 7=111 (3 bits, odd->1); 3=11 (2 bits, even->0); 5=101 (2 bits, even->0); 15=1111 (4 bits, even->0)
        assert output[-1] == '[1, 0, 0, 0]'

    def test_mapBitPopParity_edge(self):
        output = self._run('print([0, 1, 2, 4].mapBitPopParity())')
        # 0->0 bits(even->0); 1->1 bit(odd->1); 2->1 bit(odd->1); 4->1 bit(odd->1)
        assert output[-1] == '[0, 1, 1, 1]'
