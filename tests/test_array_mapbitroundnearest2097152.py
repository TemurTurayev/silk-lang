"""
Tests for array .mapBitRoundNearest2097152() method - round to nearest multiple of 2097152.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundNearest2097152:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundNearest2097152_basic(self):
        output = self._run('print([0, 1, 1048575, 1048576, 2097152].mapBitRoundNearest2097152())')
        assert output[-1] == '[0, 0, 0, 2097152, 2097152]'

    def test_mapBitRoundNearest2097152_exact(self):
        output = self._run('print([4194304, 6291456].mapBitRoundNearest2097152())')
        assert output[-1] == '[4194304, 6291456]'
