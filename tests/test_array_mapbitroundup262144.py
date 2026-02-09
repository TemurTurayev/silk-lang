"""
Tests for array .mapBitRoundUp262144() method - round up to next multiple of 262144.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp262144:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp262144_basic(self):
        output = self._run('print([0, 1, 262143, 262144, 262145].mapBitRoundUp262144())')
        assert output[-1] == '[0, 262144, 262144, 262144, 524288]'

    def test_mapBitRoundUp262144_exact(self):
        output = self._run('print([524288, 786432].mapBitRoundUp262144())')
        assert output[-1] == '[524288, 786432]'
