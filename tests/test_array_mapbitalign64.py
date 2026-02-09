"""
Tests for array .mapBitAlign64() method - align up to nearest multiple of 64.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign64_basic(self):
        output = self._run('print([1, 63, 64, 65, 127, 128].mapBitAlign64())')
        # 1->64, 63->64, 64->64, 65->128, 127->128, 128->128
        assert output[-1] == '[64, 64, 64, 128, 128, 128]'

    def test_mapBitAlign64_zero(self):
        output = self._run('print([0, 192, 256].mapBitAlign64())')
        assert output[-1] == '[0, 192, 256]'
