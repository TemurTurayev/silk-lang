"""
Tests for array .mapBitQuantize128() method - quantize to nearest multiple of 128.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize128:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize128_basic(self):
        output = self._run('print([10, 129, 256, 300].mapBitQuantize128())')
        # 10->0, 129->128, 256->256, 300->256
        assert output[-1] == '[0, 128, 256, 256]'

    def test_mapBitQuantize128_exact(self):
        output = self._run('print([0, 128, 256, 384].mapBitQuantize128())')
        assert output[-1] == '[0, 128, 256, 384]'
