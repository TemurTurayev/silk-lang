"""
Tests for array .sliding(size, step) method.
"""

from silk.interpreter import Interpreter


class TestArraySliding:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sliding_step1(self):
        output = self._run('print([1, 2, 3, 4].sliding(2, 1))')
        assert output[-1] == "[[1, 2], [2, 3], [3, 4]]"

    def test_sliding_step2(self):
        output = self._run('print([1, 2, 3, 4, 5].sliding(2, 2))')
        assert output[-1] == "[[1, 2], [3, 4]]"

    def test_sliding_size3(self):
        output = self._run('print([1, 2, 3, 4, 5].sliding(3, 1))')
        assert output[-1] == "[[1, 2, 3], [2, 3, 4], [3, 4, 5]]"
