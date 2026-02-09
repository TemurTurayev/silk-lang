"""
Tests for array .mapBitRoundUp65536() method - round up to next multiple of 65536.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp65536:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp65536_basic(self):
        output = self._run('print([0, 1, 65535, 65536, 65537].mapBitRoundUp65536())')
        assert output[-1] == '[0, 65536, 65536, 65536, 131072]'

    def test_mapBitRoundUp65536_exact(self):
        output = self._run('print([131072, 196608].mapBitRoundUp65536())')
        assert output[-1] == '[131072, 196608]'
