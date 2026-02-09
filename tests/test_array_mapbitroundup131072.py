"""
Tests for array .mapBitRoundUp131072() method - round up to next multiple of 131072.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp131072:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp131072_basic(self):
        output = self._run('print([0, 1, 131071, 131072, 131073].mapBitRoundUp131072())')
        assert output[-1] == '[0, 131072, 131072, 131072, 262144]'

    def test_mapBitRoundUp131072_exact(self):
        output = self._run('print([262144, 393216].mapBitRoundUp131072())')
        assert output[-1] == '[262144, 393216]'
