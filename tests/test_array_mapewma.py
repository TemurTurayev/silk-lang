"""
Tests for array .mapEWMA(alpha) method - exponentially weighted moving average.
"""

from silk.interpreter import Interpreter


class TestArrayMapEWMA:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapEWMA_basic(self):
        output = self._run('print([10, 20, 30].mapEWMA(0.5))')
        # EWMA: [10, 0.5*20+0.5*10=15, 0.5*30+0.5*15=22.5]
        assert output[-1] == "[10, 15, 22.5]"

    def test_mapEWMA_single(self):
        output = self._run('print([5].mapEWMA(0.3))')
        assert output[-1] == "[5]"
