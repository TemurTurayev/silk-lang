"""
Tests for array .reduceIndexed(fn, init) method.
"""

from silk.interpreter import Interpreter


class TestArrayReduceIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reduceIndexed_sum_indices(self):
        output = self._run('print([10, 20, 30].reduceIndexed(|acc, i, x| acc + i, 0))')
        assert output[-1] == "3"

    def test_reduceIndexed_weighted(self):
        output = self._run('print([1, 2, 3].reduceIndexed(|acc, i, x| acc + x * i, 0))')
        assert output[-1] == "8"
