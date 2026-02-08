"""
Tests for array .mapDivide() method - divide each element by given value.
"""

from silk.interpreter import Interpreter


class TestArrayMapDivide:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDivide_basic(self):
        output = self._run('print([10, 20, 30].mapDivide(5))')
        assert output[-1] == '[2, 4, 6]'

    def test_mapDivide_float(self):
        output = self._run('print([9, 6, 3].mapDivide(3))')
        assert output[-1] == '[3, 2, 1]'
