"""
Tests for array .mapBitQuantize256() method - quantize to nearest multiple of 256.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize256:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize256_basic(self):
        output = self._run('print([10, 257, 512, 700].mapBitQuantize256())')
        # 10->0, 257->256, 512->512, 700->512
        assert output[-1] == '[0, 256, 512, 512]'

    def test_mapBitQuantize256_exact(self):
        output = self._run('print([0, 256, 512, 768].mapBitQuantize256())')
        assert output[-1] == '[0, 256, 512, 768]'
