"""
Tests for array .mapSqrt() method - square root of each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapSqrt:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSqrt_basic(self):
        output = self._run('print([4, 9, 16].mapSqrt())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapSqrt_one(self):
        output = self._run('print([1, 0].mapSqrt())')
        assert output[-1] == "[1, 0]"
