"""
Tests for array .mapBitRoundDown16384() method - round down to nearest multiple of 16384.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown16384:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown16384_basic(self):
        output = self._run('print([1, 16383, 16384, 16385].mapBitRoundDown16384())')
        assert output[-1] == '[0, 0, 16384, 16384]'

    def test_mapBitRoundDown16384_larger(self):
        output = self._run('print([32768, 40000].mapBitRoundDown16384())')
        assert output[-1] == '[32768, 32768]'
