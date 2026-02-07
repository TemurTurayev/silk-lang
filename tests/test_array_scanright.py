"""
Tests for array .scanRight(fn, init) method.
"""

from silk.interpreter import Interpreter


class TestArrayScanRight:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_scanRight_concat(self):
        output = self._run('print(["a", "b", "c"].scanRight(|acc, x| acc + x, ""))')
        assert output[-1] == "[cba, cb, c]"

    def test_scanRight_sum(self):
        output = self._run('print([1, 2, 3].scanRight(|acc, x| acc + x, 0))')
        assert output[-1] == "[6, 5, 3]"
