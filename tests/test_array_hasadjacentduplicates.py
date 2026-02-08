"""
Tests for array .hasAdjacentDuplicates() method - any adjacent elements are equal.
"""

from silk.interpreter import Interpreter


class TestArrayHasAdjacentDuplicates:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_hasAdjacentDuplicates_true(self):
        output = self._run('print([1, 2, 2, 3].hasAdjacentDuplicates())')
        assert output[-1] == "true"

    def test_hasAdjacentDuplicates_false(self):
        output = self._run('print([1, 2, 3, 4].hasAdjacentDuplicates())')
        assert output[-1] == "false"
