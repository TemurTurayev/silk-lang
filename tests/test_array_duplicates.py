"""
Tests for array .duplicates() method - elements appearing more than once.
"""

from silk.interpreter import Interpreter


class TestArrayDuplicates:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_duplicates_basic(self):
        output = self._run('print([1, 2, 2, 3, 3, 3].duplicates())')
        assert output[-1] == "[2, 3]"

    def test_duplicates_none(self):
        output = self._run('print([1, 2, 3].duplicates())')
        assert output[-1] == "[]"
