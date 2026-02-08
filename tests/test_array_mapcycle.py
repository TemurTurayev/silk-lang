"""
Tests for array .mapCycle(n) method - cycle through array to produce n elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapCycle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCycle_basic(self):
        output = self._run('print([1, 2, 3].mapCycle(5))')
        assert output[-1] == "[1, 2, 3, 1, 2]"

    def test_mapCycle_exact(self):
        output = self._run('print([1, 2].mapCycle(4))')
        assert output[-1] == "[1, 2, 1, 2]"
