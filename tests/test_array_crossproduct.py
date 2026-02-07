"""
Tests for array .crossProduct(other) method - cartesian product.
"""

from silk.interpreter import Interpreter


class TestArrayCrossProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_crossProduct_basic(self):
        output = self._run('print([1, 2].crossProduct([3, 4]))')
        assert output[-1] == "[[1, 3], [1, 4], [2, 3], [2, 4]]"

    def test_crossProduct_single(self):
        output = self._run('print([1].crossProduct([2]))')
        assert output[-1] == "[[1, 2]]"

    def test_crossProduct_empty(self):
        output = self._run('print([1, 2].crossProduct([]))')
        assert output[-1] == "[]"
