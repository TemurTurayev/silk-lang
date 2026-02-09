"""
Tests for array .mapBitRoundNearest128() method - round to nearest multiple of 128.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest128:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest128_basic(self):
        output = self._run('print([1, 63, 64, 65, 128, 192].mapBitRoundNearest128())')
        assert output[-1] == '[0, 0, 128, 128, 128, 256]'

    def test_mapBitRoundNearest128_exact(self):
        output = self._run('print([0, 256, 384].mapBitRoundNearest128())')
        assert output[-1] == '[0, 256, 384]'
