"""
Tests for array .mapBitRoundDown32768() method - round down to nearest multiple of 32768.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown32768:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown32768_basic(self):
        output = self._run('print([1, 32767, 32768, 32769].mapBitRoundDown32768())')
        assert output[-1] == '[0, 0, 32768, 32768]'

    def test_mapBitRoundDown32768_larger(self):
        output = self._run('print([65536, 80000].mapBitRoundDown32768())')
        assert output[-1] == '[65536, 65536]'
