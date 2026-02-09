"""
Tests for array .mapBitRoundDown2097152() method - round down to nearest multiple of 2097152.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown2097152:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown2097152_basic(self):
        output = self._run('print([0, 1, 2097151, 2097152, 2097153].mapBitRoundDown2097152())')
        assert output[-1] == '[0, 0, 0, 2097152, 2097152]'

    def test_mapBitRoundDown2097152_exact(self):
        output = self._run('print([4194304, 6291455].mapBitRoundDown2097152())')
        assert output[-1] == '[4194304, 4194304]'
