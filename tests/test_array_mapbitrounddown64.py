"""
Tests for array .mapBitRoundDown64() method - round down to nearest multiple of 64.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown64_basic(self):
        output = self._run('print([63, 64, 65, 127].mapBitRoundDown64())')
        # 63->0, 64->64, 65->64, 127->64
        assert output[-1] == '[0, 64, 64, 64]'

    def test_mapBitRoundDown64_exact(self):
        output = self._run('print([0, 128, 192, 256].mapBitRoundDown64())')
        assert output[-1] == '[0, 128, 192, 256]'
