"""
Tests for array .dropRight(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayDropRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dropRight_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].dropRight(2))')
        assert output[-1] == "[1, 2, 3]"

    def test_dropRight_zero(self):
        output = self._run('print([1, 2, 3].dropRight(0))')
        assert output[-1] == "[1, 2, 3]"

    def test_dropRight_all(self):
        output = self._run('print([1, 2, 3].dropRight(3))')
        assert output[-1] == "[]"
