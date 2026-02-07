"""
Tests for array .dropWhile(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayDropWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dropWhile_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].dropWhile(|x| x < 3))')
        assert output[-1] == "[3, 4, 5]"

    def test_dropWhile_none(self):
        output = self._run('print([5, 4, 3].dropWhile(|x| x > 10))')
        assert output[-1] == "[5, 4, 3]"

    def test_dropWhile_all(self):
        output = self._run('print([1, 2, 3].dropWhile(|x| x < 10))')
        assert output[-1] == "[]"
