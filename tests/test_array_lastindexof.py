"""
Tests for array .lastIndexOf(value) method - find last index of a value.
"""

from silk.interpreter import Interpreter


class TestArrayLastIndexOf:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lastIndexOf_found(self):
        output = self._run('print([1, 2, 3, 2, 1].lastIndexOf(2))')
        assert output[-1] == "3"

    def test_lastIndexOf_not_found(self):
        output = self._run('print([1, 2, 3].lastIndexOf(5))')
        assert output[-1] == "-1"
