"""
Tests for array .filterIndexed(fn) method - filter with index.
"""

from silk.interpreter import Interpreter


class TestArrayFilterIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filterIndexed_even_index(self):
        output = self._run('print([10, 20, 30, 40].filterIndexed(|i, x| i % 2 == 0))')
        assert output[-1] == "[10, 30]"

    def test_filterIndexed_gt(self):
        output = self._run('print([5, 15, 25, 35].filterIndexed(|i, x| x > 10))')
        assert output[-1] == "[15, 25, 35]"
