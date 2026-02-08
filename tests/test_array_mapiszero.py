"""
Tests for array .mapIsZero() method - check if each element is zero.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsZero:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsZero_mixed(self):
        output = self._run('print([-1, 0, 3].mapIsZero())')
        assert output[-1] == "[false, true, false]"

    def test_mapIsZero_allZero(self):
        output = self._run('print([0, 0, 0].mapIsZero())')
        assert output[-1] == "[true, true, true]"
