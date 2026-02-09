"""
Tests for array .mapBitQuantize512() method - quantize to nearest multiple of 512.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitQuantize512:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitQuantize512_basic(self):
        output = self._run('print([10, 513, 1024, 1500].mapBitQuantize512())')
        # 10->0, 513->512, 1024->1024, 1500->1024
        assert output[-1] == '[0, 512, 1024, 1024]'

    def test_mapBitQuantize512_exact(self):
        output = self._run('print([0, 512, 1024, 1536].mapBitQuantize512())')
        assert output[-1] == '[0, 512, 1024, 1536]'
