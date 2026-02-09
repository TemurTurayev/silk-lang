"""
Tests for array .mapBitRoundNearest32768() method - round to nearest multiple of 32768.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest32768:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest32768_basic(self):
        output = self._run('print([1, 16383, 16384, 16385, 32768].mapBitRoundNearest32768())')
        assert output[-1] == '[0, 0, 32768, 32768, 32768]'

    def test_mapBitRoundNearest32768_exact(self):
        output = self._run('print([0, 65536, 98304].mapBitRoundNearest32768())')
        assert output[-1] == '[0, 65536, 98304]'
