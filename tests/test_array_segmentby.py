"""
Tests for array .segmentBy(fn) method - split when predicate result changes.
"""

from silk.interpreter import Interpreter


class TestArraySegmentBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_segmentBy_sign(self):
        output = self._run('print([1, 2, -1, -2, 3].segmentBy(|x| x > 0))')
        assert output[-1] == "[[1, 2], [-1, -2], [3]]"

    def test_segmentBy_even(self):
        output = self._run('print([2, 4, 1, 3, 6].segmentBy(|x| x % 2 == 0))')
        assert output[-1] == "[[2, 4], [1, 3], [6]]"
