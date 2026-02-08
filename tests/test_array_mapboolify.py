"""
Tests for array .mapBoolify() method - convert each to boolean.
"""

from silk.interpreter import Interpreter


class TestArrayMapBoolify:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapBoolify_basic(self):
        output = self._run('print([0, 1, 2].mapBoolify())')
        assert output[-1] == "[false, true, true]"

    def test_mapBoolify_negative(self):
        output = self._run('print([-1, 0, 3].mapBoolify())')
        assert output[-1] == "[true, false, true]"
