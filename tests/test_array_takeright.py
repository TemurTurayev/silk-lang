"""
Tests for array .takeRight(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayTakeRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_takeRight_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].takeRight(3))')
        assert output[-1] == "[3, 4, 5]"

    def test_takeRight_all(self):
        output = self._run('print([1, 2, 3].takeRight(5))')
        assert output[-1] == "[1, 2, 3]"

    def test_takeRight_none(self):
        output = self._run('print([1, 2, 3].takeRight(0))')
        assert output[-1] == "[]"
