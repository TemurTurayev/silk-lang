"""
Tests for array .mapRunningAvg() method - running average of elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapRunningAvg:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapRunningAvg_basic(self):
        output = self._run('print([2, 4, 6].mapRunningAvg())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapRunningAvg_single(self):
        output = self._run('print([10].mapRunningAvg())')
        assert output[-1] == "[10]"
