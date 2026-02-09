"""
Tests for array .mapBitRoundUp1048576() method - round up to next multiple of 1048576.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundUp1048576:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundUp1048576_basic(self):
        output = self._run('print([0, 1, 1048575, 1048576, 1048577].mapBitRoundUp1048576())')
        assert output[-1] == '[0, 1048576, 1048576, 1048576, 2097152]'

    def test_mapBitRoundUp1048576_exact(self):
        output = self._run('print([2097152, 3145728].mapBitRoundUp1048576())')
        assert output[-1] == '[2097152, 3145728]'
