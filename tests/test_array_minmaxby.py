"""
Tests for array .minBy(fn) and .maxBy(fn) methods.
"""

from silk.interpreter import Interpreter


class TestArrayMinMaxBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_minBy_basic(self):
        output = self._run('print([-3, 1, -5, 2].minBy(|x| x * x))')
        assert output[-1] == "1"

    def test_maxBy_basic(self):
        output = self._run('print([-3, 1, -5, 2].maxBy(|x| x * x))')
        assert output[-1] == "-5"

    def test_minBy_length(self):
        output = self._run('print(["cat", "a", "hello"].minBy(|s| s.length))')
        assert output[-1] == "a"
