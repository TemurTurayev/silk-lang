"""
Tests for array .mapBitAlign562949953421312() method - align up to nearest multiple of 562949953421312.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign562949953421312:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign562949953421312_basic(self):
        output = self._run('print([0, 1, 281474976710655, 281474976710656, 562949953421312].mapBitAlign562949953421312())')
        assert output[-1] == '[0, 562949953421312, 562949953421312, 562949953421312, 562949953421312]'

    def test_mapBitAlign562949953421312_exact(self):
        output = self._run('print([1125899906842624, 1688849860263936].mapBitAlign562949953421312())')
        assert output[-1] == '[1125899906842624, 1688849860263936]'
