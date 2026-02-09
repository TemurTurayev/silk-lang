"""
Tests for array .mapBitAlign16384() method - align up to nearest multiple of 16384.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign16384:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign16384_basic(self):
        output = self._run('print([1, 16383, 16384, 16385].mapBitAlign16384())')
        assert output[-1] == '[16384, 16384, 16384, 32768]'

    def test_mapBitAlign16384_zero(self):
        output = self._run('print([0, 32768, 49152].mapBitAlign16384())')
        assert output[-1] == '[0, 32768, 49152]'
