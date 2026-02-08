"""
Tests for array .mapFloorDivide() method - floor divide each element by given value.
"""

from silk.interpreter import Interpreter


class TestArrayMapFloorDivide:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFloorDivide_basic(self):
        output = self._run('print([10, 15, 20, 25].mapFloorDivide(7))')
        assert output[-1] == '[1, 2, 2, 3]'

    def test_mapFloorDivide_even(self):
        output = self._run('print([9, 6, 3].mapFloorDivide(3))')
        assert output[-1] == '[3, 2, 1]'
