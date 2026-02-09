"""
Tests for array .mapBitRoundDown4194304() method - round down to nearest multiple of 4194304.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown4194304:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown4194304_basic(self):
        output = self._run('print([0, 1, 4194303, 4194304, 4194305].mapBitRoundDown4194304())')
        assert output[-1] == '[0, 0, 0, 4194304, 4194304]'

    def test_mapBitRoundDown4194304_exact(self):
        output = self._run('print([8388608, 12582911].mapBitRoundDown4194304())')
        assert output[-1] == '[8388608, 8388608]'
