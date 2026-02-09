"""
Tests for array .mapBitAlign144115188075855872() method - align up to nearest multiple of 144115188075855872.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign144115188075855872:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign144115188075855872_basic(self):
        output = self._run('print([0, 1, 72057594037927935, 72057594037927936, 144115188075855872].mapBitAlign144115188075855872())')
        assert output[-1] == '[0, 144115188075855872, 144115188075855872, 144115188075855872, 144115188075855872]'

    def test_mapBitAlign144115188075855872_exact(self):
        output = self._run('print([288230376151711744, 432345564227567616].mapBitAlign144115188075855872())')
        assert output[-1] == '[288230376151711744, 432345564227567616]'
