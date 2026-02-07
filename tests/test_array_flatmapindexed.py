"""
Tests for array .flatMapIndexed(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayFlatMapIndexed:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_flatMapIndexed_basic(self):
        output = self._run('print([10, 20].flatMapIndexed(|i, x| [i, x]))')
        assert output[-1] == "[0, 10, 1, 20]"

    def test_flatMapIndexed_repeat(self):
        output = self._run('print([1, 2, 3].flatMapIndexed(|i, x| [x]))')
        assert output[-1] == "[1, 2, 3]"
