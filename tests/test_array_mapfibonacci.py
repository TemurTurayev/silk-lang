"""
Tests for array .mapFibonacci() method - compute nth Fibonacci number for each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapFibonacci:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapFibonacci_basic(self):
        output = self._run('print([0, 1, 2, 3, 4, 5].mapFibonacci())')
        assert output[-1] == "[0, 1, 1, 2, 3, 5]"

    def test_mapFibonacci_larger(self):
        output = self._run('print([6, 7, 8].mapFibonacci())')
        assert output[-1] == "[8, 13, 21]"
