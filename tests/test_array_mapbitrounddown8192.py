"""
Tests for array .mapBitRoundDown8192() method - round down to nearest multiple of 8192.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown8192:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown8192_basic(self):
        output = self._run('print([1, 8191, 8192, 8193].mapBitRoundDown8192())')
        assert output[-1] == '[0, 0, 8192, 8192]'

    def test_mapBitRoundDown8192_larger(self):
        output = self._run('print([16384, 20000].mapBitRoundDown8192())')
        assert output[-1] == '[16384, 16384]'
