"""
Tests for array .mapBitAlign2048() method - align up to nearest multiple of 2048.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign2048:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign2048_basic(self):
        output = self._run('print([1, 2047, 2048, 2049, 4095, 4096].mapBitAlign2048())')
        # 1->2048, 2047->2048, 2048->2048, 2049->4096, 4095->4096, 4096->4096
        assert output[-1] == '[2048, 2048, 2048, 4096, 4096, 4096]'

    def test_mapBitAlign2048_zero(self):
        output = self._run('print([0, 6144, 8192].mapBitAlign2048())')
        assert output[-1] == '[0, 6144, 8192]'
