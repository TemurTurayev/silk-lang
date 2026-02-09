"""
Tests for array .mapBitAlign2147483648() method - align up to nearest multiple of 2147483648.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2147483648:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2147483648_basic(self):
        output = self._run('print([0, 1, 1073741823, 1073741824, 2147483648].mapBitAlign2147483648())')
        assert output[-1] == '[0, 2147483648, 2147483648, 2147483648, 2147483648]'

    def test_mapBitAlign2147483648_exact(self):
        output = self._run('print([4294967296, 6442450944].mapBitAlign2147483648())')
        assert output[-1] == '[4294967296, 6442450944]'
