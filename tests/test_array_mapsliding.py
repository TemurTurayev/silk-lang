"""
Tests for array .mapSliding(n) method - sliding windows with step 1.
"""

from silk.interpreter import Interpreter


class TestArrayMapSliding:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSliding_basic(self):
        output = self._run('print([1, 2, 3, 4].mapSliding(2))')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_mapSliding_three(self):
        output = self._run('print([1, 2, 3, 4, 5].mapSliding(3))')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"
