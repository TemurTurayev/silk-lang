"""
Tests for array .weightedAverage(weights) method.
"""

from silk.interpreter import Interpreter


class TestArrayWeightedAverage:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_weightedAverage_basic(self):
        output = self._run('print([80, 90].weightedAverage([1, 3]))')
        assert output[-1] == "87.5"

    def test_weightedAverage_equal(self):
        output = self._run('print([10, 20].weightedAverage([1, 1]))')
        assert output[-1] == "15"
