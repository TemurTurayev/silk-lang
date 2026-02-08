"""
Tests for array .mapAbs() method - absolute value of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapAbs:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAbs_basic(self):
        output = self._run('print([-1, 2, -3, 4].mapAbs())')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_mapAbs_positive(self):
        output = self._run('print([0, 5, 10].mapAbs())')
        assert output[-1] == "[0, 5, 10]"
