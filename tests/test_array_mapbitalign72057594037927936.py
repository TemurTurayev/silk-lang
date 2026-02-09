"""
Tests for array .mapBitAlign72057594037927936() method - align up to nearest multiple of 72057594037927936.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign72057594037927936:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign72057594037927936_basic(self):
        output = self._run('print([0, 1, 36028797018963967, 36028797018963968, 72057594037927936].mapBitAlign72057594037927936())')
        assert output[-1] == '[0, 72057594037927936, 72057594037927936, 72057594037927936, 72057594037927936]'

    def test_mapBitAlign72057594037927936_exact(self):
        output = self._run('print([144115188075855872, 216172782113783808].mapBitAlign72057594037927936())')
        assert output[-1] == '[144115188075855872, 216172782113783808]'
