"""
Tests for array .median() method.
"""

from silk.interpreter import Interpreter


class TestArrayMedian:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_median_odd(self):
        output = self._run('print([3, 1, 2].median())')
        assert output[-1] == "2"

    def test_median_even(self):
        output = self._run('print([1, 2, 3, 4].median())')
        assert output[-1] == "2.5"

    def test_median_single(self):
        output = self._run('print([42].median())')
        assert output[-1] == "42"
