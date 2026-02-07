"""
Tests for array .someIndexed(fn) method.
"""

from silk.interpreter import Interpreter


class TestArraySomeIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_someIndexed_true(self):
        output = self._run('print([10, 20, 30].someIndexed(|i, x| i == 1))')
        assert output[-1] == "true"

    def test_someIndexed_false(self):
        output = self._run('print([10, 20, 30].someIndexed(|i, x| i > 5))')
        assert output[-1] == "false"
