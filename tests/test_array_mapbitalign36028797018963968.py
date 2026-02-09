"""
Tests for array .mapBitAlign36028797018963968() method - align up to nearest multiple of 36028797018963968.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign36028797018963968:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign36028797018963968_basic(self):
        output = self._run('print([0, 1, 18014398509481983, 18014398509481984, 36028797018963968].mapBitAlign36028797018963968())')
        assert output[-1] == '[0, 36028797018963968, 36028797018963968, 36028797018963968, 36028797018963968]'

    def test_mapBitAlign36028797018963968_exact(self):
        output = self._run('print([72057594037927936, 108086391056891904].mapBitAlign36028797018963968())')
        assert output[-1] == '[72057594037927936, 108086391056891904]'
