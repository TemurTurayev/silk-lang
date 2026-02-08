"""
Tests for array .noneEqual() method - no two adjacent elements are equal.
"""

from silk.interpreter import Interpreter


class TestArrayNoneEqual:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_noneEqual_true(self):
        output = self._run('print([1, 2, 3, 4].noneEqual())')
        assert output[-1] == "true"

    def test_noneEqual_false(self):
        output = self._run('print([1, 2, 2, 4].noneEqual())')
        assert output[-1] == "false"
