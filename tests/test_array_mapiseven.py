"""
Tests for array .mapIsEven() method - check if each element is even.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsEven:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsEven_mixed(self):
        output = self._run('print([1, 2, 3, 4].mapIsEven())')
        assert output[-1] == "[false, true, false, true]"

    def test_mapIsEven_allEven(self):
        output = self._run('print([2, 4, 6].mapIsEven())')
        assert output[-1] == "[true, true, true]"
