"""
Tests for array .splitWhen(fn) method - split when predicate returns true.
"""

from silk.interpreter import Interpreter


class TestArraySplitWhen:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_splitWhen_basic(self):
        output = self._run('print([1, 2, 5, 6, 3].splitWhen(|x| x > 4))')
        assert output[-1] == "[[1, 2], [5, 6, 3]]"

    def test_splitWhen_no_match(self):
        output = self._run('print([1, 2, 3].splitWhen(|x| x > 10))')
        assert output[-1] == "[[1, 2, 3]]"
