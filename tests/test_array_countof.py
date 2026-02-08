"""
Tests for array .countOf(value) method - count occurrences of a value.
"""

from silk.interpreter import Interpreter


class TestArrayCountOf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_countOf_found(self):
        output = self._run('print([1, 2, 3, 2, 1].countOf(2))')
        assert output[-1] == "2"

    def test_countOf_not_found(self):
        output = self._run('print([1, 2, 3].countOf(5))')
        assert output[-1] == "0"
