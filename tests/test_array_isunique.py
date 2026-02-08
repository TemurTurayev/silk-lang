"""
Tests for array .isUnique() method - all elements are unique.
"""

from silk.interpreter import Interpreter


class TestArrayIsUnique:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isUnique_true(self):
        output = self._run('print([1, 2, 3, 4].isUnique())')
        assert output[-1] == "true"

    def test_isUnique_false(self):
        output = self._run('print([1, 2, 2, 3].isUnique())')
        assert output[-1] == "false"
