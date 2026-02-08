"""
Tests for array .mapDecrement() method - subtract 1 from each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapDecrement:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapDecrement_basic(self):
        output = self._run('print([1, 2, 3].mapDecrement())')
        assert output[-1] == "[0, 1, 2]"

    def test_mapDecrement_negative(self):
        output = self._run('print([-1, 0, 5].mapDecrement())')
        assert output[-1] == "[-2, -1, 4]"
