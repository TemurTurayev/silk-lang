"""
Tests for array .mapBitRoundUp2097152() method - round up to next multiple of 2097152.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp2097152:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp2097152_basic(self):
        output = self._run('print([0, 1, 2097151, 2097152, 2097153].mapBitRoundUp2097152())')
        assert output[-1] == '[0, 2097152, 2097152, 2097152, 4194304]'

    def test_mapBitRoundUp2097152_exact(self):
        output = self._run('print([4194304, 6291456].mapBitRoundUp2097152())')
        assert output[-1] == '[4194304, 6291456]'
