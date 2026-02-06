"""
Tests for array .foldRight(fn, init) method.
"""

from silk.interpreter import Interpreter


class TestArrayFoldRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_foldRight_subtract(self):
        output = self._run('print([1, 2, 3].foldRight(|acc, x| acc - x, 10))')
        assert output[-1] == "4"

    def test_foldRight_concat(self):
        output = self._run('print(["a", "b", "c"].foldRight(|acc, x| acc + x, ""))')
        assert output[-1] == "cba"
