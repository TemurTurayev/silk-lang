"""
Tests for array .mapBitAlign4294967296() method - align up to nearest multiple of 4294967296.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4294967296:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4294967296_basic(self):
        output = self._run('print([0, 1, 2147483647, 2147483648, 4294967296].mapBitAlign4294967296())')
        assert output[-1] == '[0, 4294967296, 4294967296, 4294967296, 4294967296]'

    def test_mapBitAlign4294967296_exact(self):
        output = self._run('print([8589934592, 12884901888].mapBitAlign4294967296())')
        assert output[-1] == '[8589934592, 12884901888]'
