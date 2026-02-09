"""
Tests for array .mapBitAlign65536() method - align up to nearest multiple of 65536.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign65536:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign65536_basic(self):
        output = self._run('print([1, 65535, 65536, 65537].mapBitAlign65536())')
        assert output[-1] == '[65536, 65536, 65536, 131072]'

    def test_mapBitAlign65536_zero(self):
        output = self._run('print([0, 131072].mapBitAlign65536())')
        assert output[-1] == '[0, 131072]'
