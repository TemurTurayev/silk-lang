"""
Tests for array .mapBitRoundNearest262144() method - round to nearest multiple of 262144.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest262144:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest262144_basic(self):
        output = self._run('print([1, 131071, 131072, 131073, 262144].mapBitRoundNearest262144())')
        assert output[-1] == '[0, 0, 262144, 262144, 262144]'

    def test_mapBitRoundNearest262144_exact(self):
        output = self._run('print([0, 524288, 786432].mapBitRoundNearest262144())')
        assert output[-1] == '[0, 524288, 786432]'
