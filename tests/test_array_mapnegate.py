"""
Tests for array .mapNegate() method - negate each element.
"""

from silk.interpreter import Interpreter


class TestArrayMapNegate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapNegate_basic(self):
        output = self._run('print([1, -2, 3].mapNegate())')
        assert output[-1] == "[-1, 2, -3]"

    def test_mapNegate_zero(self):
        output = self._run('print([0, 5].mapNegate())')
        assert output[-1] == "[0, -5]"
