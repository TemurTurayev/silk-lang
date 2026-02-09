"""
Tests for array .mapBitAlign17179869184() method - align up to nearest multiple of 17179869184.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign17179869184:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign17179869184_basic(self):
        output = self._run('print([0, 1, 8589934591, 8589934592, 17179869184].mapBitAlign17179869184())')
        assert output[-1] == '[0, 17179869184, 17179869184, 17179869184, 17179869184]'

    def test_mapBitAlign17179869184_exact(self):
        output = self._run('print([34359738368, 51539607552].mapBitAlign17179869184())')
        assert output[-1] == '[34359738368, 51539607552]'
