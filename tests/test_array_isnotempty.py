"""
Tests for array .isNotEmpty() method - check if array is not empty.
"""

from silk.interpreter import Interpreter


class TestArrayIsNotEmpty:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isNotEmpty_true(self):
        output = self._run('print([1, 2, 3].isNotEmpty())')
        assert output[-1] == "true"

    def test_isNotEmpty_false(self):
        output = self._run('print([].isNotEmpty())')
        assert output[-1] == "false"
