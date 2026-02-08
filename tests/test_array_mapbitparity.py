"""
Tests for array .mapBitParity() method - overall parity (XOR of all bits = even/odd).
"""

from silk.interpreter import Interpreter


class TestArrayMapBitParity:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitParity_basic(self):
        output = self._run('print([5, 7, 8].mapBitParity())')
        # 5=101: 2 bits (even) -> 0, 7=111: 3 bits (odd) -> 1, 8=1000: 1 bit (odd) -> 1
        assert output[-1] == '[0, 1, 1]'

    def test_mapBitParity_single(self):
        output = self._run('print([0, 1, 3, 15].mapBitParity())')
        # 0:0 bits->0, 1:1 bit->1, 3=11:2 bits->0, 15=1111:4 bits->0
        assert output[-1] == '[0, 1, 0, 0]'
