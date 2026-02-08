"""
Tests for array .fillCycle(n) method - cycle elements to fill target length.
"""

from silk.interpreter import Interpreter


class TestArrayFillCycle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_fillCycle_basic(self):
        output = self._run('print([1, 2, 3].fillCycle(7))')
        assert output[-1] == "[1, 2, 3, 1, 2, 3, 1]"

    def test_fillCycle_exact(self):
        output = self._run('print([1, 2].fillCycle(4))')
        assert output[-1] == "[1, 2, 1, 2]"
