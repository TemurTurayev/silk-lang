"""
Tests for array .mapBitRoundUp1024() method - round up to nearest multiple of 1024.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp1024:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp1024_basic(self):
        output = self._run('print([1, 1024, 1025, 2047].mapBitRoundUp1024())')
        # 1->1024, 1024->1024, 1025->2048, 2047->2048
        assert output[-1] == '[1024, 1024, 2048, 2048]'

    def test_mapBitRoundUp1024_zero(self):
        output = self._run('print([0, 2048, 3072].mapBitRoundUp1024())')
        assert output[-1] == '[0, 2048, 3072]'
