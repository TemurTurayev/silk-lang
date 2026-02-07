"""
Tests for array .noneIndexed(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayNoneIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_noneIndexed_true(self):
        output = self._run('print([10, 20, 30].noneIndexed(|i, x| i > 5))')
        assert output[-1] == "true"

    def test_noneIndexed_false(self):
        output = self._run('print([10, 20, 30].noneIndexed(|i, x| i == 1))')
        assert output[-1] == "false"
