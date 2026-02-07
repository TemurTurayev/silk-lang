"""
Tests for array .accumulate() method - running sum.
"""

from silk.interpreter import Interpreter


class TestArrayAccumulate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_accumulate_basic(self):
        output = self._run('print([1, 2, 3, 4].accumulate())')
        assert output[-1] == "[1, 3, 6, 10]"

    def test_accumulate_single(self):
        output = self._run('print([5].accumulate())')
        assert output[-1] == "[5]"
