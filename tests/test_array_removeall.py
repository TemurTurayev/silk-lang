"""
Tests for array .removeAll(value) method - remove all occurrences of a value.
"""

from silk.interpreter import Interpreter


class TestArrayRemoveAll:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removeAll_basic(self):
        output = self._run('print([1, 2, 3, 2, 1].removeAll(2))')
        assert output[-1] == "[1, 3, 1]"

    def test_removeAll_not_found(self):
        output = self._run('print([1, 2, 3].removeAll(5))')
        assert output[-1] == "[1, 2, 3]"
