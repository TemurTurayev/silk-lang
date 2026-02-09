"""
Tests for array .mapBitRoundNearest65536() method - round to nearest multiple of 65536.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest65536:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest65536_basic(self):
        output = self._run('print([1, 32767, 32768, 32769, 65536].mapBitRoundNearest65536())')
        assert output[-1] == '[0, 0, 65536, 65536, 65536]'

    def test_mapBitRoundNearest65536_exact(self):
        output = self._run('print([0, 131072, 196608].mapBitRoundNearest65536())')
        assert output[-1] == '[0, 131072, 196608]'
