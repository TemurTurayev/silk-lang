"""
Tests for array .mapBitAlign1048576() method - align up to nearest multiple of 1048576.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitAlign1048576:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitAlign1048576_basic(self):
        output = self._run('print([1, 1048575, 1048576, 1048577].mapBitAlign1048576())')
        assert output[-1] == '[1048576, 1048576, 1048576, 2097152]'

    def test_mapBitAlign1048576_zero(self):
        output = self._run('print([0, 2097152].mapBitAlign1048576())')
        assert output[-1] == '[0, 2097152]'
