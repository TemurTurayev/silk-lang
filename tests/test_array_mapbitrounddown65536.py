"""
Tests for array .mapBitRoundDown65536() method - round down to nearest multiple of 65536.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown65536:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown65536_basic(self):
        output = self._run('print([1, 65535, 65536, 65537].mapBitRoundDown65536())')
        assert output[-1] == '[0, 0, 65536, 65536]'

    def test_mapBitRoundDown65536_larger(self):
        output = self._run('print([131072, 150000].mapBitRoundDown65536())')
        assert output[-1] == '[131072, 131072]'
