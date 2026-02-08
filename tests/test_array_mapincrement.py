"""
Tests for array .mapIncrement() method - add 1 to each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapIncrement:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIncrement_basic(self):
        output = self._run('print([1, 2, 3].mapIncrement())')
        assert output[-1] == "[2, 3, 4]"

    def test_mapIncrement_negative(self):
        output = self._run('print([-1, 0, 5].mapIncrement())')
        assert output[-1] == "[0, 1, 6]"
