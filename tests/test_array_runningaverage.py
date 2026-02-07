"""
Tests for array .runningAverage() method.
"""

from silk.interpreter import Interpreter


class TestArrayRunningAverage:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_runningAverage_basic(self):
        output = self._run('print([2, 4, 6].runningAverage())')
        assert output[-1] == "[2, 3, 4]"

    def test_runningAverage_single(self):
        output = self._run('print([10].runningAverage())')
        assert output[-1] == "[10]"
