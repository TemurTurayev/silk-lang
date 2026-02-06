"""
Tests for array .splitAt(n) method.
"""

from silk.interpreter import Interpreter


class TestArraySplitAt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_splitAt_middle(self):
        output = self._run('print([1, 2, 3, 4, 5].splitAt(3))')
        assert output[-1] == "[[1, 2, 3], [4, 5]]"

    def test_splitAt_start(self):
        output = self._run('print([1, 2, 3].splitAt(0))')
        assert output[-1] == "[[], [1, 2, 3]]"

    def test_splitAt_end(self):
        output = self._run('print([1, 2, 3].splitAt(3))')
        assert output[-1] == "[[1, 2, 3], []]"
