"""
Tests for array .mapCollatzLength() method - number of Collatz steps to reach 1.
"""

from silk.interpreter import Interpreter


class TestArrayMapCollatzLength:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapCollatzLength_basic(self):
        output = self._run('print([1, 2, 3, 4].mapCollatzLength())')
        # 1->0, 2->1, 3->7, 4->2
        assert output[-1] == "[0, 1, 7, 2]"

    def test_mapCollatzLength_larger(self):
        output = self._run('print([5, 6, 7].mapCollatzLength())')
        # 5->5, 6->8, 7->16
        assert output[-1] == "[5, 8, 16]"
