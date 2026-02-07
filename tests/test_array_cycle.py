"""
Tests for array .cycle(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayCycle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_cycle_basic(self):
        output = self._run('print([1, 2, 3].cycle(3))')
        assert output[-1] == "[1, 2, 3, 1, 2, 3, 1, 2, 3]"

    def test_cycle_once(self):
        output = self._run('print([1, 2].cycle(1))')
        assert output[-1] == "[1, 2]"

    def test_cycle_zero(self):
        output = self._run('print([1, 2].cycle(0))')
        assert output[-1] == "[]"
