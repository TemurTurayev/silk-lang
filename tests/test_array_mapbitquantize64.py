"""
Tests for array .mapBitQuantize64() method - quantize to nearest multiple of 64.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize64:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize64_basic(self):
        output = self._run('print([10, 65, 128, 190].mapBitQuantize64())')
        # 10->0, 65->64, 128->128, 190->128
        assert output[-1] == '[0, 64, 128, 128]'

    def test_mapBitQuantize64_exact(self):
        output = self._run('print([0, 64, 128, 192].mapBitQuantize64())')
        assert output[-1] == '[0, 64, 128, 192]'
