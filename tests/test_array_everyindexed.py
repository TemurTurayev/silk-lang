"""
Tests for array .everyIndexed(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayEveryIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_everyIndexed_true(self):
        output = self._run('print([10, 20, 30].everyIndexed(|i, x| x > 0))')
        assert output[-1] == "true"

    def test_everyIndexed_false(self):
        output = self._run('print([10, 20, 30].everyIndexed(|i, x| i > 0))')
        assert output[-1] == "false"
