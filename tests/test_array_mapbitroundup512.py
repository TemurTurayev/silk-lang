"""
Tests for array .mapBitRoundUp512() method - round up to nearest multiple of 512.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp512:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp512_basic(self):
        output = self._run('print([1, 512, 513, 1023].mapBitRoundUp512())')
        # 1->512, 512->512, 513->1024, 1023->1024
        assert output[-1] == '[512, 512, 1024, 1024]'

    def test_mapBitRoundUp512_zero(self):
        output = self._run('print([0, 1024, 1536].mapBitRoundUp512())')
        assert output[-1] == '[0, 1024, 1536]'
