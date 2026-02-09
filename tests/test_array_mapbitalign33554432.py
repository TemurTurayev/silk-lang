"""
Tests for array .mapBitAlign33554432() method - align up to nearest multiple of 33554432.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign33554432:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign33554432_basic(self):
        output = self._run('print([0, 1, 16777215, 16777216, 33554432].mapBitAlign33554432())')
        assert output[-1] == '[0, 33554432, 33554432, 33554432, 33554432]'

    def test_mapBitAlign33554432_exact(self):
        output = self._run('print([67108864, 100663296].mapBitAlign33554432())')
        assert output[-1] == '[67108864, 100663296]'
