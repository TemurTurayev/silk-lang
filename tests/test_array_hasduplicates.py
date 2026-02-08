"""
Tests for array .hasDuplicates() method - any duplicate elements exist.
"""

from silk.interpreter import Interpreter


class TestArrayHasDuplicates:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_hasDuplicates_true(self):
        output = self._run('print([1, 3, 2, 3].hasDuplicates())')
        assert output[-1] == "true"

    def test_hasDuplicates_false(self):
        output = self._run('print([1, 2, 3, 4].hasDuplicates())')
        assert output[-1] == "false"
