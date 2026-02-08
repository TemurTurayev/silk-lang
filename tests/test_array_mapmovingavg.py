"""
Tests for array .mapMovingAvg(n) method - moving average with window size n.
"""

from silk.interpreter import Interpreter


class TestArrayMapMovingAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapMovingAvg_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].mapMovingAvg(3))')
        assert output[-1] == "[2, 3, 4]"

    def test_mapMovingAvg_two(self):
        output = self._run('print([10, 20, 30].mapMovingAvg(2))')
        assert output[-1] == "[15, 25]"
