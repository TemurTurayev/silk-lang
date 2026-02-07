"""
Tests for array .mapAccum(fn, init) method - map while accumulating.
"""

from silk.interpreter import Interpreter


class TestArrayMapAccum:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAccum_running_sum(self):
        output = self._run('print([1, 2, 3].mapAccum(|acc, x| [acc + x, acc + x], 0))')
        assert output[-1] == "[[1, 3, 6], 6]"

    def test_mapAccum_prefix(self):
        output = self._run('print(["a", "b"].mapAccum(|acc, x| [acc + x, acc + x], ""))')
        assert output[-1] == "[[a, ab], ab]"
