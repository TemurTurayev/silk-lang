"""
Tests for array .flattenDeep() method.
"""

from silk.interpreter import Interpreter


class TestArrayFlattenDeep:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_flattenDeep_basic(self):
        output = self._run('print([[1, [2]], [3, [4, [5]]]].flattenDeep())')
        assert output[-1] == "[1, 2, 3, 4, 5]"

    def test_flattenDeep_flat(self):
        output = self._run('print([1, 2, 3].flattenDeep())')
        assert output[-1] == "[1, 2, 3]"
