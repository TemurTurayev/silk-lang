"""
Tests for array .dotProduct(other) method.
"""

from silk.interpreter import Interpreter


class TestArrayDotProduct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_dotProduct_basic(self):
        output = self._run('print([1, 2, 3].dotProduct([4, 5, 6]))')
        assert output[-1] == "32"

    def test_dotProduct_zeros(self):
        output = self._run('print([0, 0, 0].dotProduct([1, 2, 3]))')
        assert output[-1] == "0"

    def test_dotProduct_single(self):
        output = self._run('print([5].dotProduct([3]))')
        assert output[-1] == "15"
