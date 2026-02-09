"""
Tests for array .mapBitRoundDown524288() method - round down to nearest multiple of 524288.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown524288:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown524288_basic(self):
        output = self._run('print([1, 524287, 524288, 524289].mapBitRoundDown524288())')
        assert output[-1] == '[0, 0, 524288, 524288]'

    def test_mapBitRoundDown524288_larger(self):
        output = self._run('print([1048576, 1200000].mapBitRoundDown524288())')
        assert output[-1] == '[1048576, 1048576]'
