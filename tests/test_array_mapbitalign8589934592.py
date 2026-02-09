"""
Tests for array .mapBitAlign8589934592() method - align up to nearest multiple of 8589934592.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign8589934592:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign8589934592_basic(self):
        output = self._run('print([0, 1, 4294967295, 4294967296, 8589934592].mapBitAlign8589934592())')
        assert output[-1] == '[0, 8589934592, 8589934592, 8589934592, 8589934592]'

    def test_mapBitAlign8589934592_exact(self):
        output = self._run('print([17179869184, 25769803776].mapBitAlign8589934592())')
        assert output[-1] == '[17179869184, 25769803776]'
