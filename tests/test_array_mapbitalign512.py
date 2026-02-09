"""
Tests for array .mapBitAlign512() method - align up to nearest multiple of 512.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign512:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign512_basic(self):
        output = self._run('print([1, 511, 512, 513, 1023, 1024].mapBitAlign512())')
        # 1->512, 511->512, 512->512, 513->1024, 1023->1024, 1024->1024
        assert output[-1] == '[512, 512, 512, 1024, 1024, 1024]'

    def test_mapBitAlign512_zero(self):
        output = self._run('print([0, 1536, 2048].mapBitAlign512())')
        assert output[-1] == '[0, 1536, 2048]'
