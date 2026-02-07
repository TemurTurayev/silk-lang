"""
Tests for array .mapAccumRight(fn, init) method - map while accumulating from right.
"""

from silk.interpreter import Interpreter


class TestArrayMapAccumRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapAccumRight_running_sum(self):
        output = self._run('print([1, 2, 3].mapAccumRight(|acc, x| [acc + x, acc + x], 0))')
        assert output[-1] == "[[6, 5, 3], 6]"

    def test_mapAccumRight_prefix(self):
        output = self._run('print(["a", "b"].mapAccumRight(|acc, x| [acc + x, acc + x], ""))')
        assert output[-1] == "[[ba, b], ba]"
