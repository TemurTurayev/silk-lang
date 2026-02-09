"""
Tests for array .mapBitRoundUp4194304() method - round up to next multiple of 4194304.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp4194304:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp4194304_basic(self):
        output = self._run('print([0, 1, 4194303, 4194304, 4194305].mapBitRoundUp4194304())')
        assert output[-1] == '[0, 4194304, 4194304, 4194304, 8388608]'

    def test_mapBitRoundUp4194304_exact(self):
        output = self._run('print([8388608, 12582912].mapBitRoundUp4194304())')
        assert output[-1] == '[8388608, 12582912]'
