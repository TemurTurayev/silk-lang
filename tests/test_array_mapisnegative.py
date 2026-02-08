"""
Tests for array .mapIsNegative() method - check if each element is negative.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsNegative:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsNegative_mixed(self):
        output = self._run('print([-1, 0, 3].mapIsNegative())')
        assert output[-1] == "[true, false, false]"

    def test_mapIsNegative_allNegative(self):
        output = self._run('print([-1, -2, -3].mapIsNegative())')
        assert output[-1] == "[true, true, true]"
