"""
Tests for array .mapBitAlign131072() method - align up to nearest multiple of 131072.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign131072:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign131072_basic(self):
        output = self._run('print([1, 131071, 131072, 131073].mapBitAlign131072())')
        assert output[-1] == '[131072, 131072, 131072, 262144]'

    def test_mapBitAlign131072_zero(self):
        output = self._run('print([0, 262144].mapBitAlign131072())')
        assert output[-1] == '[0, 262144]'
