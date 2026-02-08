"""
Tests for array .mapBitInterleave() method - interleave bits of adjacent pairs.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitInterleave:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitInterleave_basic(self):
        output = self._run('print([3, 5].mapBitInterleave())')
        # 3=011, 5=101 -> interleave bits: 01_10_11 -> from LSB: 3 bit0=1, 5 bit0=1 -> 11, 3 bit1=1, 5 bit1=0 -> 01, 3 bit2=0, 5 bit2=1 -> 10
        # result = 100111 = 39
        assert output[-1] == '[39]'

    def test_mapBitInterleave_simple(self):
        output = self._run('print([0, 255].mapBitInterleave())')
        # 0=00000000, 255=11111111 -> interleave: 10101010 10101010 = 0xAAAA = 43690
        assert output[-1] == '[43690]'
