"""
Tests for array .mapBitRoundDown512() method - round down to nearest multiple of 512.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown512:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown512_basic(self):
        output = self._run('print([511, 512, 513, 1023].mapBitRoundDown512())')
        # 511->0, 512->512, 513->512, 1023->512
        assert output[-1] == '[0, 512, 512, 512]'

    def test_mapBitRoundDown512_exact(self):
        output = self._run('print([0, 1024, 1536, 2048].mapBitRoundDown512())')
        assert output[-1] == '[0, 1024, 1536, 2048]'
