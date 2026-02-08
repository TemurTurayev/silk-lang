"""
Tests for array .mapBitSwapPairs() method - swap adjacent bit pairs (bits 0-1, 2-3, etc).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSwapPairs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSwapPairs_basic(self):
        output = self._run('print([5, 10, 15].mapBitSwapPairs())')
        # 5=0101 -> swap pairs -> 1010=10; 10=1010 -> 0101=5; 15=1111 -> 1111=15
        assert output[-1] == '[10, 5, 15]'

    def test_mapBitSwapPairs_single(self):
        output = self._run('print([0, 1, 2, 3].mapBitSwapPairs())')
        # 0->0; 1=01->10=2; 2=10->01=1; 3=11->11=3
        assert output[-1] == '[0, 2, 1, 3]'
