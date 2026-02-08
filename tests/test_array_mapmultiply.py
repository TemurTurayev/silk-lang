"""
Tests for array .mapMultiply() method - multiply each element by given value.
"""

from silk.interpreter import Interpreter


class TestArrayMapMultiply:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapMultiply_basic(self):
        output = self._run('print([1, 2, 3, 4].mapMultiply(5))')
        assert output[-1] == '[5, 10, 15, 20]'

    def test_mapMultiply_negative(self):
        output = self._run('print([10, 20, 30].mapMultiply(2))')
        assert output[-1] == '[20, 40, 60]'
