"""
Tests for array .interleaveAll(arrays...) method - interleave with multiple arrays.
"""

from silk.interpreter import Interpreter


class TestArrayInterleaveAll:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_interleaveAll_basic(self):
        output = self._run('print([1, 2, 3].interleaveAll(["a", "b", "c"], [10, 20, 30]))')
        assert output[-1] == "[1, a, 10, 2, b, 20, 3, c, 30]"

    def test_interleaveAll_uneven(self):
        output = self._run('print([1, 2].interleaveAll(["a"]))')
        assert output[-1] == "[1, a, 2]"
