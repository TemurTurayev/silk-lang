"""
Tests for array .chunkBy(fn) method.
"""

from silk.interpreter import Interpreter


class TestArrayChunkBy:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_chunkBy_even_odd(self):
        output = self._run('print([1, 1, 2, 2, 1].chunkBy(|x| x % 2 == 0))')
        assert output[-1] == "[[1, 1], [2, 2], [1]]"

    def test_chunkBy_sign(self):
        output = self._run('print([1, 2, -1, -2, 3].chunkBy(|x| x > 0))')
        assert output[-1] == "[[1, 2], [-1, -2], [3]]"

    def test_chunkBy_single(self):
        output = self._run('print([5].chunkBy(|x| x > 0))')
        assert output[-1] == "[[5]]"
