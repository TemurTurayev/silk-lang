"""
Tests for array .mapInsertAt(index, value) method - insert value at index.
"""

from silk.interpreter import Interpreter


class TestArrayMapInsertAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapInsertAt_middle(self):
        output = self._run('print([1, 2, 3].mapInsertAt(1, 99))')
        assert output[-1] == "[1, 99, 2, 3]"

    def test_mapInsertAt_beginning(self):
        output = self._run('print([1, 2].mapInsertAt(0, 0))')
        assert output[-1] == "[0, 1, 2]"
