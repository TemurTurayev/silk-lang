"""
Tests for array .mapBitRoundNearest131072() method - round to nearest multiple of 131072.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest131072:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest131072_basic(self):
        output = self._run('print([1, 65535, 65536, 65537, 131072].mapBitRoundNearest131072())')
        assert output[-1] == '[0, 0, 131072, 131072, 131072]'

    def test_mapBitRoundNearest131072_exact(self):
        output = self._run('print([0, 262144, 393216].mapBitRoundNearest131072())')
        assert output[-1] == '[0, 262144, 393216]'
