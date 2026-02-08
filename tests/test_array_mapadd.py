"""
Tests for array .mapAdd() method - add a value to each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapAdd:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAdd_basic(self):
        output = self._run('print([1, 2, 3, 4].mapAdd(10))')
        assert output[-1] == '[11, 12, 13, 14]'

    def test_mapAdd_negative(self):
        output = self._run('print([10, 20, 30].mapAdd(5))')
        assert output[-1] == '[15, 25, 35]'
