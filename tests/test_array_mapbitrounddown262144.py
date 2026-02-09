"""
Tests for array .mapBitRoundDown262144() method - round down to nearest multiple of 262144.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown262144:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown262144_basic(self):
        output = self._run('print([1, 262143, 262144, 262145].mapBitRoundDown262144())')
        assert output[-1] == '[0, 0, 262144, 262144]'

    def test_mapBitRoundDown262144_larger(self):
        output = self._run('print([524288, 600000].mapBitRoundDown262144())')
        assert output[-1] == '[524288, 524288]'
