"""
Tests for array .mapSign() method - sign of each element (-1, 0, or 1).
"""

from silk.interpreter import Interpreter


class TestArrayMapSign:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapSign_mixed(self):
        output = self._run('print([-5, 0, 3].mapSign())')
        assert output[-1] == "[-1, 0, 1]"

    def test_mapSign_positive(self):
        output = self._run('print([1, 2, 3].mapSign())')
        assert output[-1] == "[1, 1, 1]"
