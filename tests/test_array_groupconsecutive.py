"""
Tests for array .groupConsecutive() method.
"""

from silk.interpreter import Interpreter


class TestArrayGroupConsecutive:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_groupConsecutive_basic(self):
        output = self._run('print([1, 1, 2, 2, 2, 3, 1].groupConsecutive())')
        assert output[-1] == "[[1, 1], [2, 2, 2], [3], [1]]"

    def test_groupConsecutive_single(self):
        output = self._run('print([1, 2, 3].groupConsecutive())')
        assert output[-1] == "[[1], [2], [3]]"

    def test_groupConsecutive_empty(self):
        output = self._run('print([].groupConsecutive())')
        assert output[-1] == "[]"
