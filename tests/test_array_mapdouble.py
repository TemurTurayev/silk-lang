"""
Tests for array .mapDouble() method - double each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDouble:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDouble_basic(self):
        output = self._run('print([1, 2, 3].mapDouble())')
        assert output[-1] == "[2, 4, 6]"

    def test_mapDouble_negative(self):
        output = self._run('print([-1, 0, 5].mapDouble())')
        assert output[-1] == "[-2, 0, 10]"
