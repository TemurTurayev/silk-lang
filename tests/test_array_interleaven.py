"""
Tests for array .interleaveN(arrays) method - interleave multiple arrays.
"""

from silk.interpreter import Interpreter


class TestArrayInterleaveN:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_interleaveN_two(self):
        output = self._run('print([1, 2].interleaveN([[3, 4]]))')
        assert output[-1] == "[1, 3, 2, 4]"

    def test_interleaveN_three(self):
        output = self._run('print([1, 2].interleaveN([[3, 4], [5, 6]]))')
        assert output[-1] == "[1, 3, 5, 2, 4, 6]"
