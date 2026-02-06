"""
Tests for array .zipWith(other, fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayZipWith:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_zipWith_add(self):
        output = self._run('print([1, 2, 3].zipWith([4, 5, 6], |a, b| a + b))')
        assert output[-1] == "[5, 7, 9]"

    def test_zipWith_multiply(self):
        output = self._run('print([2, 3].zipWith([4, 5], |a, b| a * b))')
        assert output[-1] == "[8, 15]"

    def test_zipWith_uneven(self):
        output = self._run('print([1, 2, 3].zipWith([10], |a, b| a + b))')
        assert output[-1] == "[11]"
