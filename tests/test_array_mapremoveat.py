"""
Tests for array .mapRemoveAt(index) method - remove element at index.
"""

from silk.interpreter import Interpreter


class TestArrayMapRemoveAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRemoveAt_middle(self):
        output = self._run('print([1, 2, 3, 4].mapRemoveAt(1))')
        assert output[-1] == "[1, 3, 4]"

    def test_mapRemoveAt_first(self):
        output = self._run('print([1, 2, 3].mapRemoveAt(0))')
        assert output[-1] == "[2, 3]"
