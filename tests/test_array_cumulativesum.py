"""
Tests for array .cumulativeSum() method.
"""

from silk.interpreter import Interpreter


class TestArrayCumulativeSum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_cumulativeSum_basic(self):
        output = self._run('print([1, 2, 3, 4].cumulativeSum())')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_cumulativeSum_single(self):
        output = self._run('print([5].cumulativeSum())')
        assert output[-1] == "[5]"
