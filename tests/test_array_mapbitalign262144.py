"""
Tests for array .mapBitAlign262144() method - align up to nearest multiple of 262144.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign262144:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign262144_basic(self):
        output = self._run('print([1, 262143, 262144, 262145].mapBitAlign262144())')
        assert output[-1] == '[262144, 262144, 262144, 524288]'

    def test_mapBitAlign262144_zero(self):
        output = self._run('print([0, 524288].mapBitAlign262144())')
        assert output[-1] == '[0, 524288]'
