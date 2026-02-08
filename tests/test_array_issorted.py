"""
Tests for array .isSorted() method - check if sorted ascending.
"""

from silk.interpreter import Interpreter


class TestArrayIsSorted:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSorted_true(self):
        output = self._run('print([1, 2, 3, 4].isSorted())')
        assert output[-1] == "true"

    def test_isSorted_false(self):
        output = self._run('print([1, 3, 2, 4].isSorted())')
        assert output[-1] == "false"
