"""
Tests for array .mapFactorial() method - compute factorial of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapFactorial:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFactorial_basic(self):
        output = self._run('print([1, 2, 3, 4, 5].mapFactorial())')
        assert output[-1] == "[1, 2, 6, 24, 120]"

    def test_mapFactorial_withZero(self):
        output = self._run('print([0, 1, 2].mapFactorial())')
        assert output[-1] == "[1, 1, 2]"
