"""
Tests for array .mapBitRoundUp4096() method - round up to nearest multiple of 4096.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp4096:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp4096_basic(self):
        output = self._run('print([1, 4095, 4096, 4097].mapBitRoundUp4096())')
        assert output[-1] == '[4096, 4096, 4096, 8192]'

    def test_mapBitRoundUp4096_zero(self):
        output = self._run('print([0, 8192].mapBitRoundUp4096())')
        assert output[-1] == '[0, 8192]'
