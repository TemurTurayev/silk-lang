"""
Tests for array .allEqual() method - check if all elements are equal.
"""

from silk.interpreter import Interpreter


class TestArrayAllEqual:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_allEqual_true(self):
        output = self._run('print([5, 5, 5].allEqual())')
        assert output[-1] == "true"

    def test_allEqual_false(self):
        output = self._run('print([5, 5, 3].allEqual())')
        assert output[-1] == "false"
