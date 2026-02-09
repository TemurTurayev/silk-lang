"""
Tests for array .mapBitRoundUp32768() method - round up to next multiple of 32768.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp32768:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp32768_basic(self):
        output = self._run('print([0, 1, 32767, 32768, 32769].mapBitRoundUp32768())')
        assert output[-1] == '[0, 32768, 32768, 32768, 65536]'

    def test_mapBitRoundUp32768_exact(self):
        output = self._run('print([65536, 98304].mapBitRoundUp32768())')
        assert output[-1] == '[65536, 98304]'
