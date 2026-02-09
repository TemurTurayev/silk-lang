"""
Tests for array .mapBitAlign4194304() method - align up to nearest multiple of 4194304.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4194304:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4194304_basic(self):
        output = self._run('print([0, 1, 2097151, 2097152, 4194304].mapBitAlign4194304())')
        assert output[-1] == '[0, 4194304, 4194304, 4194304, 4194304]'

    def test_mapBitAlign4194304_exact(self):
        output = self._run('print([8388608, 12582912].mapBitAlign4194304())')
        assert output[-1] == '[8388608, 12582912]'
