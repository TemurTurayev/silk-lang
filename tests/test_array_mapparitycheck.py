"""
Tests for array .mapParityCheck() method - check if each element is even.
"""

from silk.interpreter import Interpreter


class TestArrayMapParityCheck:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapParityCheck_basic(self):
        output = self._run('print([1, 2, 3, 4].mapParityCheck())')
        assert output[-1] == "[false, true, false, true]"

    def test_mapParityCheck_allEven(self):
        output = self._run('print([2, 4, 6].mapParityCheck())')
        assert output[-1] == "[true, true, true]"
