"""
Tests for array .mapBitAlign32768() method - align up to nearest multiple of 32768.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign32768:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign32768_basic(self):
        output = self._run('print([1, 32767, 32768, 32769].mapBitAlign32768())')
        assert output[-1] == '[32768, 32768, 32768, 65536]'

    def test_mapBitAlign32768_zero(self):
        output = self._run('print([0, 65536, 98304].mapBitAlign32768())')
        assert output[-1] == '[0, 65536, 98304]'
