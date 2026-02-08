"""
Tests for array .isSortedDescending() method - check if sorted descending.
"""

from silk.interpreter import Interpreter


class TestArrayIsSortedDescending:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isSortedDescending_true(self):
        output = self._run('print([4, 3, 2, 1].isSortedDescending())')
        assert output[-1] == "true"

    def test_isSortedDescending_false(self):
        output = self._run('print([4, 3, 5, 1].isSortedDescending())')
        assert output[-1] == "false"
