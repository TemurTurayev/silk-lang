"""
Tests for array .mapBitRoundDown1048576() method - round down to nearest multiple of 1048576.
"""

from silk.interpreter import Interpreter


class TestArrayMapBitRoundDown1048576:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBitRoundDown1048576_basic(self):
        output = self._run('print([1, 1048575, 1048576, 1048577].mapBitRoundDown1048576())')
        assert output[-1] == '[0, 0, 1048576, 1048576]'

    def test_mapBitRoundDown1048576_larger(self):
        output = self._run('print([2097152, 2500000].mapBitRoundDown1048576())')
        assert output[-1] == '[2097152, 2097152]'
