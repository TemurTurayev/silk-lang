"""
Tests for array .dropFirst(n) method.
"""

from silk.interpreter import Interpreter


class TestArrayDropFirst:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dropFirst_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].dropFirst(2))')
        assert output[-1] == "[3, 4, 5]"

    def test_dropFirst_zero(self):
        output = self._run('print([1, 2, 3].dropFirst(0))')
        assert output[-1] == "[1, 2, 3]"
