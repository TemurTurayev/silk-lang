"""
Tests for array .mapIsNonZero() method - check if each element is non-zero.
"""

from silk.interpreter import Interpreter


class TestArrayMapIsNonZero:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIsNonZero_mixed(self):
        output = self._run('print([1, 0, 3, 0].mapIsNonZero())')
        assert output[-1] == "[true, false, true, false]"

    def test_mapIsNonZero_allNonZero(self):
        output = self._run('print([1, 2, 3].mapIsNonZero())')
        assert output[-1] == "[true, true, true]"
