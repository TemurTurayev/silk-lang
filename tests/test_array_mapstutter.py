"""
Tests for array .mapStutter(n) method - repeat each element n times.
"""

from silk.interpreter import Interpreter


class TestArrayMapStutter:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapStutter_double(self):
        output = self._run('print([1, 2, 3].mapStutter(2))')
        assert output[-1] == "[1, 1, 2, 2, 3, 3]"

    def test_mapStutter_triple(self):
        output = self._run('print([4, 5].mapStutter(3))')
        assert output[-1] == "[4, 4, 4, 5, 5, 5]"
