"""
Tests for array .mapBitRoundDown131072() method - round down to nearest multiple of 131072.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown131072:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown131072_basic(self):
        output = self._run('print([1, 131071, 131072, 131073].mapBitRoundDown131072())')
        assert output[-1] == '[0, 0, 131072, 131072]'

    def test_mapBitRoundDown131072_larger(self):
        output = self._run('print([262144, 300000].mapBitRoundDown131072())')
        assert output[-1] == '[262144, 262144]'
