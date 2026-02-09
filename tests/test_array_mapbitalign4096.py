"""
Tests for array .mapBitAlign4096() method - align up to nearest multiple of 4096.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign4096:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign4096_basic(self):
        output = self._run('print([1, 4095, 4096, 4097, 8191, 8192].mapBitAlign4096())')
        # 1->4096, 4095->4096, 4096->4096, 4097->8192, 8191->8192, 8192->8192
        assert output[-1] == '[4096, 4096, 4096, 8192, 8192, 8192]'

    def test_mapBitAlign4096_zero(self):
        output = self._run('print([0, 12288, 16384].mapBitAlign4096())')
        assert output[-1] == '[0, 12288, 16384]'
