"""
Tests for array .mapBitSignature() method - fingerprint: count of 1s XOR bit length.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitSignature:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitSignature_basic(self):
        output = self._run('print([5, 7, 8].mapBitSignature())')
        # 5=101: popcount=2 XOR bitlength=3 -> 2^3=1; 7=111: 3^3=0; 8=1000: 1^4=5
        assert output[-1] == '[1, 0, 5]'

    def test_mapBitSignature_single(self):
        output = self._run('print([0, 1, 3].mapBitSignature())')
        # 0: 0^0=0; 1=1: 1^1=0; 3=11: 2^2=0
        assert output[-1] == '[0, 0, 0]'
