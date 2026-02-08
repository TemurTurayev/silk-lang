"""
Tests for array .mapIsPositive() method - check if each element is positive.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsPositive:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsPositive_mixed(self):
        output = self._run('print([-1, 0, 3].mapIsPositive())')
        assert output[-1] == "[false, false, true]"

    def test_mapIsPositive_allPositive(self):
        output = self._run('print([1, 2, 3].mapIsPositive())')
        assert output[-1] == "[true, true, true]"
